import streamlit as st  
from PIL import Image  
import requests  
from io import BytesIO  
  
st.title("欢迎来到美食探索!")  
st.header("让我们一起发现美味佳肴")  
  
# 显示一张图片  
image_url = "https://ts4.cn.mm.bing.net/th?id=OIP-C.Y-SwqIEoPL1G8H53wrvUkQHaLH&w=204&h=306&c=8&rs=1&qlt=90&o=6&dpr=1.5&pid=3.1&rm=2"  
response = requests.get(image_url)  
img = Image.open(BytesIO(response.content))  
st.image(img, caption="一张美食图片")  
  
# 显示/隐藏文本  
if st.checkbox("显示/隐藏介绍"):  
    st.text("这是一段关于美食的介绍文本。")  
  
# 单选按钮  
food_type = st.radio("选择你喜欢的食物类型:", ('中餐', '西餐', '日料'))  
if food_type == '中餐':  
    st.success("你选择了中餐!")  
elif food_type == '西餐':  
    st.success("你选择了西餐!")  
else:  
    st.success("你选择了日料!")  
  
# 多选框  
favorite_foods = st.multiselect("你最喜欢的食物有哪些:", ['火锅', '披萨', '寿司', '汉堡'])  
st.write("你选择的食物有:", favorite_foods)  
  
# 按钮  
if st.button("更多信息"):  
    st.text("点击了更多信息按钮!")  
  
# 文本输入框和提交按钮  
name = st.text_input("请输入你的名字:")  
if st.button("提交"):  
    st.write(f"你好, {name}!")  
  
# 滑动条  
spice_level = st.slider("选择你的辣度", 0, 10)  
st.write("你选择的辣度是:", spice_level)  
  
# 文件上传  
uploaded_file = st.file_uploader("上传一张美食图片", type=['jpg', 'png'])  
if uploaded_file is not None:  
    img = Image.open(uploaded_file)  
    st.image(img, caption="你上传的美食图片")