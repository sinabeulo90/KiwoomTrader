from tr_option.base import KWTR
from copy import deepcopy

# [ opt10053 : 당일상위이탈원요청 ]
class Opt10053(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10053'

        self.record_name_multiple = '당일상위이탈원'
        self.header_multiple = [
            '매도이탈시간', '매도수량', '매도상위이탈원', '매수이탈시간', '매수수량', '매수상위이탈원', '조회일자', '조회시간',
        ]


    def tr_opt(self, code, prev_next, screen_no):
    	# 종목코드 = 전문 조회할 종목코드

        self.core.set_input_value('종목코드', code)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
