from tr_option.base import KWTR

# [ opt10008 : 주식외국인요청 ]
class Opt10008(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = "opt10008"
        self.record_name = '주식외국인'
        self.header = [
            '일자', '종가', '전일대비', '거래량', '변동수량', '보유주식수', '비중',
            '취득가능주식수', '외국인한도', '외국인한도증감', '한도소진률',
        ]


    def tr_opt(self, code, prev_next, screen_no):
        # 종목코드 = 000:전체, 001:코스피, 101:코스닥

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
