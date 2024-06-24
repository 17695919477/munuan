import streamlit as st
from PIL import Image
import pandas as pd
import pickle
from fastai.vision.all import *
from pathlib import Path
import platform

plt = platform.system()
if plt != 'Windows':
  pathlib.WindowsPath = pathlib.PosixPath

# 加载猫品种分类模型
model_path_cat = Path("maomi.pkl")
learn_cat = load_learner(model_path_cat)

# Streamlit 界面
st.title("流浪猫猫识别系统！！！")

# 猫品种分类器部分
st.write("请上传一张猫的图片，我们将帮你识别流浪的猫猫的品种。")

uploaded_file_cat = st.file_uploader("选择一张图片...", type=["jpg", "jpeg", "png"])

if uploaded_file_cat is not None:
    img_cat = PILImage.create(uploaded_file_cat)
    st.image(img_cat, caption='上传的图片', use_column_width=True)
    st.write("")
    st.write("分类中...")

    pred_cat, pred_idx_cat, probs_cat = learn_cat.predict(img_cat)
    st.write(f"这是一只: {pred_cat}种类的猫猫")
    st.write(f"置信度: {probs_cat[pred_idx_cat]:.4f}")



# 猫品种推荐器部分
st.title('如果你想领养一只猫猫的话，请输入你的想法！！！')

with open("cat_breed_recommender.pkl", 'rb') as f:  
    clf = pickle.load(f)  
  
def predict_breed(clf, features):  
    # 假设features是一个DataFrame，包含特征值  
    predicted_breed = clf.predict(features)  
    return predicted_breed  
  
def main():  
    st.title('猫猫品种推荐系统')  
  
    # 使用滑动条和复选框收集用户输入，顺序必须与训练时相同  
    score_personality = st.slider('性格', 1, 10, 5)  
    score_social = st.slider('社交性', 1, 10, 5)  
    score_hair_loss = st.slider('掉毛程度', 1, 10, 3)  
    score_vitality = st.slider('生命力', 1, 10, 5)  
    score_appearance = st.slider('好看程度（毛色）', 1, 10, 5)  
    score_sticky = st.checkbox('是否粘人', True)  
  
    # 将用户输入转换为DataFrame，确保顺序与训练时相同  
    features_dict = {  
        '性格': [score_personality],  
        '社交性': [score_social],  
        '掉毛程度': [score_hair_loss],  
        '生命力': [score_vitality],  
        '好看程度（毛色）': [score_appearance],  
        '是否粘人': [int(score_sticky)]  # 确保顺序与训练时相同  
    }  
    features = pd.DataFrame(features_dict)  
  
    # 重置索引，因为pandas可能在创建DataFrame时添加了索引  
    features = features.reset_index(drop=True)  
  
    # 使用模型进行预测  
    predicted_breed = predict_breed(clf, features)  
    st.write(f'推荐的猫品种是: {predicted_breed[0]}')  # 因为predict返回的是数组，我们需要索引[0]来取第一个预测结果  
  
if __name__ == "__main__":  
    main()
    
