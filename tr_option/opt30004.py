from tr_option.base import KWTR
from copy import deepcopy

# [ OPT30004 : ELW괴리율요청 ]
class Opt30004(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt30004'

        self.record_name_multiple = ' ELW괴리율'
        self.header_multiple = [
            '종목코드', '발행사명', '회차', '기초자산명', '권리구분', '괴리율', '베이시스', '잔존일수', '이론가', '현재가', '대비구분', '전일대비', '등락율', '거래량', '종목명',
        ]


    def tr_opt(self, input0, input1, input2, input3, input4, prev_next, screen_no):
        # 발행사코드 = ※ 발행사 코드 참고
        # 기초자산코드 = ※ 기초자산 코드 참고
        # 권리구분 = 000: 전체, 001: 콜, 002: 풋, 003: DC, 004: DP, 005: EX, 006: 조기종료콜, 007: 조기종료풋
        # LP코드 = ※ LP코드 참고
        # 거래종료ELW제외 = 1:거래종료ELW제외, 0:거래종료ELW포함

        self.core.set_input_value('발행사코드', input0)
        self.core.set_input_value('기초자산코드', input1)
        self.core.set_input_value('권리구분', input2)
        self.core.set_input_value('LP코드', input3)
        self.core.set_input_value('거래종료ELW제외', input4)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
