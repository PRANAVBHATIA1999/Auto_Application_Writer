import docx
import uuid
def create(address, first_name, last_name, senders_class, rno,  date_from, date_till, days, app_date):

    doc = docx.Document()
    doc.add_paragraph('The Dean')
    doc.add_paragraph(address)
    doc.add_paragraph('')
    doc.add_paragraph('Date: ' + app_date)
    doc.add_paragraph('')
    doc.add_paragraph('Subject: Leave application')
    doc.add_paragraph('Respected Sir/Ma’am,')
    doc.add_paragraph('I request to state that due to sudden illness I will not be able to attend school/college for '+days+  ' days '
    'as the doctor has advised me to take the required amount of rest. I hope to recover soon and make up for the irregularity'
    ' in studies occurred. I will return to school/college as a healthy student and take due care that my work and performance do not'
    ' suffer. On the account of my sickness, I request you to kindly grant me leave from ' + date_from + ' to ' + date_till + ', I shall be utterly obliged for this.')
    doc.add_paragraph('')
    doc.add_paragraph('')
    doc.add_paragraph('')
    doc.add_paragraph('Yours obediently,')
    doc.add_paragraph(first_name + last_name)
    doc.add_paragraph(senders_class)
    doc.add_paragraph(rno)


    doc.save(str(uuid.uuid4())+'.docx')