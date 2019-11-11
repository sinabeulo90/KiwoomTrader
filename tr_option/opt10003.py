from tr_option.base import KWTR

# [ opt10003 : 체결정보요청 ]
class Opt10003(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = "opt10003"
        self.record_name = '체결정보'
        self.header = [
            '시간', '현재가', '전일대비', '대비율', '우선매도호가단위', '우선매수호가단위',
            '체결거래량', 'sign', '누적거래량', '누적거래대금', '체결강도',
        ]


    def tr_opt(self, code, prev_next, screen_no):

        self.core.set_input_value("종목코드", code)
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
