import psycopg2
from config import load_config

def delete_user(first_name,last_name):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("call delete_user(%s,%s,%s)", (first_name,last_name,None))
            invalid_user = cur.fetchone()[0]
        return invalid_user
def delete_phone(phone_number):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("call delete_phone(%s,%s)", (phone_number,None))
            invalid_phone = cur.fetchone()[0]
        return invalid_phone
    
check = input("вы хотите удалить пользователя, или номер телефона? напишите номер или имя").lower().strip()

if check == "номер":
    phone_number = input("напишите номер телефона: ")
    delete_phone(phone_number)
elif check == "имя":
    first_name = input("напишите имя: ")
    last_name = input("напишите фамилию: ")
    delete_user(first_name,last_name)
else:
    print("nahhh")
