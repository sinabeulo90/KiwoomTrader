from tr_option.base import KWTR
from copy import deepcopy

# [ OPT10024 : 거래량갱신요청 ]
class Opt10024(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10024'

        self.record_name_multiple = '거래량갱신'
        self.header_multiple = [
            '종목코드', '종목명', '현재가', '전일대비기호', '전일대비', '등락률', '이전거래량', '현재거래량', '매도호가', '매수호가',
        ]


    def tr_opt(self, market_type, input1, input2, prev_next, screen_no):
        # 시장구분 = 000:전체, 001:코스피, 101:코스닥
        # 주기구분 = 5:5일, 10:10일, 20:20일, 60:60일, 250:250일
        # 거래량구분 = 5:5천주이상, 10:만주이상, 50:5만주이상, 100:10만주이상, 200:20만주이상, 300:30만주이상, 500:50만주이상, 1000:백만주이상

        self.core.set_input_value('시장구분', market_type)
        self.core.set_input_value('주기구분', input1)
        self.core.set_input_value('거래량구분', input2)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
