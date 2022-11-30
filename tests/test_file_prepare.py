from src.price2bq_zfullio.main import prepare_novostroy_m, prepare_realty, prepare_cian, prepare_avito


def test_realty():
    df = prepare_realty("test_realty.xls")
    assert len(df)


def test_cian():
    df = prepare_cian("test_cian.xlsx")
    assert len(df) == 5


def test_avito():
    df = prepare_avito("test_avito.csv")
    assert len(df) == 5


def test_novostroy_m():
    df = prepare_novostroy_m("test_novostroy_m.xls")
    assert len(df)

