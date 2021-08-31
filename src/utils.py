from datetime import datetime


def current_year() -> int:
    obj = datetime.today()
    return int(obj.strftime("%Y"))


def current_month() -> int:
    obj = datetime.today()
    return int(obj.strftime("%m"))


def today_epoch() -> int:
    # int(datetime.now().timestamp())
    t = today_date()
    return get_epoch(t[0], t[1], t[2])


def today_date() -> (int, int, int):
    obj = datetime.today()
    return (
        int(obj.strftime("%d")),
        int(obj.strftime("%m")),
        int(obj.strftime("%Y"))
    )


def get_epoch(dia: int, mes: int, anio=current_year()) -> int:
    return int(datetime(year=anio, month=mes, day=dia).timestamp())


def date_from_epoch(epoch: int) -> str:
    d = datetime.datetime.utcfromtimestamp(epoch)
    return d.strftime("%d-%m-%Y")
