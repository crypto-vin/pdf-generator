import pymysql
from datetime import datetime

# Data to be inserted
data = {
    'emp_no': 1002,
    'birth_date': '1996-10-02',
    'first_name': 'Elvis',
    'last_name': 'Otieno',
    'gender': 'Male',
    'hire_date': '2018-03-11'
}

# Convert date strings to datetime objects
data['birth_date'] = datetime.strptime(data['birth_date'], '%Y-%m-%d').date()
data['hire_date'] = datetime.strptime(data['hire_date'], '%Y-%m-%d').date()

# Database connection parameters
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Kenya@2030',
    'database': 'employees'
}

# Connect to the database
connection = pymysql.connect(**db_config)

try:
    with connection.cursor() as cursor:
        # Create an SQL insert query
        sql = """
        INSERT INTO employees (emp_no, birth_date, first_name, last_name, gender, hire_date)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        # Execute the query
        cursor.execute(sql, (
            data['emp_no'],
            data['birth_date'],
            data['first_name'],
            data['last_name'],
            data['gender'],
            data['hire_date']
        ))
    # Commit the transaction
    connection.commit()
finally:
    # Close the connection
    connection.close()

print("Data inserted successfully")
