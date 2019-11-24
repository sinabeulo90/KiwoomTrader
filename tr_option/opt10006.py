from tr_option.base import KWTR
from copy import deepcopy

# [ OPT10006 : 주식시분요청 ]
class Opt10006(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10006'

        self.record_name_multiple = '주식시분'
        self.header_multiple = [
            '날짜', '시가', '고가', '저가', '종가', '대비', '등락률', '거래량', '거래대금', '체결강도',
        ]


    def tr_opt(self, code, prev_next, screen_no):
	    # 종목코드 = 전문 조회할 종목코드

        self.core.set_input_value('종목코드', code)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
