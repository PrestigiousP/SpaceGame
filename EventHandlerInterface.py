from abc import abstractmethod, ABC
import EventInterface


class EventHandlerInterface(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, event: EventInterface) -> None:
        """
        Receive update from subject.
        """
        pass