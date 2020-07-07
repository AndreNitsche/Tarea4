#Andre Nitsche Rodriguez - B55067 - Grupo 1 

#Librerias
import numpy as np
from scipy import signal
from scipy import integrate
import matplotlib.pyplot as plt
import pandas as pd

#Se extraen los datos del csv
bits = pd.read_csv('bits10k.csv')

#Y se crea un array con los bits 
Bits = np.array(bits)

#Pregunta 1
#Definimos N numero de bits
N = 10000
#Definimos la frecuencia de la onda portadora
F = 5000 #Hz
#Y el periodo
T = 1/F

#Numero de puntos de muestreo por periodo
p = 50

# Puntos de muestreo para cada periodo
tp = np.linspace(0, T, p)

#Creacion de la forma de onda de la portadora
sinus = np.sin(2* np.pi * F * tp)

#Visualizacion de la forma de onda de la portadora
plt.plot(tp, sinus)
plt.xlabel('Tiempo / s')
plt.savefig('Portadora.png')
plt.cla()

#Definimos la frecuencia de muestreo
Fs = p/T

# Se crea la línea temporal para toda la señal Tx
t = np.linspace(0, N*T, N*p)

# Inicializar el vector de la señal modulada Tx
senal = np.zeros(t.shape)

# Creación de la señal modulada BPSK
for k, b in enumerate(Bits):
    if b == 1:
        senal[k*p:(k+1)*p] = sinus
    else:
        senal[k*p:(k+1)*p] = -sinus
            

# Visualización de los primeros bits modulados
pb = 5
plt.figure()
plt.plot(senal[0:pb*p])
plt.title('Tx')
plt.savefig('Tx.png')
plt.show()
plt.cla()




#Pregunta 2
#Ahora pasamos al calculo de la potencia promedio

# Potencia instantánea
Pinst = senal**2

# Potencia promedio a partir de la potencia instantánea (W)
Ps = integrate.trapz(Pinst, t) / (N * T)




#Pregunta 3

#Hacemos los casos para todos los SRN propuestos
# Relación señal-a-ruido deseada SNR=-2
SNRa= -2

# Potencia del ruido para SNR y potencia de la señal dadas
Pna = Ps / (10**(SNRa / 10))

# Desviación estándar del ruido
sigmaa = np.sqrt(Pna)

# Crear ruido (Pn = sigma^2)
ruidoa = np.random.normal(0, sigmaa, senal.shape)

# Simular "el canal": señal recibida
Rxa = senal + ruidoa

# Visualización de los primeros bits recibidos
pb = 5
plt.figure()
plt.title('SNR = -2')
plt.plot(Rxa[0:pb*p])
plt.savefig('SRN-2.png')
plt.cla()



# Relación señal-a-ruido deseada SNR=-1
SNRb= -1

# Potencia del ruido para SNR y potencia de la señal dadas
Pnb = Ps / (10**(SNRb / 10))

# Desviación estándar del ruido
sigmab = np.sqrt(Pnb)

# Crear ruido (Pn = sigma^2)
ruidob = np.random.normal(0, sigmab, senal.shape)

# Simular "el canal": señal recibida
Rxb = senal + ruidob

# Visualización de los primeros bits recibidos
pb = 5
plt.figure()
plt.title('SNR = -1')
plt.plot(Rxb[0:pb*p])
plt.savefig('SRN-1.png')
plt.cla()



# Relación señal-a-ruido deseada SNR=0
SNRc= 0

# Potencia del ruido para SNR y potencia de la señal dadas
Pnc = Ps / (10**(SNRc / 10))

# Desviación estándar del ruido
sigmac = np.sqrt(Pnc)

# Crear ruido (Pn = sigma^2)
ruidoc = np.random.normal(0, sigmac, senal.shape)

# Simular "el canal": señal recibida
Rxc = senal + ruidoc

# Visualización de los primeros bits recibidos
pb = 5
plt.figure()
plt.title('SNR = 0')
plt.plot(Rxc[0:pb*p])
plt.savefig('SRN0.png')
plt.cla()



# Relación señal-a-ruido deseada SNR= 1
SNRd= 1

# Potencia del ruido para SNR y potencia de la señal dadas
Pnd = Ps / (10**(SNRd / 10))

# Desviación estándar del ruido
sigmad = np.sqrt(Pnd)

# Crear ruido (Pn = sigma^2)
ruidod = np.random.normal(0, sigmad, senal.shape)

# Simular "el canal": señal recibida
Rxd = senal + ruidod

# Visualización de los primeros bits recibidos
pb = 5
plt.figure()
plt.title('SNR = 1')
plt.plot(Rxd[0:pb*p])
plt.savefig('SRN1.jpg')
plt.cla()



# Relación señal-a-ruido deseada SNR= 2
SNRe= 2

# Potencia del ruido para SNR y potencia de la señal dadas
Pne = Ps / (10**(SNRe / 10))

# Desviación estándar del ruido
sigmae = np.sqrt(Pne)

# Crear ruido (Pn = sigma^2)
ruidoe = np.random.normal(0, sigmae, senal.shape)

# Simular "el canal": señal recibida
Rxe = senal + ruidoe

# Visualización de los primeros bits recibidos
pb = 5
plt.figure()
plt.title('SNR = 2')
plt.plot(Rxe[0:pb*p])
plt.savefig('SRN2.png')
plt.cla()



# Relación señal-a-ruido deseada SNR= 3
SNRf= 3

# Potencia del ruido para SNR y potencia de la señal dadas
Pnf = Ps / (10**(SNRf / 10))

# Desviación estándar del ruido
sigmaf = np.sqrt(Pnf)

# Crear ruido (Pn = sigma^2)
ruidof = np.random.normal(0, sigmaf, senal.shape)

# Simular "el canal": señal recibida
Rxf = senal + ruidof

# Visualización de los primeros bits recibidos
pb = 5
plt.figure()
plt.title('SNR = 3')
plt.plot(Rxf[0:pb*p])
plt.savefig('SRN3.png')
plt.cla()



#Pregunta 4

# Antes del canal ruidoso
fw, PSD = signal.welch(senal, Fs, nperseg=1024)
plt.figure()
plt.semilogy(fw, PSD)
plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad espectral de potencia / V**2/Hz')
plt.savefig('DensidadEspectral-AntesRuido.png')
plt.cla()

# Después del canal ruidoso (SNR=-2)
fw, PSD = signal.welch(Rxa, Fs, nperseg=1024)
plt.figure()
plt.semilogy(fw, PSD)
plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad espectral de potencia / V**2/Hz')
plt.savefig('DensidadEspectral-DespuesRuido.png')
plt.cla()




#Pregunta 5


# Relación señal-a-ruido deseada SNR
SNRA = np.linspace(-7, 0, 8)

# Pseudo-energía de la onda original 
Es = np.sum(sinus**2)
#Se inician BER y bitsRx en vectores de 0's
bitsRx = np.zeros(Bits.shape)
BER = np.zeros(SNRA.shape)

for j in range(len(SNRA)):
    # Potencia del ruido para SNR y potencia de la señal dadas
    Pn = Ps / (10**(SNRA[j] / 10))
    # Desviación estándar del ruido
    sigma = np.sqrt(Pn)
    # Crear ruido (Pn = sigma^2)
    ruido = np.random.normal(0, sigma, senal.shape)
    # Simular "el canal": señal recibida
    Rx = senal + ruido 
    for x, y in enumerate(Bits):
            Ep = np.sum(Rx[x*p:(x+1)*p] * sinus)
            if Ep > Es/2:
                bitsRx[x] = 1
            else:
                bitsRx[x] = 0
                
    err = np.sum(np.abs(Bits - bitsRx))
    BER[j] = err/N


print('Hay un total de {} errores en {} bits para una tasa de error de {}.'.format(err, N, BER))



#Pregunta 6

plt.figure()
plt.semilogy(SNRA, BER[0:5*p])
plt.xlabel('SNRA(dB)')
plt.ylabel('BER')
plt.title('BER vs SNR')
plt.savefig('BERvsSNR.png')