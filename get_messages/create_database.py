from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Network(Base):
    __tablename__ = 'networks'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Network(name={})>'.format(self.name)


class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, autoincrement=False)
    network_id = Column(Integer, ForeignKey("networks.id"))
    text = Column(String)
    title = Column(String)
    uid = Column(Integer)
    fwd = Column(String)
    out = Column(Integer)
    read_state = Column(Integer)
    date = Column(DateTime)

engine = create_engine('sqlite:///messages.db', echo=True)

def create_new():
    # В данном случае, создание таблицы
    Base.metadata.create_all(engine)
    # создаем сессию
    Session = sessionmaker(bind=engine)
    session = Session()
    '''
    network = Network("vk")
    session.add(network)
    network = Network("telegram")
    session.add(network)
    '''
    # удаляем все сообщения
    messages = session.query(Message).order_by(Message.id)
    for message in messages:
        session.delete(messages)
    session.commit()

    # удаляем все соц сети
    networks = session.query(Network).order_by(Network.id)
    for network in networks:
        session.delete(network)
    session.commit()

    # добавляем соц сети
    session.add_all([Network("vk"), Network("telegram")])
    session.commit()

    # проверям, что сети сохранились
    networks = session.query(Network).order_by(Network.id)
    for network in networks:
        print(network)


if __name__ == '__main__':
    while True:
        result = input('Вы действительно хотите пересоздать базу данных? ВСЕ ДАННЫЕ БУДУТ УДАЛЕНЫ. y/n ')
        if result == 'y':
            create_new()
            print('База данных успешно создана')
            break
        elif result == 'n':
            break
        else:
            print('Неверный ввод')

