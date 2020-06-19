import gpiozero


class Motor(object):
    '''
    pwm motor class
    '''

    def __init__(self, pwmPin, forwardPin, backwardPin, encoderPin=None):
        '''
        `forwardPin`: the motor rotate forward when this pin is on\n
        `backwardPin`: the motor rotate backward when this pin is on\n
        `encoderPin`: pin of motor's encoder phase A, default to None
        '''
        self.pwmPin = gpiozero.OutputDevice(pwmPin)
        self.pwmPin.on()
        self.motor = gpiozero.Motor(forwardPin, backwardPin)
        if encoderPin is not None:
            self.encoderPin = gpiozero.InputDevice(encoderPin)

    def setVelocity(self, velocity):
        '''
        `velocity`: normalized motor speed, should be between -1 and 1
        '''
        if velocity >= 0:
            self.motor.forward(velocity)
        else:
            self.motor.backward(-velocity)

    def getVelocity(self):
        '''
        return a float between -1 and 1\n
        later will be value from the encoder
        '''
        return self.motor.value


class OmniMotorsGroup(object):
    '''
    '''

    def __init__(self):
        super().__init__()

        self.motors = {}
        self.motors['LeftFront'] = Motor(17, 27, 22, 4)
        self.motors['RightFront'] = Motor(18, 23, 24, 25)
        self.motors['LeftRear'] = Motor(13, 26, 19, 6)
        self.motors['RightRear'] = Motor(16, 21, 20, 12)
        self.maxVelocity = 0.3

    def update(self, velocityList):
        '''
        `velocityList`: set velocity of motors by list

            LeftFront, RightFront, LeftRear, RightRear
        '''
        self.motors['LeftFront'].setVelocity(velocityList[0])
        self.motors['RightFront'].setVelocity(velocityList[1])
        self.motors['LeftRear'].setVelocity(velocityList[2])
        self.motors['RightRear'].setVelocity(velocityList[3])

    def throttle(self, ratio):
        '''
        forward is positive

            return a velocity list
        '''
        return [ratio] * 4

    def shift(self, ratio):
        '''
        left shift is positive

            return a velocity list
        '''
        return [-ratio, ratio, ratio, -ratio]

    def spin(self, ratio):
        '''
        clock-wise spin is positive

            return a velocity list
        '''
        return [ratio, -ratio, ratio, -ratio]

    def move(self, state):
        '''
        merge the throttle, shift and spin, then set the motors velocity

        `state`: [throttle, shift, spin]
        '''
        maxVelocity = sum([abs(item) for item in state])
        if maxVelocity > self.maxVelocity:
            state = [item / maxVelocity for item in state]
        self.update(list(map(
            lambda x: x[0] + x[1] + x[2], zip(self.throttle(state[0]), self.shift(state[1]), self.spin(state[2]))
        )))
