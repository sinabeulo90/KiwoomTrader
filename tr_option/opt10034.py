from tr_option.base import KWTR

# [ OPT10034 : 외인기간별매매상위요청 ]
class Opt10034(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10034'
        self.record_name = '외인기간별매매상위'
        self.header = [
            '순위', '종목코드', '종목명', '현재가', '전일대비기호', '전일대비', '매도호가', '매수호가', '거래량', '순매수량', '취득가능주식수',
        ]


    def tr_opt(self, market_type, input1, input2, prev_next, screen_no):
        # 시장구분 = 000:전체, 001:코스피, 101:코스닥
        # 매매구분 = 1:순매도, 2:순매수, 3:순매매
        # 기간 = 0:당일, 1:전일, 5:5일, 10;10일, 20:20일, 60:60일

        self.core.set_input_value('시장구분', market_type)
        self.core.set_input_value('매매구분', input1)
        self.core.set_input_value('기간', input2)
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
