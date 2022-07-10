from employee import  Employee, PremiumEmployee, ValueBonus, PercentBonus, ExtraBonus

def test_add_bonuses_together():
    b1 = ValueBonus(100)
    b2 = ValueBonus(200)
    b4 = PercentBonus(10)
    b5 = PercentBonus(20)

    b3 = b1 + b2
    b6 = b4 + b5

    assert b3.value == 300
    assert isinstance(b3, ValueBonus)

    assert b6.value == 30
    assert isinstance(b6, PercentBonus)


def test_percent_bonus():
    b = PercentBonus(10)
    assert b.calculate(100) == 110


def test_add_value_bonus():
    # scenariusz ValueBonus
    b1 = ValueBonus(200)
    assert b1.value == 200

    e = PremiumEmployee(name="Jan Kowalski", rate_per_hour=100)
    e.register_time(5)
    e.give_bonus(b1)

    assert e.pay_salary() == (5 * 100) + 200


def test_add_percent_bonus():

    b2 = PercentBonus(10)
    e = PremiumEmployee(name="Jan Kowalski", rate_per_hour=100)
    e.register_time(5)

    e.give_bonus(b2)
    assert e.pay_salary() == (5 * 100) + (5 * 100) * 0.1


def test_add_value_and_percent_bonuses():
    # scenariusz 1
    b1 = ValueBonus(200)
    b2 = PercentBonus(10)
    e = PremiumEmployee(name="Jan Kowalski", rate_per_hour=100)
    e.register_time(5)
    e.give_bonus(b1)
    e.give_bonus(b2)
    assert e.pay_salary() == (5 * 100) + (5 * 100) * 0.1 + 200


def test_add_many_value_and_percent_bonusses():
    # kolejny scenariusz
    b1 = ValueBonus(200)
    b2 = PercentBonus(10)
    b3 = ValueBonus(300)
    b4 = PercentBonus(20)
    b5 = ExtraBonus(100)

    e = PremiumEmployee(name="Jan Kowalski", rate_per_hour=100)
    e.register_time(5)
    e.give_bonus(b1)
    e.give_bonus(b2)
    e.give_bonus(b3)
    e.give_bonus(b4)
    e.give_bonus(b5)
    e.give_bonus(b5)

    assert e.pay_salary() == (5 * 100) + (5 * 100) * 0.3 + 200 + 300 + 400


def test_premium_employee_overhours():
    e = PremiumEmployee(name="Jan", rate_per_hour=100)
    e.register_time(10)
    assert e.pay_salary() == 1200