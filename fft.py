import numpy as np  
import matplotlib.pyplot as plt 
from scipy import signal 


# インプットファイルの読み込み
f = open('input.txt')
data = f.read()
f.close()

# データを用意
data = data.split()

data_str = []
data_f = []

dt = 0.01
for i in data:
    data_str.append(str(i))

for i in data_str:
    data_f.append(float(i))

num = len(data_f)

for i in range(num):
    if 2**i < num:
        continue;
    elif 2**i == num:
        j = i
        break;
    else:
        j = i-1
        break;

data = data_f[0:2**j]
num = len(data)

F = np.fft.fft(data)

F_abs = np.abs(F)
F_abs_amp = F_abs / num *2
F_abs_amp[0] = F_abs_amp[0]/2

fq = np.linspace(0,1.0/dt,num)

np.random.seed(0)
maximal_idx = signal.argrelmax(F_abs,order=1)[0]
peak_cut = 10
maximal_idx = maximal_idx[(F_abs[maximal_idx] > peak_cut) & (maximal_idx <= num/2)]

plt.subplot(212)
plt.xlabel('frequency(Hz)')
plt.ylabel('amplitude')
plt.axis([0,1.0/dt/2,0,max(F_abs)*1.5])
plt.xlim(0,5)
plt.plot(fq,F_abs)
plt.plot(fq[maximal_idx],F_abs[maximal_idx],'ro')
plt.show()
print('peak',fq[maximal_idx])