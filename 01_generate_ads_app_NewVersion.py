##### 기본 정보 입력 #####
# Streamlit 패키지를 가져옵니다. Streamlit을 사용해 웹 애플리케이션을 쉽게 만들 수 있습니다.
import streamlit as st
# OpenAI 패키지를 가져옵니다. 이를 통해 OpenAI의 API를 사용할 수 있습니다.
import openai

##### 기능 구현 함수 #####
# GPT 모델에 질문하고 응답을 받는 함수입니다.
def askGpt(prompt, apikey):
    # OpenAI API를 사용하기 위한 클라이언트를 생성합니다. 여기서는 사용자의 API 키가 필요합니다.
    client = openai.OpenAI(api_key=apikey)
    # GPT-3.5 모델에 질문을 전송하고 응답을 받습니다. 질문은 'prompt' 변수에 담겨 있습니다.
    response = client.chat.completions.create(
        model="gpt-4-0125-preview",  # 사용할 GPT 모델을 지정합니다.
        messages=[{"role": "user", "content": prompt}]  # 사용자의 역할과 내용을 지정합니다.
    )
    # GPT로부터 받은 첫 번째 응답의 내용을 추출합니다.
    gptResponse = response.choices[0].message.content
    # 추출한 응답을 반환합니다.
    return gptResponse

##### 메인 함수 #####
def main():
    # 웹 페이지의 설정을 합니다. 여기서는 페이지의 제목을 "광고 문구 생성 프로그램"으로 설정합니다.
    st.set_page_config(page_title="광고 문구 생성 프로그램")
    # 세션 상태에서 'OPENAI_API' 키가 없으면 초기화합니다.
    if "OPENAI_API" not in st.session_state:
        st.session_state["OPENAI_API"] = ""

    # 사이드바 구현
    with st.sidebar:
        # 사이드바에 OpenAI API 키를 입력받는 텍스트 입력 필드를 생성합니다. 비밀번호 형식으로 입력됩니다.
        open_apikey = st.text_input(label='OPENAI API 키', placeholder='Enter Your API Key', type='password')
        # 입력받은 API 키를 세션 상태에 저장합니다.
        if open_apikey:
            st.session_state["OPENAI_API"] = open_apikey
        # 사이드바에 구분선을 추가합니다.
        st.markdown('---')

    # 메인 페이지의 헤더를 추가합니다.
    st.header("🎸광고 문구 생성 프로그램")
    # 페이지에 구분선을 추가합니다.
    st.markdown('---')

    # 페이지를 두 개의 열로 나눕니다.
    col1, col2 = st.columns(2)
    with col1:
        # 첫 번째 열에 입력 필드를 추가합니다.
        name = st.text_input("제품명", placeholder=" ")
        strength = st.text_input("제품 특징", placeholder=" ")
        keyword = st.text_input("필수 포함 키워드", placeholder=" ")
    with col2:
        # 두 번째 열에 입력 필드를 추가합니다.
        com_name = st.text_input("브랜드 명", placeholder="Apple, 올리브영..")
        tone_manner = st.text_input("톤엔 매너", placeholder="발랄하게, 유머러스하게, 감성적으로..")
        value = st.text_input("브랜드 핵심 가치", placeholder="필요 시 입력")

    # "광고 문구 생성" 버튼을 클릭하면 아래 코드를 실행합니다.
    if st.button("광고 문구 생성"):
        # GPT에 전달할 지시문을 생성합니다. 제품 정보와 요구 사항이 포함됩니다.
        prompt = f'''
        아래 내용을 참고해서 1~2줄짜리 광고문구 5개 작성해줘
        - 제품명: {name}
        - 브랜드 명: {com_name}
        - 브랜드 핵심 가치: {value}
        - 제품 특징: {strength}
        - 톤엔 매너: {tone_manner}
        - 필수 포함 키워드: {keyword}
        '''
        # askGpt 함수를 호출하여 생성된 광고 문구를 받고, 정보 상자에 표시합니다.
        st.info(askGpt(prompt, st.session_state["OPENAI_API"]))

# 스크립트가 직접 실행될 때만 main 함수를 실행합니다.
if __name__ == '__main__':
    main()
