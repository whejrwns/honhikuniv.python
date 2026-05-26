import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

'# :blue[시각화 라이브러리]'

'#### :orange[Matplotlib: st.pyplot()]'

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig) # 차트 출력