from tr_option.base import KWTR
from copy import deepcopy

# [ opt10086 : 일별주가요청 ]
class Opt10086(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10086'

        self.record_name_multiple = '일별주가'
        self.header_multiple = [
            '날짜', '시가', '고가', '저가', '종가', '전일비', '등락률', '거래량', '금액(백만)', '신용비', '개인', '기관', '외인수량', '외국계', '프로그램', '외인비', '체결강도', '외인보유', '외인비중', '외인순매수', '기관순매수', '개인순매수', '신용잔고율',
        ]


    def tr_opt(self, code, input1, input2, prev_next, screen_no):
        # 종목코드 = 전문 조회할 종목코드
        # 조회일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)
        # 표시구분 = 0:수량, 1:금액(백만원)

        self.core.set_input_value('종목코드', code)
        self.core.set_input_value('조회일자', input1)
        self.core.set_input_value('표시구분', input2)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
