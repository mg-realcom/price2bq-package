from src.price2bq_zfullio.main import prepare_novostroy_m, prepare_realty, prepare_cian, prepare_avito


def test_realty() -> None:
    df = prepare_realty("test_realty.xls")
    assert len(df)


def test_cian() -> None:
    df = prepare_cian("test_cian.xlsx")
    assert len(df) == 5


def test_avito() -> None:
    df = prepare_avito("test_avito.csv")
    assert len(df) == 5


def test_novostroy_m() -> None:
    df = prepare_novostroy_m("test_novostroy_m.xls")
    assert len(df)
    df2 = prepare_novostroy_m("test_novostroy_m.xlsx")
    assert len(df2)
