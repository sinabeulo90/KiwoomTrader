from tr_option.base import KWTR
from copy import deepcopy

# [ OPT10078 : 증권사별종목매매동향요청 ]
class Opt10078(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10078'

        self.record_name_multiple = '증권사별종목매매동향'
        self.header_multiple = [
            '일자', '현재가', '대비기호', '전일대비', '등락율', '누적거래량', '순매수수량', '매수수량', '매도수량',
        ]


    def tr_opt(self, input0, code, date_from, date_to, prev_next, screen_no):
        # 회원사코드 = 888:외국계 전체, 나머지 회원사 코드는 OPT10042 조회 또는 GetBranchCodeName()함수사용
        # 종목코드 = 전문 조회할 종목코드
        # 시작일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)
        # 종료일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)

        self.core.set_input_value('회원사코드', input0)
        self.core.set_input_value('종목코드', code)
        self.core.set_input_value('시작일자', date_from)
        self.core.set_input_value('종료일자', date_to)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
