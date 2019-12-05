from tr_option.base import KWTR
from copy import deepcopy

# [ opt10063 : 장중투자자별매매요청 ]
class Opt10063(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10063'

        self.record_name_multiple = '장중투자자별매매'
        self.header_multiple = [
            '종목명', '현재가', '대비기호', '전일대비', '등락율', '누적거래량', '순매수수량', '이점시전순매수수량', '순매수증감', '매수수량', '매수수량증감', '매도수량', '매도수량증감',
        ]


    def tr_opt(self, market_type, input1, input2, input3, input4, prev_next, screen_no):
        # 시장구분 = 000:전체, 001:코스피, 101:코스닥
        # 금액수량구분 = 1:금액, 2:수량
        # 투자자별 = 6:외국인, 7:기관계, 1:투신, 0:보험, 2:은행, 3:연기금, 4:국가, 5:기타법인
        # 외국계전체 = 1:체크, 0:언체크
        # 동시순매수구분 = 1:체크, 0:언체크

        self.core.set_input_value('시장구분', market_type)
        self.core.set_input_value('금액수량구분', input1)
        self.core.set_input_value('투자자별', input2)
        self.core.set_input_value('외국계전체', input3)
        self.core.set_input_value('동시순매수구분', input4)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
