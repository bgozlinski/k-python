from abc import ABC, abstractmethod
from message import MessageType


class Device(ABC):
    @abstractmethod
    def connect(self):
        ...

    @abstractmethod
    def disconnect(self):
        ...

    @abstractmethod
    def send_message(self, message_type: MessageType, data: str):
        ...

    @abstractmethod
    def status_update(self) -> str:
        ...
