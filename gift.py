import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(
    page_icon="🎂",
    page_title="Happy Birthday Genius Madam",
    layout="wide"
)

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

cont1 = st.container()
cont2 = st.container()

with cont1:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
                <style>
                    [data-testid="column"]{
                        display: flex;
                        justify-content: center;
                        align-items: center;
                    }
                    div.row-widget.stButton{
                        display: flex;
                        justify-content: center;
                    }
                </style>
                <center>
                    <h1>Happy Birthday Genius Madam</h1>
                    <h4>Forget the past, look forward to the future, for the best things are yet to come.</h4>
                    <div style="display: flex; justify-content: flex-end;">
                        <h6>- Your Hitler Sir🦋</h6>
                    </div>
                </center>
            """, unsafe_allow_html=True
        )

    with col2:
        url = "https://assets4.lottiefiles.com/packages/lf20_l3wwobeh.json"
        st_lottie(load_lottie_url(url))
        st.balloons()
        st.balloons()
        st.balloons()


st.markdown(
    """
        <style>
            header, footer{
                visibility: hidden;
            }
        </style>
    """, unsafe_allow_html=True
)
