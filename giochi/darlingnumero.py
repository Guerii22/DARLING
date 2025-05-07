import random
import colorama

def trovato(a):
    n_gen = random.randint(0, a)
    n_input = 0

    while n_input != n_gen:
        try:
            print("Indovina il numero compreso tra 1 e", a) 
            n_input = input()
            
            if int(n_input) == n_gen:
                print(colorama.Fore.GREEN + "Numero corretto! \n" + colorama.Fore.RESET)
                break

            elif int(n_input) < n_gen:
                print(colorama.Fore.CYAN + "Numero troppo basso, riprova ['3' per uscire] [un qualsiasi tasto per continuare]" + colorama.Fore.RESET)
                c = input()
                if c != "3":
                    print("Avanzamento \t", colorama.Fore.GREEN + "[OK]" + colorama.Fore.RESET)
                    continue
                else:
                    print("Uscita in corso \t", colorama.Fore.GREEN + "[OK]" + colorama.Fore.RESET)
                    break

            elif int(n_input) > n_gen:
                print(colorama.Fore.CYAN + "Numero troppo alto, riprova ['3' per uscire] [un qualsiasi tasto per continuare]" + colorama.Fore.RESET)
                c = input()
                if c != "3":
                    print("Avanzamento \t", colorama.Fore.GREEN + "[OK]" + colorama.Fore.RESET)
                    continue
                else:
                    print("Uscita in corso \t", colorama.Fore.GREEN + "[OK]" + colorama.Fore.RESET)
                    break
        except ValueError or TypeError:
            print(colorama.Fore.RED + "Errore nell'input" + colorama.Fore.RESET)


a = 20

trovato(a)
