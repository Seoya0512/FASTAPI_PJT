#### ✏️ 프로젝트 주제

이미지 분류 모델을 활용한 투명 페트병 분리배출 서비스 (기기)


#### 🗓 수행 기간 

'21. 10. 27 ~ '21.12. 09



#### 💻 수행 도구 

- 분석 기술 패키지 : Pandas, Numpy, Sklearn 
- 수집 기술 패키지 : BeautifulSoup, Selenium, RestApi, requsests, urllib, json
- 모델링 : Darknet, Yolo, Tensorflow, OpenCv
- AI Service & Web : Naver OCR , Google DialogFlow, Google Gloud, FAST API, HTML, CSS3



#### 📦 사용 데이터

1. AI hub : 생활폐기물 데이터 

2. 인스타크램 크롤링 : #페트라떼챌린지,  #노라벨챌린지

3. 직접 수집

4. 환경부 분리배출 가이드라인


#### 🗑 서비스 소개 및 흐름도 

<img width="70%" alt="서비스소개" src="https://user-images.githubusercontent.com/87962966/145836368-728ba577-ba27-4ad7-9b5c-ef9a588835a8.png"> 
<img width="70%" alt="서비스흐름도" src="https://user-images.githubusercontent.com/87962966/145836372-411ddada-687f-448d-bf87-34cc950701d8.png">


#### 💻 웹으로 대체 시현한 기기 와 챗봇 (부가서비스)

<img width="70%" alt="챗봇" src="https://user-images.githubusercontent.com/87962966/145836429-4d246541-0dd4-480b-8cb2-1ec519fff7e7.png"> 
<img width="70%" alt="모델링 결과" src="https://user-images.githubusercontent.com/87962966/145836456-330706b3-ccbf-4769-be44-48b4477a9e81.png">

   
#### 👾 수행 결과

Yolo v4를 활용하여 투명 페트병의 라벨 부착 유무를 판단하는 모델링 구축 완료, Google Dialogflow를 활용한 애매한 분리수거 챗봇을 포함한 웹 프레임 구축 



#### ❓한계점

1. 데이터 부족 : 개인의 생활 습관에 따라 이미지 데이터의 모습이 다름
2. 모델의 한계 : 투명한 페트병을 통해 비친 배경 색 등을 함께 학습하는 경우가 많이 발생, 모델의 정확도 낮춤 







