from tr_option.base import KWTR

# [ OPT10031 : 전일거래량상위요청 ]
class Opt10031(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10031'
        self.record_name = '전일거래량상위'
        self.header = [
            '종목코드', '종목명', '현재가', '전일대비기호', '전일대비', '거래량',
        ]


    def tr_opt(self, market_type, input1, input2, input3, prev_next, screen_no):
        # 시장구분 = 000:전체, 001:코스피, 101:코스닥
        # 조회구분 = 1:전일거래량 상위100종목, 2:전일거래대금 상위100종목
        # 순위시작 = 0 ~ 100 값 중에  조회를 원하는 순위 시작값
        # 순위끝 = 0 ~ 100 값 중에  조회를 원하는 순위 끝값

        self.core.set_input_value('시장구분', market_type)
        self.core.set_input_value('조회구분', input1)
        self.core.set_input_value('순위시작', input2)
        self.core.set_input_value('순위끝', input3)
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
