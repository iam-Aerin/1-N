# 📘 Django: 1:N 관계과 ModelForm 기초
---
# 🔷 데이터 정규화란?

**데이터 정규화(Normalization)**는 중복을 줄이고, 데이터의 무결성을 보장하며, 효율적인 데이터 저장 구조를 설계하기 위한 **절차적 과정**입니다.

---

## 🔹 정규화가 필요한 이유

🧩 예시:  "게시판의 댓글 기능"
> 게시물 테이블 & 댓글 테이블을 분리 ! 

처음엔 이런 식으로 하나의 테이블로 설계할 수 있어요:

```
| 게시글ID | 게시글제목 | 댓글내용     | 댓글작성자 |
|----------|------------|--------------|-------------|
| 1        | 안녕하세요 | 재밌게 봤어요 | 사용자1     |
| 1        | 안녕하세요 | 감사합니다    | 사용자2     |
```

### ❗ 문제점
- 게시글 제목이 **중복 저장**됨
- 댓글 수가 많아질수록 **게시글 데이터가 반복**됨
- 게시글 제목을 수정하려면 **모든 행을 수정해야 함**

---

## 🔷 정규화 적용 후 구조

정규화를 통해 아래처럼 테이블을 나눕니다.

### 🔸 게시글 테이블 (Posts)
```
| 게시글ID | 게시글제목   |
|----------|----------------|
| 1        | 안녕하세요     |
```

### 🔸 댓글 테이블 (Comments)
```
| 댓글ID | 게시글ID | 댓글내용     | 댓글작성자 |
|--------|-----------|--------------|-------------|
| 1      | 1         | 재밌게 봤어요 | 사용자1     |
| 2      | 1         | 감사합니다    | 사용자2     |
```

### 🔁 장점
- 게시글 정보 **중복 없이 관리**
- 댓글은 게시글과 **외래키(ForeignKey)**로 연결
- 게시글 제목 수정 시 **한 번만 수정**하면 됨

---

## 🔹 정규화 핵심 요약

| 항목       | 설명                                   |
|------------|----------------------------------------|
| 🎯 목적     | 중복 제거, 무결성 유지, 이상현상 방지       |
| 🧩 적용 방법 | 테이블 분리, 외래키(FK)로 관계 설정        |
| 🛠 예시     | 게시글 테이블 + 댓글 테이블 분리 구조 설계 |

---

데이터 정규화는 구조를 더 **깔끔하고 확장 가능하게** 만들어 줍니다. 댓글 기능을 포함한 게시판 설계에서 필수적인 개념이에요. 🔧
---
# Django 설정정

## 🔧 기본 개념 정보

### ✅ Model vs Form

- **Model**: 데이터베이스의 구조를 정의. (예: 게시글, 댓글 등)
- **Form**: 사용자로부터 데이터를 입력받는 인터페이스 (예: `<input>`, `<textarea>`, `<submit>`)

### ✅ ModelForm

> Model과 Form을 **동시에 다루는** Django 기능.  
> 데이터 구조와 입력 양식을 연결해\uuc11c **자동으로 form을 생성**하고, **유효성 검사**까지 해줍니다.

---

## ⚙️ Django 프로젝트 초기 설정

### 1. 가상환경 설정

```bash
python -m venv venv
source venv/Scripts/activate  # Mac/Linux는 source venv/bin/activate
```

### 2. 프로젝트 구조

```plaintext
your-project/
│
├── manage.py
├── your_project/
│   └── settings.py
├── your_app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py ← 직접 생성
├── templates/ ← 직접 생성
├── README.md
├── .gitignore
```

---

## 📦 Django 설치 및 프로젝트 생성

```bash
pip install django
django-admin startproject <project-name> .
python manage.py runserver  # 서버 실행
```

### 앱 생성 및 등록

```shell
django-admin startapp articles
```


> 앱 이름 추가가
```python
# settings.py
INSTALLED_APPS = [
    ...,
    '<app-name>',
]
```

```bash
python manage.py startapp <app-name>
```

---

## 🧱 모델 정의: `models.py`

```python
from django.db import models

class Article(models.Model):
    # 모델 클래스 이름은 단수형
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 처음 생성 시 자동 저장
    updated_at = models.DateTimeField(auto_now=True)      # 저장될 때마다 자동 갱신

    def __str__(self):
        return self.title
```

---

## 🔄 모델 → 데이터베이스 변환

1. 마이그리얼생성
```bash
python manage.py makemigrations
```

2. 데이터베이스에 반영
```bash
python manage.py migrate
```

---

## 💠 관리자 기능 설정

1. 관리자 등록 - `admin.py`

```python
from django.contrib import admin
from .models import Article

admin.site.register(Article)
```

2. 관리자 계정 생성
```bash
python manage.py createsuperuser
```

3. 서버 실행 후 `/admin` 에서 로그인

---

## 🌐 템플릿 설정

### 프로젝트 전역 템플릿 폴더 생성

1. `templates/` 디렉터리 생성
2. `settings.py`에 템플릿 건 가져오기

```python
TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'],
        ...
    },
]
```

---

## 🔗 앱 별 URLConf 추가

`your_app/urls.py` 파일 직접 생성

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

`project/urls.py`에서 include 해줍니다:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('your_app.urls')),  # 앱별 url 연결
]
```

---

## 🧐 1:N 관계란?

> **1:N 관계(One-to-Many)**  
하나의 객체(예: 게시글)가 여러 객체(예: 댓글)를 가지는 관계

### 예시:
```python
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
```

- `ForeignKey`는 "N"  \uc쯤에서(자식 모델) 선정
- `on_delete=models.CASCADE`: 관련된 Article가 삭제되면 Comment도 같이 삭제

---

## ✅ 정리 요약

| 항목 | 설명 |
|------|------|
| Model | 데이터 구조 정의 (DB와 연결) |
| Form | 사용자 입력 처리 |
| ModelForm | 모델 기반으로 자동 생성된 폼 |
| 마이그리션 | 파이썬 코드 → 데이터베이스 반영 |
| admin | 관리자 페이지를 통해 CRUD 가능 |
| 1:N 관계 | 하나의 객체가 여러 객체를 가지는 관계 |
| templates | HTML 템플릿 저장 위치 |
| urls.py | URL과 뷰 연결 |

---

