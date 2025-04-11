from bmi import calculate_bmi


def test_bmi_underweight():
    bmi = round(calculate_bmi(45, 1.75), 2)
    assert bmi < 18.5


def test_bmi_normal():
    bmi = round(calculate_bmi(68, 1.75), 2)
    assert 18.5 <= bmi < 25
    


def test_bmi_overweight():
    bmi = round(calculate_bmi(85, 1.75), 2)
    assert 25 <= bmi < 30


def test_bmi_obese():
    bmi = round(calculate_bmi(100, 1.75), 2)
    assert bmi >= 30


def test_bmi_zero_height():
    try:
        calculate_bmi(70, 0)
    except ValueError:
        assert True
