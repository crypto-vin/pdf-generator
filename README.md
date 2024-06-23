# Project Name
Invoice/Receipt Generator
[![License: ISC](https://img.shields.io/badge/License-ISC-blue.svg)]
# Table of Contents
1. [Description](#description)
2. [Features](#features)
3. [Technologies Used](#technologies)
4. [Installation Guide](#install)
5. [Usage Guide](#usage)
6. [Database Interaction](#database)
7. [Resources](#resources)
8. [Contribution](#contribution)
9. [License](#license)
10. [Questions](#questions)

## Project Description <a name="description"></a>
This web application is a Flask-based invoice/receipt PDF generator that follows the MVC (Model-View-Controller) design pattern. It simplifies the process of generating invoices and receipts by automating the creation and formatting of PDF documents. The application is designed to handle a large number of invoices and receipts efficiently.
## Features <a name="features"></a>
- Generate professional-looking invoices/receipts in PDF format.

- Customize the invoice/receipt template with your branding and specific details.

- Store generated invoices/receipts in a secure and organized manner.

- Follows the MVC design pattern for organized and modular code structure.

## Technologies Used <a name="technologies"></a>
- Python: The primary programming language for the backend logic and PDF generation.
- HTML5, CSS3, and Bootstrap: Used for designing and styling the user interface.
- JavaScript: Used for interactive elements and client-side functionality.
- Flask: A lightweight Python web framework for developing the application.
- MySQL: The chosen database management system for storing and retrieving data.
- ReportLab: A PDF generation library used for creating PDF documents.
## Installation Guide <a name="install"></a>
1. Clone the repository: `git clone <repository-url>`
2. Change to the project directory: `cd pdf-generator`
3. Install project dependencies using pipenv: `pipenv install PyMySQL flask`
4. Activate the project's virtual environment: `pipenv shell`
5. Create a file named `.env` in the project's root directory.
6. Inside the `.env` file, set the following environment variables:

```
USER=
PASSWORD=
```
Adjust the values according to your MySQL database configuration.

7. Install ReportLab and python-dotenv libraries: `pip install reportlab python-dotenv`

8. Create a directory named `Invoice` at the root level of the project where the generated files will be stored. `C:\Users\User\Downloads\Invoices`

## Usage Guide <a name="usage"></a>
1. Start the Flask development server: `python server.py`
2. Access the application in your web browser at `http://localhost:5000`
3. Provide the necessary details for generating an invoice/receipt, such as customer information, itemized list, and payment details.
4. Customize the template as needed by selecting different styles, layouts, or adding your logo.
5. Click on the <button style="color:red;">Generate PDF</button> button to generate the invoice/receipt in PDF format.
6. The generated PDF file will be saved in the "Invoice" 📁 directory. `C:\Users\User\Downloads\Invoices`

## Database Interaction <a name="database"></a>
To retrieve data from the MySQL database, the application utilizes two different approaches:
1. Class Method with SQL Query:

```python
@classmethod
def get_all(cls):
    query = "SELECT * FROM employees.employees;"
    results = connectToMySQL('employees').query_db(query)
    employees = []
    for e in results:
        employees.append(e)
    return employees
```

2. Stored Procedure Approach:

```python
@classmethod
def get_all(cls):
    instance = connectToMySQL('employees')
    connection = instance.connection

    try:
        cursorObject = connection.cursor()
        cursorObject.execute("call employees.get_all()")
        employees = []
        for result in cursorObject.fetchall():
            employees.append(result)
        return employees
    finally:
        connection.close()
```

MySQL Srored Procedure:

```mysql
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_all`()
BEGIN
    SELECT * FROM employees.employees;
END
```
Choose the appropriate approach based on your database setup and preference. Update the code as needed to match your specific requirements.

## Resources <a name="resources"></a>
- [ReportLab Documentation](https://docs.reportlab.com/reportlab/userguide/ch7_tables/)
- [Creating PDF Documents With Python](https://chat.openai.com/#:~:text=ReportLab%20Documentation-,Creating%20PDF%20Documents%20With%20Python,-Contribution)

## Contribution <a name="contribution"></a>
If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch

## License <a name="license"></a>
ISC https://opensource.org/licenses/ISC
Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies.
      THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
## Questions <a name="questions"></a>
[![GitHub followers](https://img.shields.io/github/followers/F-Nunnez?logo=github&style=for-the-badge&color=0891b2&labelColor=1c1917)](https://www.github.com/F-Nunnez)

✉️ You can contact me at: [francisconunez582@gmail.com](mailto:francisconunez582@gmail.com)
