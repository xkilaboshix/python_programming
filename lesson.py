"""
REST

HTTPメソッド　クライアントが行いたい処理をサーバーに伝える

GET    データの参照
POST   データの新規登録
PUT    データの更新
DELETE データの削除
"""

import urllib.request
import json


url = 'http://httpbin.org/get'
with urllib.request.urlopen(url) as f:
    r = json.loads(f.read().decode('utf-8'))
    print(type(r))