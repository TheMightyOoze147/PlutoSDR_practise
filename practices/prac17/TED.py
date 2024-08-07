from context import QAM256, QAM64, QAM16, QPSK, randomDataGenerator, plot_QAM, text_to_bits
import matplotlib.pyplot as plt
import numpy as np

def TED(data): # for plot TED
    err = np.zeros(len(data)//10, dtype = "complex_")
    ted_plot = np.zeros(20, dtype = "complex_")
    #data = np.roll(data,-2)
    #err = []
    buffer = np.zeros(len(data)//10, dtype = "complex_")
    nsp = 10
    for n in range(0,20):
        for ns in range(0,len(data)-(2*nsp+9),nsp):
            real = (data.real[n+ns] - data.real[n+nsp+ns]) * data.real[n+nsp//2+ns]
            imag = (data.imag[n+ns] - data.imag[n+nsp+ns]) * data.imag[n+nsp//2+ns]
            err[ns//nsp] = real + imag 
            buffer[ns//nsp] = err[ns//nsp]    
        ted_plot[n] = np.mean(buffer)
        buffer.fill(0)
        #plt.plot(err) 
        #plt.show()
    return ted_plot

def TED1(data): #original ted
    err = np.zeros(len(data)//10, dtype = "complex_")
    #data = np.roll(data,-2)
    nsp = 10
    
    for ns in range(0,len(data)-(2*nsp+9),nsp):
        real = (data.real[ns] - data.real[nsp+ns]) * data.real[nsp//2+ns]
        imag = (data.imag[ns] - data.imag[nsp+ns]) * data.imag[nsp//2+ns]
        err[ns//nsp] = real + imag 


    return err

def gardner(conv,tau):
    ted = np.zeros(len(conv)//10+1,dtype=np.complex128)
    #tau = np.zeros((len(conv)))
    #for i in range(0,len(conv),10):
        #tau[i] = 1//len(conv)*i
    #print(len())
    symbol = 10
    for i in range(10,len(conv),symbol):
        ted[i//symbol] = ((conv[i-symbol]+tau[i//symbol]) - (conv[i]+tau[i//symbol])) * conv[(i-symbol)+(symbol//2)] + tau[i//symbol]
    return ted


def gardner_one_symbol(conv,tau):
    
    ted = np.zeros(len(tau), dtype=np.complex128)
    for i in range(len(tau)):
        ted[i] = ((conv[0]+tau[i]) - (conv[10]+tau[i])) * conv[5] + tau[i]

    return ted


def gardner_3(conv,tau):
    ted = np.zeros(len(conv)//10+1,dtype=np.complex128)
 
    symbol = 10
    for i in range(10,len(conv),symbol):
        ted[i//symbol] = ((conv[i-symbol]+tau) - (conv[i]+tau)) * conv[(i-symbol)+(symbol//2)] + tau
    return np.mean(ted)


data = list(map(int, text_to_bits("Masha ela kashu, malo kashi Mashe")))

not_data = randomDataGenerator(20)

print("------",len(data[244:]))
print(type(not_data))
buffer = data[244:] + data + data[:20]
print(len(buffer))



h1 = np.ones(10)
QPSK = QPSK(buffer)
QPSK = np.repeat(QPSK, 10)
noise = np.random.normal(0,0,len(QPSK))

QPSK = QPSK + noise
print(len(QPSK))
conv = np.convolve(h1,QPSK,'full')

#plt.plot(conv.real)
print(len(conv))


tau = np.arange(-1,1,2/(len(conv)//10+1))
print("tau", len(tau))
#for i in range(0,len(conv),10):
    #tau[i] = 1//len(conv)*i

ted = gardner(conv,tau)
print("ted", len(ted))
plt.figure(1)
plt.plot(tau,ted)
plt.title("Gardner TED")
plt.xlabel("tau")
plt.ylabel("")


plt.figure(2)
tau2 = np.arange(-1,1,0.01)
ted2 = gardner_one_symbol(conv,tau2)
print("ted2", len(ted2))
print("tau2", len(tau2))
plt.plot(tau2,ted2)



tau3 = np.arange(-1,1,0.01)
t3 = []
for i in range(len(tau3)):
    ted3 = gardner_3(conv,tau3[i])
    t3.append(ted3)

t3 = np.asarray(t3)

plt.figure(3)
plt.plot(tau3,t3)
plt.show()

