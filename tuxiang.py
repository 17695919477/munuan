import streamlit as st
from fastai.vision.all import *
from pathlib import Path
import pickle

# 加载训练好的模型
model_path = "/home/featurize/qimozuoye.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)
    

# Streamlit 界面
st.title("猫咪识别与推荐")

# 用户上传图片
uploaded_file = st.file_uploader("选择一张猫咪图片...", type=["jpg", "png"])

if uploaded_file is not None:
    # 加载图片并进行识别
    img = PILImage.create(uploaded_file)
    pred, pred_idx, probs = learn.predict(img)
    st.write(f"识别出的猫咪品种: {pred}")
    st.write(f"置信度: {probs[pred_idx]:.4f}")

  
    

    # 根据用户评分和偏好调整推荐分数
    # 这里将添加推荐逻辑

# 运行 Streamlit 应用程序
if __name__ == "__main__":
    main()
