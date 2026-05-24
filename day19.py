'''
INSERT INTO `student` (`id`, `name`, `address`, `phone`, `age`, `email`) VALUES ('1', 'Sammy', NULL, '123', '19', 'sammy@gmail.com')

INSERT INTO `student` (`id`, `name`, `address`, `phone`, `age`, `email`) VALUES (NULL, 'Janice', 'New York', '6123', '21', 'janice@gmail.com'), (NULL, 'Goyun', 'Seoul', '41234', '20', 'goyuna123@gmail.com');
'''

import mysql.connector

db = mysql.connector.connect(
    user  = "root",
    host = "localhost",
    password = "",
    port = 3306,
    database = "pythonmay22"
)
terminal = db.cursor()

'''
insert_query = "INSERT INTO student (name, address, phone, age, email) VALUES ('Emma', 'New York', '6125', '18', 'emma@gmail.com');"
terminal.execute(insert_query)
db.commit()
'''
'''
update_query = "UPDATE student SET email = 'emma123@gmail.com' where phone = 6125"
terminal.execute(update_query)
db.commit()
'''
'''
delete_query = "DELETE FROM student where phone = 6125"
terminal.execute(delete_query)
db.commit()
'''

select_query = 'SELECT * from student'
terminal.execute(select_query)
result = terminal.fetchall()
for i in result:
    print(i[0], i[1], i[3])
print(db)