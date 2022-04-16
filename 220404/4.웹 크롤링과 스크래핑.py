import sqlite3
###저장###
f=sqlite3.connect("Ex2_data.db")#db파일 연결 sqlite3.connect("파일의 이름")
c=f.cursor()#시작지점확인
c.execute("DROP TABLE IF EXISTS data")#한줄작성 c.execute("DROP TABLE IF EXISTS 테이블의 이름")
c.execute("CREATE TABLE data(data1 text,data2 text,data3 text)")#db의 테이블 생성
c.execute("INSERT INTO data VALUES(:data1,:data2,:data3)",{"data1":10,"data2":20,"data3":30})
#c.executemany()#여러줄작성(제공된 data(list)의 길이로 반복횟수 결정)
c.executemany("INSERT INTO data VALUES(:data1,:data2,:data3)",[{"data1":10,"data2":20,"data3":30},{"data1":10,"data2":20,"data3":30},{"data1":10,"data2":20,"data3":30}])
f.commit()
f.close()

###출력###
f=sqlite3.connect("Ex2_data.db")
c=f.cursor()
c.execute('SELECT * FROM data')
for i in c.fetchall():
    print(f"data1:{i[0]},data2:{i[1]},data3:{i[2]}")

