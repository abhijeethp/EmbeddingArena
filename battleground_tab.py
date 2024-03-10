import streamlit as st
from embedding_models.registry import registry as embedding
from similarity_models.registry import registry as similarity
import pandas as pd


def calculate_similarity(text_1, text_2):
    # TODO: pick any N random embedding models
    similarity_scores = []

    # TODO: pick any random similarity model
    similarity_model = similarity.models()["cosine"]
    for name, model in embedding.models().items():
        embedding_1 = model.embed(text_1)
        embedding_2 = model.embed(text_2)

        similarity_scores.append((name, similarity_model.score(embedding_1, embedding_2)))
    return similarity_scores


class BattlegroundTab:

    def __init__(self):
        pass

    def ui(self):
        st.header("Battleground")
        st.write("Battle embedding models with each other! May the best win!")

        col1, col2 = st.columns(2)
        with col1:
            text_1 = st.text_input("Enter first text here!")

        with col2:
            text_2 = st.text_input("Enter second text here!")

        expected_sc = st.slider(
            'How similar do feel these words are',
            min_value=1, max_value=10, step=1, value=5) / 10
        st.write('Expected Similarity Score = ', expected_sc)

        if st.button("Calculate Similarity Score"):
            similarity_scores = calculate_similarity(text_1, text_2)
            df = pd.DataFrame(similarity_scores, columns=['Model', 'Score'])
            df['Loss'] = abs(df['Score'] - expected_sc)
            winner_model = df.loc[df['Loss'].idxmin(), 'Model']
            df['Winner'] = ''
            df.loc[df['Model'] == winner_model, 'Winner'] = '👑'
            df = df.drop(columns=['Loss'])
            markdown_table = df.to_markdown(index=False)
            st.markdown(markdown_table)
