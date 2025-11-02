import mysql.connector

print("Before connect()")

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",          # Important: not "localhost"
        user="root",
        password="",               # Empty since you didn’t enter one
        database="",               # Optional
        port=3306,
        auth_plugin='mysql_native_password'  # Needed for MariaDB sometimes
    )
    print("After connect()")

    if conn.is_connected():
        print("✅ Connection successful!")
        print("Server version:", conn.get_server_info())
    else:
        print("❌ Connection failed.")

except mysql.connector.Error as e:
    print("MySQL Error:", e)

except Exception as e:
    print("Other Error:", e)

finally:
    try:
        if conn.is_connected():
            conn.close()
            print("Connection closed.")
    except NameError:
        pass
