from tr_option.base import KWTR
from copy import deepcopy

# [ opt10084 : 당일전일체결요청 ]
class Opt10084(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10084'

        self.record_name_multiple = '당일전일체결'
        self.header_multiple = [
            '시간', '현재가', '전일대비', '대비율', '우선매도호가단위', '우선매수호가단위', '체결거래량', 'sign', '누적거래량', '누적거래대금', '체결강도',
        ]


    def tr_opt(self, code, input1, input2, input3, prev_next, screen_no):
        # 종목코드 = 전문 조회할 종목코드
        # 당일전일 = 당일 : 1, 전일 : 2
        # 틱분 = 틱 : 0 , 분 : 1
        # 시간 = 조회시간 4자리, 오전 9시일 경우 '0900', 오후 2시 30분일 경우 '1430'

        self.core.set_input_value('종목코드', code)
        self.core.set_input_value('당일전일', input1)
        self.core.set_input_value('틱분', input2)
        self.core.set_input_value('시간', input3)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
