import pandas as pd
import pandas.io.sql
import pyodbc
import xlrd

# подключение к MsSql
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=FINEMAN-PC\SQLEXPRESS;"
    "Database=Test;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()

# чтение excel файла и вывод
data = pd.read_excel("forimportsql.xls", index_col=0)
'''data.sort_values(by=["Age"]).head(7)'''
print(data.head(7))
print()

# открываем книгу и определяем рабочий лист
book = xlrd.open_workbook("forimportsql.xls")
sheet = book.sheet_by_name("Sheet1")

# удаление существующей таблицы
cursor.execute("drop table excel")
conn.commit()

# создание таблицы
query1 = '''create table excel(
    id int primary key,
    FirstName varchar(15) not null,
    LastName varchar(15) not null,
    Age int not null,
    PhoneNumber int
    )'''

query = '''insert into excel(
    id,
    FirstName,
    LastName,
    Age,
    PhoneNumber
    ) values (?, ?, ?, ?, ?)'''

# выполняем создание таблицы(Конструкция try-except для обработки исключений)
try:
    cursor.execute(query1)
    conn.commit()
except pyodbc.ProgrammingError:
    pass

# берем существующее кол-во строк в бд для последующей проверки
cursor.execute("select * from excel")
before_import = cursor.fetchone()

for r in range(1, sheet.nrows):
    id = sheet.cell(r, 0).value
    FirstName = sheet.cell(r, 1).value
    LastName = sheet.cell(r, 2).value
    Age = sheet.cell(r, 3).value
    PhoneNumber = sheet.cell(r, 4).value

    # присваиваем значения из каждой строки
    values = (id, FirstName, LastName, Age, PhoneNumber)

    # выполняем sql-запрос
    cursor.execute(query, values)

# сохраняем изменения
conn.commit()
# если вы хотите проверить, все ли строки импортированы
cursor.execute("select * from excel order by Age, FirstName")
for row in cursor:
    print(f'{row}')
print()

conn.commit()
cursor.close()
conn.close()
