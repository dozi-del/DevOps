import pymysql

# MySQL 서버에 연결
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="exampledb",
)
# 커서 생성 => 명령어 작성
cursor = conn.cursor()

sql = """
INSERT INTO employees(employee_id,name,department_name)
VALUES(0,"최요원","현무1팀")
"""
cursor.execute(sql)
conn.commit()

print("데이터 삽입 완")

# 연결 해제
conn.close()