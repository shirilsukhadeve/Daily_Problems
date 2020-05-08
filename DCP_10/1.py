import schedule
import time
def doRun():
    print ("Hello World")

def run(job, a):
    a = float(a)
    time.sleep(a)
    job()

run(doRun, '1')
