from tr_option.base import KWTR

# [ OPT10022 : 잔량율급증요청 ]
class Opt10022(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10022'
        self.record_name = '잔량율급증'
        self.header = [
            '종목코드', '종목명', '현재가', '전일대비기호', '전일대비', '기준률', '현재비율', '급증률', '총매도잔량', '총매수잔량',
        ]


    def tr_opt(self, market_type, input1, input2, input3, input4, prev_next, screen_no):
        # 시장구분 = 001:코스피, 101:코스닥
        # 비율구분 = 1:매수/매도비율, 2:매도/매수비율
        # 시간구분 = 분 입력
        # 거래량구분 = 5:5천주이상, 10:만주이상, 50:5만주이상, 100:10만주이상
        # 종목조건 = 0:전체조회, 1:관리종목제외, 5:증100제외, 6:증100만보기, 7:증40만보기, 8:증30만보기, 9:증20만보기

        self.core.set_input_value('시장구분', market_type)
        self.core.set_input_value('비율구분', input1)
        self.core.set_input_value('시간구분', input2)
        self.core.set_input_value('거래량구분', input3)
        self.core.set_input_value('종목조건', input4)
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
