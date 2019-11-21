from tr_option.base import KWTR

# [ OPT10035 : 외인연속순매매상위요청 ]
class Opt10035(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10035'
        self.record_name = '신용비율상위'
        self.header = [
            '종목코드', '종목명', '현재가', '전일대비기호', '전일대비', 'D-1', 'D-2', 'D-3', '합계', '한도소진율', '전일대비1', '전일대비2', '전일대비3',
        ]


    def tr_opt(self, market_type, input1, input2, prev_next, screen_no):
        # 시장구분 = 000:전체, 001:코스피, 101:코스닥
        # 매매구분 = 1:연속순매도, 2:연속순매수
        # 기준일구분 = 0:당일기준, 1:전일기준

        self.core.set_input_value('시장구분', market_type)
        self.core.set_input_value('매매구분', input1)
        self.core.set_input_value('기준일구분', input2)
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
