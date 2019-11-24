from tr_option.base import KWTR
from copy import deepcopy

# [ OPT10018 : 고저가근접요청 ]
class Opt10018(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10018'

        self.record_name_multiple = '고저가근접'
        self.header_multiple = [
            '종목코드', '종목명', '현재가', '전일대비기호', '전일대비', '등락률', '거래량', '매도호가', '매수호가', '당일고가', '당일저가',
        ]


    def tr_opt(self, input0, input1, input2, input3, input4, input5, prev_next, screen_no):
        # 고저구분 = 1:고가, 2:저가
        # 근접율 = 05:0.5 10:1.0, 15:1.5, 20:2.0. 25:2.5, 30:3.0
        # 시장구분 = 000:전체, 001:코스피, 101:코스닥
        # 거래량구분 = 00000:전체조회, 00010:만주이상, 00050:5만주이상, 00100:10만주이상, 00150:15만주이상, 00200:20만주이상, 00300:30만주이상, 00500:50만주이상, 01000:백만주이상
        # 종목조건 = 0:전체조회,1:관리종목제외, 3:우선주제외, 5:증100제외, 6:증100만보기, 7:증40만보기, 8:증30만보기
        # 신용조건 = 0:전체조회, 1:신용융자A군, 2:신용융자B군, 3:신용융자C군, 4:신용융자D군, 9:신용융자전체

        self.core.set_input_value('고저구분', input0)
        self.core.set_input_value('근접율', input1)
        self.core.set_input_value('시장구분', input2)
        self.core.set_input_value('거래량구분', input3)
        self.core.set_input_value('종목조건', input4)
        self.core.set_input_value('신용조건', input5)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
