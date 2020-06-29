import time

from asciimatics.event import KeyboardEvent, MouseEvent
from asciimatics.screen import Screen

import devices


class Controller:
    def __init__(self):
        self.events = {
            'w': self.forward,
            's': self.backward,
            'a': self.left_shift,
            'd': self.right_shift,
            'j': self.turn_left,
            'l': self.turn_right,
            ' ': self.stop,
        }
        self.state = [0, 0, 0]
        self.car = devices.OmniMotorsGroup()

    def forward(self):
        self.state[0] += 0.2

    def backward(self):
        self.state[0] += -0.2

    def left_shift(self):
        self.state[1] += 0.2

    def right_shift(self):
        self.state[1] += -0.2

    def turn_left(self):
        self.state[2] += 0.2

    def turn_right(self):
        self.state[2] += -0.2

    def stop(self):
        self.state = [0, 0, 0]

    def update(self):
        self.car.move(self.state)
        return self.state


def ui(screen):
    key = 0
    ctl = Controller()
    while True:
        # catch keyboard event
        event = screen.get_event()
        if isinstance(event, KeyboardEvent):
            key = event.key_code
            if key == ord('q'):
                break
            if chr(key) in ctl.events:
                ctl.events[chr(key)]()
        # refresh the screen
        screen.clear()
        screen.print_at(str(ctl.update()), 0, 0)
        screen.refresh()
        time.sleep(0.1)


Screen.wrapper(ui)
