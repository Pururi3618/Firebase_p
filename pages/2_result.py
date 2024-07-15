import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
key_dict = json.loads(st.secrets["textkey"])

cred = credentials.Certificate(key_dict)

ref = db.reference('user/score')
st.write(st.session_state.name, '님의 점수는', ref.get(), '점 입니다.')