from src.calculadora import soma, subtração

def test_soma():
  assert soma(2, 3) == 5
  
def test_subtração():
  assert subtração(5, 3) == 2
