from app.texte import est_palindrome


def test_est_palindrome_normal():
    assert est_palindrome("radar") is True


def test_est_palindrome_limite():
    assert est_palindrome("a") is True


def test_est_palindrome_erreur():
    assert est_palindrome("") is True