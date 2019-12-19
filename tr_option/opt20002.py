from tr_option.base import KWTR
from copy import deepcopy

# [ OPT20002 : 업종별주가요청 ]
class Opt20002(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt20002'

        self.record_name_multiple = '업종별주가'
        self.header_multiple = [
            '종목코드', '종목명', '현재가', '전일대비기호', '전일대비', '등락률', '현재거래량', '매도호가', '매수호가', '시가', '고가', '저가',
        ]


    def tr_opt(self, market_type, input1, prev_next, screen_no):
        # 시장구분 = 0:코스피, 1:코스닥, 2:코스피200
        # 업종코드 = 001:종합(KOSPI), 002:대형주, 003:중형주, 004:소형주 101:종합(KOSDAQ), 201:KOSPI200, 302:KOSTAR, 701: KRX100 나머지 ※ 업종코드 참고

        self.core.set_input_value('시장구분', market_type)
        self.core.set_input_value('업종코드', input1)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
