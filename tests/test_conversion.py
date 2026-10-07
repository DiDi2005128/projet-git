import pytest
from app.conversion import celsius_fahrenheit, km_miles, euros_devise

#  Tests celsius_fahrenheit (normal, limite, erreur) 
def test_celsius_normal():
    assert celsius_fahrenheit(20) == 68.0

def test_celsius_limite():
    assert celsius_fahrenheit(-273.15) == -459.67

def test_celsius_erreur():
    with pytest.raises(ValueError):
        celsius_fahrenheit(-300)


#  Tests km_miles (normal, limite, erreur) 
def test_km_normal():
    assert km_miles(10) == 6.21

def test_km_limite():
    assert km_miles(0) == 0.0

def test_km_erreur():
    with pytest.raises(ValueError):
        km_miles(-5)


# Tests euros_devise (normal, limite, erreur) 
def test_euros_normal():
    assert euros_devise(100, "USD") == 108.0

def test_euros_limite():
    assert euros_devise(0, "USD") == 0.0

def test_euros_erreur_devise():
    with pytest.raises(ValueError):
        euros_devise(50, "XYZ")

def test_euros_erreur_montant():
    with pytest.raises(ValueError):
        euros_devise(-10, "USD")