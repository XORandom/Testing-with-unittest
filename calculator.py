class Calculator:
    color = 'black'

    def __init__(self, base_value):
        self.value = base_value

    def iadd(self, value):
        self.value += value

    @classmethod
    def set_color(cls, color):
        cls.color = color

    @staticmethod
    def add(value1, value2):
        return value1 + value2


if __name__ == '__main__':
    Calculator.set_color('red')
    print(Calculator.color)

