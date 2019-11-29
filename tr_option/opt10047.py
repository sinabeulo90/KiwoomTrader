from tr_option.base import KWTR
from copy import deepcopy

# [ opt10047 : 체결강도추이일별요청 ]
class Opt10047(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10047'

        self.record_name_multiple = '체결강도추이일별'
        self.header_multiple = [
            '일자', '현재가', '전일대비', '전일대비기호', '등락율', '거래량', '누적거래대금', '누적거래량', '체결강도', '체결강도5분', '체결강도20분', '체결강도60분',
        ]


    def tr_opt(self, code, input1, input2, prev_next, screen_no):
        # 종목코드 = 전문 조회할 종목코드
        # 틱구분 = 설정값 1
        # 체결강도구분 = 설정값 1

        self.core.set_input_value('종목코드', code)
        self.core.set_input_value('틱구분', input1)
        self.core.set_input_value('체결강도구분', input2)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
