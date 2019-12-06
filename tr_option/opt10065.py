from tr_option.base import KWTR
from copy import deepcopy

# [ OPT10065 : 장중투자자별매매상위요청 ]
class Opt10065(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10065'

        self.record_name_multiple = '장중투자자별매매상위'
        self.header_multiple = [
            '종목코드', '종목명', '매도량', '매수량', '순매도',
        ]


    def tr_opt(self, input0, market_type, input2, prev_next, screen_no):
        # 매매구분 = 1:순매수, 2:순매도
        # 시장구분 = 000:전체, 001:코스피, 101:코스닥
        # 기관구분 = 9000:외국인, 9100:외국계, 1000:금융투자, 3000:투신, 5000:기타금융, 4000:은행, 2000:보험, 6000:연기금, 7000:국가, 7100:기타법인, 9999:기관계

        self.core.set_input_value('매매구분', input0)
        self.core.set_input_value('시장구분', market_type)
        self.core.set_input_value('기관구분', input2)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
