"""
Adapted from https://refactoring.guru/design-patterns/observer/python/example
"""

import random
from collections import defaultdict
from random import randrange
from typing import Any

from yhkee0404.pattern_observer.core import Observer, Subject


class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state: int | None = None
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: defaultdict[Observer, Any] = defaultdict(int)
    """
    Set of subscribers. In real life, the set of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers[observer]

    def detach(self, observer: Observer) -> None:
        self._observers.pop(observer)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()

    @property
    def state(self) -> int | None:
        return self._state


"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.
"""


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if isinstance(subject, ConcreteSubject) and subject.state is not None and subject.state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if (
            isinstance(subject, ConcreteSubject)
            and subject.state is not None
            and (subject.state == 0 or subject.state >= 2)
        ):
            print("ConcreteObserverB: Reacted to the event")


def test_sample():
    """
    >>> test_sample()
    Subject: Attached an observer.
    Subject: Attached an observer.
    <BLANKLINE>
    Subject: I'm doing something important.
    Subject: My state has just changed to: 0
    Subject: Notifying observers...
    ConcreteObserverA: Reacted to the event
    ConcreteObserverB: Reacted to the event
    <BLANKLINE>
    Subject: I'm doing something important.
    Subject: My state has just changed to: 5
    Subject: Notifying observers...
    ConcreteObserverB: Reacted to the event
    <BLANKLINE>
    Subject: I'm doing something important.
    Subject: My state has just changed to: 0
    Subject: Notifying observers...
    ConcreteObserverB: Reacted to the event
    """
    # The client code.

    random.seed(633)

    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()
