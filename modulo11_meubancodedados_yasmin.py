import sqlite3


conn = sqlite3.connect('alls_sall.db')
cursor = conn.cursor()


cursor.execute(
'''
CREATE TABLE IF NOT EXISTS tasks(
   id INTEGER PRIMARY KEY AUTOINCREMENTS,
   task_name TEXT NOT NULL,
   data_fish NUMBER NOT NULL,
   data_star NUMBER NOT NULL,
   tarefa_about STRING NOT NULL
       )
    

'''
   




)