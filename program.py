import compute_days

def compute_and_print_result(date):
    
    # Calcula o número de dias e printa o resultado
    n_days = compute_days.compute_days(date)
    print(f"\n- Data: {date.strip()}" )
    print(f"- Há {n_days} dias entre as duas datas")


def dates_from_file(file_path):
    
    # Pega as datas do arquivo txt e retorna erro se não for possível
    try:
        with open(file_path, 'r') as file:
            dates = file.readlines()
            return dates
        
    except FileNotFoundError:
        print(f"O arquivo '{file_path}' não foi encontrado.")


def get_user_response():
    
    # Pega a data pelo console
    response = input("\n- Você deseja inserir a data pelo console? s/n: ").lower()
    run = False
    if response in ["s", "sim", "y", "yes"]:
        run = True

    return run


def console_program():
    
    # Cria um loop para o programa e o roda
    print("● Este programa calcula o número de dias entre duas datas")
    print("● Insira as datas no formato do exemplo: '28 de Agosto de 2023 - 18 de Setembro de 2023'")

    run = get_user_response()
    
    while run:
        date = input("\nInforme as datas: ")
        compute_and_print_result(date)
        run = get_user_response()

    else:

        file_path = input("\n● Em qual arquivo estão as datas?: ")
        

        dates = dates_from_file(file_path)
        for date in dates:
            compute_and_print_result(date)