##
# 邮件自动推送 -- 20191105 created by terrell
# 配置相关变量
# 设置主题、正文等信息
# 添加附件
# 登录、发送#
import time
import os
import smtplib
import email
import datetime
import sys
import traceback
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

year = int(datetime.datetime.now().strftime('%Y'))
month = int(datetime.datetime.now().strftime('%m'))
day = int(datetime.datetime.now().strftime('%d'))
print(day)
print(month)
print(year)
target = " 离考试只有： " + str((datetime.datetime(2020,12,21)-datetime.datetime(year,month,day)).days) + "天了！"
print(target)

# 配置变量
sender = "2516234365@qq.com"
qqCode = 'lnxcnjuvmtqmdjif'


receiver = '1203562850@qq.com'
cc = '2516234365@qq.com'

subject = "向同学☺加油, 我们一起上岸！ " + target
username = "2516234365@qq.com"
password = "yuyali2010970514"


# 邮件主题、正文设置
massage = MIMEMultipart()
massage['subject'] = subject
massage['to'] = receiver
massage['Cc'] = cc
massage['from'] = 'dongjian.yu@qtdatas.com'
body = '''Dear 向同学：

昨天学了吗？
今天要学吗？
   任务完成了吗？
    ①英语
    ②政治
    ③专业理论
    ④毕业创作
    ⑤毕业论文

------------------
Terrell

QTdatas dongjian.yu
Mobile: +86 15188593321
Email: dongjian.yu@qtdatas.com'''
massage.attach(MIMEText(body, 'plain', 'utf-8'))
# 添加附件
# for i in filekkkk:
#     appendix = MIMEApplication(open(file, 'rb').read())
#     appendix.add_header('content-disposition', 'attachment', filename=file_name)
#     massage.attach(appendix)


def main():
    # smtp_server = 'smtp.exmail.qq.com'
    smtp_server = 'smtp.qq.com'
    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.login(sender, qqCode)
    server.set_debuglevel(1)
    # server.ehlo()
    # server.starttls()
    server.login(username, password)
    print('登录成功')
    server.sendmail(sender, receiver.split(',') + cc.split(','), massage.as_string())
    print('邮件发送完成')
    # except Exception as e:
    #     print('报错了...')
    #     traceback.print_exc()
    #     print(e)
    # else:
    #     server.quit()


main()


