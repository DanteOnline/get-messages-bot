from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, autoincrement=False)
    network = Column(String)
    text = Column(String)
    title = Column(String)
    uid = Column(Integer)
    fwd = Column(String)
    out = Column(Integer)
    read_state = Column(Integer)
    date = Column(DateTime)

    def __str__(self):
        return '{}/{}/{}'.format(str(self.date), self.uid, self.text)


engine = create_engine('sqlite:///messages.db', echo=False)


def create_new():
    # В данном случае, создание таблицы
    Base.metadata.create_all(engine)
    # создаем сессию
    Session = sessionmaker(bind=engine)
    session = Session()

    # удаляем все сообщения
    messages = session.query(Message).order_by(Message.id)
    for message in messages:
        session.delete(message)
    session.commit()


def get_all_messages():
    Session = sessionmaker(bind=engine)
    session = Session()
    messages = session.query(Message).order_by(Message.date)
    return messages


class MessageSaver:
    def __init__(self, loader, adapter_cls):
        self.loader = loader
        self.adapter_cls = adapter_cls

    def is_new_message(self, mid, session):
        message_by_mid = session.query(Message).get(mid)
        return message_by_mid is None

    def save_message(self, message):
        # получаем id сообщения
        adapter = self.adapter_cls(message)
        mid = adapter.get_message_id()
        if self.is_new_message(mid, self.session):
            dict = adapter.to_message_dict()
            new_message = Message(**dict)
            # сохраняем данные в базу
            self.session.add(new_message)
        else:
            print('Сообщение с идентификатором {} уже есть в базе'.format(mid))

    def save_messages(self, messages):
        for message in messages:
            self.save_message(message)
        # делаем коммит
        print('Сохраняем изменения')
        self.session.commit()

    def open_sesson(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def save(self):
        self.open_sesson()
        messages = self.loader.get_messages()
        for part in messages:
            self.save_messages(part)
