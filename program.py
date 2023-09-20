from date_handler import date_normalizer, compute_days

def compute_and_print_result(date):
    
    # Calcula o número de dias e printa o resultado
    date_1, date_2 = date_normalizer(date)
    n_days = compute_days(date_1, date_2)
    print(f"\n- Data: {date.strip()}" )
    print(f"- Há {n_days} dias entre as duas datas")


def dates_from_file(file_path):
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
