from core import KWCore
from constants import KWErrorCode

class KWTrader(KWCore):

    def initialize(self):
        self.tr_list['opt10001'] = {'조회' : self._opt10001_data}
        self.tr_list['opt10002'] = {'조회' : self._opt10002_data, '연속' : self._opt10002_data_ex}
        self.tr_list['opt10003'] = {'조회' : self._opt10003_data, '연속' : self._opt10003_data_ex}

    def connection(self):
        self.comm_connect()


    # [ opt10001 : 주식기본정보요청 ]
    def opt10001(self, code, prev_next, screen_no):
        rq_name = tr_code = "opt10001"

        self.set_input_value("종목코드", code)
        self.comm_rq_data(rq_name, tr_code, prev_next, screen_no)

        return self.receive_tr_data_handler

    def _opt10001_data(self, tr_code, rq_name, index):
        ret = {
            'header' : [
                '종목코드', '종목명', '결산월', '액면가', '자본금', '상장주식', '신용비율',
                '연중최고', '연중최저', '시가총액', '시가총액비중', '외인소진률', '대용가',
                'PER', 'EPS', 'ROE', 'PBR', 'EV', 'BPS', '매출액', '영업이익', '당기순이익',
                '250최고', '250최저', '시가', '고가', '저가', '상한가', '하한가', '기준가',
                '예상체결가', '예상체결수량', '250최고가일', '250최고가대비율', '250최저가일', '250최저가대비율',
                '현재가', '대비기호', '전일대비', '등락율', '거래량', '거래대비', '액면가단위', '유통주식', '유통비율'
            ],
            'rows' : [[
                self.get_comm_data(tr_code, rq_name, index, '종목코드'),
                self.get_comm_data(tr_code, rq_name, index, '종목명'),
                self.get_comm_data(tr_code, rq_name, index, '결산월'),
                self.get_comm_data(tr_code, rq_name, index, '액면가'),
                self.get_comm_data(tr_code, rq_name, index, '자본금'),
                self.get_comm_data(tr_code, rq_name, index, '상장주식'),
                self.get_comm_data(tr_code, rq_name, index, '신용비율'),
                self.get_comm_data(tr_code, rq_name, index, '연중최고'),
                self.get_comm_data(tr_code, rq_name, index, '연중최저'),
                self.get_comm_data(tr_code, rq_name, index, '시가총액'),
                self.get_comm_data(tr_code, rq_name, index, '시가총액비중'),
                self.get_comm_data(tr_code, rq_name, index, '외인소진률'),
                self.get_comm_data(tr_code, rq_name, index, '대용가'),
                self.get_comm_data(tr_code, rq_name, index, 'PER'),
                self.get_comm_data(tr_code, rq_name, index, 'EPS'),
                self.get_comm_data(tr_code, rq_name, index, 'ROE'),
                self.get_comm_data(tr_code, rq_name, index, 'PBR'),
                self.get_comm_data(tr_code, rq_name, index, 'EV'),
                self.get_comm_data(tr_code, rq_name, index, 'BPS'),
                self.get_comm_data(tr_code, rq_name, index, '매출액'),
                self.get_comm_data(tr_code, rq_name, index, '영업이익'),
                self.get_comm_data(tr_code, rq_name, index, '당기순이익'),
                self.get_comm_data(tr_code, rq_name, index, '250최고'),
                self.get_comm_data(tr_code, rq_name, index, '250최저'),
                self.get_comm_data(tr_code, rq_name, index, '시가'),
                self.get_comm_data(tr_code, rq_name, index, '고가'),
                self.get_comm_data(tr_code, rq_name, index, '저가'),
                self.get_comm_data(tr_code, rq_name, index, '상한가'),
                self.get_comm_data(tr_code, rq_name, index, '하한가'),
                self.get_comm_data(tr_code, rq_name, index, '기준가'),
                self.get_comm_data(tr_code, rq_name, index, '예상체결가'),
                self.get_comm_data(tr_code, rq_name, index, '예상체결수량'),
                self.get_comm_data(tr_code, rq_name, index, '250최고가일'),
                self.get_comm_data(tr_code, rq_name, index, '250최고가대비율'),
                self.get_comm_data(tr_code, rq_name, index, '250최저가일'),
                self.get_comm_data(tr_code, rq_name, index, '250최저가대비율'),
                self.get_comm_data(tr_code, rq_name, index, '현재가'),
                self.get_comm_data(tr_code, rq_name, index, '대비기호'),
                self.get_comm_data(tr_code, rq_name, index, '전일대비'),
                self.get_comm_data(tr_code, rq_name, index, '등락율'),
                self.get_comm_data(tr_code, rq_name, index, '거래량'),
                self.get_comm_data(tr_code, rq_name, index, '거래대비'),
                self.get_comm_data(tr_code, rq_name, index, '액면가단위'),
                self.get_comm_data(tr_code, rq_name, index, '유통주식'),
                self.get_comm_data(tr_code, rq_name, index, '유통비율')
            ]]
        }

        return ret


    #  [ opt10002 : 주식거래원요청 ]
    def opt10002(self, code, prev_next, screen_no):
        rq_name = tr_code = "opt10002"

        self.set_input_value("종목코드", code)
        self.comm_rq_data(rq_name, tr_code, prev_next, screen_no)

        return self.receive_tr_data_handler

    def _opt10002_data(self, tr_code, rq_name, index):
        ret = {
            'header' : [
                '종목코드', '종목명', '현재가', '등락부호', '기준가', '전일대비', '등락율',
                '매도거래원명1', '매도거래원1', '매도거래량1', '매수거래원명1', '매수거래원1', '매수거래량1',
                '매도거래원명2', '매도거래원2', '매도거래량2', '매수거래원명2', '매수거래원2', '매수거래량2',
                '매도거래원명3', '매도거래원3', '매도거래량3', '매수거래원명3', '매수거래원3', '매수거래량3',
                '매도거래원명4', '매도거래원4', '매도거래량4', '매수거래원명4', '매수거래원4', '매수거래량4',
                '매도거래원명5', '매도거래원5', '매도거래량5', '매수거래원명5', '매수거래원5', '매수거래량5'
            ],
            'rows' : [[
                self.get_comm_data(tr_code, rq_name, index, '종목코드'),
                self.get_comm_data(tr_code, rq_name, index, '종목명'),
                self.get_comm_data(tr_code, rq_name, index, '현재가'),
                self.get_comm_data(tr_code, rq_name, index, '등락부호'),
                self.get_comm_data(tr_code, rq_name, index, '기준가'),
                self.get_comm_data(tr_code, rq_name, index, '전일대비'),
                self.get_comm_data(tr_code, rq_name, index, '등락율'),
                self.get_comm_data(tr_code, rq_name, index, '매도거래원명1'),
                self.get_comm_data(tr_code, rq_name, index, '매도거래원1'),
                self.get_comm_data(tr_code, rq_name, index, '매도거래량1'),
                self.get_comm_data(tr_code, rq_name, index, '매수거래원명1'),
                self.get_comm_data(tr_code, rq_name, index, '매수거래원1'),
                self.get_comm_data(tr_code, rq_name, index, '매수거래량1'),
                self.get_comm_data(tr_code, rq_name, index, '매도거래원명2'),
                self.get_comm_data(tr_code, rq_name, index, '매도거래원2'),
                self.get_comm_data(tr_code, rq_name, index, '매도거래량2'),
                self.get_comm_data(tr_code, rq_name, index, '매수거래원명2'),
                self.get_comm_data(tr_code, rq_name, index, '매수거래원2'),
                self.get_comm_data(tr_code, rq_name, index, '매수거래량2'),
                self.get_comm_data(tr_code, rq_name, index, '매도거래원명3'),
                self.get_comm_data(tr_code, rq_name, index, '매도거래원3'),
                self.get_comm_data(tr_code, rq_name, index, '매도거래량3'),
                self.get_comm_data(tr_code, rq_name, index, '매수거래원명3'),
                self.get_comm_data(tr_code, rq_name, index, '매수거래원3'),
                self.get_comm_data(tr_code, rq_name, index, '매수거래량3'),
                self.get_comm_data(tr_code, rq_name, index, '매도거래원명4'),
                self.get_comm_data(tr_code, rq_name, index, '매도거래원4'),
                self.get_comm_data(tr_code, rq_name, index, '매도거래량4'),
                self.get_comm_data(tr_code, rq_name, index, '매수거래원명4'),
                self.get_comm_data(tr_code, rq_name, index, '매수거래원4'),
                self.get_comm_data(tr_code, rq_name, index, '매수거래량4'),
                self.get_comm_data(tr_code, rq_name, index, '매도거래원명5'),
                self.get_comm_data(tr_code, rq_name, index, '매도거래원5'),
                self.get_comm_data(tr_code, rq_name, index, '매도거래량5'),
                self.get_comm_data(tr_code, rq_name, index, '매수거래원명5'),
                self.get_comm_data(tr_code, rq_name, index, '매수거래원5'),
                self.get_comm_data(tr_code, rq_name, index, '매수거래량5'),
            ]]
        }

        return ret

    def _opt10002_data_ex(self, tr_code, rq_name):
        ret = {
            'header' : [
                '종목코드', '종목명', '현재가', '등락부호', '기준가', '전일대비', '등락율',
                '매도거래원명1', '매도거래원1', '매도거래량1', '매수거래원명1', '매수거래원1', '매수거래량1',
                '매도거래원명2', '매도거래원2', '매도거래량2', '매수거래원명2', '매수거래원2', '매수거래량2',
                '매도거래원명3', '매도거래원3', '매도거래량3', '매수거래원명3', '매수거래원3', '매수거래량3',
                '매도거래원명4', '매도거래원4', '매도거래량4', '매수거래원명4', '매수거래원4', '매수거래량4',
                '매도거래원명5', '매도거래원5', '매도거래량5', '매수거래원명5', '매수거래원5', '매수거래량5'
            ],
            'rows' : self.get_comm_data_ex(tr_code, rq_name)
        }

        return ret


    #  [ opt10003 : 체결정보요청 ]
    def opt10003(self, code, prev_next, screen_no):
        rq_name = tr_code = "opt10003"

        self.set_input_value("종목코드", code)
        self.comm_rq_data(rq_name, tr_code, prev_next, screen_no)

        return self.receive_tr_data_handler

    def _opt10003_data(self, tr_code, rq_name, index):
        ret = {
            'header' : [
                '시간', '현재가', '전일대비', '대비율', '우선매도호가단위', '우선매수호가단위',
                '체결거래량', 'sign', '누적거래량', '누적거래대금', '체결강도'
            ],
            'rows' : [[
                self.get_comm_data(tr_code, rq_name, index, '시간'),
                self.get_comm_data(tr_code, rq_name, index, '현재가'),
                self.get_comm_data(tr_code, rq_name, index, '전일대비'),
                self.get_comm_data(tr_code, rq_name, index, '대비율'),
                self.get_comm_data(tr_code, rq_name, index, '우선매도호가단위'),
                self.get_comm_data(tr_code, rq_name, index, '우선매수호가단위'),
                self.get_comm_data(tr_code, rq_name, index, '체결거래량'),
                self.get_comm_data(tr_code, rq_name, index, 'sign'),
                self.get_comm_data(tr_code, rq_name, index, '누적거래량'),
                self.get_comm_data(tr_code, rq_name, index, '누적거래대금'),
                self.get_comm_data(tr_code, rq_name, index, '체결강도'),
            ]]
        }

        return ret

    def _opt10003_data_ex(self, tr_code, rq_name):
        ret = {
            'header' : [
                '시간', '현재가', '전일대비', '대비율', '우선매도호가단위', '우선매수호가단위',
                '체결거래량', 'sign', '누적거래량', '누적거래대금', '체결강도'
            ],
            'rows' : self.get_comm_data_ex(tr_code, rq_name)
        }

        return ret


