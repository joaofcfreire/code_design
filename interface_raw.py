from abc import ABC, abstractmethod

class NoficationSender(ABC):

    @abstractmethod
    def send_notification(self, message: str) -> None:
        pass

class EmailNotificationSender:

    def send_notification(self, message: str) -> None:
        print(message)

obj = NotificationSender()
obj.send_notification("Olá, mundo!")