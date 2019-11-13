from tr_option.base import KWTR

# [ opt10002 : 주식거래원요청 ]
class Opt10002(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10002'
        self.record_name = '주식거래원'
        self.header = [
            '종목코드', '종목명', '현재가', '등락부호', '기준가', '전일대비', '등락율',
            '매도거래원명1', '매도거래원1', '매도거래량1', '매수거래원명1', '매수거래원1', '매수거래량1',
            '매도거래원명2', '매도거래원2', '매도거래량2', '매수거래원명2', '매수거래원2', '매수거래량2',
            '매도거래원명3', '매도거래원3', '매도거래량3', '매수거래원명3', '매수거래원3', '매수거래량3',
            '매도거래원명4', '매도거래원4', '매도거래량4', '매수거래원명4', '매수거래원4', '매수거래량4',
            '매도거래원명5', '매도거래원5', '매도거래량5', '매수거래원명5', '매수거래원5', '매수거래량5',
        ]


    def tr_opt(self, code, prev_next, screen_no):
	    # 종목코드 = 전문 조회할 종목코드

        self.core.set_input_value('종목코드', code)
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
