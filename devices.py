import time

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


class omniMotorsGroup(object):
    '''
    '''

    def __init__(self):
        super().__init__()

        self.motors = {}
        self.motors['LeftFront'] = Motor(17, 27, 22, 4)
        self.motors['RightFront'] = Motor(18, 23, 24, 25)
        self.motors['LeftRear'] = Motor(13, 26, 19, 6)
        self.motors['RightRear'] = Motor(16, 21, 20, 12)

    def update(self, velocityDict=None, velocityList=None):
        '''
        `velocityList`: set velocity of motors by list

            LeftFront, RightFront, LeftRear, RightRear
        '''
        if velocityDict is not None:
            for motor in velocityDict:
                self.motors[motor].setVelocity(velocityDict[motor])
        elif velocityList is not None:
            self.motors['LeftFront'].setVelocity(velocityList[0])
            self.motors['RightFront'].setVelocity(velocityList[1])
            self.motors['LeftRear'].setVelocity(velocityList[2])
            self.motors['RightRear'].setVelocity(velocityList[3])

