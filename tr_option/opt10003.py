from tr_option.base import KWTR

class Opt10003(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.header = [
            '시간', '현재가', '전일대비', '대비율', '우선매도호가단위', '우선매수호가단위',
            '체결거래량', 'sign', '누적거래량', '누적거래대금', '체결강도'
        ]


    def tr_opt(self, code, prev_next, screen_no):
        rq_name = tr_code = "opt10003"

        self.core.set_input_value("종목코드", code)
        self.core.comm_rq_data(rq_name, tr_code, prev_next, screen_no)

        return self.core.receive_tr_data_handler


    def tr_opt_data(self, tr_code, rq_name, index):
        ret = {
            'header' : self.header,
            'rows' : [[
                self.core.get_comm_data(tr_code, rq_name, index, '시간'),
                self.core.get_comm_data(tr_code, rq_name, index, '현재가'),
                self.core.get_comm_data(tr_code, rq_name, index, '전일대비'),
                self.core.get_comm_data(tr_code, rq_name, index, '대비율'),
                self.core.get_comm_data(tr_code, rq_name, index, '우선매도호가단위'),
                self.core.get_comm_data(tr_code, rq_name, index, '우선매수호가단위'),
                self.core.get_comm_data(tr_code, rq_name, index, '체결거래량'),
                self.core.get_comm_data(tr_code, rq_name, index, 'sign'),
                self.core.get_comm_data(tr_code, rq_name, index, '누적거래량'),
                self.core.get_comm_data(tr_code, rq_name, index, '누적거래대금'),
                self.core.get_comm_data(tr_code, rq_name, index, '체결강도'),
            ]]
        }

        return ret


    def tr_opt_data_ex(self, tr_code, rq_name):
        ret = {
            'header' : self.header,
            'rows' : self.core.get_comm_data_ex(tr_code, rq_name)
        }

        return ret
