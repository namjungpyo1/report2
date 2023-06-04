import pandas as pd
import Levenshtein_Distance as ld

data = pd.read_csv('ChatbotData.csv') # CSV 파일 내용을 취득
questions = data['Q'].tolist()  # 질문열만 뽑아 파이썬 리스트로 저장
answers = data['A'].tolist()   # 답변열만 뽑아 파이썬 리스트로 저장

while True: # '종료'라는 단어가 입력될 때까지 챗봇과의 대화를 반복
    input_sentence = input('You: ') # 학습데이터 입력
    if input_sentence.lower() == '종료': # 학습데이터에 '종료'라고 입력할 경우
        break # 처챗봇과의 대화 종료
    idx = 0 # 가장 유사한 질문 인덱스 설정용
    list = [] # 유사도 설정용 리스트
    for n in questions: # 질문 수 만큼 반복
        response = ld.calc_distance(input_sentence, n) # 학습데이터의 질문과 chat의 질문의 유사도를 레벤슈타인 거리를 이용해 구하기
        list.append(response) # 레벤슈타인 거리를 이용해 구한 유사도 값을 리스트에 추가
    idx = list.index(min(list)) # chat의 질문과 레벤슈타인 거리와 가장 유사한 학습데이터의 질문의 인덱스를 구하기
    print('Chatbot:', answers[idx]) # 학습 데이터의 인덱스의 답을 chat의 답변을 채택한 뒤 출력