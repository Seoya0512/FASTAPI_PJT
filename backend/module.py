key = './ocr/key_ocr.txt'
with open(key) as f: KEY = f.read()
# 본인의 Secret Key로 치환

URL = './ocr/url_ocr.txt'
with open(URL) as f: URL = f.read()
# 본인의 APIGW Invoke URL로 치환


# ocr로 사용자의 정보를 입력 받는다 
# Module 1 : 사진파일 >> 텍스트 
def call_picture(pic):
  import json
  import base64
  import requests

  f = open(pic, "rb")
  img = base64.b64encode(f.read())

  headers = {
      "Content-Type": "application/json",
      "X-OCR-SECRET": KEY
  }
      
  data = {
      "version": "V2",
      "requestId": "string",
      "timestamp": 0,         # 현재 시간값
      "lang":"ko",
      "images": [
          {
              "name": "sample_image",
              "format": "png",
              "data": img.decode('utf-8')
            # "templateIds": [400]  # 설정하지 않을 경우, 자동으로 템플릿을 찾음 
          }
      ]
  }
  data = json.dumps(data)
  response = requests.post(URL, data=data, headers=headers)
  res = json.loads(response.text)
  id = res['images'][0]['title']['inferText']
  return id


# Module 2 : yolo 함수
