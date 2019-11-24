from tr_option.base import KWTR
from copy import deepcopy

# [ OPT10035 : 외인연속순매매상위요청 ]
class Opt10035(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10035'

        self.record_name_multiple = '신용비율상위'
        self.header_multiple = [
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

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
