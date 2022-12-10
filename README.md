# 導入方法 how to install
## 1. インストールする
```python
https://github.com/ANKM0/django_sample_template.git
# (必要なら pipenv shell)

#(pipenvの場合、pip->pipenvに変更)
pip install django
```

## 2. 設定
コマンドを実行してsecrets.jsonを作成する
```python
python "django_sample\gen_secrets.py"
```
出来たsecrets.jsonをdjango_sample直下に移動させる
```python
#(pipenvの場合、pip->pipenvに変更)
cd django_sample
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
