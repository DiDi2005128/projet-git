from app.texte import est_palindrome, compter_voyelles, inverser


def test_est_palindrome_normal():
    assert est_palindrome("radar") is True


def test_est_palindrome_limite():
    assert est_palindrome("a") is True


def test_est_palindrome_erreur():
    assert est_palindrome("") is True



def test_compter_voyelles_normal():
    assert compter_voyelles("Bonjour") == 3


def test_compter_voyelles_limite():
    assert compter_voyelles("a") == 1


def test_compter_voyelles_erreur():
    assert compter_voyelles("") == 0


def test_inverser_normal():
    assert inverser("bonjour") == "ruojnob"


def test_inverser_limite():
    assert inverser("a") == "a"


def test_inverser_erreur():
    assert inverser("") == ""