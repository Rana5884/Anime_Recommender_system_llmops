import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline

from dotenv import load_dotenv 

st.set_page_config(page_title="Anime Recommender", layout="wide")


load_dotenv()

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("Anime Recommender System")

query = st.text_input("Enter you anime prefrences eg: a young shonen wants to become a hokage")
if query:
    with st.spinner("Fetching Recomendataion for you"):
        respone = pipeline.recommend(query)
        st.markdown("### Recomendation")
        st.write(respone)