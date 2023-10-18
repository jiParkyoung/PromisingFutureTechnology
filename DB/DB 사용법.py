import cx_Oracle
    
#삽입
def DB_insert(cursor,connection,table,data):
    sql="INSERT INTO {table} VALUES ({data})".format(table=table,data=data)
    cursor.execute(sql)
    connection.commit()
#읽기
def DB_select(cursor,column,table):
    sql = "SELECT {column} from {table}".format(column=column,table=table)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

#업데이트
def DB_update(cursor,connection,table,setcondition,where):
    sql = "update {table} set {setcondition} where {where}".format(table=table,setcondition=setcondition,where=where)
    print(sql)
    cursor.execute(sql)
    connection.commit()

#삭제
def DB_delete(cursor,connection,table,where):
    sql="DELETE FROM {table} WHERE title='{where}'".format(table=table,where=where)
    cursor.execute(sql)
    connection.commit()

#연결 
def connect():
    cx_Oracle.init_oracle_client(lib_dir="/usr/local/oracle/instantclient_19_8") 
    global connection
    connection = cx_Oracle.connect(user='admin', password='', dsn='thesis_high',encoding="UTF-8")
    cursor = connection.cursor()
    return cursor

#다건 삽입
def DB_union_ALL(cursor,connection,table,data):# / 데이터 [[1,2,3,4],[4,5,6,7]] 식으로 전달
    sub_sql=""
    for i in data:#SQL 만들기
        if len(i[3])>1300:
            clob="TO_CLOB('{under4000}')".format(under4000=i[3][0:1300])
            for j in range(1,(len(i[3])//1300)+1):
                clob+="||TO_CLOB('{under4000}')".format(under4000=i[3][j*1300:j*1300+1300])
        else:
            clob="TO_CLOB('{under4000}')".format(under4000=i[3])
        v4=clob
        
        if i == data[-1]:
            sub_sql+="SELECT '{V1}', '{V2}', '{V3}', {V4}  FROM DUAL ".format(V1=i[0], V2=i[1], V3=i[2], V4=v4)
        else:
            sub_sql += "SELECT '{V1}', '{V2}', '{V3}', {V4}  FROM DUAL UNION ALL  ".format(V1=i[0], V2=i[1], V3=i[2], V4=v4)
    
    sql="INSERT INTO {table} (title,searchq,year,content) {sub_sql}".format(table=table,sub_sql=sub_sql)
    
    cursor.execute(sql)
    connection.commit()
 
    
# #postgre
# def selectDB(cursor,colum,table):
#     sql = " SELECT {colum} from {table}".format(colum=colum,table=table)
#     cursor.execute(sql)
#     result = cursor.fetchall()
    
#     return result

# ##postgre에서 데이터 받아오기
# db=pg2.connect(host='localhost', dbname='technology',user='postgres',password='',port=5432)#DB명: technology연결 (thesis는 테이블 이름)
# db.autocommit=True#오토커밋
# cursor=db.cursor()#커서 설정
# result=selectDB(cursor,'*','thesis')

# #오라클에 넣기
# cx_Oracle.init_oracle_client(lib_dir="./instantclient_21_3") 
# connection = cx_Oracle.connect(user='admin', password='', dsn='thesis_high')
# cursor = connection.cursor()
# DB_union_ALL(cursor,connection,'THESIS',result)


####################테스트#######################
# cursor=connect()
# cursor.execute("drop table thesis") #테이블삭제
# cursor.execute("CREATE TABLE thesis(\
#                 TITLE VARCHAR2(100) primary key,\
#                 searchQ VARCHAR2(20),\
#                 year VARCHAR2(10), \
#                 content CLOB)")#테이블 생성
#################################################
# cursor.execute("update test set column_copy = 'title'")
# connection.commit()
# DB_union_ALL(cursor,connection,'test',[[722,2,3,4],[338,5,6,8],[1021,4,5,5]])
# for row in DB_select(cursor,'title','test'):
# print(row[0])
# DB_update(cursor,connection,'test',"content='aaaaaa'","title='zdz'") #clob 형태 조건으로쓰려면 to_char 해야한다고함
# DB_delete(cursor,connection,'test','')
# DB_insert(cursor,connection,'test',"'','dd','aa','cc'") #"로 다 묶고 '로 하나하나 묶기
# connection.close()

