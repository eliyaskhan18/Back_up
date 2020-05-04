from __future__ import unicode_literals


import schedule
import time


def testing():
	print "hello-------------------from scheduler"

def testing1():
        print "hello-------------------from scheduler1"
schedule.every(1).minutes.do(testing1)
while True:
    schedule.run_pending()
    time.sleep(1)

from apscheduler.schedulers.blocking import BlockingScheduler

def some_job():
    print "Decorated job-----------------"

scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', minutes=1)
scheduler.start()
