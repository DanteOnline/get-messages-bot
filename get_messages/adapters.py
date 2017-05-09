import datetime


class VkMessageAdapter:
    def __init__(self, message):
        self.message = message

    def get_message_id(self):
        return int(self.message['mid'])

    def to_message_dict(self):
        # социальная сеть
        network = 'vk'
        # пересылаемые сообщения
        fwd = str(self.message['fwd_messages']) if 'fwd_messages' in self.message else ''
        # дата сообщения, вконтакте выдает в секундах с текущего момента
        # TODO: сделать перевод даты, пока берем текущую
        date = datetime.datetime.now()
        # создаем сообщение
        dict = {
            'id': int(self.message['mid']),
            'network': network,
            'text': self.message['body'],
            'title': self.message['title'],
            'uid': int(self.message['uid']),
            'fwd': fwd,
            'out': int(self.message['out']),
            'read_state': int(self.message['read_state']),
            'date': date
        }
        return dict