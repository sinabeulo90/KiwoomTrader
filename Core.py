from __future__ import
    absolute_import, division,
    print_function, unicode_literals

from builtins import
    bytes, dict, int, list, object, range, str,
    ascii, chr, hex, input, next, oct, open,
    pow, round, super,
    filter, map, zip

import sys
import time
import datetime
import os

import pandas as pd
import numpy as np

from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *

class Kiwoom_Event_Handler:
    def event_connect(self, error_code):
        print(error_code['description'])



class Kiwoom(QAxWidget):

    def __init__(self):
        super().__init__()
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")
        self.init_connect_events()


    def init_connect_events(self):
        self.OnEventConnect.connect(self.signal_event_connect)
        self.OnReceiveTrData.connect(self.signal_event_receive_tr_data)

    # Kiwoom Method
    def comm_connect(self):
        """
        설명
            - 로그인 윈도우 실행
        반환값
            - 0 : 성공
            - 1 : 실패
        """
        self.dynamicCall("CommConnect()")
        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()


    def comm_rq_data(self, rqname, trcode, prev_next, screen_no):
        """
        설명
            - Tran을 서버로 송신
        입력값
            - rqname : 사용자구분 명
            - trcode : Trans명 입력
            - prev_next : 0(조회), 2(연속)
            - screen_no : 4자리의 화면번호
        반환값
            - OP_ERR_SISE_OVERFLOW : 과도한 시세조회로 인한 통신불가
            - OP_ERR_RQ_STRUCT_FAIL : 입력 구조체 생성 실패
            - OP_ERR_RQ_STRING_FAIL : 요청전문 작성 실패
            - OP_ERR_NONE : 정상처리
        """
        self.dynamicCall("CommRqData(QString, QString, int, QString", rqname, trcode, prev_next, screen_no)
        self.tr_event_loop = QEventLoop()
        self.tr_event_loop.exec_()

    
    def _TODO_get_login_info(self, tag):
        """
        설명
            - 로그인한 사용자 정보를 반환
        입력값
            - tag : 사용자 정보 구분값
                - "ACCOUNT_CNT" : 전체 계좌 개수를 반환한다.
                - "ACCNO"   : 전체 계좌를 반환한다. 계좌별 구분은 ‘;’이다.
                - "USER_ID" : 사용자 ID를 반환한다.
                - "USER_NAME" : 사용자명을 반환한다.
                - "KEY_BSECGB" :  키보드보안 해지여부. 0:정상, 1:해지
                - "FIREW_SECGB" : 방화벽 설정 여부. 0:미설정, 1:설정, 2:해지
        """
        self.dynamicCall("GetLoginInfo(Qstring)", tag)
        # TODO: event_loop 설정

    
    def _TODO_send_order(self, rqname, screen_no, account_no, order_type, code, qty, price, hoga_gb, org_order_no):
        """
        설명
            - 주식 주문을 서버로 전송
        입력값
            - rqname : 사용자 구부 요청 명
            - screen_no : 화면 번호
            - account_no : 계좌번호
            - order_type : 주문유형
                - 1 :신규매수, 2:신규매도, 3:매수취소, 4:매도취소, 5:매수정정, 6:매도정정
            - code : 주식종목코드
            - qty : 주문수량
            - price : 주문단가
            - hoga_gb : 거래구분
                - 00:지정가, 03:시장가, 05:조건부지정가, 06:최유리지정가, 07:최우선지정가, 10:지정 가IOC, 13:시장가IOC, 16:최유리IOC, 20:지정가FOK, 23:시장가FOK, 26:최유리FOK, 61:장전시간 외종가, 62:시간외단일가, 81:장후시간외종가
                * 시장가, 최유리지정가, 최우선지정가, 시장가IOC, 최유리IOC, 시장가FOK, 최유리FOK, 장전시 간외, 장후시간외 주문시 주문가격을 입력하지 않습니다.
            - org_order_no : 원주문번호
        반환값
            - 에러코드
        """
        self.dynamicCall("SendOrder(QString, QString, QString, int, QString, int, int, QString, QString)", tag, screen_no, account_no, order_type, code, qty, price, hoga_gb, org_order_no)
        # TODO: event_loop 설정


    def get_code_list_by_market(self, market):
        time.sleep(0.4)
        ret = self.dynamicCall("GetCodeListByMarket(QString)", market)
        
        return ret.strip().split(';')

    def set_input_value(self, id, value):
        self.dynamicCall(
            "SetInputValue(QString, QString)",
            id, value
        )
        
    def signal_event_connect(self, status_code):
        print(status_code["description"])
        self.login_event_loop.exit()
        

    def _get_comm_data(self, code, record_name, index, item_name):
        time.sleep(0.4)
        ret = self.dynamicCall("GetCommData(QString, QString, int, QString", [code,
                               record_name, index, item_name])
        return ret.strip()

    
    def _get_comm_data_ex(self, code, record_name):
        time.sleep(0.4)
        ret = self.dynamicCall("GetCommDataEx(QString, QString", [code, record_name])
        return ret

    
    def _comm_get_data(self, code, real_type, field_name, index, item_name):
        time.sleep(0.4)
        ret = self.dynamicCall("CommGetData(QString, QString, QString, int, QString", code,
                               real_type, field_name, index, item_name)
        return ret.strip()
    
    def call_get_repeat_cnt(self, trcode, rqname):
        time.sleep(0.4)
        ret = self.dynamicCall("GetRepeatCnt(QString, QString)", trcode, rqname)
        
        return ret

    def _receive_tr_data(self, screen_no, rqname, trcode, record_name, next, unused1, unused2, unused3, unused4):
        if next == '2':
            self.remained_data = True
        else:
            self.remained_data = False

        if rqname == "opt10081_req":
            self._opt10081(rqname, trcode)
        elif rqname == "opt10060_req":
            self._opt10060(rqname, trcode)
        elif rqname == "opt10060_ex_req":
            self._opt10060_ex(rqname, trcode)

        try:
            self.tr_event_loop.exit()
        except AttributeError:
            pass

    def _opt10060(self, rqname, trcode):
        data_cnt = self._get_repeat_cnt(trcode, rqname)
        
        columns = [
            "일자", "현재가", "전일대비", "누적거래대금",
            "개인투자자", "외국인투자자", "기관계", "금융투자",
            "보험", "투신", "기타금융", "은행", "연기금등", "사모펀드",
            "국가", "기타법인", "내외국인"
        ]
        
        self.df = pd.DataFrame(columns=columns)
        
        for i in range(data_cnt):
            self.df.loc[i] = [
              self._get_comm_data(trcode, rqname, i, "일자"),
              self._get_comm_data(trcode, rqname, i, "현재가"),
              self._get_comm_data(trcode, rqname, i, "전일대비"),
              self._get_comm_data(trcode, rqname, i, "누적거래대금"),
              self._get_comm_data(trcode, rqname, i, "개인투자자"),
              self._get_comm_data(trcode, rqname, i, "외국인투자자"),
              self._get_comm_data(trcode, rqname, i, "기관계"),
              self._get_comm_data(trcode, rqname, i, "금융투자"),
              self._get_comm_data(trcode, rqname, i, "보험"),
              self._get_comm_data(trcode, rqname, i, "투신"),
              self._get_comm_data(trcode, rqname, i, "기타금융"),
              self._get_comm_data(trcode, rqname, i, "은행"),
              self._get_comm_data(trcode, rqname, i, "연기금등"),
              self._get_comm_data(trcode, rqname, i, "사모펀드"),
              self._get_comm_data(trcode, rqname, i, "국가"),
              self._get_comm_data(trcode, rqname, i, "기타법인"),
              self._get_comm_data(trcode, rqname, i, "내외국인")
            ]

    def _opt10060_ex(self, rqname, trcode):
        df_list = self._get_comm_data_ex(trcode, rqname)

        columns = [
            "일자", "현재가", "전일대비", "누적거래대금",
            "개인투자자", "외국인투자자", "기관계", "금융투자",
            "보험", "투신", "기타금융", "은행", "연기금등", "사모펀드",
            "국가", "기타법인", "내외국인"
        ]
        
        self.df = pd.DataFrame(df_list, columns=columns)
        
        self.df_list = df_list
