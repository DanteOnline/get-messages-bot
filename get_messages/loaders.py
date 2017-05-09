import vk
from my_data import MyVkData


class VkLoader:
    def __init__(self):
        session = vk.AuthSession(app_id=MyVkData.APP_ID, user_login=MyVkData.LOGIN,
                                 user_password=MyVkData.GET_PASSWORD(),
                                 scope='messages')
        vkapi = vk.API(session)
        self.vkapi = vkapi


    def get_messages(self):
        # входящие сообщения
        count = 200
        offset = 2000
        while True:
            messages = self.vkapi.messages.get(out=0, count=count, offset=offset)
            #если вышли за границу
            if len(messages) == 1:
                #выходим
                break
            else:
                #добавляем смещение
                offset += count
                # возвращаем сообщения
                yield messages[1:]
        # исходящие сообщения
        count = 200
        offset = 2000
        while True:
            messages = self.vkapi.messages.get(out=1, count=count, offset=offset)
            # если вышли за границу
            if len(messages) == 1:
                # выходим
                break
            else:
                # добавляем смещение
                offset += count
                # возвращаем сообщения
                yield messages[1:]