import unittest as uni
import sys

def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result

class TestFactorial(uni.TestCase):
    def setUp(self) -> None:
        self.factorial = factorial
    
    def test_factorial_str(self) -> None:
        self.assertRaises(TypeError, self.factorial, "5")
    
    def test_factorial_plusfloat(self) -> None:
        self.assertRaises(TypeError, self.factorial, 4.8)

    def test_factorial_minus(self) -> None:
        self.assertRaises(ValueError, self.factorial, -7)
    
    def test_factorial_large(self) -> None:
        self.assertRaises(ValueError, self.factorial, 98)
    
    def test_factorial_bool(self) -> None:
        self.assertEqual(self.factorial(True), 1)
    
    def test_factorial_zero(self) -> None:
        self.assertEqual(self.factorial(0), 1)
    
    def test_factorial_normal(self) -> None:
        self.assertEqual(self.factorial(11), 39916800)
    
    def tearDown(self) -> None:
        self.factorial = None

uni.main()