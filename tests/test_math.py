from app.math import factorielle, est_premier

def test_factorielle_normal():
    assert factorielle(5) == 120

def test_factorielle_limite():
    assert factorielle(0) == 1

def test_factorielle_erreur():
    try:
        factorielle(-1)
    except ValueError as e:
        assert str(e) == "Le nombre doit être positif"


def test_est_premier_normal():
    assert est_premier(7) == True

def test_est_premier_limite():
    assert est_premier(1) == False

def test_est_premier_erreur():
    assert est_premier(-5) == False
