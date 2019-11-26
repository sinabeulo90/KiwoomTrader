from tr_option.base import KWTR
from copy import deepcopy

# [ opt10041 : 조기종료통화단위요청 ]
class Opt10041(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10041'

        self.record_name_multiple = '조기종료통화단위'
        self.header_multiple = [
            '조기종료여부', '통화단위'
        ]


    def tr_opt(self, code, input1, prev_next, screen_no):
        # 종목코드 = 전문 조회할 종목코드
        # SetInputValue("영웅클럽구분"	,  "입력값 2");

        self.core.set_input_value('종목코드', code)
        self.core.set_input_value('영웅클럽구분', input1)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
