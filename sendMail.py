import smtplib
from email.mime.text import MIMEText
#构建邮件格式
subject = "老边的学习邮件"
content = """
hello world,还不快快好好学习
"""
sender = "13331153360@163.com"
recver = """3392279511@qq.com,
1490932430@qq.com,
1041369205@qq.com,
2126579184@qq.com,
576492000@qq.com"""

password = "123456a"

message = MIMEText(content,"plain","utf-8")
    #内容
    #内容类型
    #编码格式
message["Subject"] = subject
message["From"] = sender
message["To"] = recver
#发送邮件
smtp = smtplib.SMTP_SSL("smtp.163.com",465)
smtp.login(sender,password)
smtp.sendmail(sender,recver.split(",\n"),message.as_string())
    #发送人
    #接收人 需要是一个列表 []
    #发送邮件 as_string是一种类似json的封装方式，目的是为了在协议上传输邮件内容
smtp.close()