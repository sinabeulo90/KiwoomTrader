from tr_option.base import KWTR

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

        return self.core.receive_tr_data_handler


    def tr_opt_data(self, tr_code, rq_name, index):
        ret = {
            'header' : self.header,
            'rows' : [
                [ self.core.get_comm_data(tr_code, rq_name, index, column) for column in self.header ]
            ]
        }

        return ret


    def tr_opt_data_ex(self, tr_code, rq_name):
        ret = {
            'header' : self.header,
            'rows' : self.core.get_comm_data_ex(tr_code, rq_name)
        }

        return ret
