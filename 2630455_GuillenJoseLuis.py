# COVER PAGE
# Name:      José Luis Guillen González
# Student ID:       2630455
# Group:     IM 1-2
# Course:    Programming Methodologies
# Topic:     Numeric types (int, float) and booleans in Python
# GitHub repository: <https://github.com/RzSolo/Manejo-de-n-meros-y-booleanos-en-Python/upload>

# EXECUTIVE SUMMARY

# Los tipos int y float sirven para trabajar con números: int guarda números
# enteros (edad, horas completas, puntaje) y float guarda números con decimales
# (temperatura, salario, BMI). La diferencia principal es que un float puede
# representar fracciones pero puede tener pequeños errores de redondeo.
# Un booleano (True/False) se obtiene al comparar valores con operadores como
# <, >=, == y se combina con and, or, not para tomar decisiones con if.
# Validar rangos y evitar divisiones entre cero es importante para que el
# programa no se caiga ni de resultados absurdos (por ejemplo un ingreso de 0).

# PRINCIPLES AND BEST PRACTICES

# - Usar tipos apropiados: int para contadores, float para cantidades con decimales.
# - Evitar duplicar expresiones complejas: guardar resultados intermedios en variables.
# - Validar datos antes de operar (por ejemplo, que horas y salarios no sean negativos).
# - Usar nombres de variables descriptivos y mensajes claros para el usuario.
# - Documentar cómo se interpretan los booleanos: en este archivo true significa
#   que la condición se cumple (por ejemplo, "High temperature: true" quiere
#   decir que la temperatura es mayor o igual que 30.0) y false que no se cumple.

# MAIN MENU

# El programa pregunta qué problema ejecutar: 1-6, o 0 para ejecutar todos.
VALID_CHOICES = ["0", "1", "2", "3", "4", "5", "6"]

choice = input("Select problem (1-6, 0 = run all): ").strip()
if choice not in VALID_CHOICES:
    print("Error: invalid input")


# =============================================================================
# Problem 1: Temperature converter and range flag
# =============================================================================
# Description: Converts a temperature in Celsius (float) to Fahrenheit and
#   Kelvin. It also creates the boolean is_high_temperature, which is true
#   when the temperature in Celsius is greater than or equal to 30.0.
#
# Inputs:
#   - temp_c (float; temperature in °C)
#
# Outputs:
#   - "Fahrenheit:" <temp_f>
#   - "Kelvin:" <temp_k>
#   - "High temperature:" true|false
#
# Validations:
#   - temp_c must be convertible to float (try/except ValueError).
#   - The temperature cannot be below absolute zero (temp_k < 0.0 is an error).
#   - Any error shows "Error: invalid input".
#
# Test cases:
#   1) Normal: temp_c = 25
#        -> Fahrenheit: 77.0 / Kelvin: 298.15 / High temperature: false
#   2) Border: temp_c = 30 (exactly the limit)
#        -> Fahrenheit: 86.0 / Kelvin: 303.15 / High temperature: true
#   3) Error: temp_c = "abc" -> Error: invalid input
#      Error: temp_c = -300 (below absolute zero) -> Error: invalid input
if choice == "1" or choice == "0":
    print("\n--- Problem 1 ---")
    HIGH_TEMPERATURE = 30.0

    temp_c_text = input("Enter temperature in Celsius: ").strip()
    try:
        temp_c = float(temp_c_text)
        temp_k = temp_c + 273.15

        if temp_k < 0.0:
            print("Error: invalid input")
        else:
            temp_f = temp_c * 9 / 5 + 32
            is_high_temperature = (temp_c >= HIGH_TEMPERATURE)

            print("Fahrenheit:", temp_f)
            print("Kelvin:", temp_k)
            print("High temperature:", str(is_high_temperature).lower())

    except ValueError:
        print("Error: invalid input")


# =============================================================================
# Problem 2: Work hours and overtime payment
# =============================================================================
# Description: Calculates the weekly pay of a worker. Up to 40 hours are paid
#   at hourly_rate (float). Overtime hours (> 40) are paid at 150% of the
#   normal rate. It also creates the boolean has_overtime, which is true when
#   the worker did overtime.
#
# Inputs:
#   - hours_worked (float; hours worked in the week)
#   - hourly_rate (float; pay per hour)
#
# Outputs:
#   - "Regular pay:" <regular_pay>
#   - "Overtime pay:" <overtime_pay>
#   - "Total pay:" <total_pay>
#   - "Has overtime:" true|false
#
# Validations:
#   - Both inputs must be convertible to float (try/except ValueError).
#   - hours_worked >= 0
#   - hourly_rate > 0
#   - If any of them fails, it shows "Error: invalid input".
#
# Test cases:
#   1) Normal: hours_worked = 45, hourly_rate = 100
#        -> Regular pay: 4000.0 / Overtime pay: 750.0
#           Total pay: 4750.0 / Has overtime: true
#   2) Border: hours_worked = 40, hourly_rate = 100 (exactly 40 hours)
#        -> Regular pay: 4000.0 / Overtime pay: 0.0
#           Total pay: 4000.0 / Has overtime: false
#   3) Error: hours_worked = -5, hourly_rate = 100 -> Error: invalid input
#      Error: hours_worked = 10, hourly_rate = 0 -> Error: invalid input
if choice == "2" or choice == "0":
    print("\n--- Problem 2 ---")
    MAX_REGULAR_HOURS = 40
    OVERTIME_MULTIPLIER = 1.5

    hours_text = input("Hours worked: ").strip()
    rate_text = input("Hourly rate: ").strip()
    try:
        hours_worked = float(hours_text)
        hourly_rate = float(rate_text)
        is_valid = hours_worked >= 0 and hourly_rate > 0
    except ValueError:
        is_valid = False

    if not is_valid:
        print("Error: invalid input")
    else:
        regular_hours = min(hours_worked, MAX_REGULAR_HOURS)
        overtime_hours = max(hours_worked - MAX_REGULAR_HOURS, 0)
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * OVERTIME_MULTIPLIER
        total_pay = regular_pay + overtime_pay
        has_overtime = (hours_worked > MAX_REGULAR_HOURS)

        print("Regular pay:", regular_pay)
        print("Overtime pay:", overtime_pay)
        print("Total pay:", total_pay)
        print("Has overtime:", str(has_overtime).lower())


# =============================================================================
# Problem 3: Discount eligibility with booleans
# =============================================================================
# Description: Determines whether a customer gets a discount. The customer is
#   eligible if is_student is true OR is_senior is true OR purchase_total is
#   greater than or equal to 1000.0. When eligible, a 10% discount is applied
#   to the total.
#
# Inputs:
#   - purchase_total (float; total of the purchase)
#   - is_student_text (string; "YES" or "NO")
#   - is_senior_text (string; "YES" or "NO")
#
# Outputs:
#   - "Discount eligible:" true|false
#   - "Final total:" <final_total>
#
# Validations:
#   - purchase_total must be convertible to float (try/except ValueError)
#     and purchase_total >= 0.0
#   - is_student_text and is_senior_text are normalized to uppercase with
#     upper() and converted to the booleans is_student and is_senior.
#   - If a text is not "YES" or "NO", it shows "Error: invalid input".
#
# Test cases:
#   1) Normal: purchase_total = 500, student "YES", senior "NO"
#        -> Discount eligible: true / Final total: 450.0
#   2) Border: purchase_total = 1000, student "NO", senior "NO"
#        (exactly 1000.0 is enough) -> Discount eligible: true
#           Final total: 900.0
#   3) Error: purchase_total = 500, student "maybe", senior "NO"
#        -> Error: invalid input
#      Error: purchase_total = -10, student "NO", senior "NO"
#        -> Error: invalid input
if choice == "3" or choice == "0":
    print("\n--- Problem 3 ---")
    DISCOUNT_MIN_TOTAL = 1000.0
    DISCOUNT_FACTOR = 0.9

    purchase_text = input("Purchase total: ").strip()
    is_student_text = input("Is student? (YES/NO): ").strip().upper()
    is_senior_text = input("Is senior? (YES/NO): ").strip().upper()
    try:
        purchase_total = float(purchase_text)
        is_valid = (purchase_total >= 0.0
                    and is_student_text in ("YES", "NO")
                    and is_senior_text in ("YES", "NO"))
    except ValueError:
        is_valid = False

    if not is_valid:
        print("Error: invalid input")
    else:
        is_student = (is_student_text == "YES")
        is_senior = (is_senior_text == "YES")
        discount_eligible = (is_student or is_senior
        or purchase_total >= DISCOUNT_MIN_TOTAL)

        if discount_eligible:
            final_total = purchase_total * DISCOUNT_FACTOR
        else:
            final_total = purchase_total

        print("Discount eligible:", str(discount_eligible).lower())
        print("Final total:", final_total)


# =============================================================================
# Problem 4: Basic statistics of three integers
# =============================================================================
# Description: Reads three integers and calculates the sum, the average
#   (float), the maximum value, the minimum value and the boolean all_even,
#   which is true when the three numbers are even.
#
# Inputs:
#   - n1 (int)
#   - n2 (int)
#   - n3 (int)
#
# Outputs:
#   - "Sum:" <sum_value>
#   - "Average:" <average_value>
#   - "Max:" <max_value>
#   - "Min:" <min_value>
#   - "All even:" true|false
#
# Validations:
#   - The three values must be convertible to int (try/except ValueError).
#     Text like "abc" or a decimal like "3.5" is an error.
#   - No additional restrictions (negative numbers are allowed).
#
# Test cases:
#   1) Normal: n1 = 4, n2 = 7, n3 = 10
#        -> Sum: 21 / Average: 7.0 / Max: 10 / Min: 4 / All even: false
#   2) Border: n1 = -2, n2 = 0, n3 = 2 (negative number and zero)
#        -> Sum: 0 / Average: 0.0 / Max: 2 / Min: -2 / All even: true
#   3) Error: n1 = "abc", n2 = 1, n3 = 2 -> Error: invalid input
#      Error: n1 = 3.5, n2 = 1, n3 = 2 -> Error: invalid input
if choice == "4" or choice == "0":
    print("\n--- Problem 4 ---")
    n1_text = input("Enter first integer: ").strip()
    n2_text = input("Enter second integer: ").strip()
    n3_text = input("Enter third integer: ").strip()
    try:
        n1 = int(n1_text)
        n2 = int(n2_text)
        n3 = int(n3_text)
        is_valid = True
    except ValueError:
        is_valid = False

    if not is_valid:
        print("Error: invalid input")
    else:
        sum_value = n1 + n2 + n3
        average_value = sum_value / 3
        max_value = max(n1, n2, n3)
        min_value = min(n1, n2, n3)
        all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

        print("Sum:", sum_value)
        print("Average:", average_value)
        print("Max:", max_value)
        print("Min:", min_value)
        print("All even:", str(all_even).lower())


# =============================================================================
# Problem 5: Loan eligibility (income and debt ratio)
# =============================================================================
# Description: Determines whether a person is eligible for a loan using
#   monthly_income (float), monthly_debt (float) and credit_score (int).
#   debt_ratio = monthly_debt / monthly_income. The person is eligible if
#   monthly_income >= 8000.0 AND debt_ratio <= 0.4 AND credit_score >= 650.
#
# Inputs:
#   - monthly_income (float; monthly income)
#   - monthly_debt (float; monthly debt payments)
#   - credit_score (int; credit score)
#
# Outputs:
#   - "Debt ratio:" <debt_ratio>
#   - "Eligible:" true|false
#
# Validations:
#   - monthly_income and monthly_debt must be convertible to float and
#     credit_score to int (try/except ValueError).
#   - monthly_income > 0.0 (avoids division by zero)
#   - monthly_debt >= 0.0
#   - credit_score >= 0
#   - If any of them fails, it shows "Error: invalid input".
#
# Test cases:
#   1) Normal: monthly_income = 10000, monthly_debt = 2000, credit_score = 700
#        -> Debt ratio: 0.2 / Eligible: true
#   2) Border: monthly_income = 8000, monthly_debt = 3200, credit_score = 650
#        (income, debt ratio and score are exactly at the limits)
#        -> Debt ratio: 0.4 / Eligible: true
#   3) Error: monthly_income = 0, monthly_debt = 500, credit_score = 700
#        -> Error: invalid input
#      Error: monthly_income = "abc", monthly_debt = 500, credit_score = 700
#        -> Error: invalid input
if choice == "5" or choice == "0":
    print("\n--- Problem 5 ---")
    MIN_INCOME = 8000.0
    MAX_DEBT_RATIO = 0.4
    MIN_CREDIT_SCORE = 650

    income_text = input("Monthly income: ").strip()
    debt_text = input("Monthly debt: ").strip()
    score_text = input("Credit score: ").strip()
    try:
        monthly_income = float(income_text)
        monthly_debt = float(debt_text)
        credit_score = int(score_text)
        is_valid = monthly_income > 0 and monthly_debt >= 0 and credit_score >= 0
    except ValueError:
        is_valid = False

    if not is_valid:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income

        eligible = (
            monthly_income >= MIN_INCOME
            and debt_ratio <= MAX_DEBT_RATIO
            and credit_score >= MIN_CREDIT_SCORE
        )

        print("Debt ratio:", debt_ratio)
        print("Eligible:", str(eligible).lower())


# =============================================================================
# Problem 6: Body Mass Index (BMI) and category flag
# =============================================================================
# Description: Calculates the body mass index (BMI) with
#   bmi = weight_kg / (height_m * height_m). It also creates three booleans:
#   is_underweight (bmi < 18.5), is_normal (18.5 <= bmi < 25.0) and
#   is_overweight (bmi >= 25.0).
#
# Inputs:
#   - weight_kg (float; weight in kilograms)
#   - height_m (float; height in meters)
#
# Outputs:
#   - "BMI:" <bmi rounded to 2 decimals>
#   - "Underweight:" true|false
#   - "Normal:" true|false
#   - "Overweight:" true|false
#
# Validations:
#   - Both inputs must be convertible to float (try/except ValueError).
#   - weight_kg > 0.0
#   - height_m > 0.0 (also avoids division by zero)
#   - If any of them fails, it shows "Error: invalid input".
#
# Test cases:
#   1) Normal: weight_kg = 70, height_m = 1.75
#        -> BMI: 22.86 / Underweight: false / Normal: true / Overweight: false
#   2) Border: weight_kg = 100, height_m = 2.0 (bmi is exactly 25.0)
#        -> BMI: 25.0 / Underweight: false / Normal: false / Overweight: true
#   3) Error: weight_kg = 0, height_m = 1.7 -> Error: invalid input
#      Error: weight_kg = 70, height_m = -1.7 -> Error: invalid input
if choice == "6" or choice == "0":
    print("\n--- Problem 6 ---")
    UNDERWEIGHT_LIMIT = 18.5
    OVERWEIGHT_LIMIT = 25.0

    weight_text = input("Weight in kg: ").strip()
    height_text = input("Height in meters: ").strip()
    try:
        weight_kg = float(weight_text)
        height_m = float(height_text)
        is_valid = weight_kg > 0 and height_m > 0
    except ValueError:
        is_valid = False

    if not is_valid:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)

        is_underweight = (bmi < UNDERWEIGHT_LIMIT)
        is_normal = (UNDERWEIGHT_LIMIT <= bmi < OVERWEIGHT_LIMIT)
        is_overweight = (bmi >= OVERWEIGHT_LIMIT)

        print("BMI:", round(bmi, 2))
        print("Underweight:", str(is_underweight).lower())
        print("Normal:", str(is_normal).lower())
        print("Overweight:", str(is_overweight).lower())


# CONCLUSIONS

# Los enteros y los flotantes se usan juntos en cálculos reales: por ejemplo
# en el Problema 5 un int (credit_score) se combina con floats (ingreso y
# deuda) y en el Problema 4 la suma es int pero el promedio es float.
# Las comparaciones (>=, <, ==) generan booleanos que permiten decidir con if
# si algo aplica o no como el descuento del Problema 3 o las horas extra del
# Problema 2. Validar rangos y evitar divisiones entre cero (ingreso 0 en el
# Problema 5, estatura 0 en el Problema 6) evita errores y resultados sin
# sentido. También aprendí a combinar condiciones con and, or y not cuidando
# los límites exactos (>= 30.0, <= 0.4, > 40). Estos patrones se repiten en
# problemas de nómina, descuentos, préstamos y salud.

# REFERENCES

# References:
# 1) Python documentation - Built-in Types: Numeric Types (int, float, complex).
#    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
# 2) Python documentation - Boolean Type (bool) and Boolean Operations.
#    https://docs.python.org/3/library/stdtypes.html#boolean-type-bool
# 3) Python Tutorial - An Informal Introduction to Python (numbers).
#    https://docs.python.org/3/tutorial/introduction.html
# 4) van Rossum, G., Warsaw, B., Coghlan, A. PEP 8 - Style Guide for Python
#    Code. https://peps.python.org/pep-0008/
# 5) Apuntes de clase de la materia (Programación).
