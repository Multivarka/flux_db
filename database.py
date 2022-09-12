import sqlite3

conn = sqlite3.connect("orders.db", check_same_thread=False)
cursor = conn.cursor()


def add(details):
    sql = "INSERT INTO orders(name, sum, description) VALUES(?, ?, ?)"

    cursor.execute("SELECT sum FROM orders WHERE name = ?", [details[0]])
    money = cursor.fetchone()
    cursor.execute("SELECT description FROM orders WHERE name = ?", [details[0]])
    description = cursor.fetchone()
    if not money:
        cursor.execute(sql, details)
    else:
        sql = "UPDATE orders SET sum = ? WHERE name = ?"
        cursor.execute(sql, [money[0] + details[1], details[0]])
        sql = "UPDATE orders SET description = ? WHERE name = ?"
        cursor.execute(sql, [details[2] + ", " + description[0], details[0]])
    conn.commit()

def get():
    cursor.execute("select * from orders ORDER BY sum DESC")
    res = cursor.fetchall()
    result = ""
    for i in res:
        result += f"{i[0]}: ({i[1]}, [{i[2]}])\n———————————————————-\n"
    if result:
        return f"{result} Итого: {str(get_sum())} руб."
    else:
        return "Таблица пустая"

def get_sum():
    cursor.execute("SELECT sum FROM orders")
    money = cursor.fetchall()
    summa = 0
    for i in money:
        summa += i[0]
    return summa

def get_deleted():
    cursor.execute("select * from orders ORDER BY sum DESC")
    res = cursor.fetchall()
    result = ""
    for i in range(len(res)):
        result += f"{i + 1}) {res[i][0]}: ({res[i][1]}, [{res[i][2]}])\n———————————————————-\n"
    return result

def delete(num):
    cursor.execute("SELECT name FROM orders ORDER BY sum DESC")
    names = cursor.fetchall()
    for i in range(len(names)):
        if i == num - 1:
            cursor.execute("DELETE FROM orders WHERE name = ?", [names[i][0]])
    conn.commit()