from lib.reminder import *
def test_reminder_to_do_task():
    reminder = Reminder("Yusur")
    reminder.remind_me_to("Feed the cat")
    result = reminder.remind()
    assert result == "Feed the cat, Yusur!"

#line 3 is the fucntion for self.name.
#line 3 is the fucntion for the self.task
#result is Reminder fucntion on the remind method 
#assert the result (on line 9 of lib/reminder.py it returns self.task then self.name)
