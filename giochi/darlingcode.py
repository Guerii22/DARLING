import subprocess
import os
import colorama
import azioniinterne.rilevalingua as rilevalingua

ling = rilevalingua.leggling()
it = [
    "Output del file python :",
    "Errore durante l'esecuzione del file: ",
    "Output del programma C++:",
    "Errore durante l'esecuzione del programma C++:",
    "avvio di darling code...",
    "inserisci il nome del file da eseguire\n",
    "linguaggio non trovato ",
    "criteri gestione file ",
]
eng = [
    "Output of python file:",
    "Error while executing file:",
    "Output of C++ program:",
    "Error while executing C++ program:",
    "starting darling code...",
    "enter the name of the file to execute\n",
    "language not found",
    "file handling criteria ",
]
por = [
    "Saída do arquivo python:",
    "Erro ao executar o arquivo:",
    "Saída do programa C++:",
    "Erro ao executar o programa C++:",
    "iniciando o querido código...",
    "insira o nome do arquivo a ser executado\n",
    "idioma não encontrado",
    "critérios de gerenciamento de arquivos ",
]
parla = [it, eng, por]


def esegui_file_python(nome_file):

    try:
        print(colorama.Fore.YELLOW + ("-") * 100 + colorama.Fore.RESET)
        risultato = subprocess.run(["python", nome_file], capture_output=True, text=True, check=True)
        print(parla[ling][0], "\n", colorama.Fore.YELLOW + ("-") * 100 + colorama.Fore.RESET,)
        print(risultato.stdout)

    except subprocess.CalledProcessError as e:
        print(parla[ling][1])
        print(f"Output error: {e.stderr}")


def file_cpp(nome_file):

    try:
        print(colorama.Fore.YELLOW + ("-") * 100 + colorama.Fore.RESET)
        risultato = subprocess.run([nome_file], capture_output=True, text=True, check=True)
        print(parla[ling][2], "\n", colorama.Fore.YELLOW + ("-") * 100 + colorama.Fore.RESET,)
        print(risultato.stdout)
    except subprocess.CalledProcessError as e:
        print(parla[ling][3])
        print(f"Output error {e.stderr}")


def esegui():
    print(colorama.Fore.GREEN + parla[ling][4] + colorama.Fore.RESET)
    while True:
        nome_file = input(parla[ling][5])
        if nome_file == "darling.close":
            return
        if os.path.exists(nome_file) == True:
            gao, linguaggio = os.path.splitext(nome_file)
            if linguaggio == ".py":

                esegui_file_python(nome_file)
            elif linguaggio == ".cpp":
                file_cpp(nome_file)
            else:
                print(colorama.Fore.RED + parla[ling][6] + colorama.Fore.RESET + "[" + colorama.Fore.BLUE, linguaggio, colorama.Fore.RESET + "]",)
        else:
            print(parla[ling][7], "[", colorama.Fore.RED + "ERRORE" + colorama.Fore.RESET + "]",)


esegui()
