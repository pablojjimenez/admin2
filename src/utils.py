from datetime import datetime

MONTHS_NAMES = 'ENERO,FEBRERO,MARZO,ABRIL,MAYO,JUNIO,JULIO,AGOSTO,SEPTIEMBRE,OCTUBRE,NOVIEMBRE,DICIEMBRE'.split(',')


def current_year() -> int:
    obj = datetime.today()
    return int(obj.strftime("%Y"))


def current_month() -> int:
    obj = datetime.today()
    return int(obj.strftime("%m"))


def today_epoch() -> int:
    return int(datetime.now().timestamp())


def today_date() -> (int, int, int):
    obj = datetime.today()
    return (
        int(obj.strftime("%d")),
        int(obj.strftime("%m")),
        int(obj.strftime("%Y"))
    )


def get_epoch(dia: int, mes=current_month(), anio=current_year()) -> int:
    return int(datetime(year=anio, month=mes, day=dia).timestamp())


def next_month(month: int = None) -> int:
    if month:
        solve = (month + 1) % 13
        return solve if solve != 0 else 1
    else:
        solve = (today_date()[1] + 1) % 13
        return solve if solve != 0 else 1


def translate_from_epoch(epoch: int) -> str:
    d = datetime.utcfromtimestamp(epoch)
    return d.strftime("%d-%m-%Y")
