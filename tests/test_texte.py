from app.texte import est_palindrome


def test_est_palindrome():
    assert est_palindrome("radar") is True
    assert est_palindrome("bonjour") is False