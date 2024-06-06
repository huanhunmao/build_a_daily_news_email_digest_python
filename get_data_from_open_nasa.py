import requests
import streamlit as st

# 获取NASA APOD的API数据
api_key = 'xxx'
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# 拿到数据 并拆一下
response = requests.get(url)
# print('request', response) # request <Response [200]>
data = response.json()

title = data['title']
image_url = data['url']
explanation = data['explanation']

# 下载图片并保存
image_filepath = 'image.png'
response2 = requests.get(image_url)
with open(image_filepath, 'wb') as file:
    file.write(response2.content)

# 使用Streamlit显示内容 到网页 streamlit run get_data_from_open_nasa.py
st.title(title)
st.image(image_filepath)
st.write(explanation)