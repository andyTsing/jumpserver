from datetime import datetime

from django.utils.translation import ugettext as _

from common.utils import reverse, get_request_ip_or_data, get_request_user_agent
from notifications.notifications import UserMessage


class ResetPasswordMsg(UserMessage):
    def get_common_msg(self):
        user = self.user
        subject = _('Reset password')
        message = _("""
            Hello %(name)s:
            <br>
            Please click the link below to reset your password, if not your request, concern your account security
            <br>
            <a href="%(rest_password_url)s?token=%(rest_password_token)s">Click here reset password</a>
            <br>
            This link is valid for 1 hour. After it expires, <a href="%(forget_password_url)s?email=%(email)s">request new one</a>
        
            <br>
            ---
        
            <br>
            <a href="%(login_url)s">Login direct</a>
        
            <br>
            """) % {
            'name': user.name,
            'rest_password_url': reverse('authentication:reset-password', external=True),
            'rest_password_token': user.generate_reset_token(),
            'forget_password_url': reverse('authentication:forgot-password', external=True),
            'email': user.email,
            'login_url': reverse('authentication:login', external=True),
        }
        return {
            'subject': subject,
            'message': message
        }


class ResetPasswordSuccessMsg(UserMessage):
    def __init__(self, user, request):
        super().__init__(user)
        self.request = request

    def get_common_msg(self):
        user = self.user

        subject = _('Reset password success')
        message = _("""
        
        Hi %(name)s:
        <br>
        
        
        <br>
        Your JumpServer password has just been successfully updated.
        <br>
        
        <br>
        If the password update was not initiated by you, your account may have security issues. 
        It is recommended that you log on to the JumpServer immediately and change your password.
        <br>

        <br>
        If you have any questions, you can contact the administrator.
        <br>
        <br>
        ---
        <br>
        <br>
        IP Address: %(ip_address)s
        <br>
        <br>
        Browser: %(browser)s
        <br>
        
        """) % {
            'name': user.name,
            'ip_address': get_request_ip_or_data(self.request),
            'browser': get_request_user_agent(self.request),
        }
        return {
            'subject': subject,
            'message': message
        }


class PasswordExpirationReminderMsg(UserMessage):
    def get_common_msg(self):
        user = self.user

        subject = _('Security notice')
        message = _("""
        Hello %(name)s:
        <br>
        Your password will expire in %(date_password_expired)s,
        <br>
        For your account security, please click on the link below to update your password in time
        <br>
        <a href="%(update_password_url)s">Click here update password</a>
        <br>
        If your password has expired, please click 
        <a href="%(forget_password_url)s?email=%(email)s">Password expired</a> 
        to apply for a password reset email.
    
        <br>
        ---
    
        <br>
        <a href="%(login_url)s">Login direct</a>
    
        <br>
        """) % {
            'name': user.name,
            'date_password_expired': datetime.fromtimestamp(datetime.timestamp(
                user.date_password_expired)).strftime('%Y-%m-%d %H:%M'),
            'update_password_url': reverse('users:user-password-update', external=True),
            'forget_password_url': reverse('authentication:forgot-password', external=True),
            'email': user.email,
            'login_url': reverse('authentication:login', external=True),
        }
        return {
            'subject': subject,
            'message': message
        }


class UserExpirationReminderMsg(UserMessage):
    def get_common_msg(self):
        subject = _('Expiration notice')
        message = _("""
           Hello %(name)s:
           <br>
           Your account will expire in %(date_expired)s,
           <br>
           In order not to affect your normal work, please contact the administrator for confirmation.
           <br>
           """) % {
                'name': self.user.name,
                'date_expired': datetime.fromtimestamp(datetime.timestamp(
                    self.user.date_expired)).strftime('%Y-%m-%d %H:%M'),
        }
        return {
            'subject': subject,
            'message': message
        }


class ResetSSHKeyMsg(UserMessage):
    def get_common_msg(self):
        subject = _('SSH Key Reset')
        message = _("""
        Hello %(name)s:
        <br>
        Your ssh public key has been reset by site administrator.
        Please login and reset your ssh public key.
        <br>
        <a href="%(login_url)s">Login direct</a>
    
        <br>
        """) % {
            'name': self.user.name,
            'login_url': reverse('authentication:login', external=True),
        }

        return {
            'subject': subject,
            'message': message
        }


class ResetMFAMsg(UserMessage):
    def get_common_msg(self):
        subject = _('MFA Reset')
        message = _("""
        Hello %(name)s:
        <br>
        Your MFA has been reset by site administrator.
        Please login and reset your MFA.
        <br>
        <a href="%(login_url)s">Login direct</a>
    
        <br>
        """) % {
            'name': self.user.name,
            'login_url': reverse('authentication:login', external=True),
        }
        return {
            'subject': subject,
            'message': message
        }
