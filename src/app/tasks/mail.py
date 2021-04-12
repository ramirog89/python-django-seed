from src.app.celery import app

@app.task
def sendEmail():
    print("im sending an email in parallel! woaala")
