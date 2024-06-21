#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st  
import pandas as pd  
import pickle  
  
# 加载模型  
# 注意：现在使用pickle.load而不是joblib.load  
with open('/home/featurize/cat_breed_recommender.pkl', 'rb') as f:  
    clf = pickle.load(f)  
  
def predict_breed(clf, features):  
    # 假设features是一个DataFrame，包含特征值  
    predicted_breed = clf.predict(features)  
    return predicted_breed  
  
def main():  
    st.title('你想领养什么类型的猫猫')  
  
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


# In[ ]:




