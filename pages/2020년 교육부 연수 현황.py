import streamlit as st
import pandas as pd

# 데이터 불러오기
file_path = 'path_to_your_file/data_practice.csv'
data = pd.read_csv(file_path)

# Streamlit 앱
st.title('프로그램 이수율 및 승인인원 분석')

# 옵션 선택
option = st.selectbox('옵션 선택:', 
                      ['이수율이 높은 상위 10개 프로그램 확인하기', 
                       '이수율이 낮은 하위 10개 프로그램 확인하기', 
                       '승인인원이 높은 상위 10개 프로그램 확인하기', 
                       '승인인원이 낮은 하위 10개 프로그램 확인하기'])

# 조건에 따른 데이터 출력
if option == '이수율이 높은 상위 10개 프로그램 확인하기':
    top_10_completion = data.sort_values(by='이수율', ascending=False).head(10)
    st.write('이수율이 높은 상위 10개 프로그램:')
    st.dataframe(top_10_completion[['과정명', '이수율']])

elif option == '이수율이 낮은 하위 10개 프로그램 확인하기':
    bottom_10_completion = data.sort_values(by='이수율').head(10)
    st.write('이수율이 낮은 하위 10개 프로그램:')
    st.dataframe(bottom_10_completion[['과정명', '이수율']])

elif option == '승인인원이 높은 상위 10개 프로그램 확인하기':
    top_10_approved = data.sort_values(by='승인인원', ascending=False).head(10)
    st.write('승인인원이 높은 상위 10개 프로그램:')
    st.dataframe(top_10_approved[['과정명', '승인인원']])

elif option == '승인인원이 낮은 하위 10개 프로그램 확인하기':
    bottom_10_approved = data.sort_values(by='승인인원').head(10)
    st.write('승인인원이 낮은 하위 10개 프로그램:')
    st.dataframe(bottom_10_approved[['과정명', '승인인원']])
