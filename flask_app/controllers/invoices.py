# invoices.py
from flask_app import app
from flask import render_template, redirect, request, session, flash, url_for, send_file
from flask_app.models.invoice import Employees
from pathlib import Path
import time, datetime
# importing reportlab modules
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import inch


import os

static_folder = os.path.join(app.root_path, 'static')

@app.route('/')
def invoices():
    
    return render_template("generate_pdf.html")

@app.route('/generate', methods=["POST"])
def generate():
    
    # Define the data for the table
    employees = Employees.get_all()    
    
    # Create the table objec
    for emp in employees:
        data = {
            "emp_no":emp['emp_no'],
            "birth_date":emp['birth_date'],
            "first_name":emp['first_name'],
            "last_name":emp['last_name'],
            "gender":emp['gender'],
            "hire_date":emp['hire_date']    
        }
        
        table_data = [
            ['Emp No', 'Birth Date', 'First Name', 'Last Name', 'gender', 'Hire Date'],
            [data['emp_no'], data['birth_date'], data['first_name'], data['last_name'], data['gender'], data['hire_date']]  
        ]
        
        # Initializing variables with values
        emp_no = emp['emp_no']
        first_name = emp['first_name']
        last_name = emp['last_name']
        invoice_date = datetime.datetime.now().strftime("%A, %B %d %Y")
        
        # Create a directory in your Downlods 
        fileName = str(Path.home() / f"Downloads/Invoices/{emp_no}-invoice.pdf")
        
        # Call the static method to validate the file    
        if not Employees.validate_file(fileName):
            return redirect("/")
        
        documentTitle = 'sample'
        title = 'Webcrawler Inc.'
        subTitle = 'Employee Invoice'
        textLines = [
            'The data below is the generated invoice for the',
            'specified recipient accrued during the month of',
            f'{datetime.datetime.now().strftime("%B")}. This data is official and is proven to be ',
            'authentic, hence is subject to NO ALTERATION.'
        ]
        
        image = os.path.join(static_folder, 'img/icons8-logo-48.png')
        
        # Creating a pdf object
        pdf = canvas.Canvas(fileName)
        
        # Setting the title of the document
        pdf.setTitle(documentTitle)
        
        # Registering a external font in python 
        
        pdfmetrics.registerFont(
            TTFont('Kablammo-Regular', os.path.join(static_folder, 'Kablammo-Regular.ttf'))
        )

        pdfmetrics.registerFont(
            TTFont('TimesNewRoman', os.path.join(static_folder, 'TimesNewRoman.ttf'))
        )
        
        pdfmetrics.registerFont(
            TTFont('PressStart2P-Regular', os.path.join(static_folder, 'PressStart2P-Regular.ttf'))
        )
        
        # Creating the title by setting it's font
        # and putting it on the canvas
        #pdf.setFont('Kablammo-Regular', 36)
        pdf.setFillColorRGB(0, 20, 155)
        pdf.setFont('TimesNewRoman', 34)
        pdf.drawCentredString(300, 770, title)
        
        # Creating the subtitle by setting it's font,
        # colour and putting it on the canvas
        pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("PressStart2P-Regular", 24)
        pdf.drawCentredString(290, 720, subTitle)
        
        # Draw a line
        pdf.line(30, 710, 550, 710)
        
        # Creating a multiline text using 
        # textline and for loop
        text = pdf.beginText(40, 680)
        text.setFont("Courier", 18)
        text.setFillColor(colors.green)
        
        for line in textLines:
            text.textLine(line)
        pdf.drawText(text)     
        
        pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("PressStart2P-Regular", 10)
        
        pdf.drawString(40, 500, 'Employee No')
        pdf.drawString(40, 480, f"{emp_no}")
        pdf.drawString(340, 500, invoice_date)
        
        pdf.drawString(340, 450, 'Amount Owed:')
        pdf.drawString(460, 450, "$2,000.00")
        
        pdf.drawString(40, 453, 'Received By:')
        
        pdf.drawString(40, 433, f"{first_name}, {last_name}")
        
        table = Table(table_data)    

        # Apply styles to the table
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), 'gray'),
            ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), 'white'),
            ('GRID', (0, 0), (-1, -1), 0.5, 'black'),
        ])
        table.setStyle(style)

        # Get the table size
        table_width, table_height = table.wrap(0, 0)

        # Set the position of the table
        x = (letter[0] - table_width) / 2
        y = letter[1] - 250  # Adjust the y-coordinate as needed

        # Draw the table on the canvas
        table.drawOn(pdf, x, y)
        
        # Drawing a image at the 
        # specified (x.y) position
        pdf.drawInlineImage(image, 40, 300)
        
        # saving the pdf
        pdf.save() 
        
        time.sleep(1)   
            
    return redirect('/')
#generate()





