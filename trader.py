#-*- coding: utf-8 -*-

from PyQt5.QAxContainer import *

from core import KWCore
from constants import KWErrorCode

class KWTrader(KWCore):

    def initialize(self):
        self.tr_list["opt10001"] = self._opt10001_data

    def connection(self):
        self.comm_connect()


    # [ opt10001 : 주식기본정보요청 ]
    def opt10001(self, code, pre_next, screen_no):
        rq_name = "RQName"
        tr_code = "opt10001"
        self.set_input_value("종목코드", code)
        self.comm_rq_data(rq_name, tr_code, pre_next, screen_no)
        
        handler = self.receive_tr_data_handler
        return handler
    
    def _opt10001_data(self, tr_code, rq_name):
        ret = {
            '종목코드': self.get_comm_data(tr_code, rq_name, 0, "종목코드"),
            '종목명': self.get_comm_data(tr_code, rq_name, 0, "종목명"),
            '결산월': self.get_comm_data(tr_code, rq_name, 0, "결산월"),
            '액면가': self.get_comm_data(tr_code, rq_name, 0, "액면가"),
            '자본금': self.get_comm_data(tr_code, rq_name, 0, "자본금"),
            '상장주식': self.get_comm_data(tr_code, rq_name, 0, "상장주식"),
            '신용비율': self.get_comm_data(tr_code, rq_name, 0, "신용비율"),
            '연중최고': self.get_comm_data(tr_code, rq_name, 0, "연중최고"),
            '연중최저': self.get_comm_data(tr_code, rq_name, 0, "연중최저"),
            '시가총액': self.get_comm_data(tr_code, rq_name, 0, "시가총액"),
            '시가총액비중': self.get_comm_data(tr_code, rq_name, 0, "시가총액비중"),
            '외인소진률': self.get_comm_data(tr_code, rq_name, 0, "외인소진률"),
            '대용가': self.get_comm_data(tr_code, rq_name, 0, "대용가"),
            'PER': self.get_comm_data(tr_code, rq_name, 0, "PER"),
            'EPS': self.get_comm_data(tr_code, rq_name, 0, "EPS"),
            'ROE': self.get_comm_data(tr_code, rq_name, 0, "ROE"),
            'PBR': self.get_comm_data(tr_code, rq_name, 0, "PBR"),
            'EV': self.get_comm_data(tr_code, rq_name, 0, "EV"),
            'BPS': self.get_comm_data(tr_code, rq_name, 0, "BPS"),
            '매출액': self.get_comm_data(tr_code, rq_name, 0, "매출액"),
            '영업이익': self.get_comm_data(tr_code, rq_name, 0, "영업이익"),
            '당기순이익': self.get_comm_data(tr_code, rq_name, 0, "당기순이익"),
            '250최고': self.get_comm_data(tr_code, rq_name, 0, "250최고"),
            '250최저': self.get_comm_data(tr_code, rq_name, 0, "250최저"),
            '시가': self.get_comm_data(tr_code, rq_name, 0, "시가"),
            '고가': self.get_comm_data(tr_code, rq_name, 0, "고가"),
            '저가': self.get_comm_data(tr_code, rq_name, 0, "저가"),
            '상한가': self.get_comm_data(tr_code, rq_name, 0, "상한가"),
            '하한가': self.get_comm_data(tr_code, rq_name, 0, "하한가"),
            '기준가': self.get_comm_data(tr_code, rq_name, 0, "기준가"),
            '예상체결가': self.get_comm_data(tr_code, rq_name, 0, "예상체결가"),
            '예상체결수량': self.get_comm_data(tr_code, rq_name, 0, "예상체결수량"),
            '250최고가일': self.get_comm_data(tr_code, rq_name, 0, "250최고가일"),
            '250최고가대비율': self.get_comm_data(tr_code, rq_name, 0, "250최고가대비율"),
            '250최저가일': self.get_comm_data(tr_code, rq_name, 0, "250최저가일"),
            '250최저가대비율': self.get_comm_data(tr_code, rq_name, 0, "250최저가대비율"),
            '현재가': self.get_comm_data(tr_code, rq_name, 0, "현재가"),
            '대비기호': self.get_comm_data(tr_code, rq_name, 0, "대비기호"),
            '전일대비': self.get_comm_data(tr_code, rq_name, 0, "전일대비"),
            '등락율': self.get_comm_data(tr_code, rq_name, 0, "등락율"),
            '거래량': self.get_comm_data(tr_code, rq_name, 0, "거래량"),
            '거래대비': self.get_comm_data(tr_code, rq_name, 0, "거래대비"),
            '액면가단위': self.get_comm_data(tr_code, rq_name, 0, "액면가단위"),
            '유통주식': self.get_comm_data(tr_code, rq_name, 0, "유통주식"),
            '유통비율': self.get_comm_data(tr_code, rq_name, 0, "유통비율")
        }

        return ret