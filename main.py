def sum(number1, number2):
    return number1 + number2


def main():
    sum(20, 40)

def test_sum():
    assert sum(10, 20), 30

if __name__ == "__main__":
    main()
