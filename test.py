import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calculator = Calculator

    def test_multiply_success(self):
        assert self.calculator.multiply(self, 12, 10) == 120

    def test_subtraction_success(self):
        assert self.calculator.subtraction(self, 120, 10) == 110

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calculator.division(self, 5, 0)


    def test_adding_success(self):
        assert self.calculator.adding(self, 500, 100) == 600


    def teardown (self):
        print('Выполнение метода TearDown')