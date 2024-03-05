
##### 기본 정보 입력 #####
# Streamlit 패키지 추가
import streamlit as st
# OpenAI 패키지 추가
import openai 

##### 기능 구현 함수 #####
def askGpt(prompt, apikey):
    client = openai.OpenAI(api_key=apikey)
    response = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=[{"role": "user", "content": prompt}]
    )
    getResponse = response.choices[0].message.content
    return gptResponse

##### 메인 함수 #####
def main():
    st.set_page_config(page_title="광고 문구 생성 프로그램")
    if "OPENAI_API" not in st.session_state:
        st.session_state["OPENAI_API"] = ""
        
    # 사이드바 구현
    with st.sidebar:
        # 사이드바에 OpenAI API 키를 입력받는 텍스트 입력 필드를 생성합니다. 비밀번호 형식으로 입력됩니다.
        open_apikey = st.text_input(label='OPEN API 키', placeholder='Enter Your API Key', type='password')
        # 입력 받은 API 키를 세션 상태에서 저장합니다.
        if open_apikey:
            st.session_state["OPENAI_API"] = open_apikey
        # 사이드바에서 구분선을 추가합니다.
        st.markdown('---')
        
    # 메인 페이지의 헤더를 추가합니다.
    st.header("🎸광고 문구 생성 프로그램")
    # 페이지에 구분선을 추가합니다.
    st.markdown('---')
    
    # 페이지를 두 개의 열로 나눕니다.
    col1, col2 = st.column(2)
    with col1:
        # 첫 번째 열에 입력 필드를 추가합니다.
        name = st.text_input("제품명", placeholder=" ")
        strength = st.text_input("제품 특징", placeholder=" ")
        keyword = st.text_input("필수 포함 키워드", placeholder=" ")
    with col2:
        # 두 번째 열에 입력 필드를 추가합니다.
        com_name = st.text_input("브랜드 명", placeholder="Apple, 올리브영...")
        tone_manner = st.text_input("톤앤 매너", placeholder="발랄하게, 유머러스하게, 감성적으로...")
        value = st.text_input("브랜드 핵심 가치", placeholder="필요 시 입력")
        
    # '광고 문구 생성' 버튼을 클릭하면 아래 코드를 실행합니다.
    if st.button("광고 문구 생성"):
        # GPT에 전달할 지시문을 생성합니다. 제품 정보와 요구사항이 포함됩니다.
        prompt = f'''
        아래 내용을 참고해서 1~2줄짜리 광고문구 5개를 작성해줘
        - 제품명: {name}
        - 브랜드명: {com_name}
        - 브랜드 핵심 가치: {value}
        - 제품 특징: {strength}
        - 톤앤 매너: {tone_manner}
        - 필수 포함 키워드: {keyword}
        '''
        # askGpt 함수를 호출하여 생성된 광고 문구를 받고, 정보 상자에 표시합니다.
        st.info(askGpt(prompt, st.session_state["OPENAI_API"]))

# 스크립트가 직접 실행될 때만 main 함수를 실행합니다.
if __name__ == '__main__':
    main()












