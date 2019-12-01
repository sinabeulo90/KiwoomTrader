from tr_option.base import KWTR
from copy import deepcopy

# [ OPT10051 : 업종별투자자순매수요청 ]
class Opt10051(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10051'

        self.record_name_multiple = '업종별순매수'
        self.header_multiple = [
            '업종코드', '업종명', '현재가', '대비부호', '전일대비', '등락율', '거래량',
            '증권순매수', '보험순매수', '투신순매수', '은행순매수', '종신금순매수', '기금순매수', '기타법인순매수',
            '개인순매수', '외국인순매수', '내국인대우외국인순매수', '국가순매수', '사모펀드순매수', '기관계순매수',
        ]


    def tr_opt(self, market_type, input1, input2, prev_next, screen_no):
        # 시장구분 = 코스피:0, 코스닥:1
        # 금액수량구분 = 금액:0, 수량:1
        # 기준일자 = YYYYMMDD (20170101 연도4자리, 월 2자리, 일 2자리 형식)

        self.core.set_input_value('시장구분', market_type)
        self.core.set_input_value('금액수량구분', input1)
        self.core.set_input_value('기준일자', input2)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
