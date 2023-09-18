import doctest
import compute_days

if __name__ == "__main__":
    print("● Este programa calcula o número de dias entre duas datas")
    print("● Insira as datas no formato do exemplo: '28 de Agosto de 2023 - 18 de Setembro de 2023'")

    response = input("\n- Você deseja inserir a data pelo console? s/n: ").lower()
    
    if response in ["s", "sim"]:
        continuar = "s" 
        while continuar in ["s", "sim"]:
            date = input("\nInforme as datas: ")
            n_days = compute_days.compute_days(date)
            print(f"\n Há {n_days} dias entre as duas datas")

            continuar = input("\n - Deseja continuar? s/n: ").lower()