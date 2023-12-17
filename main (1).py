import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon
nltk.download('vader_lexicon')


# Sentiment analysis function
def sentiment_res(review):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(review)
    neg = sentiment['neg']
    pos = sentiment['pos']
    neutral = sentiment['neu']
    print(f"negative score: {neg}")
    print(f"positive score: {pos}")
    print(f"neutral score: {neutral}")
    return sentiment


# Streamlit app
st.title("Movie Review Sentiment Analysis")

# Text input
review_text = st.text_area("Review Text", "Type your review here...")

if st.button("Analyze"):
    # Call the sentiment analysis function
    sentiment = sentiment_res(review_text)

    # Display the scores
    # st.markdown("### Sentiment Analysis Results")
    # st.markdown(f"**Positive Score:** `{sentiment['pos']}`")
    # st.markdown(f"**Negative Score:** `{sentiment['neg']}`")
    # st.markdown(f"**Neutral Score:** `{sentiment['neu']}`")

    # Display horizontal bars
    st.markdown("#### Visualization")
    pos_col1, pos_col2 = st.columns(2)
    with pos_col1:
        st.markdown("##### Positive")
        st.progress(sentiment['pos'])
    with pos_col2:
        st.markdown(f"`{sentiment['pos']}`")
    neg_col1, neg_col2 = st.columns(2)
    with neg_col1:
        st.markdown("##### Negative")
        st.progress(sentiment['neg'])
    with neg_col2:
        st.markdown(f"`{sentiment['neg']}`")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("##### Neutral")
        st.progress(sentiment['neu'])
    with col2:
        st.markdown(f"`{sentiment['neu']}`")
