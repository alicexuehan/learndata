import itchat
import  time

import schedule


itchat.auto_login(True)


class TestClass(object):
    val1 = 3
    val2 = 5
    val3 = 2
    val4 = 1


    @classmethod
    def job(self):
        author = itchat.search_friends(name='赵子荷')[0]
        if self.val1%3 == 0:
            hug="[拥抱]"*self.val2
        elif self.val1%3 == 1:
            hug="[拥抱]"*self.val3
        else:
            hug="[拥抱]"*self.val4
        author.send('记得喝水! '+hug)
        self.val1+=1



schedule.every(3).seconds.do(TestClass.job)
i=0
while True:
    schedule.run_pending()
    time.sleep(1)
    # print(i)
    i+=1