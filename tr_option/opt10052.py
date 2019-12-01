from tr_option.base import KWTR
from copy import deepcopy

# [ opt10052 : 거래원순간거래량요청 ]
class Opt10052(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10052'

        self.record_name_multiple = '거래원순간거래량'
        self.header_multiple = [
            '시간', '종목코드', '종목명', '거래원명', '구분', '순간거래량', '누적순매수', '현재가', '전일대비기호', '전일대비', '전일대비',
        ]


    def tr_opt(self, input0, code, input2, input3, input4, prev_next, screen_no):
        # 회원사코드 = 888:외국계 전체, 나머지 회원사 코드는 OPT10042 조회 또는 GetBranchCodeName()함수사용
        # SetInputValue("종목코드"	,  "입력값 2");
        # 시장구분 = 0:전체, 1:코스피, 2:코스닥, 3:종목
        # 수량구분 = 0:전체, 1:1000주, 2:2000주, 3:, 5:, 10:10000주, 30: 30000주, 50: 50000주, 100: 100000주
        # 가격구분 = 0:전체, 1:1천원 미만, 8:1천원 이상, 2:1천원 ~ 2천원, 3:2천원 ~ 5천원, 4:5천원 ~ 1만원, 5:1만원 이상

        self.core.set_input_value('회원사코드', input0)
        self.core.set_input_value('종목코드', code)
        self.core.set_input_value('시장구분', input2)
        self.core.set_input_value('수량구분', input3)
        self.core.set_input_value('가격구분', input4)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
