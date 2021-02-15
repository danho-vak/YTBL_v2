# 여따버려v2 (YTBL_v2)
<hr>
DEMO : https://hovak.pythonanywhere.com/
<hr>

기존에 만들었던 YTBL는 FBV로 작성되었으나, 다양한 Generic View, Mixin을 이용해보고자
CBV로 다시 리빌딩한 코드(기존 게시판은 POST와 성격이 비슷하여 제외함)

<hr>

### 후기 

```
  사실 처음 여따버려v1을 개발 할 당시 CBV의 개념도 몰랐다... 
  기능 구현을위해 다른 사람들이 작성한 코드를 보는데 너무 간단하고 가독성이 좋았다. 
  그래서 일단 기능 구현하고자 내가 아는 방식인(FBV)로 개발을 마무리짓고 View 코드들을 다시 CBV로 재작성해보고 싶어 진행한 프로젝트인데
  Django의 생산성에 또 한번 감탄하게된 계기였다.
  
```

<hr>

### 기존 YTBLv1과 다른 점

  1. decorator를 적용하여 특정 기능에 인증되지 않은 사용자 접근을 제한함
  2. Django-Imagekit을 이용해 이미지 썸네일 적용
