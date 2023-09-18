import doctest
from datetime import date

def compute_days(date_string):
    """Recebe duas datas e retorna o número de dias entre as duas datas

    Parâmetro
    ----------
    date_string : string
        Deve conter as duas datas separadas por "-".

    Returns
    -------
    n_days
        Retorna a quantidade de dias entre as duas datas
    
    Doctest
    -------   
    
    Calcula a diferença entre as duas datas e retorna o resultado correto
    >>> compute_days("18 de Agosto de 2023 - 28 de Agosto de 2023")
    10
    
    Calcula a diferença entre as duas datas e retorna o resultado incorreto
    >>> compute_days("18 de Agosto de 2023 - 28 de Agosto de 2023")
    12
    """
    
    if type(date_string) is not str:
        raise TypeError
    
    else:
        # Pega a string date_string e remove a string "de" dela
        date_string = date_string.replace("de", "")
        
        # Divide a string em duas datas diferentes
        date_1, date_2 = date_string.split("-")
        
        # Quebra ambas as datas em seus respectivos dias, meses e anos
        day_1, month_1, year_1 = date_1.split()
        day_2, month_2, year_2  = date_2.split()
        
        # Tranforma em inteiro todas as datas
        day_1 = int(day_1) 
        day_2 = int(day_2)
        year_1 = int(year_1)
        year_2 = int(year_2)

        # Relaciona os meses com os inteiros acima, assim Janeiro é o inteiro 1, Fevereiro, 2, etc.
        month_mapper = {"Janeiro": 1, "Fevereiro": 2, "Março": 3, "Abril": 4, "Maio": 5, "Junho": 6, "Julho": 7, "Agosto": 8, "Setembro": 9, "Outubro": 10, "Novembro": 11, "Dezembro": 12}
        
        # Pega de month_mapper os meses desejados
        month_1 = month_mapper[month_1]
        month_2 = month_mapper[month_2]

        n_days = (date(day=day_2, month=month_2, year=year_2) - date(day=day_1, month=month_1, year=year_1)).days

        return n_days


if __name__ == "__main__":
    doctest.testmod(verbose=True)