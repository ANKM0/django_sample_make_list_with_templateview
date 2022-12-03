# Read Me
1. インストールする
```python
git clone https://github.com/ANKM0/django_sample_make_form_or_list_with_templateview.git
# (必要なら pipenv shell)

#(pipenvの場合、pip->pipenv)
pip install django
```

2. 設定
```python
python "D:\programs\test\django_sample_make_form_or_list_with_templateview\django_sample\gen_secrets.py"
```
出来たsecrets.jsonはdjango_sample直下に移動させる
```python
#(pipenvの場合、pip->pipenv)
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser
```
