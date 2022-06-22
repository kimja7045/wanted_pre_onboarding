# 프리온보딩 백엔드 코스 3차 선발과제


## 설치
```
가상환경 설치
python -m venv .venv

가상환경 활성화
. .venv/bin/activate

패키지 설치
pip install -r requirements.txt
```

## 실행
```
서버 실행
python manage.py runserver
```

## 가산점요소
 - 채용공고 검색 기능
 
 - 회사가올린다른채용공고 기능
 
 - 사용자는 채용공고에 지원합니다 기능
 
 
 ## 요구사항 분석
  1 - 설계할 모델(테이블) 정리
   
   ### 모델
    유저, 채용공고, 회사, 채용지원
    
  2 - 모델 간 관계를 포함하여 각 모델 간에 필요한 컬럼 나열
  
  3 - 요구사항에 맞게 serializer 설정
  
  4 - 각 api 로직이 있는 View 설정
  
  5 - 요구사항에 따른 api도메인 설정 및 각 api도메인에 맞는 View 설정
  
  6 - 테스트 및 수정