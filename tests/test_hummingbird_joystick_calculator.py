#from hummingbird_joystick_calculator.cli import main
from src import HummingbirdJoystickCalculator

#def test_main():
#    assert main([]) == 0

def test_new_method_structure():
    calculator = HummingbirdJoystickCalculator.HummingbirdJoystickCalculator()

    assert calculator.speeds(20, 100) == (100, 100)
    assert calculator.speeds(-20, -100) == (-100, -100)
    assert calculator.speeds(100, 0) == (100, -75.0)
    assert calculator.speeds(50, 50) == (50, -37.5)
    assert calculator.speeds(50, -50) == (-50, -37.5)
    assert calculator.speeds(-50, -50) == (-37.5, -50)
    assert calculator.speeds(-50, 50) == (-37.5, 50)

class MyHummingbirdJoystickCalculator(HummingbirdJoystickCalculator.HummingbirdJoystickCalculator):
    def straight_back(self, speed, x, y):
        return(10, 11)

    def straight_forward(self, speed, x, y):
        return(20, 21)

    def left_back(self, speed, x, y):
        return(30, 31)

    def left_forward(self, speed, x, y):
        return(40, 41)

    def right_back(self, speed, x, y):
        return(50, 51)

    def right_forward(self, speed, x, y):
        return(60, 61)

def test_overriding_calculation_methods():
    calculator = MyHummingbirdJoystickCalculator()

    assert calculator.speeds(20, 100) == (20, 21)
    assert calculator.speeds(-20, -100) == (10, 11)
    assert calculator.speeds(100, 0) == (60, 61)
    assert calculator.speeds(50, 50) == (60, 61)
    assert calculator.speeds(50, -50) == (50, 51)
    assert calculator.speeds(-50, -50) == (30, 31)
    assert calculator.speeds(-50, 50) == (40, 41)

