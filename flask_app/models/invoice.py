from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import os


class Employees:
    def __init__( self, data ):
        self.emp_no = data['emp_no']
        self.birth_date = data['birth_date']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.gender = data['gender']
        self.hire_date = data['hire_date']
    
    @classmethod
    def get_all( cls ):
        query = "SELECT * FROM employees.employees;" 
        results = connectToMySQL('employees').query_db(query)
        employees = []
        for e in results:
            # employees.append( cls(e) ) 
            employees.append( e ) 
        return employees
    
    # Stored Procedure approach
    # @classmethod
    # def get_all( cls ):
    #     instance = connectToMySQL('employees')
    #     connection = instance.connection
        
    #     try:
    #         # Cursor object creation
    #         cursorObject = connection.cursor()
            
    #         # Execute the sqlQuery
            
    #         cursorObject.execute("call employees.get_all()")
            
    #         employees = []
    #         for result in cursorObject.fetchall():
    #             employees.append( result ) 
    #             # print("employees", employees)
    #         return employees
            
    #     finally:
    #         connection.close()
    
    @staticmethod
    def validate_file(fileName):
        is_valid = True
        if os.path.exists(fileName):
            flash("Invoice already generated. Please remove files from the Invoice Folder 📁.")
            is_valid = False
        return is_valid        