# KiwoomTrader

<br>

# TODO

1. Core
    - [ ] 싱글 데이터 수집할 때, 전체 index 수집 (현재: index = 0)
    - [ ] 전체 데이터 수집을 위해 comm_rq_data 재요청 및 재수집 (현재: 수집하지 않음)

2. 입력 변수 확인

### Validation 테스트

1. 주문 요청 후
    - [ ] opt10012(주문체결요청) : 주문 요청한 이후에 Vadlidation 테스트

2. 장 중
    - [x] opt10014 (공매도추이요청)
    - [ ] opt10028 (시가대비등락률요청)
    - [ ] opt10035 (외인연속순매매상위요청)
    - [ ] opt10039 (증권사별매매상위요청)
    - [x] opt10046 (체결강도추이시간별요청)
    - [ ] opt10049 (ELW투자지표요청)
    - [ ] opt10050 (ELW민감도지표요청)

3. 실행 되지 않는 Opt
    - [ ] opt10048 : (ELW일별민감도지표요청)
    - [ ] opt10070 : (당일주요거래원요청)
    - [ ] opt10072 : (일자별종목별실현손익요청)
    - [ ] opt10073 : (일자별종목별실현손익요청)
    - [ ] opt10074 : (일자별실현손익요청)
    - [ ] opt10075 : (실시간미체결요청)

4. 기타
    - [ ] opt10076 : (실시간체결요청)
    - [ ] opt10077 : (당일실현손익상세요청)
    - [ ] opt10085 : (계좌수익률요청)
    - [ ] 장 중에 CommRqData 호출 할 경우, OnReceiveTrData, OnReceiveRealData 모두 호출되는 것으로 보임.  
실시간 데이터가 언제 호출되며, 어떤 데이터를 얻는지 확인 필요

5. Input 정보 부족
    - [ ] opt30001 : (ELW가격급등락요청)
    - [ ] opt30002 : (거래원별ELW순매매상위요청)
    - [ ] opt30003 : (ELWLP보유일별추이요청)
    - [ ] opt30004 : (ELW괴리율요청)
    