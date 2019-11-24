from tr_option.base import KWTR
from copy import deepcopy

# [ opt10026 : 고저PER요청 ]
class Opt10026(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10026'

        self.record_name = '고저PER'
        self.header = [
            '종목코드', '종목명', 'PER', '현재가', '전일대비기호', '전일대비', '등락률', '현재거래량', '매도호가',
        ]


    def tr_opt(self, per_type, prev_next, screen_no):
	    # PER구분 = 1:코스피저PER, 2:코스피고PER, 3:코스닥저PER, 4:코스닥고PER

        self.core.set_input_value('PER구분', per_type)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
