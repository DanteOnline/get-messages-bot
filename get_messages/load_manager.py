from loaders import VkLoader
from adapters import VkMessageAdapter
from db import MessageSaver


def start_load():
    loader = VkLoader()
    adapter_cls = VkMessageAdapter
    ms = MessageSaver(loader, adapter_cls)
    ms.save()