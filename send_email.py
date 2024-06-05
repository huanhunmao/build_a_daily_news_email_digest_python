import smtplib, ssl, os


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = 'markfu1996@gmail.com'
    # 和 js 不一样 不是单独 .env 文件 写在系统 环境变量中  open ~/.zshrc
    password =  '应用专用密码'

    receiver = 'markfu1996@gmail.com'

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(host, port, context=context,
                              timeout=30) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
            print("邮件发送成功！")
    except Exception as e:
        print(f"发送邮件时出错：{e}")