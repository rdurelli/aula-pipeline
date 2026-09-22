from main import soma, eh_par


def test_soma():
    assert soma(2, 3) == 5


def test_numero_par():
    assert eh_par(4) == True
