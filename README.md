# 🎬 FINAL PJT

### **✔ 개요**

제  작  자 : 김지원, 박서영

|            [김지원](https://github.com/wonjw3638)            |            [박서영](https://github.com/manchott)             |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| <a href="https://github.com/wonjw3638"><img src=https://github.com/wonjw3638.png width="150px;" alt="https://github.com/wonjw3638"/></a> | <a href="https://github.com/manchott"><img src=https://github.com/manchott.png width="150px;" alt="https://github.com/manchott"/></a> |
|                         **Frontend**                         |                         **Backend**                          |

날        짜 : 2022-11-17 ~ 2022-11-24

환        경 : Windows 10 Pro

개발도구 : Visual Studio Code, Google Chrome, Git Lab

사용 프레임워크 : Django 3.2+, Bootstrap

영화 원천 데이터 : TMDB API

그 외 사용 툴 : Figma, notion, favicon generator

<br>

### **✔ 역할**

Frontend 구현 : 김지원

Backend 구현 : 박서영

<br>

## ⭐ 목표 및 제작동기

**영화 장르 취향을 찾아 줄 수 있는 페이지**

<br>

### ✔ **제작동기**

OTT 서비스를 이용하기 위해 가입을 하다보면 좋아하는 영화를 물어보며 취향을 찾는 경우가 많다. 그러나 시청한 적이 없는 영화가 있다면 그것을 싫어하는 지, 혹은 안 본 것인지 구분할 수 가 없다. 또한 영화를 많이 시청하지 않은 사용자라면 자신에게 맞춰진 영화 추천받기가 힘들 것이다. 이를 보완하기 위해 영화의 트레일러를 보고 사용자가 어떤 장르를 좋아하는 지 파악하여 사용자가 좋아할 것으로 추측되는 장르를 추천해주는 페이지를 제작해보고자 하였다.

<br>

### ✔ **구현 목표**

- 사용자는 5, 10, 20개의 영화 트레일러를 랜덤으로 확인할 수 있다.
- 트레일러를 확인한 후에는 Good, Bad를 통해 좋은지 싫은지 나타낼 수 있다.
- 사용자가 좋다고 표현한 영화들을 바탕으로 가장 좋아하는 장르 3가지를 추려서 보여준다. 
- 결과페이지에서는 사용자가 좋아하는 3가지 장르와, 전 페이지에서 사용자가 좋다고 했던 영화목록들을 확인할 수 있다.

#### 🔹 **Extra**

- 페이지는 로그인을 해야 사용할 수 있다.
- 로그인한 사용자는 프로필 페이지에서 그동안 좋다고 표시한 영화와 상위 장르 3가지에 대한 장르별 영화 목록을 확인할 수 있다.
- 프로필 페이지와 결과 페이지에서 영화 포스터를 누르면 영화의 detail 정보를 확인할 수 있다.
- detial 페이지에서는 간단한 리뷰를 남길 수 있다.
- 트레일러를 확인하는 페이지에서 위의 영화별 리뷰들을 랜덤으로 확인할 수 있다.

<br>

## 🖼 초기 디자인

### **🖌 FIgma**

![TV - 1](https://user-images.githubusercontent.com/109324634/203835594-81737ab5-a78f-4f3d-9bdc-30fa5ef41cb2.png)

![TV - 3](https://user-images.githubusercontent.com/109324634/203835612-f0172ca7-9261-4ad3-a821-11a6ff8ab9ce.png)

![TV - 4](https://user-images.githubusercontent.com/109324634/203835645-036b06c9-8b1a-4270-add9-2b5a6a3f242c.png)

![TV - 5](https://user-images.githubusercontent.com/109324634/203835667-25f8c6f5-f995-48f1-b0f1-b11bd0a72c90.png)

![TV - 8](https://user-images.githubusercontent.com/109324634/203835692-d2260760-3355-4730-9831-93bbf9a4e81b.png)

![TV - 9](https://user-images.githubusercontent.com/109324634/203835721-1450906b-c5d0-4601-8766-ca08addc1db7.png)

![TV - 10](https://user-images.githubusercontent.com/109324634/203835746-1d74744b-ba40-4de1-9db5-9d0e0a0f7349.png)

![TV - 11](https://user-images.githubusercontent.com/109324634/203835784-3aeb7fac-9551-4edd-a67f-94d584007113.png)

![TV - 12](https://user-images.githubusercontent.com/109324634/203835813-972292b0-f303-43d2-870a-6ab8de77b5cc.png)

<br>

### **🎨 Color Palette**

![Untitled](https://user-images.githubusercontent.com/109324634/203837218-10d476a0-72ef-46ce-87c8-f09de8f363ec.png)





## 🗂DIAGRAM

### ✔ **ERD (Entity-Relationship Digram)**

![ERD](https://user-images.githubusercontent.com/109324634/203836096-7a2c5fb4-067e-4d01-ac15-1e5031897704.png)

<br>

### ✔  **Django APP**

`choices` : 메인페이지, 트레일러 확인 및 결과 확인 페이지 제작. 트레일러 선택에 따른 장르 도출 기능 구현.

`movies` : 영화 정보 model, 리뷰 model 구현. 영화 detail 페이지 제작

`accounts` : 유저의 회원가입, 로그인, 로그아웃 기능 구현, 프로필 페이지 제작

<br>

### ✔**URL**

#### **🔹 chocies**

| URL 패턴          | 역할                                                       |
| ----------------- | ---------------------------------------------------------- |
| /choices/         | 영화 취향 찾기 시작 페이지                                 |
| /choices/start/   | 영화 취향 찾기 설명서와 평가할 영화 개수를 선택하는 페이지 |
| /choices/trailer/ | 단일 트레일러 감상                                         |
| /choices/result/  | 선호하는 장르 확인, 고른 영화를 확인할 수 있는 페이지      |

<br>

#### **🔹 movies**

| URL 패턴                            | 역할                       |
| ----------------------------------- | -------------------------- |
| /movies/                            | 영화 취향 찾기 시작 페이지 |
| /movies/<movie_id>/                 | 단일 영화 상세 페이지 조회 |
| /movies/<movie_id>/comments/        | 단일 영화의 모든 댓글 조회 |
| /movies/<movie_id>/comments/create/ | 단일 영화에 댓글 작성      |

<br>

#### **🔹 accounts**

| URL 패턴                      | 역할                                               |
| ----------------------------- | -------------------------------------------------- |
| /accounts/signup/             | 회원 가입 페이지 & 단일 회원 데이터 생성(회원가입) |
| /accounts/login/              | 로그인 페이지 & 세션 데이터 생성 및 저장(로그인)   |
| /accounts/logout/             | 세션 데이터 삭제(로그아웃)                         |
| /accounts/<username>/         | 사용자 상세 조회 페이지(프로필)                    |
| /accounts/<username>/<genre>/ | 사용자가 선호하는 장르 목록 페이지                 |

<br>

### ✔**View**

#### **🔹 chocies**

| View 함수명 | 역할                                                         | 허용 HTTP Method |
| ----------- | ------------------------------------------------------------ | ---------------- |
| index       | 영화 취향 찾기 시작 페이지 조회                              | GET              |
| start       | 평가할 영화 개수 선택                                        | GET, POST        |
| option      | 유저가 선택한 영화 개수만큼 영화를 랜덤으로 저장             | GET, POST        |
| trailer     | 랜덤으로 저장된 영화 조회                                    | GET              |
| select      | 트레일러를 본 영화를 좋아요/싫어요                           | GET, POST        |
| result      | 취향 찾기 결과 조회. 최다 선택된 장르 3개에 해당하는 영화 추천과 사용자가 선택한 영화 조회 페이지 |                  |

<br>

#### **🔹 movies**

| View 함수명    | 역할                  | 허용 HTTP Method |
| -------------- | --------------------- | ---------------- |
| detail         | 영화 상세 정보 조회   | GET              |
| get_comments   | 단일 영화의 댓글 조회 | GET              |
| create_comment | 단일 영화에 댓글 생성 | GET, POST        |

<br>

#### **🔹 accounts**

| View 함수명 | 역할                                                      | 허용 HTTP Method |
| ----------- | --------------------------------------------------------- | ---------------- |
| signup      | 회원 가입 & 단일 회원 데이터 생성(회원가입)               | GET, POST        |
| login       | 로그인 & 세션 데이터 생성 및 저장                         | GET, POST        |
| logout      | 세션 데이터 삭제(로그아웃)                                | POST             |
| profile     | 사용자 상세 조회(프로필)                                  | GET              |
| genre       | 사용자가 선호하는 모든 영화와 좋아하는 장르 상위 3개 조회 | GET              |

<br>

## 📆 초기 계획 및 일간 기록

### 📋 초기 계획

✔  **2022-11-20 까지**

- Data 수집 완료
- 초기 계획까지의 기능 및 페이지 제작 완료

<br>

✔ **2022-11-24 까지**

- 초기 계획 + extra 기능 및 페이지 제작 완료
- README.md 작성
- 발표 준비

<br>

### ⏰ Daily Record

#### 🔖 Frontend : 김지원

**🔹 2022-11-16 (수)**

main page 완성

select page 완성

trailer page 제작 중

- 글씨체를 조금 더 찾아봐야겠다
- tailer 개수 선택하는 UI가 기본 form 형태 -> Customize 해야한다

<br>

**🔹 2022-11-17 (목)**

trailer page 완성

result page 완성

- 반응형 제대로 되는지 한 번 확인하기
- 결과 페이지에서 장르를 바꿔서 확인 할 때, 아코디언이 닫혔다가 열리면서 깜빡이는 것 처럼 보이는 게 조금 거슬린다. 개선할 방법을 찾아봐야겠다.

model form 사용

<br>

**🔹 2022-11-18 (금)**

detail page 제작

메뉴 개수 받아오기 js 구현

result page에 carousel이 2개씩 나오는 오류 개선

장르별 carousel이 열려있는데, 좋아요를 누른 영화 목록을 확인할 때 닫히지 않는 오류 개선

<br>

**🔹 2022-11-21 (월)**

accounts app 제작 완료

회원 가입, 로그인 페이지 제작 완료

create user form customize

프로필 페이지 구상, 기획

프로필 페이지 제작 시작

<br>

**🔹 2022-11-22 (화)**

프로필 페이지 제작 완료

detail 페이지 제작 시작

유저 이름, 이메일 글자수 제한.

<br>

**🔹 2022-11-23 (수)**

리뷰 버튼 제작 - bootstrap Popover

리뷰 남기는 modal 제작

<br>

**🔹 2022-11-24 (목)**

리뷰 작성 form customize 완료

detail page 제작 완료



#### 🔖 Backend : 박서영

**🔹 2022-11-16 (수)**

movies, choices model 완성

choices/start에서 유저가 5, 10, 15개 중에 선택하기 완료

choices/choose에서 유저가 고른 개수만큼 영화 긁어오기 완료

- 영화를 좌우로 움직일 방법 생각해보자

<br>

**🔹 2022-11-17 (목)**

choice 모델 변경

- 유저가 고른 개수만큼의 영화 저장(option_choices)
- 좋아요 영화(like_choices)
- 싫어요 영화(dislike_choices)

좋아요, 싫어요 버튼 누르면 각각의 데이터베이스에 영화 저장됨

마지막 영화에서 좋아요/싫어요 누르면 최종 페이지 넘어가야하는데 안넘어가는 오류

<br>

**🔹 2022-11-18 (금)**

최종 페이지 넘어가는 오류 개선

마지막 영화가 DB에 저장되지 않는 오류

<br>

**🔹 2022-11-21 (월)**

fixtures 제작 완료

- 한국에서 개봉한 영화만
- 19+ 제외
- 1000+개

<br>

**🔹 2022-11-22 (화)**

url, view 정리

user 모델에 choice를 연결

결과창에 장르 보여지게 함

<br>

**🔹 2022-11-23 (수)**

결과창 carousel을 DB와 연결함

프로필 페이지에서 선택한 영화들 / 선호하는 장르의 영화들 볼 수 있음

영화 디테일 페이지 데베와 연결함

트레일러 볼 때 버튼 누르면 리뷰 있는지 없는지 확인 가능 - 랜덤 리뷰 뜨게 할 예정

<br>

**🔹 2022-11-24 (목)**

리뷰 점수 데베에 반영하기 성공 / 1~10 마우스 호버 하면 색 바뀜

카로셀 누르면 영화 상세페이지로 넘어감

각 장르별 색깔 지정해서 영화 상세 페이지에서 볼 수 있게 됨

트레일러 볼 때 버튼 누르면 영화 없음 or 랜덤 리뷰 뜸

<br>

## 🖥 구현결과

### **🔹 메인 페이지**

![image](https://user-images.githubusercontent.com/109324634/203841939-c447e6bd-8beb-4e16-a41f-1cae273523d1.png)

- 비로그일 때 보이는 메인 페이지
- 회원가입, 로그인이 필요한 서비스임을 알리고 회원가입/로그인만 가능함

<br>

![image](https://user-images.githubusercontent.com/109324634/203844767-5ab6d3f4-3532-413c-980c-3daa3b818e41.png)

- 로그인 시 보이는 페이지
- 취향찾기 시작, 프로필 페이지 이동, 로그아웃이 가능함

<br>

### **🔹 회원가입, 로그인**

![image](https://user-images.githubusercontent.com/109324634/203842110-e0637804-44db-43d0-a18f-0798649248af.png)

<br>

![image](https://user-images.githubusercontent.com/109324634/203843041-c2326e6d-efe7-4d46-a5c9-f97f9e1b72c1.png)

![image](https://user-images.githubusercontent.com/109324634/203843399-5c399938-d01b-4f03-ab3c-dbeae857df71.png)

- 회원가입시 양식에 맞지 않으면 error message를 보여줌

<br>

![image](https://user-images.githubusercontent.com/109324634/203844332-fe11ccd2-a521-43c7-8726-5b912a5159ef.png)

![image](https://user-images.githubusercontent.com/109324634/203844401-74d6c9cb-b2d2-4c98-a81d-4750fe7f369a.png)

- 아이디와 비밀번호가 맞지 않거나 양식이 틀리는 경우 error message를 보여줌

<br>

### **🔹 선택 페이지**

![image](https://user-images.githubusercontent.com/109324634/203845230-a0b889c0-b9d9-4455-812c-7ce12d948011.png)

- 뒤에 나올 페이지의 사용법을 설명
- 몇개의 트레일러를 확인할 지 선택할 수 있음

<br>

### **🔹 트레일러 페이지**

![image](https://user-images.githubusercontent.com/109324634/203845564-b019da35-7443-48ef-807b-07214c24202a.png)

- 영화의 트레일러와 제목, 몇번째 트레일러 인지 보여줌
- 확인할 트레일러의 개수를 바꿀 수 있음
- Good, Bad 버튼으로 평가를 할 수 있음
- Review 버튼으로 영화에 대한 사람들의 리뷰를 확인할 수 있음

<br>

![image](https://user-images.githubusercontent.com/109324634/203845784-14608bc9-2da9-4d48-920b-b8148e7e29e3.png)

- 리뷰가 없는 경우 리뷰 버튼을 누르면 보이는 toast

<br>

![image](https://user-images.githubusercontent.com/109324634/203846046-be22245c-30aa-4b08-b3f5-cbcc0ce32488.png)

![image](https://user-images.githubusercontent.com/109324634/203845986-ceca7710-c4d7-4094-a025-e7b869aa478c.png)

- 리뷰가 있는 경우 보이는 페이지
- 리뷰 버튼을 누를 때 마다 리뷰들이 랜덤으로 보여짐.
- 리뷰를 남긴 사람의 이름과 내용을 확인할 수 있음

<br>

### **🔹 결과 페이지 **

![image](https://user-images.githubusercontent.com/109324634/203846243-7c89ee4c-cf8c-4f18-a441-f4b21a5d7e1f.png)

- 사용자가 좋다고한 영화들의 장르를 바탕으로 3개의 장르를 나타냄
- 바로 프로필로 이동이 가능함
- 로그아웃 또한 가능함 -> 로그아웃시 메인 페이지로 이동, 비로그인시 나타나는 페이지가 나타남

<br>

![image](https://user-images.githubusercontent.com/109324634/203846984-19cfefb4-f949-4034-a2fa-a9c8aa8e679b.png)

- 선택한 영화에 따라 3개의 장르가 채워지지 않은 경우에는 해당 개수의 장르만 보여줌

<br>

![image](https://user-images.githubusercontent.com/109324634/203847091-c537076e-481e-4df1-8e45-b6b57ddd52e4.png)

- 모든 영화에 bad를 선택한 경우에 보이는 페이지

<br>

![image](https://user-images.githubusercontent.com/109324634/203846389-085c6078-61e8-45c1-9765-d54a4fcc32a2.png)

![image](https://user-images.githubusercontent.com/109324634/203846465-a1b925cd-ab39-42bc-ba4a-556e3d47ea7c.png)

- 장르별로 5개의 영화를 추천해줌
- Carousel을 사용해서 보여주며 영화 포스터를 누르면 영화 detail 페이지로 이동이 가능함

<br>

![image](https://user-images.githubusercontent.com/109324634/203846582-9c76f48a-bbc4-48b9-b058-9b872dbbd897.png)

- 고른 영화들 버튼을 누르면 Good 버튼을 누른 영화들을 Carousel을 사용해서 나타냄
- 마찬가지로 영화 포스터를 누르면 영화 detail 페이지로 이동이 가능함

<br>

### **🔹 프로필 페이지**

![image](https://user-images.githubusercontent.com/109324634/203845106-4303402c-acdf-4438-a792-51c4d6f11aa1.png)

- 회원가입 직후, 아무 영화도 고르지 않았을 때 보이는 페이지

<br>

![image](https://user-images.githubusercontent.com/109324634/203847467-5adb6234-775a-420d-a99e-818565e20dd4.png)

- 트레일러를 보고 Good을 누른 영화들을 확인 할 수 있음

<br>

![image](https://user-images.githubusercontent.com/109324634/203847739-5659a9e8-27e3-4974-b55e-1871420f9276.png)

- 왼쪽에는 사용자가 고른 영화들의 상위 장르 3개가 나타남
- 해당 버튼을 누르면 사용자가 Good을 누른 영화들 중 해당 장르의 영화들을 확인할 수 있음

<br>

![image](https://user-images.githubusercontent.com/109324634/203847946-e79f1090-a6af-4d6f-84f1-840cbd03fabd.png)

- 영화 목록들은 반응형으로 창의 너비에 맞춰 다른 화면을 보여줌

<br>

### **🔹 영화 detail 페이지**

![image](https://user-images.githubusercontent.com/109324634/203848762-5269e4ca-24a2-4000-8c40-56eec9177a95.png)

- 리뷰가 없을 때 보이는 페이지
- 영화의 포스터, 개봉 날짜, 장르, 평점, 줄거리를 확인할 수 있다.

<br>

![image](https://user-images.githubusercontent.com/109324634/203848819-88ba7a6c-7e30-4e9f-b506-b067262a0119.png)

- 리뷰작성 버튼을 누르면 modal이 나타나고 리뷰를 작성할 수 있음

<br>

![image](https://user-images.githubusercontent.com/109324634/203848970-4f16cc41-eb60-4524-8ac0-aa2a0495c05b.png)

- 마우스 hover event에 따라 숫자(선택한 평점 이하)에 불이 켜짐
- 클릭하면 켜진 불은 고정됨

![image](https://user-images.githubusercontent.com/109324634/203849018-76f451e3-44a9-4f0d-a1d2-c67f03443bfa.png)

- 리뷰가 있다면 리뷰의 개수를 오른쪽에 나타낸다.
- 리뷰를 남긴 사용자의 이름과 내용, 평점을 나타낸다.

![image](https://user-images.githubusercontent.com/109324634/203849131-6c731d03-61d5-49d1-a554-fdc79ba251cc.png)

- 리뷰가 많은 경우

<br>

## 🙋‍♀️ 회고

### 📌 겪었던 시행착오

#### ✔ 양질의 DataBase 만들기

TMDB Movie의 popluar movies에서 영화 데이터를 가져왔는데 낯선 영화가 너무 많았다. 트레일러에 한국어 자막이 없는 것도 있었고, 국내 사용자의 정서와는 맞지 않을 것 같은 영화 Data들이 너무 많았다. 

이를 해결하기 위해 한국에서 개봉한 영화들이라는 조건으로 필터링을 했다. 익숙한 영화들로 많이 채워지게 되었고, 영화 포스터와 트레일러 또한 한국어 자막이 당연하게 있었다. 그러나 성인 영화가 굉장히 많았고 이는 `adult = false` 조건으로는 필터링 되지 않았다. TMDB에서 제공하는 Data를 잘 찾아본 결과, 성인 영화는 release date에 있는 관람등급을 사용해 필터링 할 수 있었다.

트레일러 페이지에서 영화의 트레일러, 예고편이 아닌 인터뷰 영상, 비하인드 씬과 같은 영상들도 나왔다. TMDB에서 제공하는 영화 data에 있는 첫 영상을 가져왔더니 발생한 문제였다. 이는 영상 중에서 trailer, teaser인 경우로 필터링을 하여 해결하였다.

<br>

#### ✔ Rating Event

Review의 평점을 남길 때, 숫자에 마우스 hover 이벤트가 발생하면 뒤의 불을 키도록 하였다. 평점마다 색이 다르기 때문에 `.active_1` `.active_2` 같은 식으로 class를 설정하여 CSS를 작성했다. hover를 했을 시에 그 전의 값들을 모두 켜야 했기에 같은 코드가 굉장히 많이 반복되었다. 이를 간결화 시키기 위해서 `for`반복문을 사용하였고 `active_${i}` 와 같이 다른 부분만 변수처리를 하여 tag에 각각의 class를 부여할 수 있었다.

불이 켜지는 경우 숫자가 한쪽으로 치우쳐져 있는 등. 위치를 맞추는 것이 굉장히 힘들었다. 개발자 모드로 여러 정렬들을 적용해 보면서 해결했다.

<br>

#### ✔ 반응형 페이지

프로필 페이지에는 굉장히 많은 영화의 포스터가 보여지게 된다. 반응형으로 이를 구성하지 않으면 창의 크기를 줄였을 때 아예 사용할 수 없게 된다. 이를 해결하기 위해 왼쪽에 프로필이 보이는 부분과 영화가 보여지는 부분을 나누었다. 가장 큰 화면에서는 `2:10`의 비율을 가지고 있고, 창이 작아질 수록 비율이 비슷해지다가 완전히 작아졌을 때는 온전히 하나씩 보이게 설정하였다. 영화부분 내의 영화 포스터들 또한 가장 큰 화면에서는 2씩 값을 부여해 총 6개가 보이다가 창이 작아지면 점점 부여받은 값을 키워, 창이 가장 작아지게 되면 하나만 보이게 설정하였다.

<br>

#### ✔ 협업 툴

깃랩으로 협업을 하며 각자 브랜치를 만들어서 merge를 했다. 초반에는 각자 맡은 App이 달랐기 때문에 충돌이 일어나지 않았다. 개발 후반 단계가 되면서 추가 기능을 구현하게 되면서 같은 파일을 수정하는 일이 발생했고 충돌이 발생했다. 이를 컨펌하고 병합하는 과정에서 실수가 발생해 이전 것으로 덮어버리는 일이 발생했다. 다행히 다른 팀원의 로컬에 파일이 남아있었기에 해결할 수 있었다. 같은 실수를 반복하지 않기 위해 구현할 기능과 수정할 파일에 대한 확인을 미리 한 후에 파일을 수정했다.

![image](https://user-images.githubusercontent.com/109324634/203851607-dfd8f62d-6d3a-4c95-b178-710ba7fa6c21.png)



<br>

### 💬 후기

페어프로젝트였기 때문에 팀원간에 의지하는 것이 굉장히 컸다. 서로 역할을 담당하고 풀리지 않는 문제가 생기면 함께 의논해 해결해 나갔다. 역할을 분담하고 협업해 개발할 수 있는 값진 경험이었다. 

간단한 기능만 구현하는 것과 그것들을 한데 모아 하나의 프로젝트를 만드는 것은 굉장히 다르다는 것을 느꼈다. 이러한 기능이 있으면 좋겠다는 생각이 들어서 기능 하나를 추가하려고 하면, 다른 부분에 수정하거나 추가해야하는 것들이 계속 생겨났고 원래의 것과 충돌을 일으키곤 했다. 기획 단계에서 구체적이고 꼼꼼한 기획이 중요하다는 것을 몸소 깨닫게 되었다.

함께 기획하고 구상했던 페이지가 실제로 완성되니 함께 이런 프로젝트를 만들었다는 것이 굉장히 뿌듯하다. 시간이 짧았기에 디테일한 부분을 챙기지 못해서 아쉬운 부분이 조금 남는다. 더 공부한 후에 프로젝트를 수정, 보수 해보고 싶다.
