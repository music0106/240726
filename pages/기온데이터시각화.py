import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = 'path_to_your_file/daily_temp.csv'
data = pd.read_csv(file_path)

# Clean the data
data.columns = data.columns.str.strip()
data['날짜'] = data['날짜'].str.strip()
data['날짜'] = pd.to_datetime(data['날짜'], errors='coerce')

# Extract year from the date
data['연도'] = data['날짜'].dt.year

# Group by year and calculate the mean, minimum, and maximum temperatures
annual_data = data.groupby('연도').agg({'평균기온(℃)': 'mean', '최저기온(℃)': 'min', '최고기온(℃)': 'max'}).reset_index()

# Streamlit app
st.title('Annual Temperature Trends')

# Chart selection
chart_type = st.selectbox('Select chart type:', ['Line Chart', 'Bar Chart'])

# Plotting
if chart_type == 'Line Chart':
    fig, ax = plt.subplots()
    ax.plot(annual_data['연도'], annual_data['평균기온(℃)'], label='Average Temperature', marker='o')
    ax.plot(annual_data['연도'], annual_data['최저기온(℃)'], label='Minimum Temperature', marker='o')
    ax.plot(annual_data['연도'], annual_data['최고기온(℃)'], label='Maximum Temperature', marker='o')
    ax.set_xlabel('Year')
    ax.set_ylabel('Temperature (℃)')
    ax.set_title('Annual Temperature Trends')
    ax.legend()
    st.pyplot(fig)
else:
    fig, ax = plt.subplots()
    bar_width = 0.25
    years = annual_data['연도']
    r1 = range(len(years))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]
    
    ax.bar(r1, annual_data['평균기온(℃)'], color='b', width=bar_width, edgecolor='grey', label='Average Temperature')
    ax.bar(r2, annual_data['최저기온(℃)'], color='g', width=bar_width, edgecolor='grey', label='Minimum Temperature')
    ax.bar(r3, annual_data['최고기온(℃)'], color='r', width=bar_width, edgecolor='grey', label='Maximum Temperature')
    
    ax.set_xlabel('Year')
    ax.set_ylabel('Temperature (℃)')
    ax.set_title('Annual Temperature Trends')
    ax.set_xticks([r + bar_width for r in range(len(years))])
    ax.set_xticklabels(years, rotation=90)
    ax.legend()
    st.pyplot(fig)
