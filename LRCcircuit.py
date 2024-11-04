import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

# Streamlit 앱 제목 설정
st.title("RLC 직렬 교류 회로 계산기")

# 입력 받을 값 설정
R = st.number_input("저항 (R, 옴)", value=1000.0, format="%.12f")
L = st.number_input("인덕턴스 (L, 헨리)", value=0.0025, format="%.12f")
C = st.number_input("캐패시턴스 (C, 패럿)", value=0.00000000056, format="%.12f")

# 그래프용 각진동수 범위 설정
omega_min = 1000 * st.number_input("그래프 최소 진동수 (kHz)", value=0.1)
omega_max = 1000 * st.number_input("그래프 최대 진동수 (kHz)", value=750.0)
num_points = st.slider("그래프 각진동수 데이터 포인트 수", min_value=100, max_value=2000, value=500)

# 그래프용 각진동수 배열 생성
frequency = np.linspace(omega_min, omega_max, num_points)

# V_r / V 계산
V_r_over_V = R / np.sqrt(R ** 2 + (2 * math.pi * frequency * L - 1 / (2 * math.pi * frequency * C)) ** 2)

# 공명 각진동수 계산
omega_resonance = 1 / np.sqrt(L * C)
st.write(f"공명 진동수 (f_res): {omega_resonance / (2 * math.pi):.2f} rad/s")

# 특정 각진동수에서의 임피던스 계산
omega_input = st.number_input("임피던스 확인용 각진동수 (rad/s)", value=100.0)
Z_input = np.sqrt(R**2 + (omega_input * L - 1 / (omega_input * C))**2)
st.write(f"입력한 각진동수 {omega_input:.2f} rad/s에서의 임피던스: {Z_input:.2f} Ω")

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot(frequency, V_r_over_V, label="V_R / V")
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("V_r / V (Ratio)")
ax.set_title("Frequency vs. Voltage Ratio (V_R / V)")
ax.legend()
ax.grid(True)

# Streamlit에 그래프 표시
st.pyplot(fig)


