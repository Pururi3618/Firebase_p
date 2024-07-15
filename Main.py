import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
key_dict = json.loads(st.secrets["textkey"])

# Fetch the service account key JSON file contents
cred = credentials.Certificate(key_dict)

#Initialize the app with a custom auth variable, limiting the server's access
if not firebase_admin._apps :
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://iot-firebase-9402e-default-rtdb.firebaseio.com/'
    })

st.markdown("# 수학")
name = st.text_input('이름을 입력하세요.')
sn = st.text_input('학번을 입력하세요.')
if st.button('제출') :
    if 'name' not in st.session_state:
        st.session_state.name = name
    else:
        st.session_state.name = name
    if 'sn' not in st.session_state:
        st.session_state.sn = sn
    else:
        st.session_state.sn = sn