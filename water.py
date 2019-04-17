import itchat
import  time
import random
import schedule


itchat.auto_login(True)


class TestClass(object):
    val2 = "记得喝水![拥抱]"
    val3 = "赵日天，快去喝水![拥抱]"
    val4 = "宝宝，快去喝水吧![拥抱]"
    val5 = "亲爱的，快去喝水吧![拥抱]"
    val6 = "小荷学姐，快去喝水吧![拥抱]"
    dict = {1: val2, 2: val3, 3:val4,4:val5, 5:val6}
    @classmethod
    def job(self):
        author = itchat.search_friends(name='赵子荷')[0]
        x=random.randint(1,5)
        author.send(self.dict[x])
        self.val1+=1



schedule.every(3).seconds.do(TestClass.job)
i=0
while True:
    schedule.run_pending()
    time.sleep(1)
    # print(i)
    i+=1