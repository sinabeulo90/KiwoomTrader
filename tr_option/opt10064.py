from tr_option.base import KWTR
from copy import deepcopy

# [ opt10064 : 장중투자자별매매차트요청 ]
class Opt10064(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10064'

        self.record_name_multiple = '장중투자자별매매차트'
        self.header_multiple = [
            '시간', '외국인투자자', '기관계', '투신', '보험', '은행', '연기금등', '기타법인', '국가',
        ]


    def tr_opt(self, market_type, input1, input2, code, prev_next, screen_no):
        # 시장구분 = 000:전체, 001:코스피, 101:코스닥
        # 금액수량구분 = 1:금액, 2:수량
        # 매매구분 = 0:순매수, 1:매수, 2:매도
        # 종목코드 = 전문 조회할 종목코드

        self.core.set_input_value('시장구분', market_type)
        self.core.set_input_value('금액수량구분', input1)
        self.core.set_input_value('매매구분', input2)
        self.core.set_input_value('종목코드', code)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
