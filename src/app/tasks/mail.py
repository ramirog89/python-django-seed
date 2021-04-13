from src.app.celery import app

# @app.task(ignore_result=True)
@app.task
def send():
    print("im sending an email in parallel! woaala")


@app.task
def success(self):
    print('The email has been sended sucessfuly')

@app.task
def error_handler(request, exc, traceback):
    print('Task {0} raised exception: {1!r}\n{2!r}'.format(
          request.id, exc, traceback))