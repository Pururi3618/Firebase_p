import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
key_dict = json.loads(st.secrets["textkey"])

total = 0

genre = st.radio(
    "다음 중 피타고라스 정리의 식으로 알맞은 것은?",
    ["a^2 / b^2 = c^2", "a^2 * b^2 = c^2", "a^2 * a^2 = b^2", "a * b = c", "a / b = c"])
if genre == "a^2 * b^2 = c^2":
    total += 30

"y = -3(x - 3)^2 + 10의 최댓값을 구하시오."
prob = st.text_input('정답을 입력하세요.')
if prob == '10':
    total += 70

        # Fetch the service account key JSON file contents
cred = credentials.Certificate(key_dict)

ref1 = db.reference('user')
ref1.set({"score" : total})