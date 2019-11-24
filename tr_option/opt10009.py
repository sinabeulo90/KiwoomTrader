from tr_option.base import KWTR
from copy import deepcopy

# [ OPT10009 : 주식기관요청 ]
class Opt10009(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10009'

        self.record_name_multiple = '주식기관'
        self.header_multiple = [
            '날짜', '종가', '대비', '기관기간누적', '기관일변순매매', '외국인일변순매매', '외국인지분율',
        ]


    def tr_opt(self, code, prev_next, screen_no):
        # 종목코드 = 전문 조회할 종목코드

        self.core.set_input_value('종목코드', code)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
