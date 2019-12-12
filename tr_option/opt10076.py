from tr_option.base import KWTR
from copy import deepcopy

# [ opt10076 : 실시간체결요청 ]
class Opt10076(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10076'

        self.record_name_multiple = '실시간체결'
        self.header_multiple = [
            '주문번호', '종목명', '주문구분', '주문가격', '주문수량', '체결가', '체결량', '미체결수량', '당일매매수수료', '당일매매세금', '주문상태', '매매구분', '원주문번호', '주문시간', '종목코드',
        ]


    def tr_opt(self, code, input1, input2, input3, input4, input5, input6, prev_next, screen_no):
        # 종목코드 = 전문 조회할 종목코드
        # 조회구분 = 0:전체, 1:종목
        # 매도수구분 = 0:전체, 1:매도, 2:매수
        # 계좌번호 = 전문 조회할 보유계좌번호
        # 비밀번호 = 사용안함(공백)
        # 주문번호 = 조회할 주문번호
        # 체결구분 = 0:전체, 2:체결, 1:미체결

        self.core.set_input_value('종목코드', code)
        self.core.set_input_value('조회구분', input1)
        self.core.set_input_value('매도수구분', input2)
        self.core.set_input_value('계좌번호', input3)
        self.core.set_input_value('비밀번호', input4)
        self.core.set_input_value('주문번호', input5)
        self.core.set_input_value('체결구분', input6)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
