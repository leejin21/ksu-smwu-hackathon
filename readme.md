# file for the manual using python.django making website

## 1. django 설치하고 설정하기
설치하는데 참고하는 사이트: https://tutorial.djangogirls.org/ko/django_installation/
기본 참고용 사이트: https://lsjsj92.tistory.com/m/477
참고 사이트
++ ```conda deactivate```는 가상환경에서 빠져나가기: 관련 명령어 https://hiseon.me/python/anaconda-tutorial/ 여기 참고


**conda에서 하기: 성공한 버전**
```
#anaconda prompt에서,
conda create --name ToyProject python=3.6
conda activate ToyProject
mkdir toy_dj
cd ./toy_dj
pip install django
django-admin.py startproject mysite .
# 이 뒤에 settings 설정하는 부분은 덜함

```
유의할 점: 이건 aws에서 가상 서버 구축해서 올린 게 아니라는 점, aws 이용하면 유닉스 명령어로 다시 해야 함.

```
# django 설정하기: 메뉴얼에 따라 쓰면 됨
```

```
# 다하고 나서 이거 입력하면 웹 들어갈 수 있음!
python manage.py runserver

```
https://tutorial.djangogirls.org/ko/django_start_project/
## 2. db 만들기 X
```
# toy/models.py 파일을 열어서 안에 모든 내용을 삭제한 후 아래 코드를 추가하세요.
# 추가하기: 이때 우리 디비 어떻게 구성될 지만 나중에 확인하기
# use atom
# 이후 toy 직전 디렉토리에서 아래 코드 치기

python manage.py makemigrations blog
python manage.py migrate blog

```

### 3. 웹 연동하기
```
# git clone
git status
git add --all .
git status
git commit -m "Changed the HTML for the site."
git push

```
