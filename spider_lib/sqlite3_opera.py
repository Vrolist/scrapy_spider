import sqlite3

base_url = "/home/shiyanlou/Desktop/shiyanlou_spider.sqlite3.db"
table_name = "course_info"

def create_table():
    sql3_db = sqlite3.connect(base_url)
    create_sql = "create table {} (url varchar(1024), title varchar(256), teacher varchar(128), study_num int, tag varchar(256), types varchar(256), info varchar(1024), tests_name varchar(1024))".format(table_name)
    try:
        sql3_db.execute(create_sql)
    except:
        return False
    sql3_db.close()
    return True

def insert_or_update_data(url, title, teacher, study_num, tag, types, info, tests_name):
    create_table() # 创建一次数据库，没有表格时创建，表格存在时不作操作
    if query(title): # 如果查询到title存在，则是更新
        sql3_db = sqlite3.connect(base_url)
        update_sql = "update {} set study_num={}, info='{}', tests_name='{}', url='{}' where title='{}'".format(table_name, study_num, info, tests_name, url, title)
        try:
            sql3_db.execute(update_sql)
            sql3_db.commit()
        except:
            return False
        sql3_db.close()
        return True
    else: # 查询不到title，则插入
        sql3_db = sqlite3.connect(base_url)
        insert_sql = "insert into {} (url, title, teacher, study_num, tag, types, info, tests_name) values('{}', '{}', '{}', {}, '{}', '{}', '{}', '{}')".format(table_name,url, title, teacher, study_num, tag, types, info, tests_name)
        try:
            sql3_db.execute(insert_sql)
            sql3_db.commit()
        except:
            return False
        sql3_db.close()
        return True
    return False

def query(title):
    sql3_db = sqlite3.connect(base_url)
    query_sql = "select * from {} where title = '{}'".format(table_name, title)
    cu = sql3_db.cursor()
    cu.execute(query_sql)
    record_list = cu.fetchall()
    if len(record_list)>0:
        return True
    else:
        return False
    return False

if __name__=="__main__":
    insert_or_update_data('url','title','teacher',12138,'vip','web','infos_infos','课程一 课程二')