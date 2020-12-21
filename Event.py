import pygame
import EventHandlerInterface
from EventInterface import EventInterface

class Event(EventInterface):
    # Not sure yet
    state: pygame.event = None

    _observers = []

    def __init__(self):
        pass

    # Maybe static, idk yet
    def set_event(self, event):
        self.state = event

    def attach(self, observer: EventHandlerInterface):
        self._observers.append(observer)

    def detach(self, observer: EventHandlerInterface):
        self._observers.remove(observer)

    def notify(self, event):
        """
        Trigger an update in each subscriber.
        """
        for observers in self._observers:
            observers.update(event)
