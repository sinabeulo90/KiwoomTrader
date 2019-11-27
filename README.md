# KiwoomTrader

<br>

# TODO 

1. Trading Option
    - [ ] on_receive_tr_data : prev_next = 2 일 경우, 데이터 연속 요청
    - [ ] opt10012(주문체결요청) : 주문 요청한 이후에 Vadlidation 테스트
    - [ ] opt100XX input 명 정리

2. 장 중에 Validation 테스트
    - [x] opt10014 (공매도추이요청)
    - [ ] opt10028 (시가대비등락률요청)
    - [ ] opt10035 (외인연속순매매상위요청)
    - [ ] opt10039 (증권사별매매상위요청)
    - [ ] opt10046 (체결강도추이시간별요청)

3. Core
    - [ ] 싱글 데이터 수집할 때, 전체 index 수집 (현재: index = 0)
    - [ ] 전체 데이터 수집을 위해 comm_rq_data 재요청 및 재수집 (현재: 수집하지 않음)
<br>

# NOTE

1. 장 중에 CommRqData 호출 할 경우, OnReceiveTrData, OnReceiveRealData 모두 호출되는 것으로 보임.  
실시간 데이터가 언제 호출되며, 어떤 데이터를 얻는지 확인 필요
2. 알수 없는 입력 변수
    - opt10037 : '현재가조건'
    - opt10041 : '영웅클럽구분'
