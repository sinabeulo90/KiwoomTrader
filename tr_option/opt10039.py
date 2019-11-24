from tr_option.base import KWTR
from copy import deepcopy

# [ OPT10039 : 증권사별매매상위요청 ]
class Opt10039(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10039'

        self.record_name_multiple = '증권사별매매상위'
        self.header_multiple = [
            '순위', '종목코드', '종목명', '기간중주가등락', '등락율', '기간중거래량', '순매수', '매수거래량', '매도거래량',
        ]


    def tr_opt(self, input0, input1, input2, input3, prev_next, screen_no):
        # 회원사코드 = 888:외국계 전체, 나머지 회원사 코드는 OPT10042 조회 또는 GetBranchCodeName()함수사용
        # 거래량구분 = 0:전체, 5:5000주, 10:1만주, 50:5만주, 100:10만주, 500:50만주, 1000: 100만주
        # 매매구분 = 1:순매수, 2:순매도
        # 기간 = 1:전일, 5:5일, 10:10일, 60:60일

        self.core.set_input_value('회원사코드', input0)
        self.core.set_input_value('거래량구분', input1)
        self.core.set_input_value('매매구분', input2)
        self.core.set_input_value('기간', input3)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
