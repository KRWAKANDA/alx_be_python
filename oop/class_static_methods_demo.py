
class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static Method:
        Performs addition without needing class or instance data.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class Method:
        Can access class attributes (like calculation_type) using cls.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
