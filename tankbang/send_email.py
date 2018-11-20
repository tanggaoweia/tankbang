#! /user/bin/ env python3
# -*- coding: utf-8 -*-
# Author:GaoWei Tang
# 发送html内容的邮件
import smtplib, time, os, re
from email.mime.text import MIMEText
from email.header import Header


def send_mail_html(file):
    """发送html内容邮件"""
    receiver_list = ['xx@163.com','xx.com']
    for receiver in receiver_list:
        # 发送邮箱
        sender = 'xx@163.com'
        # 接收邮箱
        # receiver
        # 发送邮件主题
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        subject = '自动化测试结果_' + t
        # 发送邮箱服务器
        smtpserver = 'smtp.163.com'
        # 发送邮箱用户/密码
        username = 'xxx@163.com'
        password = 'xxx'
        # 读取html文件内容
        f = open(file, 'rb')
        mail_body = f.read()
        f.close()

        # 组装邮件内容和标题，中文需参数‘utf-8’，单字节字符不需要
        msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = sender
        msg['To'] = receiver
        # 登录并发送邮件
        try:
             smtp = smtplib.SMTP()
             smtp.connect(smtpserver)
             smtp.login(username, password)
             smtp.sendmail(sender, receiver, msg.as_string())
        except Exception as e:
             print("邮件发送失败！", e)
        else:
             print("邮件发送成功！")
        finally:
             smtp.quit()


def find_new_file(dir):
     '''查找目录下最新的文件'''
     file_lists = os.listdir(dir)
     file_lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" + fn)
                     if not os.path.isdir(dir + "\\" + fn)
                     else 0)
     # print('最新的文件为： ' + file_lists[-1])
     file = os.path.join(dir, file_lists[-1])
     print('完整文件路径：', file)
     return file


dir = r'G:\python\tankbang_auto_test\report'  # 指定文件目录
file = find_new_file(dir)  # 查找最新的html文件
# send_mail_html(file)  # 发送html内容邮

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
receiver_list = ['xx@163.com', 'xx@qq.com']

for receiver in receiver_list:
        mail = MIMEMultipart()
        mail.attach(MIMEText('下载附件查看完整测试报告', _subtype='html', _charset='utf-8'))
        # 构造附件att1，若是要带多个附件，可根据下边的格式构造
        att1 = MIMEText(open(file, 'rb').read(), 'base64', 'utf-8')
        att1['Content-Type'] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="%s"' % file
        mail.attach(att1)

        mail['Subject'] = '罐车在线接口自动化测试'
        mail['From'] = 'xx@163.com' # 需与邮件服务器的认证用户一致
        mail['To'] = receiver

        smtp = smtplib.SMTP('smtp.163.com', port=25) # 设置邮件服务器地址与端口
        smtp.login('xx@163.com', 'xx') # 登录邮件服务器
        smtp.sendmail('xx@163.com', receiver, mail.as_string()) # 发送邮件
        smtp.quit() # 关闭邮件服务器
