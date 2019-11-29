from tr_option.base import KWTR
from copy import deepcopy

# [ OPT10049 : ELW투자지표요청 ]
class Opt10049(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10049'

        self.record_name_single = 'ELW투자지표'
        self.header_single = [
            '연속구분', '연속키',
        ]

        self.record_name_multiple = 'ELW투자지표배열'
        self.header_multiple = [
            '시간', '패리티', '프리미엄', '기어링비율', '손익분기율', '현재가', '레버리지',
        ]


    def tr_opt(self, input0, input1, code, prev_next, screen_no):
        # SetInputValue("연속구분"	,  "입력값 1");
        # SetInputValue("연속키"	,  "입력값 2");
        # SetInputValue("종목코드"	,  "입력값 3");

        self.core.set_input_value('연속구분', input0)
        self.core.set_input_value('연속키', input1)
        self.core.set_input_value('종목코드', code)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
