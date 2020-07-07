# Tarea4 - Andre Nitsche Rodriguez - B55067
En el trabajo  propuesto se propone realizar un trabajo programado en Python en donde se trabaja con transmision, recepcion y modulacion de ondas.

-Pregunta1: Crear un esquema de modulación BPSK para los bits presentados. Esto implica asignar una forma de onda sinusoidal normalizada (amplitud unitaria) para cada bit y 
luego una concatenación de todas estas formas de onda.

Lo primero es extraer los datos del archivo "bits10k.csv" y ingresarlos en un array. En seguida se definen valores importantes como el numero de bits, la frecuencia, el 
perdiodo, la cantidad de puntos de muestreo por periodo. Despues de definir la onda portadora, podemos hacer la modulacion con una frecuencia de muestreo definida, siguiendo la 
regla del BPSK (Binary Phase Shifting Key): con entrada binaria 1 se mantiene la fase de la portadora, y con entrada 0 se presenta un desface de 180°.
Se obtiene entonces de esta manera la forma de Tx.


-Pregunta 2: Calcular la potencia promedio de la señal modulada generada.

En este punto basta con calcular la potencia instantanea, y luego a partir de esta la potencia promedio.
En este caso obtenemos que esta ultima es Ps = 0.48995197990395956


-Pregunta 3: Simular un canal ruidoso del tipo AWGN (ruido aditivo blanco gaussiano) con una relación señal a ruido (SNR) desde -2 hasta 3 dB.

Para esta pregunta hay que definir los SNR especificados, para luego poder ver la forma de la señal con un nivel de ruido especifico.
Para esta parte obtenemos una grafica por SNR, y tambien hay que calcular la potencia del ruido para el SNR y potencia de la señal dadas, la desviación estándar del ruido,
crear el ruido en si. Finalmente se simula la señal recibida y se grafica.

-Pregunta 4: Graficar la densidad espectral de potencia de la señal con el método de Welch (SciPy), antes y después del canal ruidoso.

En este caso se usa el metodo de Welch para graficar la densidad espectral de potencia de la señal antes y despues del canal ruidoso. En este caso lo hacemos para el canal con un SNR= -2dB


-Pregunta 5: Demodular y decodificar la señal y hacer un conteo de la tasa de error de bits (BER, bit error rate) para cada nivel SNR.

En esta seccion se crea un vector nuevo de SNR's para obtener errores mas grandes. Ahora SNR = [-7, -6, -5, -4, -3, -2, -1, 0]

Hay un total de 277 errores en 10000 bits para una tasa de error de 0.0277. SNR = -7 dB

Hay un total de 184 errores en 10000 bits para una tasa de error de 0.0184. SNR = -6 dB

Hay un total de 110 errores en 10000 bits para una tasa de error de 0.011. SNR = -5 dB

Hay un total de 53 errores en 10000 bits para una tasa de error de 0.0053. SNR = -4 dB

Hay un total de 24 errores en 10000 bits para una tasa de error de 0.0024. SNR = -3 dB

Hay un total de 13 errores en 10000 bits para una tasa de error de 0.0013. SNR = -2 dB

Hay un total de 3 errores en 10000 bits para una tasa de error de 0.0003. SNR = -1 dB

Hay un total de 4 errores en 10000 bits para una tasa de error de 0.0004. SNR = 0 dB


-Pregunta 6:Graficar BER versus SNR.

Ahora procedemos a graficar la curva de BER vs SNR obtenidos en el punto anterior. Dado el comportamiento lo graficamos con el comando plt.semilogy().

