import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
file_path = 'daily_temp.csv'
data = pd.read_csv(file_path)

# 데이터 정리
data.columns = data.columns.str.strip()
data['날짜'] = data['날짜'].str.strip()
data['날짜'] = pd.to_datetime(data['날짜'], errors='coerce')

# 날짜에서 연도 추출
data['연도'] = data['날짜'].dt.year

# 연도별로 그룹화하여 평균, 최저, 최고 기온 계산
annual_data = data.groupby('연도').agg({'평균기온(℃)': 'mean', '최저기온(℃)': 'min', '최고기온(℃)': 'max'}).reset_index()

# Streamlit 앱
st.title('연도별 기온 변화 추이')

# 차트 선택
chart_type = st.selectbox('차트 유형 선택:', ['꺾은선 그래프', '막대 그래프'])

# 그래프 그리기
if chart_type == '꺾은선 그래프':
    fig, ax = plt.subplots()
    ax.plot(annual_data['연도'], annual_data['평균기온(℃)'], label='평균 기온', marker='o')
    ax.plot(annual_data['연도'], annual_data['최저기온(℃)'], label='최저 기온', marker='o')
    ax.plot(annual_data['연도'], annual_data['최고기온(℃)'], label='최고 기온', marker='o')
    ax.set_xlabel('연도')
    ax.set_ylabel('기온 (℃)')
    ax.set_title('연도별 기온 변화 추이')
    ax.legend()
    st.pyplot(fig)
else:
    fig, ax = plt.subplots()
    bar_width = 0.25
    years = annual_data['연도']
    r1 = range(len(years))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]
    
    ax.bar(r1, annual_data['평균기온(℃)'], color='b', width=bar_width, edgecolor='grey', label='평균 기온')
    ax.bar(r2, annual_data['최저기온(℃)'], color='g', width=bar_width, edgecolor='grey', label='최저 기온')
    ax.bar(r3, annual_data['최고기온(℃)'], color='r', width=bar_width, edgecolor='grey', label='최고 기온')
    
    ax.set_xlabel('연도')
    ax.set_ylabel('기온 (℃)')
    ax.set_title('연도별 기온 변화 추이')
    ax.set_xticks([r + bar_width for r in range(len(years))])
    ax.set_xticklabels(years, rotation=90)
    ax.legend()
    st.pyplot(fig)
