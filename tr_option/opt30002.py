from tr_option.base import KWTR
from copy import deepcopy

# [ OPT30002 : 거래원별ELW순매매상위요청 ]
class Opt30002(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt30002'

        self.record_name_multiple = ' 거래원별ELW순매매상위'
        self.header_multiple = [
            '종목코드', '종목명', '주가등락', '등락율', '거래량', '순매수', '매수거래량', '매도거래량',
        ]


    def tr_opt(self, input0, input1, input2, input3, input4, prev_next, screen_no):
        # 발행사코드 = ※ 발행사코드 참고
        # 거래량구분 = 0:전체, 5:5천주, 10:만주, 50:5만주, 100:10만주, 500:50만주, 1000:백만주
        # 매매구분 = 1:순매수, 2:순매도
        # 기간 = 1:전일, 5:5일, 10:10일, 40:40일, 60:60일
        # SetInputValue("거래종료ELW제외"	,  "입력값 5");

        self.core.set_input_value('발행사코드', input0)
        self.core.set_input_value('거래량구분', input1)
        self.core.set_input_value('매매구분', input2)
        self.core.set_input_value('기간', input3)
        self.core.set_input_value('거래종료ELW제외', input4)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
