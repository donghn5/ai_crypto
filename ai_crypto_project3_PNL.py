Import pandas as pd
#pands 라이브러리 호출 및 pd 로 모듈 간소화
#CSV file read
df = pd.read_csv('ai-crypto-project-3-live-btc-krw.csv')
#PnL(Profit and Loss) 계산
#PnL= 거래 수량 * 거래 가격 *(2*side–1)
#2*side-1 이란 sell일때quantity*price에 -1을 곱하고, buy일때 1을 곱하는 식 df['PnL'] = df['quantity'] * df['price'] * (df['side'] * 2 - 1)
#누적 PnL 계산
df['Cumulative PnL'] = df['PnL'].cumsum()
#Cumulative Quantity = (quantity * (2 * side - 1))
#quantity에 sell이면 -1, buy면 1을 곱한뒤Cumulativequantity에 누적하여 보유 수량 계 산
df['Cumulativequantity'] = (df['quantity'] * (df['side'] * 2 - 1)).cumsum()
#결과 출력
#간략한 csv파일과보유 수량, 누적 PnL을 출력하고 누적 PnL로 손익판단 가능 print(df )
print(f"누적 보유 수량: {df['Cumulativequantity'].iloc[-1]}")
print(f"누적 PnL: {df['CumulativePnL'].iloc[-1]:.2f}")
#누적 PnL이 34405642.04 가 나왔으므로 2024.03.27 23:28 부터 2024.03.31 23:34 까지 거래한 암호화폐는 이익을 봤음.