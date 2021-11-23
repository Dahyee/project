import pymysql
import pandas as pd

# 연결할 접속 정보
test_db = pymysql.connect(
    user='root', 
    passwd='970130da@@', 
    host='127.0.0.1', 
    db='dahyedb', 
    charset='utf8'
)

# DB 와 상호작용하기 위한 cursor 객체 생성
cursor = test_db.cursor(pymysql.cursors.DictCursor)


# SELECT
sql = "SELECT * FROM test_table;"
cursor.execute(sql)
result = cursor.fetchall()

result = pd.DataFrame(result, columns=['name'])    # name 컬럼만 가져오기
result = resule.values.tolist()
print(result)


# INSERT/UPDATE/DELETE
sql = "INSERT INTO test_table(no, name) VALUES(1, 'test')"
cursor.execute(sql)
test_db.commit()
