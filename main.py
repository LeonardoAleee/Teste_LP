from program import get_user_response, compute_and_print_result, dates_from_file

    
print("● Este programa calcula o número de dias entre duas datas")
print("● Insira as datas no formato do exemplo: '28 de Agosto de 2023 - 18 de Setembro de 2023'")

run = get_user_response()

# Cria um loop para o programa e o roda
while run:
    date = input("\nInforme as datas: ")
    compute_and_print_result(date)
    run = get_user_response()

else:

    file_path = input("\n● Em qual arquivo estão as datas?: ")
    

    dates = dates_from_file(file_path)
    for date in dates:
        compute_and_print_result(date)