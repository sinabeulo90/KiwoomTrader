from tr_option.base import KWTR

class Opt10002(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.header = [
            '종목코드', '종목명', '현재가', '등락부호', '기준가', '전일대비', '등락율',
            '매도거래원명1', '매도거래원1', '매도거래량1', '매수거래원명1', '매수거래원1', '매수거래량1',
            '매도거래원명2', '매도거래원2', '매도거래량2', '매수거래원명2', '매수거래원2', '매수거래량2',
            '매도거래원명3', '매도거래원3', '매도거래량3', '매수거래원명3', '매수거래원3', '매수거래량3',
            '매도거래원명4', '매도거래원4', '매도거래량4', '매수거래원명4', '매수거래원4', '매수거래량4',
            '매도거래원명5', '매도거래원5', '매도거래량5', '매수거래원명5', '매수거래원5', '매수거래량5'
        ]


    def tr_opt(self, code, prev_next, screen_no):
        rq_name = tr_code = "opt10002"

        self.core.set_input_value("종목코드", code)
        self.core.comm_rq_data(rq_name, tr_code, prev_next, screen_no)

        return self.core.receive_tr_data_handler


    def tr_opt_data(self, tr_code, rq_name, index):
        ret = {
            'header' : self.header,
            'rows' : [[
                self.core.get_comm_data(tr_code, rq_name, index, '종목코드'),
                self.core.get_comm_data(tr_code, rq_name, index, '종목명'),
                self.core.get_comm_data(tr_code, rq_name, index, '현재가'),
                self.core.get_comm_data(tr_code, rq_name, index, '등락부호'),
                self.core.get_comm_data(tr_code, rq_name, index, '기준가'),
                self.core.get_comm_data(tr_code, rq_name, index, '전일대비'),
                self.core.get_comm_data(tr_code, rq_name, index, '등락율'),
                self.core.get_comm_data(tr_code, rq_name, index, '매도거래원명1'),
                self.core.get_comm_data(tr_code, rq_name, index, '매도거래원1'),
                self.core.get_comm_data(tr_code, rq_name, index, '매도거래량1'),
                self.core.get_comm_data(tr_code, rq_name, index, '매수거래원명1'),
                self.core.get_comm_data(tr_code, rq_name, index, '매수거래원1'),
                self.core.get_comm_data(tr_code, rq_name, index, '매수거래량1'),
                self.core.get_comm_data(tr_code, rq_name, index, '매도거래원명2'),
                self.core.get_comm_data(tr_code, rq_name, index, '매도거래원2'),
                self.core.get_comm_data(tr_code, rq_name, index, '매도거래량2'),
                self.core.get_comm_data(tr_code, rq_name, index, '매수거래원명2'),
                self.core.get_comm_data(tr_code, rq_name, index, '매수거래원2'),
                self.core.get_comm_data(tr_code, rq_name, index, '매수거래량2'),
                self.core.get_comm_data(tr_code, rq_name, index, '매도거래원명3'),
                self.core.get_comm_data(tr_code, rq_name, index, '매도거래원3'),
                self.core.get_comm_data(tr_code, rq_name, index, '매도거래량3'),
                self.core.get_comm_data(tr_code, rq_name, index, '매수거래원명3'),
                self.core.get_comm_data(tr_code, rq_name, index, '매수거래원3'),
                self.core.get_comm_data(tr_code, rq_name, index, '매수거래량3'),
                self.core.get_comm_data(tr_code, rq_name, index, '매도거래원명4'),
                self.core.get_comm_data(tr_code, rq_name, index, '매도거래원4'),
                self.core.get_comm_data(tr_code, rq_name, index, '매도거래량4'),
                self.core.get_comm_data(tr_code, rq_name, index, '매수거래원명4'),
                self.core.get_comm_data(tr_code, rq_name, index, '매수거래원4'),
                self.core.get_comm_data(tr_code, rq_name, index, '매수거래량4'),
                self.core.get_comm_data(tr_code, rq_name, index, '매도거래원명5'),
                self.core.get_comm_data(tr_code, rq_name, index, '매도거래원5'),
                self.core.get_comm_data(tr_code, rq_name, index, '매도거래량5'),
                self.core.get_comm_data(tr_code, rq_name, index, '매수거래원명5'),
                self.core.get_comm_data(tr_code, rq_name, index, '매수거래원5'),
                self.core.get_comm_data(tr_code, rq_name, index, '매수거래량5'),
            ]]
        }

        return ret


    def tr_opt_data_ex(self, tr_code, rq_name):
        ret = {
            'header' : self.header,
            'rows' : self.core.get_comm_data_ex(tr_code, rq_name)
        }

        return ret
