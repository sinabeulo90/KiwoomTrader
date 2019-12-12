from tr_option.base import KWTR
from copy import deepcopy

# [ opt10075 : 실시간미체결요청 ]
class Opt10075(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10075'

        self.record_name_multiple = '실시간미체결'
        self.header_multiple = [
            '계좌번호', '주문번호', '관리사번', '종목코드', '업무구분', '주문상태', '종목명', '주문수량', '주문가격', '미체결수량', '체결누계금액',
            '원주문번호', '주문구분', '매매구분', '시간', '체결번호', '체결가', '체결량', '현재가', '매도호가', '매수호가', '단위체결가', '단위체결량', '당일매매수수료', '당일매매세금', '개인투자자',
        ]


    def tr_opt(self, input0, input1, input2, code, input4, prev_next, screen_no):
        # 계좌번호 = 전문 조회할 보유계좌번호
        # 전체종목구분 = 0:전체, 1:종목
        # 매매구분 = 0:전체, 1:매도, 2:매수
        # 종목코드 = 전문 조회할 종목코드
        # 체결구분 = 0:전체, 2:체결, 1:미체결

        self.core.set_input_value('계좌번호', input0)
        self.core.set_input_value('전체종목구분', input1)
        self.core.set_input_value('매매구분', input2)
        self.core.set_input_value('종목코드', code)
        self.core.set_input_value('체결구분', input4)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
