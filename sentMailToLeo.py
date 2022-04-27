# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import datetime
import time

import schedule


def sent(to_email_addr):
    from_addr = '2516234365@qq.com'  # 邮件发送账号

    # to_addrs = ['2516234365@qq.com', '929702557@qq.com', '641163577@qq.com']  # 接收邮件账号
    to_addrs = to_email_addr
    qqCode = 'dvchgjuilquudhie'  # 授权码（这个要填自己获取到的）
    smtp_server = 'smtp.qq.com'  # 固定写死
    smtp_port = 465  # 固定端口




    # 配置服务器
    stmp = smtplib.SMTP_SSL(smtp_server, smtp_port)
    stmp.login(from_addr, qqCode)
    year = int(datetime.datetime.now().strftime('%Y'))
    month = int(datetime.datetime.now().strftime('%m'))
    day = int(datetime.datetime.now().strftime('%d'))
    target = " 离考试只有： " + str((datetime.datetime(2021, 12, 25) - datetime.datetime(year, month, day)).days) + "天了！"

    body = '''Dear 向同学、邵同学：
    
    只有  10月, 11月了
    只有  10月, 11月了
    只有  10月, 11月了
           
    07：00起床
    07：30-08：30 学习英语
    08：30-12：00 学习专业课1
    
    12：30-13：30 午休
    13：30-18：00 学习专业课2
    
    18：30-21：00 复习今日专业课
    21：00-22：00 复习英语
    22：00-22：30 整理今日错题
    23：00休息

    ------------------
    那年那月那个孤独的考研人，
    那山那水那条寂寞的考研路，
    那曰那夜那颗迷茫的考研心，
    那风那雨那个执著的考研梦。
    我亲爱的研友请你坚持到底！
    
    '''

    # 组装发送内容
    message = MIMEText(body, 'plain', 'utf-8')  # 发送的内容
    message['From'] = Header("余同学 ", 'utf-8')  # 发件人
    message['To'] = Header("向上的向同学", 'utf-8')  # 收件人
    subject = "向同学☺加油, 我们一起上岸！ " + target
    message['Subject'] = Header(subject, 'utf-8')  # 邮件标题

    try:
        stmp.sendmail(from_addr, to_addrs, message.as_string())
    except Exception as e:
        print('邮件发送失败--' + str(e))
    print('邮件发送成功')
    time.sleep(60)


sent(['2516234365@qq.com'])
