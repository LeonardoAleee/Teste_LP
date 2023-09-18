from datetime import date 

def compute_days(date_string):

    date_string = date_string.replace("de", "")

    date_1, date_2 = date_string.split("-")

    day_1, month_1, year_1 = date_1.split()
    day_2, month_2, year_2  = date_2.split()

    day_1 = int(day_1)
    day_2 = int(day_2)
    year_1 = int(year_1)
    year_2 = int(year_2)

    month_mapper = {"Janeiro": 1, "Fevereiro": 2, "Março": 3, "Abril": 4, "Maio": 5, "Junho": 6, "Julho": 7, "Agosto": 8, "Setembro": 9, "Outubro": 10, "Novembro": 11, "Dezembro": 12}

    month_1 = month_mapper[month_1]
    month_2 = month_mapper[month_2]

    n_days = date(day=day_2, month=month_2, year=year_2) - date(day=day_1, month=month_1, year=year_1)

    return n_days.days
