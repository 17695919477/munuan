import streamlit as st  
from random import choices  
from fastai.vision.all import load_learner  # 确保你安装了fastai并且模型路径是正确的  
import pandas as pd  
  
# 加载模型（假设这是FastAI模型，但这里我们不会实际使用它进行推荐）  
model_path = 'C:\\xiaohua.pkl'  # 假设路径是正确的  
loaded_model = load_learner(model_path)  # 但我们在这里不会用它  
  
# 加载笑话  
def load_jokes_from_excel(file_path):  
    jokes_df = pd.read_excel(file_path, sheet_name=0, header=None)  
    return jokes_df.iloc[:, 0].tolist()  
  
# 随机获取笑话  
def get_random_jokes(jokes_list, n=3):  
    return choices(jokes_list, k=n)  
  
# 示例推荐函数（你需要根据你的模型来实现真正的推荐逻辑）  
def recommend_jokes_placeholder(jokes_list, model=None):  
    return get_random_jokes(jokes_list)  
  
# 用户评分逻辑  
def rate_joke(joke_id, rating):  
    if 'joke_ratings' not in st.session_state:  
        st.session_state.joke_ratings = {}  
    st.session_state.joke_ratings[joke_id] = rating  
  
# 计算用户满意度  
def calculate_satisfaction(ratings):  
    if not ratings:  
        return 0  
    # 假设我们允许负分，但简单起见，我们只计算平均分（不考虑正负）  
    return sum(ratings.values()) / len(ratings)  
  
def main():  
    st.title("笑话推荐系统")  
  
    jokes_list = load_jokes_from_excel('C:\\data\\Dataset4JokeSet.xlsx')  
  
    if 'random_jokes' not in st.session_state:  
        st.session_state.random_jokes = get_random_jokes(jokes_list)  
  
    random_jokes = st.session_state.random_jokes  
  
    # 用户互动部分（展示随机笑话并允许评分）  
    with st.expander("随机笑话"):  
        for idx, joke in enumerate(random_jokes):  
            st.markdown(f"**笑话 {idx+1}**: {joke}")  
            rating = st.slider("为笑话评分（0-5）:", 0, 5, 1, key=f"rating_{idx}")  
            rate_joke(idx, rating)  
  
    # 推荐系统部分（这里只是一个示例）  
    if 'recommended_jokes' not in st.session_state:  
        st.session_state.recommended_jokes = recommend_jokes_placeholder(jokes_list)  
  
    recommended_jokes = st.session_state.recommended_jokes  
  
    with st.expander("推荐笑话"):  
        for idx, joke in enumerate(recommended_jokes):  
            st.markdown(f"**推荐笑话 {idx+1}**: {joke}")  
            rating = st.slider("为推荐笑话评分（0-5）:", 0, 5, 1, key=f"recommended_rating_{idx}")  
            rate_joke(f"recommended_{idx}", rating)  
  
    # 显示用户满意度  
    with st.expander("用户满意度"):  
        ratings = st.session_state.joke_ratings  
        satisfaction = calculate_satisfaction(ratings)  
        st.markdown(f"**用户满意度：{satisfaction*10:.2f}/10**")  
  
if __name__ == '__main__':  
    main()