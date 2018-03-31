import schedule
import threading


class TaskLoop (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
       while True:
           schedule.run_pending()
