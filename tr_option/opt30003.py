from tr_option.base import KWTR
from copy import deepcopy

# [ OPT30003 : ELWLP보유일별추이요청 ]
class Opt30003(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt30003'

        self.record_name_multiple = ' ELWLP보유일별추이'
        self.header_multiple = [
            '일자', '현재가', '대비구분', '전일대비', '등락율', '거래량', '거래대금', '변동수량', 'LP보유수량', '비중',
            ]


    def tr_opt(self, input0, input1, prev_next, screen_no):
        # SetInputValue("기초자산코드"	,  "입력값 1");
        # SetInputValue("기준일자"	,  "입력값 2");

        self.core.set_input_value('기초자산코드', input0)
        self.core.set_input_value('기준일자', input1)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
