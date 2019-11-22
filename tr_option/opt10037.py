from tr_option.base import KWTR

# [ opt10037 : 외국계창구매매상위요청 ]
class Opt10037(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10037'
        self.record_name = '외국계창구매매상위'
        self.header = [
            '순위', '종목코드', '종목명', '현재가', '전일대비기호', '전일대비', '등락율', '매도거래량', '매수거래량', '순매수거래량', '순매수대금', '거래량', '거래대금',
        ]


    def tr_opt(self, market_type, input1, input2, input3, input4, prev_next, screen_no):
        # 시장구분 = 000:전체, 001:코스피, 101:코스닥
        # 기간 = 0:당일, 1:전일, 5:5일, 10;10일, 20:20일, 60:60일
        # 매매구분 = 1:순매수, 2:순매도, 3:매수, 4:매도
        # 정렬구분 = 1:금액, 2:수량
        # SetInputValue("현재가조건", "입력값 5");

        self.core.set_input_value('시장구분', market_type)
        self.core.set_input_value('기간', input1)
        self.core.set_input_value('매매구분', input2)
        self.core.set_input_value('정렬구분', input3)
        self.core.set_input_value('현재가조건', input4)
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
