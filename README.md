# KiwoomTrader

<br>

# TODO 

Trading Option

- [ ] on_receive_tr_data : prev_next = 2 일 경우, 데이터 연속 요청
- [ ] opt10012(주문체결요청) : 주문 요청한 이후에 Vadlidation 테스트
- [x] opt10014(공매도추이요청) : 장 중에 Vadlidation 테스트
- [ ] opt100XX input 명 정리

<br>

# NOTE

1. 장 중에 CommRqData 호출 할 경우, OnReceiveTrData, OnReceiveRealData 모두 호출되는 것으로 보임.  
실시간 데이터가 언제 호출되며, 어떤 데이터를 얻는지 확인 할 필요 있음
