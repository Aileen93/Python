import matplotlib.pyplot as plt
import numpy as np

# // 임의의 x,y 데이터 생성
vector_set = []
for i in range(100) :                          # 0~99
    x = np.random.normal(0,1)                  # normal(평균, 표준편차) : 표준정규분포
    y = x * 0.1 + 0.2 + np.random.normal(0,1)
    vector_set.append([x, y])                  # [[x1, y1], [x2, y2], [x3, y3], ... ,[x100, y100]]

x_data = [ v[0]  for v in vector_set ]      # v = [x1, ]
y_data = [ v[1]  for v in vector_set ]      # v = [, y1]

# // 시각화
plt.plot(x_data, y_data, 'ro')
plt.title("multi chart draw")      # 차트 제목
plt.xlabel('stage')                 # x축
plt.ylabel('random number')    # y축
plt.legend(loc='best')            # 범례
plt.show()