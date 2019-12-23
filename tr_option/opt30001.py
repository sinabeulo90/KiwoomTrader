from tr_option.base import KWTR
from copy import deepcopy

# [ OPT30001 : ELW가격급등락요청 ]
class Opt30001(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt30001'

        self.record_name_single = '기준가시간'
        self.header_single = [
            '기준가시간',
        ]

        self.record_name_multiple = 'ELW가격급등락'
        self.header_multiple = [
            '종목코드', '순위', '종목명', '대비기호', '전일대비', '거래종료ELW기준가', '현재가', '기준대비', '거래량', '급등율',
        ]


    def tr_opt(self, input0, input1, input2, input3, input4, input5, input6, input7, input8, prev_next, screen_no):
        # 등락구분 = 1:급등, 2:급락
        # 시간구분 = 1:분전, 2:일전
        # SetInputValue("시간"	,  "입력값 3");
        # 거래량구분 = 0:전체, 10:만주이상, 50:5만주이상, 100:10만주이상, 300:30만주이상, 500:50만주이상, 1000:백만주이상
        # 발행사코드 = ※ 발행사코드 참고
        # 기초자산코드 = ※ 기초자산코드 참고
        # 권리구분 = 000:전체, 001:콜, 002:풋, 003:DC, 004:DP, 005:EX, 006:조기종료콜, 007:조기종료풋
        # LP코드 = ※ LP코드 참고
        # SetInputValue("거래종료ELW제외"	,  "입력값 9");

        self.core.set_input_value('등락구분', input0)
        self.core.set_input_value('시간구분', input1)
        self.core.set_input_value('시간', input2)
        self.core.set_input_value('거래량구분', input3)
        self.core.set_input_value('발행사코드', input4)
        self.core.set_input_value('기초자산코드', input5)
        self.core.set_input_value('권리구분', input6)
        self.core.set_input_value('LP코드', input7)
        self.core.set_input_value('거래종료ELW제외', input8)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
