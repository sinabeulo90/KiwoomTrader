from tr_option.base import KWTR

# [ opt10004 : 주식호가요청 ]
class Opt10004(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = "opt10004"
        self.record_name = '주식호가'
        self.header = [
            '호가잔량기준시간',
            '매도10차선잔량대비', '매도10차선잔량', '매도10차선호가', '매도9차선잔량대비', '매도9차선잔량', '매도9차선호가', '매도8차선잔량대비', '매도8차선잔량', '매도8차선호가', '매도7차선잔량대비', '매도7차선잔량', '매도7차선호가', '매도6차선잔량대비', '매도6차선잔량', '매도6차선호가',
            '매도5차선잔량대비', '매도5차선잔량', '매도5차선호가', '매도4차선잔량대비', '매도4차선잔량', '매도4차선호가', '매도3차선잔량대비', '매도3차선잔량', '매도3차선호가', '매도2차선잔량대비', '매도2차선잔량', '매도2차선호가', '매도1차선잔량대비', '매도최우선잔량', '매도최우선호가',
            '매수최우선호가', '매수최우선잔량', '매수1차선잔량대비', '매수2차선호가', '매수2차선잔량', '매수2차선잔량대비', '매수3차선호가', '매수3차선잔량', '매수3차선잔량대비', '매수4차선호가', '매수4차선잔량', '매수4차선잔량대비', '매수5차선호가', '매수5차선잔량', '매수5차선잔량대비',
            '매수6차선호가', '매수6차선잔량', '매수6차선잔량대비', '매수7차선호가', '매수7차선잔량', '매수7차선잔량대비', '매수8차선호가', '매수8차선잔량', '매수8차선잔량대비', '매수9차선호가', '매수9차선잔량', '매수9차선잔량대비', '매수10차선호가', '매수10차선잔량', '매수10차선잔량대비',
            '총매도잔량직전대비', '총매도잔량', '총매수잔량', '총매수잔량직전대비', '시간외매도잔량대비', '시간외매도잔량', '시간외매수잔량', '시간외매수잔량대비',
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
