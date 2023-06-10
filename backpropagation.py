import math
import matplotlib.pyplot as plt
import random

x = [[0,0],[0,1],[1,0],[1,1]]
y = [0,1,1,0]

w1 = [[random.randint(0,1)/10,random.randint(0,1)/10],[random.randint(0,1)/10,random.randint(0,1)/10]]
b1 = [random.randint(0,1)/10,random.randint(0,1)/10]

w2 = [random.randint(0,1)/10,random.randint(0,1)/10]
b2 = random.randint(0,1)/10

ep = 20001
lr = 0.1
mse = []

for i in range(ep):
    E = []
    result = []
    for j in range(len(x)):
        # hidden layer
        Ha = []
        for k in range(len(w1)):
            Ha.append(1 / (1 + math.exp(-(sum([a*b for a,b in zip(x[j],w1[k])]) + b1[k]))))
        # output layer
        Hb = 1 / (1 + math.exp(-(sum([a*b for a,b in zip(Ha,w2)]) + b2)))
        E.append(y[j] - Hb)
        result.append(Hb)
        
        # backpropagation

        # 계산 편리
        alpha_2 = E[j] * Hb * (1-Hb)
        alpha_1 = [alpha_2 * Ha[0] * (1-Ha[0]) * w2[0],alpha_2 * Ha[1] * (1-Ha[1]) * w2[1]]
        
        # 가중치 갱신
        w2 = [w2[0] + lr * alpha_2 * Ha[0],w2[1] + lr * alpha_2 * Ha[1]]
        b2 = b2 + lr * alpha_2
        
        w1 = [[w1[0][0] + lr * alpha_1[0] * x[j][0],w1[0][1] + lr * alpha_1[0] * x[j][1]],
              [w1[1][0] + lr * alpha_1[1] * x[j][0],w1[1][1] + lr * alpha_1[1] * x[j][1]]]
        b1 = [b1[0] + lr * alpha_1[0],b1[1] + lr * alpha_1[1]]
        
    print('EPOCH : %05d MSE : %04f RESULTS : 0 0 => %04f 0 1 => %04f 1 0 => %04f 1 1 => %04f'
          %(i,sum([a**2 for a in E])/len(E),result[0],result[1],result[2],result[3]))
    
    mse.append(sum([a**2 for a in E])/len(E))

    if i%20000 == 0:
        plt.xlabel('EPOCH')
        plt.ylabel('MSE')
        plt.title('MLP TEST')
        plt.plot(mse)
        plt.show()

# 결과 확인
for i in range(len(x)):
    Ha = []
    for j in range(len(w1)):
        Ha.append(1 / (1 + math.exp(-(sum([a*b for a,b in zip(x[i],w1[j])]) + b1[j]))))
    Hb = 1 / (1 + math.exp(-(sum([a*b for a,b in zip(Ha,w2)]) + b2)))
    print('INPUT : %s RESULT : %s' %(x[i],Hb))