import vk
from my_data import MyVkData
from create_database import Network, Message, sessionmaker, engine

session = vk.AuthSession(app_id=MyVkData.APP_ID, user_login=MyVkData.LOGIN, user_password=MyVkData.GET_PASSWORD(), scope='messages')
vkapi = vk.API(session)

MESSAGE = 'Hello from Python Again'
#vkapi.wall.post(message=MESSAGE)
#входящие сообщения
messages = vkapi.messages.get(out=0)
print(messages)
#исходящие сообщения
messages = vkapi.messages.get(out=1)
print(messages)

Session = sessionmaker(bind=engine)
session = Session()

networks = session.query(Network).order_by(Network.id)
for network in networks:
    print(network)


