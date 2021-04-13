from serum import dependency

from celery.result import AsyncResult


from src.app.tasks.mail import send, success, error_handler


@dependency
class MailService:

    def sendMail(self):
        # result = send.delay()
        result = send.apply_async((), link=success.s(), link_error=error_handler.s())
