from tr_option.base import KWTR
from copy import deepcopy

# [ opt10038 : 종목별증권사순위요청 ]
class Opt10038(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10038'

        self.record_name_single = '종목별증권사순위_합산'
        self.header_single = [
            '순위1', '순위2', '순위3', '기간중거래량',
        ]

        self.record_name_multiple = '종목별증권사순위'
        self.header_multiple = [
            '순위', '회원사명', '매도수량', '매수수량', '누적순매수량',
        ]


    def tr_opt(self, input0, input1, input2, input3, input4, prev_next, screen_no):
        # 종목코드 = 전문 조회할 종목코드
        # 시작일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)
        # 종료일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)
        # 조회구분 = 1:순매도순위정렬, 2:순매수순위정렬
        # SetInputValue("기간"	,  "입력값 5");

        self.core.set_input_value('종목코드', input0)
        self.core.set_input_value('시작일자', input1)
        self.core.set_input_value('종료일자', input2)
        self.core.set_input_value('조회구분', input3)
        self.core.set_input_value('기간', input4)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])
        
        return self.tr_data
