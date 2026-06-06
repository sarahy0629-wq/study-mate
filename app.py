import streamlit as st
import pandas as pd
import random

# 제목
st.title("📚 Study Mate")
st.subheader("공부 습관 관리 웹사이트")

st.write("공부 계획을 세우고 학습 습관을 관리하기 위해 제작한 웹사이트입니다.")

# 이름 입력
name = st.text_input("이름을 입력하세요")

if name:
    st.success(f"{name}님 환영합니다!")

# 공부 시간 설정
st.header("⏰ 공부 시간 설정")

study_time = st.slider(
    "오늘 공부할 목표 시간을 선택하세요",
    0,
    15,
    3
)

st.write(f"오늘 목표 공부 시간 : {study_time}시간")

# 오늘의 할 일
st.header("✅ 오늘의 할 일")

todo1 = st.text_input("할 일 1")
todo2 = st.text_input("할 일 2")
todo3 = st.text_input("할 일 3")

check1 = st.checkbox(todo1 if todo1 else "할 일 1")
check2 = st.checkbox(todo2 if todo2 else "할 일 2")
check3 = st.checkbox(todo3 if todo3 else "할 일 3")

count = sum([check1, check2, check3])

st.write(f"완료한 항목 수 : {count}개")

# 과목별 공부 시간
st.header("📊 과목별 공부 시간")

physics_time = st.number_input("물리 공부 시간", 0, 15, 2)
python_time = st.number_input("파이썬 공부 시간", 0, 15, 3)
english_time = st.number_input("영어 공부 시간", 0, 15, 1)

data = pd.DataFrame({
    "과목": ["물리", "파이썬", "영어"],
    "시간": [physics_time, python_time, english_time]
})

st.bar_chart(data.set_index("과목"))

# 공부 명언
st.header("💡 오늘의 공부 명언")

quotes = [
    "포기하지 말자!",
    "꾸준함이 가장 중요하다.",
    "오늘의 노력이 내일의 실력이 된다.",
    "작은 발전도 큰 변화를 만든다.",
    "시작이 반이다."
]

if st.button("명언 보기"):
    st.info(random.choice(quotes))

# 공부 점수
st.header("⭐ 오늘의 공부 점수")

score = study_time * 10 + count * 10

st.write(f"오늘의 공부 점수는 {score}점입니다.")

# 마무리
st.write("---")
st.write("Study Mate를 이용해 꾸준한 공부 습관을 만들어보세요!")