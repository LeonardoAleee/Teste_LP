import doctest
from datetime import date

def date_normalizer(date_string:str) -> tuple:
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

    # Relaciona os meses com os inteiros acima, assim Janeiro é o inteiro 1, Fevereiro, 2, etc.
    month_mapper = {"janeiro": 1, "fevereiro": 2, "março": 3, "abril": 4, "maio": 5, "junho": 6, "julho": 7, "agosto": 8, "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12}
        
    if type(date_string) is not str:
            raise TypeError
        
    else:
        date_string = date_string.lower()

        # Divide a string em duas datas diferentes
        date_1, date_2 = date_string.split("-")
        
        # Quebra ambas as datas em seus respectivos dias, meses e anos
        day_1, _, month_1, _, year_1 = date_1.split()
        day_2, _, month_2, _, year_2  = date_2.split()
        
        # Tranforma em inteiro todas as datas
        day_1 = int(day_1) 
        day_2 = int(day_2)
        year_1 = int(year_1)
        year_2 = int(year_2)

        # Pega de month_mapper os meses desejados
        month_1 = month_mapper[month_1]
        month_2 = month_mapper[month_2]

        date_normalized_1 = date(day=day_1, month=month_1, year=year_1)
        date_normalized_2 = date(day=day_2, month=month_2, year=year_2)

        return date_normalized_1, date_normalized_2

def compute_days(date_1, date_2):

    n_days = (date_2 - date_1).days

    return n_days


if __name__ == "__main__":
    doctest.testmod(verbose=True)