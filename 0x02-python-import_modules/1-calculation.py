if __name__ == "__main__":
    a = 10
    b = 5

    import calculator_1

    addition_result = calculator_1.add(a, b)
    subtraction_result = calculator_1.subtract(a, b)
    multiplication_result = calculator_1.multiply(a, b)
    division_result = calculator_1.divide(a, b)

    print("Addition: {}".format(addition_result))
    print("Subtraction: {}".format(subtraction_result))
    print("Multiplication: {}".format(multiplication_result))
    print("Division: {}".format(division_result))
