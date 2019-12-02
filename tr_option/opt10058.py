from tr_option.base import KWTR
from copy import deepcopy

# [ OPT10058 : 투자자별일별매매종목요청 ]
class Opt10058(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10058'

        self.record_name_multiple = '투자자별일별매매종목'
        self.header_multiple = [
            '종목코드', '종목명', '순매도수량', '순매도금액', '추정평균가', '현재가', '대비기호', '전일대비', '평균가대비', '대비율', '기간거래량',
        ]


    def tr_opt(self, from_date, to_date, input2, input3, input4, prev_next, screen_no):
        # 시작일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)
        # 종료일자 = YYYYMMDD (20160101 연도4자리, 월 2자리, 일 2자리 형식)
        # 매매구분 = 전체:순매수(2)/순매도(1) 각각조회해서 비교, 순매도:1, 순매수:2
        # 시장구분 = 001:코스피, 101:코스닥
        # 투자자구분 = 8000:개인, 9000:외국인, 1000:금융투자, 3000:투신, 5000:기타금융, 4000:은행, 2000:보험, 6000:연기금, 7000:국가, 7100:기타법인, 9999:기관계

        self.core.set_input_value('시작일자', from_date)
        self.core.set_input_value('종료일자', to_date)
        self.core.set_input_value('매매구분', input2)
        self.core.set_input_value('시장구분', input3)
        self.core.set_input_value('투자자구분', input4)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
