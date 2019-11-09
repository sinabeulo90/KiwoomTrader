#-*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division,
    print_function, unicode_literals
)

from builtins import (
    bytes, dict, int, list, object, range, str,
    ascii, chr, hex, input, next, oct, open,
    pow, round, super,
    filter, map, zip
)

import sys
import time
import datetime
import os

import pandas as pd
import numpy as np

from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *

from constants import KWErrorCode

class KWCore(QAxWidget):

    tr_list = {}

    def __init__(self):
        super().__init__()
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")
        self._init_connect_events()


    def _init_connect_events(self):
        # 서버 접속 관련 이벤트
        self.loop_event_connect = QEventLoop()
        self.OnEventConnect.connect(self.on_event_connect)

        # 서버통신 후 데이터를 받은 시점을 알려준다.
        self.response_comm_rq_data = None
        self.receive_tr_data_handler = None
        self.loop_receive_tr_data = QEventLoop()
        self.OnReceiveTrData.connect(self.on_receive_tr_data)

        # 실시간데이터를 받은 시점을 알려준다.
        self.loop_receive_real_data = QEventLoop()
        self.OnReceiveRealData.connect(self.on_receive_real_data)

        # 서버통신 후 메시지를 받은 시점을 알려준다.
        self.loop_receive_msg = QEventLoop()
        self.OnReceiveMsg.connect(self.on_receive_msg)

        # 체결데이터를 받은 시점을 알려준다.
        self.loop_receive_chejan_data = QEventLoop()
        self.OnReceiveChejanData.connect(self.on_receive_chejan_data)

        # 조건검색 실시간 편입,이탈 종목을 받을 시점을 알려준다.
        self.loop_receive_condition = QEventLoop()
        self.OnReceiveRealCondition.connect(self.on_receive_condition)

        # 조건검색 조회응답으로 종목리스트를 구분자(";")로 붙어서 받는 시점.
        self.loop_receive_tr_condition = QEventLoop()
        self.OnReceiveTrCondition.connect(self.on_receive_tr_condition)

        # 로컬에 사용자 조건식 저장 성공 여부를 확인하는 시점
        self.loop_receive_condition_ver = QEventLoop()
        self.OnReceiveConditionVer.connect(self.on_receive_condition_ver)


    # SECTION 1) CommConnect
    def comm_connect(self):
        """
        원형 : LONG CommConnect()
        설명 : 로그인 윈도우 실행
        반환값 : 0 - 성공, 음수값은 실패
        비고 : 로그인이 성공하거나 실패하는 경우 OnEventConnect 이벤트가 발생하고 이벤트의 인자 값으로 로그인 성공 여부를 알 수 있다.
        """
        self.dynamicCall("CommConnect()")
        self.loop_event_connect.exec_()
    # !SECTION


    # SECTION 3) CommRqData -> on_receive_tr_data
    def comm_rq_data(self, rq_name, tr_code, prev_next, screen_no):
        """
        원형 : LONG CommRqData(BSTR sRQName, BSTR sTrCode, long nPrevNext, BSTR sScreenNo)
        설명 : Tran을 서버로 송신한다.
        입력값 :
            BSTR sRQName
            BSTR sTrCode
            long nPrevNext
            BSTR sScreenNo
        반환값
            OP_ERR_SISE_OVERFLOW - 과도한 시세조회로 인한 통신불가
            OP_ERR_RQ_STRUCT_FAIL - 입력 구조체 생성 실패
            OP_ERR_RQ_STRING_FAIL - 요청전문 작성 실패
            OP_ERR_NONE - 정상처리
        비고
            sRQName – 사용자구분 명
            sTrCode - Tran명 입력
            nPrevNext - 0:조회, 2:연속
            sScreenNo - 4자리의 화면번호
            Ex) openApi.CommRqData( "RQ_1", "OPT00001", 0, "0101");
        """
        self.response_comm_rq_data = self.dynamicCall("CommRqData(QString, QString, int, QString", rq_name, tr_code, prev_next, screen_no)
        self.loop_receive_tr_data.exec_()
    # !SECTION 


    # SECTION 4) GetLoginInfo
    def get_login_info(self, tag):
        """
        원형 : BSTR GetLoginInfo(BSTR sTag)
        설명 : 로그인한 사용자 정보를 반환한다.
        입력값 : BSTR sTag : 사용자 정보 구분 TAG값 (비고)
        반환값 : TAG값에 따른 데이터 반환
        비고 :
            BSTRsTag에 들어 갈 수 있는 값은 아래와 같음
            "ACCOUNT_CNT" – 전체 계좌 개수를 반환한다.
            "ACCNO" – 전체 계좌를 반환한다. 계좌별 구분은 ';'이다.
            "USER_ID" - 사용자 ID를 반환한다.
            "USER_NAME" – 사용자명을 반환한다.
            "KEY_BSECGB" – 키보드보안 해지여부. 0:정상, 1:해지
            "FIREW_SECGB" – 방화벽 설정 여부. 0:미설정, 1:설정, 2:해지
            Ex) openApi.GetLoginInfo("ACCOUNT_CNT");
        """
        return self.dynamicCall("GetLoginInfo(QString)", tag)
    # !SECTION


    # 5) SendOrder
    def _TODO_send_order(self, rq_name, screen_no, account_no, order_type, code, qty, price, hoga_gb, org_order_no):
        """
        원형 : LONG SendOrder(
                BSTR sRQName,
                BSTR sScreenNo,
                BSTR sAccNo,
                LONG nOrderType,
                BSTR sCode,
                LONG nQty,
                LONG nPrice,
                BSTR sHogaGb, BSTR sOrgOrderNo
            )
        설명 : 주식 주문을 서버로 전송한다.
        입력값 :
            sRQName - 사용자 구분 요청 명
            sScreenNo - 화면번호[4]
            sAccNo - 계좌번호[10]
            nOrderType - 주문유형 (1:신규매수, 2:신규매도, 3:매수취소, 4:매도취소, 5:매수정정, 6:매도정정)
            sCode, - 주식종목코드
            nQty – 주문수량
            nPrice – 주문단가
            sHogaGb - 거래구분
            sOrgOrderNo – 원주문번호
        반환값 : 에러코드 <4.에러코드표 참고>
        비고 :
            sHogaGb – 00:지정가, 03:시장가, 05:조건부지정가, 06:최유리지정가, 07:최우선지정가, 10:지정 가IOC, 13:시장가IOC, 16:최유리IOC, 20:지정가FOK, 23:시장가FOK, 26:최유리FOK, 61:장전시간 외종가, 62:시간외단일가, 81:장후시간외종가
            ※ 시장가, 최유리지정가, 최우선지정가, 시장가IOC, 최유리IOC, 시장가FOK, 최유리FOK, 장전시 간외, 장후시간외 주문시 주문가격을 입력하지 않습니다.
            Ex) 지정가 매수 - openApi.SendOrder("RQ_1", "0101", "5015123410", 1, "000660", 10, 48500, "00", "");
                시장가 매수 - openApi.SendOrder("RQ_1", "0101", "5015123410", 1, "000660", 10, 0, "03", "");
                매수 정정 - openApi.SendOrder("RQ_1","0101", "5015123410", 5, "000660", 10, 49500, "00", "1");
                매수 취소 - openApi.SendOrder("RQ_1", "0101", "5015123410", 3, "000660", 10, 0, "00", "2");
        """
        self.dynamicCall("SendOrder(QString, QString, QString, int, QString, int, int, QString, QString)", tag, screen_no, account_no, order_type, code, qty, price, hoga_gb, org_order_no)
        # TODO: event_loop 설정


    # 6) SendOrderCredit
    def _TODO_send_order_credit(self, rq_name, screen_no, acc_no, order_type, code, qty, price, hoga_gb, credit_gb, loan_date, org_order_no):
        """
        원형 : LONG SendOrderCredit(
                LPCTSTR sRQName,
                LPCTSTR sScreenNo,
                LPCTSTR sAccNo,
                LONG nOrderType,
                LPCTSTR sCode,
                LONG nQty,
                LONG nPrice,
                LPCTSTR sHogaGb,
                LPCTSTR sCreditGb,
                LPCTSTR sLoanDate,
                LPCTSTR sOrgOrderNo
            )
        설명 : 신용주식 주문을 서버로 전송한다.
        입력값 :
            sRQName - 사용자 구분 요청 명
            sScreenNo - 화면번호[4]
            sAccNo - 계좌번호[10]
            nOrderType - 주문유형 (1:신규매수, 2:신규매도, 3:매수취소, 4:매도취소, 5:매수정정, 6:매도정정)
            sCode - 주식종목코드
            nQty – 주문수량
            nPrice – 주문단가
            sHogaGb – 거래구분
            sCreditGb – 신용구분
            sLoanDate – 대출일
            sOrgOrderNo – 원주문번호
        반환값 : 에러코드 <4.에러코드표 참고>
        비고 :
            sCreditGb – 신용구분 (신용매수:03, 신용매도 융자상환:33,신용매도 융자합:99)
            신용매수 주문
                - 신용구분값 "03", 대출일은 "공백"
            신용매도 융자상환 주문
                - 신용구분값 "33", 대출일은 종목별 대출일 입력
                - OPW00005/OPW00004 TR조회로 대출일 조회
            신용매도 융자합 주문시
                - 신용구분값 "99", 대출일은 "99991231"
                - 단 신용잔고 5개까지만 융자합 주문가능

            나머지 입력값은 SendOrder()함수 설명참고
        """
        self.dynamicCall("SendOrderCredit(QString, QString, QString, int, QString, int, int, QString, QString)", rq_name, screen_no, acc_no, order_type, code, qty, price, hoga_gb, credit_gb, loan_date, org_order_no)
        # TODO: event_loop 설정


    # SECTION 7) SetInputValue
    def set_input_value(self, id, value):
        """
        원형 : void SetInputValue(BSTR sID, BSTR sValue)
        설명 : Tran 입력 값을 서버통신 전에 입력한다.
        입력값 :
            sID – 아이템명
            sValue – 입력 값
        반환값 : 없음
        비고 :
            Ex) openApi.SetInputValue("종목코드", "000660");
                openApi.SetInputValue("계좌번호", "5015123401");
        """
        self.dynamicCall("SetInputValue(QString, QString)", id, value)
    # !SECTION 


    # TODO 테스트 필요
    # 10) DisconnectRealData
    def disconnect_real_data(self, screen_no):
        """
        원형 : void DisconnectRealData(LPCTSTR sScnNo)
        설명 : 화면 내 모든 리얼데이터 요청을 제거한다.
        입력값 : sScnNo – 화면번호[4]
        반환값 : 없음
        비고 :
            화면을 종료할 때 반드시 위 함수를 호출해야 한다.
            Ex) openApi.DisconnectRealData("0101");
        """
        self.dynamicCall("DisconnectRealData(QString)", screen_no)


    # TODO 테스트 필요
    # 11) GetRepeatCnt
    def get_repeat_cnt(self, tr_code, record_name):
        """
        원형 : LONG GetRepeatCnt(LPCTSTR sTrCode, LPCTSTR sRecordName)
        설명 : 레코드 반복횟수를 반환한다.
        입력값 :
            sTrCode – Tran 명
            sRecordName – 레코드 명
        반환값 : 레코드의 반복횟수
        비고 : Ex) openApi.GetRepeatCnt("OPT00001", "주식기본정보");
        """
        return self.dynamicCall("GetRepeatCnt(QString, QString)", tr_code, record_name)


    # 12) CommKwRqData
    def _TODO_comm_kw_rq_data(self, arr_code, next, code_count, type_flag, rq_name, screen_no):
        """
        원형 : LONG CommKwRqData(LPCTSTR sArrCode, BOOL bNext, int nCodeCount, int nTypeFlag, LPCTSTR sRQName, LPCTSTR sScreenNo)
        설명 : 복수종목조회 Tran을 서버로 송신한다.
        입력값 :
            sArrCode – 종목리스트
            bNext – 연속조회요청
            nCodeCount – 종목개수
            nTypeFlag – 조회구분
            sRQName – 사용자구분 명
            sScreenNo – 화면번호[4]
        반환값 :
            OP_ERR_RQ_STRING – 요청 전문 작성 실패
            OP_ERR_NONE - 정상처리
        비고 :
            sArrCode – 종목간 구분은 ';'이다.
            nTypeFlag – 0:주식관심종목정보, 3:선물옵션관심종목정보
            Ex) openApi.CommKwRqData("000660;005930", 0, 2, 0, "RQ_1", "0101");
        """
        self.dynamicCall("CommKwRqData(QString, bool, int, int, QString, QString)", arr_code, next, code_count, type_flag, rq_name, screen_no)
        # TODO: event_loop 설정


    # SECTION 13) GetAPIModulePath
    def get_api_module_path(self):
        """
        원형 : BSTR GetAPIModulePath()
        설명 : OpenAPI모듈의 경로를 반환한다.
        입력값 : 없음
        반환값 : 경로
        """
        return self.dynamicCall("GetAPIModulePath()")
    # !SECTION


    # SECTION 14) GetCodeListByMarket
    def get_code_list_by_market(self, market):
        """
        원형 : BSTR GetCodeListByMarket(LPCTSTR sMarket)
        설명 : 시장구분에 따른 종목코드를 반환한다.
        입력값 : sMarket – 시장구분
        반환값 : 종목코드 리스트, 종목간 구분은 ';'이다.
        비고 : sMarket – 0:장내, 3:ELW, 4:뮤추얼펀드, 5:신주인수권, 6:리츠, 8:ETF, 9:하이일드펀드, 10:코스닥, 30:K-OTC, 50:코넥스(KONEX)
        """
        ret = self.dynamicCall("GetCodeListByMarket(QString)", market)

        return ret.strip().split(';')
    # !SECTION


    # SECTION 15) GetConnectState
    def get_connect_state(self):
        """
        원형 : LONG GetConnectState()
        설명 : 현재접속상태를 반환한다.
        입력값 : 없음
        반환값 : 접속상태
        비고 : 0:미연결, 1:연결완료
        """
        return self.dynamicCall("GetConnectState()")
    # !SECTION


    # SECTION 16) GetMasterCodeName
    def get_master_code_name(self, code):
        """
        원형 : BSTR GetMasterCodeName(LPCTSTR strCode)
        설명 : 종목코드의 한글명을 반환한다.
        입력값 : strCode – 종목코드
        반환값 : 종목한글명
        비고 : 장내외, 지수선옵, 주식선옵 검색 가능.
        """
        return self.dynamicCall("GetMasterCodeName(QString)", code)
    # !SECTION


    # SECTION 17) GetMasterListedStockCnt
    def get_master_listed_stock_cnt(self, code):
        """
        원형 : LONG GetMasterListedStockCnt(LPCTSTR strCode)
        설명 : 종목코드의 상장주식수를 반환한다.
        입력값 : strCode – 종목코드
        반환값 : 상장주식수
        """
        return self.dynamicCall("GetMasterListedStockCnt(QString)", code)
    # !SECTION


    # SECTION 18) GetMasterConstruction
    def get_master_construction(self, code):
        """
        원형 : BSTR GetMasterConstruction(LPCTSTR strCode)
        설명 : 종목코드의 감리구분을 반환한다.
        입력값 : strCode - 종목코드
        반환값 : 감리구분
        비고 : 감리구분 - 정상, 투자주의, 투자경고, 투자위험, 투자주의환기종목
        """
        return self.dynamicCall("GetMasterConstruction(QString)", code)
    # !SECTION


    # SECTION 19) GetMasterListedStockDate
    def get_master_listed_stock_date(self, code):
        """
        원형 : BSTR GetMasterListedStockDate(LPCTSTR strCode)
        설명 : 종목코드의 상장일을 반환한다.
        입력값 : strCode – 종목코드
        반환값 : 상장일
        비고 :상장일 포멧 – xxxxxxxx[8]
        """
        return self.dynamicCall("GetMasterListedStockDate(QString)", code)
    # !SECTION


    # SECTION 20) GetMasterLastPrice
    def get_master_last_price(self, code):
        """
        원형 : BSTR GetMasterLastPrice(LPCTSTR strCode)
        설명 : 종목코드의 전일가를 반환한다.
        입력값 : strCode – 종목코드
        반환값 : 전일가
        """
        return self.dynamicCall("GetMasterLastPrice(QString)", code)
    # !SECTION


    # SECTION 21) GetMasterStockState
    def get_master_stock_state(self, code):
        """
        원형 : BSTR GetMasterStockState(LPCTSTR strCode)
        설명 : 종목코드의 종목상태를 반환한다.
        입력값 : strCode – 종목코드
        반환값 : 종목상태
        비고 : 종목상태 – 정상, 증거금100%, 거래정지, 관리종목, 감리종목, 투자유의종목, 담보대출, 액면분할, 신용가능
        """
        return self.dynamicCall("GetMasterStockState(QString)", code)
    # !SECTION


    # 22) GetDataCount
    def _TODO_get_data_count(self, record_name):
        """
        원형 : LONG GetDataCount(LPCTSTR strRecordName)
        설명 : 레코드의 반복개수를 반환한다.
        입력값 : strRecordName – 레코드명
        반환값 : 레코드 반복개수
        비고 : Ex) openApi.GetDataCount("주식기본정보");
        """
        pass


    # 23) GetOutputValue
    def _TODO_get_output_value(self, record_name, repeat_idx, item_idx):
        """
        원형 : BSTR GetOutputValue(LPCTSTR strRecordName, long nRepeatIdx, long nItemIdx)
        설명 : 레코드의 반복순서와 아이템의 출력순서에 따라 수신데이터를 반환한다.
        입력값 :
            nRepeatIdx – 반복순서
            nItemIdx – 아이템 순서
        반환값 : 수신 데이터
        비고 : Ex) 현재가출력 - openApi.GetOutputValue("주식기본정보", 0, 36);
        """
        pass


    # 24) GetCommData
    def get_comm_data(self, tr_code, record_name, index, item_name):
        """
        원형 : BSTR GetCommData(LPCTSTR strTrCode, LPCTSTR strRecordName, long nIndex, LPCTSTR strItemName)
        설명 : 수신 데이터를 반환한다.
        입력값 :
            strTrCode – Tran 코드
            strRecordName – 레코드명
            nIndex – 복수데이터 인덱스
            strItemName – 아이템명
        반환값 : 수신 데이터
        비고 : Ex)현재가출력 - openApi.GetCommData("OPT00001", "주식기본정보", 0, "현재가");
        """
        return self.dynamicCall("GetCommData(QString, QString, int, QString)", tr_code, record_name, index, item_name).strip()


    # 25) GetCommRealData
    def _TODO_get_comm_real_data(self, code, fid):
        """
        원형 : BSTR GetCommRealData(LPCTSTR strCode, long nFid)
        설명 : 실시간 시세 데이터를 반환한다.
        입력값 :
            strCode – 종목코드
            nFid – 실시간 아이템
        반환값 : 수신 데이터
        비고 :
            Ex) 현재가출력 - openApi.GetCommRealData("039490", 10);
            참고) strCode는 OnReceiveRealData 첫번째 매개변수를 사용
        """
        pass


    # 26) GetChejanData
    def _TODO_get_chejan_data(self, fid):
        """
        원형 : BSTR GetChjanData(long nFid)
        설명 : 체결잔고 데이터를 반환한다.
        입력값 : nFid – 체결잔고 아이템
        반환값 : 수신 데이터
        비고 : Ex) 현재가출력 – openApi.GetChejanData(10);
        """
        pass


    # SECTION 27) GetThemeGroupList
    def get_theme_group_list(self, type):
        """
        원형 : BSTR GetThemeGroupList(long nType)
        설명 : 테마코드와 테마명을 반환한다.
        입력값 : nType – 정렬순서 (0:코드순, 1:테마순)
        반환값 : 코드와 코드명 리스트
        비고 :
            반환값의 코드와 코드명 구분은 '|' 코드의 구분은 ';'
            Ex) 100|태양광_폴리실리콘;152|합성섬유
        """
        return self.dynamicCall("GetThemeGroupList(int)", type)
    # !SECTION


    # 28) GetThemeGroupCode
    def _TODO_get_theme_group_code(self, theme_code):
        """
        원형 : BSTR GetThemeGroupCode(LPCTSTR strThemeCode)
        설명 : 테마코드에 소속된 종목코드를 반환한다.
        입력값 : strThemeCode – 테마코드
        반환값 : 종목코드 리스트
        비고 :
            반환값의 종목코드간 구분은 ';'
            Ex) A000660;A005930
        """
        pass


    # SECTION 29) GetFutureList
    def get_future_list(self):
        """
        원형 : BSTR GetFutureList()
        설명 : 지수선물 리스트를 반환한다.
        반환값 : 종목코드 리스트
        비고 :
            반환값의 종목코드간 구분은 ';'
            Ex) 101J9000;101JC000
        """
        return self.dynamicCall("GetFutureList()")
    # !SECTION


    # SECTION 30) GetFutureCodeByIndex
    def get_future_code_by_index(self, index):
        """
        원형 : BSTR GetFutureCodeByIndex(int nIndex)
        설명 : 지수선물 코드를 반환한다.
        입력값 : nIndex – 0~3 지수선물코드, 4~7 지수스프레드
        반환값 : 종목코드
        비고 :
            Ex) 최근월선물 - openApi.GetFutureCodeByIndex(0);
                최근월스프레드 - openApi.GetFutureCodeByIndex(4);
        """
        return self.dynamicCall("GetFutureCodeByIndex(int)", index)
    # !SECTION


    # SECTION 31) GetActPriceList
    def get_act_price_list(self):
        """
        원형 : BSTR GetActPriceList()
        설명 : 지수옵션 행사가 리스트를 반환한다.
        반환값 : 행사가
        비고 : 반환값의 행사가간 구분은 ';' Ex) 265.00;262.50;260.00
        """
        return self.dynamicCall("GetActPriceList()")
    # !SECTION


    # SECTION 32) GetMonthList
    def get_month_list(self):
        """
        원형 : BSTR GetMonthList()
        설명 : 지수옵션 월물 리스트를 반환한다.
        반환값 : 월물
        비고 :
            반환값의 월물간 구분은 ';'
            Ex) 201412;201409;201408;201407;201407;201408;201409;201412
        """
        return self.dynamicCall("GetMonthList()")
    # !SECTION


    # 33) GetOptionCode
    def _TODO_get_option_code(self, act_price, cp, month):
        """
        원형 : BSTR GetOptionCode(LPCTSTR strActPrice, int nCp, LPCTSTR strMonth)
        설명 : 행사가와 월물 콜풋으로 종목코드를 구한다.
        입력값 :
            strActPrice – 행사가(소수점포함)
            nCp – 콜풋구분 2:콜, 3:풋
            strMonth – 월물(6자리)
        반환값 : 종목코드
        비고 : Ex) openApi.GetOptionCode("260.00", 2, "201407");
        """
        pass


    # 34) GetOptionCodeByMonth
    def _TODO_get_option_code_by_month(self, code, cp, month):
        """
        원형 : BSTR GetOptionCodeByMonth(LPCTSTR strCode, int nCp, LPCTSTR strMonth)
        설명 : 입력된 종목코드와 동일한 행사가의 코드중 입력한 월물의 코드를 구한다.
        입력값 :
            strCode – 종목코드
            nCp – 콜풋구분 2:콜, 3:풋
            strMonth – 월물(6자리)
        반환값 : 종목코드
        비고 :
            Ex) openApi.GetOptionCodeByMonth("201J7260", 2, "201412");
            결과값 = 201JC260
        """
        pass


    # 35) GetOptionCodeByActPrice
    def _TODO_get_option_code_by_act_price(self, code, cp, tick):
        """
        원형 : BSTR GetOptionCodeByActPrice(LPCTSTR strCode, int nCp, int Tick)
        설명 : 입력된 종목코드와 동일한 월물의 코드중 입력한 틱만큼 벌어진 코드를 구한다.
        입력값 :
            strCode – 종목코드
            nCp – 콜풋구분 2:콜, 3:풋
            nTick – 행사가 틱
        반환값 : 종목코드
        비고 :
            Ex) openApi.GetOptionCodeByActPrice("201J7260", 2, -1);
            결과값 = 201J7262
        """
        pass


    # 36) GetSFutureList
    def _TODO_get_s_future_list(self, base_asset_code):
        """
        원형 : BSTR GetSFutureList(LPCTSTR strBaseAssetCode)
        설명 : 주식선물 코드 리스트를 반환한다.
        입력값 : strBaseAssetCode – 기초자산코드
        반환값 : 종목코드 리스트
        비고 : 출력값의 코드간 구분은 ';'이다.
        """
        pass


    # 37) GetSFutureCodeByIndex
    def _TODO_get_s_future_code_by_index(self, base_asset_code, index):
        """
        원형 : BSTR GetSFutureCodeByIndex(LPCTSTR strBaseAssetCode, int nIndex)
        설명 : 주식선물 코드를 반환한다.
        입력값 :
            strBaseAssetCode – 기초자산코드
            nIndex – 0~3 지수선물코드, 4~7 지수스프레드, 8~11 스타 선물, 12~ 스타 스프레드
        반환값 : 종목코드
        비고 : Ex) openApi.GetSFutureCodeByIndex("11", 0);
        """
        pass



    # 38) GetSActPriceList
    def _TODO_get_s_act_price_list(self, base_asset_gb):
        """
        원형 : BSTR GetSActPriceList(LPCTSTR strBaseAssetGb)
        설명 : 주식옵션 행사가 리스트를 반환한다.
        입력값 : strBaseAssetGb – 기초자산코드구분
        반환값 : 행사가 리스트, 행사가간 구분은 ';'
        비고 : Ex) openApi.GetSActPriceList("11");
        """
        pass


    # 39) GetSMonthList
    def _TODO_get_s_month_list(self, base_asset_gb):
        """
        원형 : BSTR GetSMonthList(LPCTSTR strBaseAssetGb)
        설명 : 주식옵션 월물 리스트를 반환한다.
        입력값 : strBaseAssetGb – 기초자산코드구분
        반환값 : 월물 리스트, 월물간 구분은 ';'
        비고 : Ex) openApi.GetSActPriceList("11");
        """
        pass


    # 40) GetSOptionCode
    def _TODO_get_s_option_code(self, base_asset_gb, act_price, cp, month):
        """
        원형 : BSTR GetSOptionCode(LPCTSTR strBaseAssetGb, LPCTSTR strActPrice, int nCp, LPCTSTR strMonth)
        설명 : 주식옵션 코드를 반환한다.
        입력값 :
            strBaseAssetGb – 기초자산코드구분
            strActPrice – 행사가
            nCp – 콜풋구분
            strMonth – 월물
        반환값 : 주식옵션 코드
        비고 : Ex) openApi.GetSOptionCode("11", "1300000", 2, "1412");
        """
        pass


    # 41) GetSOptionCodeByMonth
    def _TODO_get_s_option_code_by_month(self, base_asset_gb, code, cp, month):
        """
        원형 : BSTR GetSOptionCodeByMonth(LPCTSTR strBaseAssetGb, LPCTSTR strCode, int nCp, LPCTSTR strMonth)
        설명 : 입력한 주식옵션 코드에서 월물만 변경하여 반환한다.
        입력값 :
            strBaseAssetGb – 기초자산코드구분
            strCode – 종목코드
            nCp – 콜풋구분
            strMonth – 월물
        반환값 : 주식옵션 코드
        비고 : Ex) openApi.GetSOptionCodeByMonth("11", "211J8045", 2, "1412");
        """
        pass


    # 42) GetSOptionCodeByActPrice
    def _TODO_get_s_option_code_by_act_price(self, base_asset_gb, code, cp, tick):
        """
        원형 : BSTR GetSOptionCodeByActPrice(LPCTSTR strBaseAssetGb, LPCTSTR strCode, int nCp, int nTick)
        설명 : 입력한 주식옵션 코드에서 행사가만 변경하여 반환한다.
        입력값 :
            strBaseAssetGb – 기초자산코드구분
            strCode – 종목코드
            nCp – 콜풋구분
            nTick– 월물
        반환값 : 주식옵션 코드
        비고 : Ex) openApi.GetSOptionCodeByActPrice("11", "211J8045", 2, 4);
        """
        pass


    # SECTION 43) GetSFOBasisAssetList
    def get_s_fo_basis_asset_list(self):
        """
        원형 : BSTR GetSFOBasisAssetList()
        설명 : 주식선옵 기초자산코드/종목명을 반환한다.
        반환값 :
            기초자산코드/종목명, 코드와 종목명 구분은 '|' 코드간 구분은';'
            Ex) 211J8045|삼성전자 C 201408;212J8009|SK텔레콤 C 201408
        비고 : Ex) openApi.GetSFOBasisAssetList();
        """
        return self.dynamicCall("GetSFOBasisAssetList()")
    # !SECTION


    # SECTION 44) GetOptionATM
    def get_option_atm(self):
        """
        원형 : BSTR GetOptionATM()
        설명 : 지수옵션 ATM을 반환한다.
        반환값 : ATM
        비고 : Ex) openApi.GetOptionATM();
        """
        return self.dynamicCall("GetOptionATM()")
    # !SECTION


    # SECTION 46) GetBranchCodeName
    def get_branch_code_name(self):
        """
        원형 : BSTR GetBranchCodeName()
        설명 : 회원사 코드와 이름을 반환합니다.
        반환값 : 회원사코드|회원사명;회원사코드|회원사명;...
        비고 : Ex) openApi.GetBranchCodeName();
        """
        return self.dynamicCall("GetBranchCodeName()")
    # !SECTION


    # 47) CommInvestRqData
    def _TODO_comm_invest_rq_data(self, market_gb, rq_name, screen_no):
        """
        원형 : BSTR CommINvestRqData(LPCTSTR sMarketGb, LPCTSTR sRQName, LPCTSTR sScreenNo)
        설명 : 지원하지 않는 함수
        입력값 :
            sMarketGb – 시장구분
            001:코스피, 002:코스닥, 003:선물, 004:콜옵션, 005:풋옵션, 006:스타선물 007:주식선물, 008:3년국채, 009:5년국채, 010:10년국채, 011:달러선물, 012:엔선물 013:유로선물, 014:미니금선물, 015:금선물, 016:돈육선물, 017:달러콜옵션, 018:달러풋옵션
            sRQName – 사용자구분값
            sScreenNo – 화면번호
        반환값 : 통신결과
        비고 : Ex) openApi.CommInvestRqData("T00108;T00109", 0, 2, "RQ_1", "0101");
        """
        pass


    # 48) SetInfoData
    def _TODO_set_info_data(self, info_data):
        """
        원형 : LONG SetInfoData(LPCTSTR sInfoData)
        설명 : 다수의 아이디로 자동로그인이 필요할 때 사용한다.
        입력값 : sInfoData – 아이디
        반환값 : 통신결과
        비고 : Ex) openApi.SetInfoData("UserID");
        """
        pass


    # 49) SetRealReg
    def _TODO_set_real_reg(self, screen_no, code_list, fid_list, real_type):
        """
        원형 : SetRealReg(LPCTSTR strScreenNo, LPCTSTR strCodeList, LPCTSTR strFidList, LPCTSTR strRealType)
        설명 : 실시간 등록을 한다.
        입력값 :
            strScreenNo – 실시간 등록할 화면 번호
            strCodeList – 실시간 등록할 종목코드(복수종목가능 – "종목1;종목2;종목3;....")
            strFidList – 실시간 등록할 FID("FID1;FID2;FID3;.....")
            strRealType – "0", "1" 타입
        반환값 : 통신결과
        비고 :
            strRealType이 "0" 으로 하면 같은화면에서 다른종목 코드로 실시간 등록을 하게 되면 마지막 에 사용한 종목코드만 실시간 등록이 되고 기존에 있던 종목은 실시간이 자동 해지됨.
            "1"로 하면 같은화면에서 다른 종목들을 추가하게 되면 기존에 등록한 종목도 함께 실시간 시세 를 받을 수 있음.
            꼭 같은 화면이여야 하고 최초 실시간 등록은 "0"으로 하고 이후부터 "1"로 등록해야함.
        """
        pass


    # 50) SetRealRemove
    def _TODO_set_real_remove(self, screen_no, del_code):
        """
        원형 : Void SetRealRemove(LPCTSTR strScrNo, LPCTSTR strDelCode)
        설명 : 종목별 실시간 해제.
        입력값 :
            strScrNo – 실시간 해제할 화면 번호
            strDelCode – 실시간 해제할 종목.
        반환값 : 통신결과
        비고 : SetRealReg() 함수로 실시간 등록한 종목만 실시간 해제 할 수 있다.
        """
        pass


    # 51) GetConditionLoad
    def _TODO_get_condition_load(self):
        """
        원형 : long GetConditionLoad()
        설명 : 서버에 저장된 사용자 조건식을 조회해서 임시로 파일에 저장.
        반환값 : 사용자 조건식을 파일로 임시 저장.
        비고 :
            System 폴더에 아이디_NewSaveIndex.dat파일로 저장된다. Ocx가 종료되면 삭제시킨다.
            조건검색 사용시 이함수를 최소 한번은 호출해야 조건검색을 할 수 있다.
            영웅문에서 사용자 조건을 수정 및 추가하였을 경우에도 최신의 사용자 조건을 받고 싶으면 다시 조회해야한다.
        """
        pass


    # 52) GetConditionNameList
    def _TODO_get_condition_name_list(self):
        """
        원형 : BSTR GetConditionNameList()
        설명 : 조건검색 조건명 리스트를 받아온다.
        반환값 : 조건명 리스트(인덱스^조건명)
        비고 :
            조건명 리스트를 구분(";")하여 받아온다.
            Ex) 인덱스1^조건명1;인덱스2^조건명2;인덱스3^조건명3;...
        """
        pass


    # 53) SendCondition
    def _TODO_send_condition(self, screen_no, condition_name, index, search):
        """
        원형 : BOOL SendCondition(LPCTSTR strScrNo, LPCTSTR strConditionName, int nIndex, int nSearch)
        설명 : 조건검색 종목조회TR송신한다.
        입력값 :
            LPCTSTR strScrNo : 화면번호
            LPCTSTR strConditionName : 조건명
            int nIndex : 조건명인덱스
            int nSearch : 조회구분(0:일반조회, 1:실시간조회, 2:연속조회)
        반환값 : 성공 1, 실패 0
        비고 :
            단순 조건식에 맞는 종목을 조회하기 위해서는 조회구분을 0으로 하고, 실시간 조건검색을 하기 위해서는 조회구분을 1로 한다.
            OnReceiveTrCondition으로 결과값이 온다.
            연속조회가 필요한 경우에는 응답받는 곳에서 연속조회 여부에 따라 연속조회를 송신하면된다.
        """
        pass


    # 54) SendConditionStop
    def _TODO_send_condition_stop(self, screen_no, condition_name, index):
        """
        원형 : Void SendConditionStop(LPCTSTR strScrNo, LPCTSTR strConditionName, int nIndex)
        설명 : 조건검색 실시간 중지TR을 송신한다.
        입력값 :
            LPCTSTR strScrNo : 화면번호 LPCTSTR strConditionName : 조건명
            int nIndex : 조건명인덱스
        비고 :
            해당 조건명의 실시간 조건검색을 중지하거나, 다른 조건명으로 바꿀 때 이전 조건명으로 실시간 조건검색을 반드시 중지해야한다.
            화면 종료시에도 실시간 조건검색을 한 조건명으로 전부 중지해줘야 한다.
        """
        pass


    # SECTION 55) GetCommDataEx
    def get_comm_data_ex(self, tr_code, record_name):
        """
        원형 : VARIANT GetCommDataEx(LPCTSTR strTrCode, LPCTSTR strRecordName)
        설명 : 차트 조회 데이터를 배열로 받아온다.
        입력값 :
            LPCTSTR strTrCode : 조회한TR코드
            LPCTSTR strRecordName: 조회한 TR명
        비고 :
            조회 데이터가 많은 차트 경우 GetCommData()로 항목당 하나씩 받아오는 것 보다 한번에 데이터 전부를 받아서 사용자가 처리할 수 있도록 배열로 받는다.
        """
        print("GetCommDataEx", tr_code, record_name)
        return self.dynamicCall("GetCommDataEx(QString, QString)", tr_code, record_name)
    # !SECTION 


    # SECTION 1) OnReceiveTrData
    def on_receive_tr_data(self, screen_no, rq_name, tr_code, record_name, prev_next, data_length, error_code, message, sp_im_msg):
        """
        원형 : void OnReceiveTrData(LPCTSTR sScrNo, LPCTSTR sRQName, LPCTSTR sTrCode, LPCTSTR sRecordName, LPCTSTR sPreNext, LONG nDataLength, LPCTSTR sErrorCode, LPCTSTR sMessage, LPCTSTR sSplmMsg)
        설명 : 서버통신 후 데이터를 받은 시점을 알려준다.
        입력값 :
            sScrNo – 화면번호
            sRQName – 사용자구분 명
            sTrCode – Tran 명
            sRecordName – Record 명
            sPreNext – 연속조회 유무
            nDataLength – 1.0.0.1 버전 이후 사용하지 않음.
            sErrorCode – 1.0.0.1 버전 이후 사용하지 않음.
            sMessage – 1.0.0.1 버전 이후 사용하지 않음.
            sSplmMsg - 1.0.0.1 버전 이후 사용하지 않음.
        반환값 : 없음
        비고 :
            sRQName – CommRqData의 sRQName과 매핑되는 이름이다.
            sTrCode – CommRqData의 sTrCode과 매핑되는 이름이다.
        """
        print("Called OnReceiveTrData event!", tr_code, rq_name)

        comm_data = None
        for opt, func in self.tr_list.items():
            if opt == tr_code:
                comm_data = func(tr_code, rq_name)
                break

        response = self.response_comm_rq_data
        self.receive_tr_data_handler = {
            "response" : response,
            "screen_no" : screen_no,
            "rq_name" : rq_name,
            "tr_code" : tr_code,
            "record_name" : record_name,
            "pre_next" : prev_next,
            "comm_data" : comm_data
        }

        if self.loop_receive_tr_data.isRunning():
            print("Ended OnReceiveTrData event!")
            self.loop_receive_tr_data.exit()
    # !SECTION 


    # 2) OnReceiveRealData
    def on_receive_real_data(self, jongmok_code, real_type, real_data):
        """
        원형 : void OnReceiveRealData(LPCTSTR sJongmokCode, LPCTSTR sRealType, LPCTSTR sRealData)
        설명 : 실시간데이터를 받은 시점을 알려준다.
        입력값 :
            sJongmokCode – 종목코드
            sRealType – 리얼타입
            sRealData – 실시간 데이터전문
        반환값 : 없음
        """
        print("on_receive_real_data")
        pass


    # 3) OnReceiveMsg
    def on_receive_msg(self, screen_no, rq_name, tr_code, msg):
        """
        원형 : void OnReceiveMsg(LPCTSTR sScrNo, LPCTSTR sRQName, LPCTSTR sTrCode, LPCTSTR sMsg)
        설명 : 서버통신 후 메시지를 받은 시점을 알려준다.
        입력값 :
            sScrNo – 화면번호
            sRQName – 사용자구분 명
            sTrCode – Tran 명
            sMsg – 서버메시지
        반환값 : 없음
        비고 :
            sScrNo – CommRqData의 sScrNo와 매핑된다.
            sRQName – CommRqData의 sRQName 와 매핑된다.
            sTrCode – CommRqData의 sTrCode 와 매핑된다.
        """
        print("on_receive_msg")
        pass


    # 4) OnReceiveChejanData
    def on_receive_chejan_data(self, gubun, item_cnt, fid_list):
        """
        원형 : void OnReceiveChejanData(LPCTSTR sGubun, LONG nItemCnt, LPCTSTR sFidList);
        설명 : 체결데이터를 받은 시점을 알려준다.
        입력값 :
            sGubun – 체결구분
            nItemCnt - 아이템갯수
            sFidList – 데이터리스트
        반환값 : 없음
        비고 :
            sGubun – 0:주문체결통보, 1:잔고통보, 3:특이신호
            sFidList – 데이터 구분은 ';' 이다.
        """
        print("on_receive_chejan_data")
        pass


    # 5) OnEventConnect
    def on_event_connect(self, err_code):
        """
        원형 : void OnEventConnect(LONG nErrCode);
        설명 : 서버 접속 관련 이벤트
        입력값 : LONG nErrCode : 에러 코드
        반환값 : 없음
        비고 :
            nErrCode가 0이면 로그인 성공, 음수면 실패
            음수인 경우는 에러 코드 참조
        """
        print("on_event_connect")

        if err_code == KWErrorCode.OP_ERR_NONE:
            print("연결 성공")
        else:
            print("연결 실패")

        if self.loop_event_connect.isRunning():
            self.loop_event_connect.exit()


    # 6) OnReceiveCondition
    def on_receive_condition(self, code, type, condition_name, condition_index):
        """
        원형 : void OnReceiveRealCondition(LPCTSTR strCode, LPCTSTR strType, LPCTSTR strConditionName, LPCTSTR strConditionIndex)
        설명 : 조건검색 실시간 편입,이탈 종목을 받을 시점을 알려준다.
        입력값 :
            LPCTSTR strCode : 종목코드
            LPCTSTR strType : 편입("I"), 이탈("D")
            LPCTSTR strConditionName : 조건명
            LPCTSTR strConditionIndex : 조건명 인덱스
        반환값 : 없음
        비고 :
            strConditionName에 해당하는 종목이 실시간으로 들어옴.
            strType으로 편입된 종목인지 이탈된 종목인지 구분한다.
        """
        print("on_receive_condition")
        pass


    # 7) OnReceiveTrCondition
    def on_receive_tr_condition(self, screen_no, code_list, condition_name, index, next):
        """
        원형 : void OnReceiveTrCondition(LPCTSTR sScrNo, LPCTSTR strCodeList, LPCTSTR strConditionName, int nIndex, int nNext)
        설명 : 조건검색 조회응답으로 종목리스트를 구분자(";")로 붙어서 받는 시점.
        입력값 :
            LPCTSTR sScrNo : 종목코드
            LPCTSTR strCodeList : 종목리스트(";"로 구분)
            LPCTSTR strConditionName : 조건명
            int nIndex : 조건명 인덱스
            int nNext : 연속조회(2:연속조회, 0:연속조회없음)
        반환값 : 없음
        """
        print("on_receive_tr_condition")
        pass


    # 8) OnReceiveConditionVer
    def on_receive_condition_ver(self, ret, msg):
        """
        원형 : void OnReceiveConditionVer(long lRet, LPCTSTR sMsg)
        설명 : 로컬에 사용자 조건식 저장 성공 여부를 확인하는 시점
        입력값 : long lRet - 사용자 조건식 저장 성공여부 (1: 성공, 나머지 실패)
        반환값 : 없음
        """
        print("on_receive_condition_ver")
        pass




    """
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

    def call_get_repeat_cnt(self, tr_code, rq_name):
        time.sleep(0.4)
        ret = self.dynamicCall("GetRepeatCnt(QString, QString)", tr_code, rq_name)

        return ret

    def _receive_tr_data(self, screen_no, rq_name, tr_code, record_name, next, unused1, unused2, unused3, unused4):
        if next == '2':
            self.remained_data = True
        else:
            self.remained_data = False

        if rq_name == "opt10081_req":
            self._opt10081(rq_name, trcode)
        elif rq_name == "opt10060_req":
            self._opt10060(rq_name, trcode)
        elif rq_name == "opt10060_ex_req":
            self._opt10060_ex(rq_name, trcode)

        try:
            self.tr_event_loop.exit()
        except AttributeError:
            pass

    def _opt10060(self, rq_name, trcode):
        data_cnt = self._get_repeat_cnt(tr_code, rq_name)

        columns = [
            "일자", "현재가", "전일대비", "누적거래대금",
            "개인투자자", "외국인투자자", "기관계", "금융투자",
            "보험", "투신", "기타금융", "은행", "연기금등", "사모펀드",
            "국가", "기타법인", "내외국인"
        ]

        self.df = pd.DataFrame(columns=columns)

        for i in range(data_cnt):
            self.df.loc[i] = [
              self._get_comm_data(tr_code, rq_name, i, "일자"),
              self._get_comm_data(tr_code, rq_name, i, "현재가"),
              self._get_comm_data(tr_code, rq_name, i, "전일대비"),
              self._get_comm_data(tr_code, rq_name, i, "누적거래대금"),
              self._get_comm_data(tr_code, rq_name, i, "개인투자자"),
              self._get_comm_data(tr_code, rq_name, i, "외국인투자자"),
              self._get_comm_data(tr_code, rq_name, i, "기관계"),
              self._get_comm_data(tr_code, rq_name, i, "금융투자"),
              self._get_comm_data(tr_code, rq_name, i, "보험"),
              self._get_comm_data(tr_code, rq_name, i, "투신"),
              self._get_comm_data(tr_code, rq_name, i, "기타금융"),
              self._get_comm_data(tr_code, rq_name, i, "은행"),
              self._get_comm_data(tr_code, rq_name, i, "연기금등"),
              self._get_comm_data(tr_code, rq_name, i, "사모펀드"),
              self._get_comm_data(tr_code, rq_name, i, "국가"),
              self._get_comm_data(tr_code, rq_name, i, "기타법인"),
              self._get_comm_data(tr_code, rq_name, i, "내외국인")
            ]

    def _opt10060_ex(self, rq_name, trcode):
        df_list = self._get_comm_data_ex(tr_code, rq_name)

        columns = [
            "일자", "현재가", "전일대비", "누적거래대금",
            "개인투자자", "외국인투자자", "기관계", "금융투자",
            "보험", "투신", "기타금융", "은행", "연기금등", "사모펀드",
            "국가", "기타법인", "내외국인"
        ]

        self.df = pd.DataFrame(df_list, columns=columns)

        self.df_list = df_list
    """
