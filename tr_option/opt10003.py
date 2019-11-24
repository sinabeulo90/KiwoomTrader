from tr_option.base import KWTR
from copy import deepcopy

# [ opt10003 : 체결정보요청 ]
class Opt10003(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10003'

        self.record_name_multiple = '체결정보'
        self.header_multiple = [
            '시간', '현재가', '전일대비', '대비율', '우선매도호가단위', '우선매수호가단위',
            '체결거래량', 'sign', '누적거래량', '누적거래대금', '체결강도',
        ]


    def tr_opt(self, code, prev_next, screen_no):
	    # 종목코드 = 전문 조회할 종목코드

        self.core.set_input_value('종목코드', code)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
