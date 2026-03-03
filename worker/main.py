import schedule
import time
from model import run_forecast
from notifier import send_alert

def job():
    print("Rodando previsão...")
    result = run_forecast()
    if result:
        send_alert(result)

schedule.every(6).hours.do(job)

if __name__ == "__main__":
    job()
    while True:
        schedule.run_pending()
        time.sleep(60)
