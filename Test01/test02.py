#-*- coding: utf-8 -*-
import numpy
import matplotlib.pyplot as plt

# Git - 각 브랜치 독립성 확인 테스트 branchTest

# 데이터 준비
x = numpy.arange(0, 6, 0.1) # 0에서 6까지 0.1간격으로 생성
y1 = numpy.sin(x)
y2 = numpy.cos(x)

# 그래프 그리기
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos") # cos 함수는 점선으로 그리기
plt.xlabel("x") # x축 이름
plt.ylabel("y") # y축 이름
plt.title("sin & cos") # 재목
plt.legend()
plt.show()


