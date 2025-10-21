import pymysql

# MySQL 서버에 연결
conn = pymysql.connect(
    host="localhost",   # MySQL 서버 주소, 이건 로컬인 경우
    user="root",
    password="1234",
    database="exampledb",
    # charset="utf8mb4",   # utf-8 확장버전
    # cursorclass=pymysql.cursors.DictCursor
)
# 커서 생성 => 명령어 작성
cursor = conn.cursor()

sql="SELECT * FROM employees"
cursor.execute(sql)
employees=cursor.fetchall()
for employee in employees:
    print(employee)

print("데이터 조회 완")

# 연결 해제
conn.close()