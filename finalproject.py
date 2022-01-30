import smtplib
from email.message import EmailMessage



#masukkan email pengirim, password pengirim dan daftar email tujuan (https://youtu.be/mxf0yPeiihQ)
emailku = 'emelianianggi13@gmail.com'
passwordku = 'shelladj123'
recipient_list = ['alirobert863@gmail.com', 'anggiemeliani13012002@gmail.com']


msg=EmailMessage()
msg['From'] = emailku
msg['To'] = recipient_list
msg['Subject']= 'final project Indonesia AI'

#Menambahkan lampiran (https://youtu.be/yzfLVL34_oA)

with open ("Output.xlsx", "rb") as f:
    file_data=f.read()
    print("File data in binary", file_data)
    file_name=f.name
    print("File name is",file_name)
    msg.add_attachment(file_data,maintype="application",subtype='xlsx',filename = file_name)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(emailku, passwordku)
    server.send_message(msg)
     
print("email berhasil terkirim!")
