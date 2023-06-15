from users.models import EmailVerifyRecord
from django.core.mail import send_mail
import random
import string



def random_str(randomlength=7):
    # 生成a-z,A-Z,0-9左右的字符
    chars = string.ascii_letters + string.digits
    # 从a-zA-Z0-9生成指定数量的随机字符
    strcode = ''.join(random.sample(chars, randomlength))
    return strcode

def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str()
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

# 验证码保存之后，我们就要把带有验证码的链接发送到注册时的邮箱！  
    if send_type == 'register':
        email_title = '[北极来的企鹅]激活你的账号'
        email_body = '轻点以激活账号:http://127.0.0.1:8000/users/active/{0}'.format(code)

        send_status = send_mail(email_title, email_body, 'bjldqe@yeah.net', [email])
        if send_status:
            pass

    elif send_type == 'forget':
        email_title = '[北极来的企鹅]重置你的密码'
        email_body = '轻点以重置密码:http://127.0.0.1:8000/users/forget_user/{0}'.format(code)
        
        send_status = send_mail(email_title, email_body, 'bjldqe@yeah.net', [email])
        if send_status:
            pass