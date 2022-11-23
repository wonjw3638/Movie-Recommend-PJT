## 1차 합본 설명서

* movies 볼필요 없음
* choices가 메인
* 


urls.py
```py
from django.urls import path
from . import views


app_name = 'choices'
urlpatterns = [
    path('', views.start, name='start'),
    path('<int:option>/', views.choose, name='choose'),
    path('<int:idx>/<str:prefer>/', views.main, name='main'),
    path('final/', views.final, name='final'),
]

```