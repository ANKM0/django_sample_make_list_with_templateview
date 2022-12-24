# django_sample_make_list_with_templateview
Djangoのサンプルです <br>
TemplateViewを使ってリストを作る方法 のソースコードです <br>

<br>

各ブランチは以下のようになっています
- mainブランチ <br>
get_context_dataをオーバーライドする方法

- feature/#8ブランチ <br>
getをオーバーライドする方法

- feature/#4ブランチ <br>
Listviewを使う方法

# 導入方法 how to install
# 1. インストールする
```python
https://github.com/ANKM0/django_sample_make_list_with_templateview.git
# pipenv shell (pipenv使用する場合)


pip install django  #(pipenvを使用する場合、pip->pipenvに変更)
```

# 2. 設定
コマンドを実行してsecrets.jsonを作成する
```python
# カレントディレクトリ:django_sample_template
python "./django_sample/gen_secrets.py"

```
出来たsecrets.jsonをdjango_sample直下に移動させる
```python
cd django_sample
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# よくあるエラー


##  No such file or directory

<details>
<summary>No such file or directory</summary>

以下のコマンドを実行する時に発生する
```python
python "./django_sample/gen_secrets.py"
```
### <原因>
ルートディレクトリでコマンドを実行していないこと
<br>

### <解決策>
cdコマンドを使って README.md と同じディレクトリ(django_sample_template)に移動して実行する
```cmd
cd django_sample_template
```
```python
python "./django_sample/gen_secrets.py"
```

もしくはフルパスでgen_secrets.pyを指定する
```python
python "C:\programs\django_sample\gen_secrets.py"
```
<br>
<br>

</details>


## secrets.json could not be found

<details>
<summary>secrets.json could not be found</summary>

### <原因>
python manage.py runserver　を実行した時などに発生する <br>
secrets.jsonが上手く読み込まれていないことが原因
<br>

### <解決策>
- secrets.jsonが存在しない場合 <br>
django_sample_templateディレクトリに移動した後に以下のコマンドを実行する
```python
python "django_sample\gen_secrets.py"
```


- secrets.jsonが存在する場合 <br>
secrets.jsonをdjango_sample直下に移動させる <br>
それでもエラーになる場合は一度消してから作り直す

</details>
