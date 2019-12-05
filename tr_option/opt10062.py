from tr_option.base import KWTR
from copy import deepcopy

# [ opt10062 : 동일순매매순위요청 ]
class Opt10062(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10062'

        self.record_name_multiple = '동일순매매순위'
        self.header_multiple = [
            '종목순위', '순위', '종목명', '현재가', '대비기호', '전일대비', '등락율', '누적거래량',
            '기관순매매수량', '기관순매매금액', '기관순매매평균가', '외인순매매수량', '외인순매매금액', '외인순매매평균가', '순매매수량', '순매매금액',
        ]


    def tr_opt(self, date_from, date_to, input2, input3, input4, input5, prev_next, screen_no):
        # 시작일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)
        # 종료일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)
        # 시장구분 = 000:전체, 001: 코스피, 101:코스닥
        # 매매구분 = 1:순매수, 2:순매도
        # 정렬조건 = 1:수량, 2:금액
        # 단위구분 = 1:단주, 1000:천주

        self.core.set_input_value('시작일자', date_from)
        self.core.set_input_value('종료일자', date_to)
        self.core.set_input_value('시장구분', input2)
        self.core.set_input_value('매매구분', input3)
        self.core.set_input_value('정렬조건', input4)
        self.core.set_input_value('단위구분', input5)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
