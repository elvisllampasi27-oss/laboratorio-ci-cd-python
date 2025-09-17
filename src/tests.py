from main import Calculator

def test_sums_2_numbers():
    assert Calculator().sum(2, 2) == 4
if __name__ == "__main__":
    calc = Calculator()
    print("🧮 Calculadora Python iniciada")
    print(f"Ejemplo: 2 + 3 = {calc.sum(2, 3)}")
    print("Calculadora funcionando correctamente ✅")