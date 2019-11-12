from tr_option.base import KWTR

# [ opt10005 : 주식일주월시분요청 ]
class Opt10005(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = "opt10005"
        self.record_name = '주식일주월시분'
        self.header = [
            '날짜', '시가', '고가', '저가', '종가', '대비', '등락률', '거래량', '거래대금', '체결강도',
            '외인보유', '외인비중', '외인순매수', '기관순매수', '개인순매수', '외국계', '신용잔고율', '프로그램',
        ]


    def tr_opt(self, code, prev_next, screen_no):
	    # 종목코드 = 전문 조회할 종목코드

        self.core.set_input_value("종목코드", code)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        return self.core.receive_tr_data_handler


    def tr_opt_data(self, tr_code, rq_name, index):
        ret = {
            'header' : self.header,
            'rows' : [
                [ self.core.get_comm_data(tr_code, rq_name, index, column) for column in self.header ]
            ]
        }

        return ret


    def tr_opt_data_ex(self, tr_code, rq_name):
        ret = {
            'header' : self.header,
            'rows' : self.core.get_comm_data_ex(tr_code, rq_name)
        }

        return ret
