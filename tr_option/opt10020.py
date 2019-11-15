from tr_option.base import KWTR

# [ OPT10020 : 호가잔량상위요청 ]
class Opt10020(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10020'
        self.record_name = '호가잔량상위'
        self.header = [
            '종목코드', '종목명', '현재가', '전일대비기호', '전일대비', '거래량', '총매도잔량', '총매수잔량', '순매수잔량', '매수비율',
        ]


    def tr_opt(self, market_type, input1, input2, input3, input4, prev_next, screen_no):
        # 시장구분 = 001:코스피, 101:코스닥
        # 정렬구분 = 1:순매수잔량순, 2:순매도잔량순, 3:매수비율순, 4:매도비율순
        # 거래량구분 = 0000:장시작전(0주이상), 0010:만주이상, 0050:5만주이상, 00100:10만주이상
        # 종목조건 = 0:전체조회, 1:관리종목제외, 5:증100제외, 6:증100만보기, 7:증40만보기, 8:증30만보기, 9:증20만보기
        # 신용조건 = 0:전체조회, 1:신용융자A군, 2:신용융자B군, 3:신용융자C군, 4:신용융자D군, 9:신용융자전체
        
        self.core.set_input_value('시장구분', market_type)
        self.core.set_input_value('정렬구분', input1)
        self.core.set_input_value('거래량구분', input2)
        self.core.set_input_value('종목조건', input3)
        self.core.set_input_value('신용조건', input4)
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
