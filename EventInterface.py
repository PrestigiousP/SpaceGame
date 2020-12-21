from abc import abstractmethod, ABC
import EventHandlerInterface


class EventInterface(ABC):
    """
    Trigger events
    """

    @abstractmethod
    def attach(self, observer: EventHandlerInterface):
        """
        Add an observer to the subject
        """
        pass

    @abstractmethod
    def detach(self, observer: EventHandlerInterface):
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self, event) -> None:
        """
        Notify all observers about an event.
        """
        pass
