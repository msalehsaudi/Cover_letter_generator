from docxtpl import DocxTemplate
import datetime


company_name = input("Enter name of the Company : ") 
address1 = input("Enter address1 of the Company : ") 
address2 = input("Enter address2 of the Company : ")
position_name = input("Enter name of the Position: ")
hiring_manager = input("Enter name of the hiring manager: ")
field = input("Enter field of the industry: ")

today_date = datetime.datetime.today().strftime('%m/%d/%Y')

doc = DocxTemplate("master_cover_letter.docx")
context = { 'today_date': today_date, 
           'company_name' : company_name, 
           'position_name' : position_name, 
           'address1' : address1, 
           'address2' : address2,
           'hiring_manager': hiring_manager, 
           'field': field}

doc.render(context)

doc.save('Cover_letter_'+company_name+'_'+position_name+'.docx')