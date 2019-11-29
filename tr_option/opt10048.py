from tr_option.base import KWTR
from copy import deepcopy

# [ OPT10048 : ELW일별민감도지표요청 ]
class Opt10048(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt1004'

        self.record_name_multiple = 'ELW일별민감도지표'
        self.header_multiple = [
            '일자', 'IV', '델타', '감마', '쎄타', '베가', '로', 'LP',
        ]


    def tr_opt(self, code, prev_next, screen_no):
	    # 종목코드 = 전문 조회할 종목코드

        self.core.set_input_value('종목코드', code)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
