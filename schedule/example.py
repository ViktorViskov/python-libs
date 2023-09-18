import time
from datetime import datetime

import schedule


def task():
    # DO SOME TASK
    pass

# Define a function to schedule the task every hour
def schedule_task():
    current_hour = time.strftime("%H:%M")
    
    # every hour
    if current_hour != "03:00":
        task()

    # at 3 am
    else:
        task()

# Schedule the task to run every hour
schedule.every().hour.at(":00").do(schedule_task)

while True:
    schedule.run_pending()
    time.sleep(1)