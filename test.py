import pandas as pd
import streamlit as st
import sympy 

st.title("202021065 kwon yeon taek")

s = sympy.symbols('s')
G1 = 100
H1 = (s + 2)*(s + 3)
Ts = G1/(H1 + G1)
st.write(Ts)

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

#transfer function
num = [1]
den = [1, 5, 106]
sys = signal.TransferFunction(num, den)

#compute the step response of the system
t, y = signal.step(sys)

#plot the step response of the system
fig = plt.figure()
plt.title('unit step')
plt.plot(t, y)
plt.xlabel('time')
plt.ylabel('Output')
plt.show()
st.pyplot(fig)

s1 = signal.lti([100], [1], [5], [106])


frequencies = np.logspace(-2, 2, 500)

w, mag, phase = s1.bode(frequencies)
fig2 = plt.figure()
plt.subplot(2, 1, 1)
plt.semilogx(w, mag)
plt.title('bode plot of T(s)=100/((s + 2)(s + 3) + 100)')
plt.ylabel('magnitude [dB]')
plt.xlabel('Frequency [Hz]')
plt.show()
st.pyplot(fig2)

fig3 = plt.figure()
plt.subplot(2, 1, 2)
plt.semilogx(w, phase)
plt.ylabel('Phase [degrees]')
plt.xlabel('Frequency [Hz]')
plt.show()
st.pyplot(fig3)
