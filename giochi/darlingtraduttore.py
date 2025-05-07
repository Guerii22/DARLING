from deep_translator import GoogleTranslator
import azioniinterne.wifi as wifi
import colorama
import os


def translator():
    lingue = {
        "afrikaans": "af",
        "albanian": "sq",
        "amharic": "am",
        "arabic": "ar",
        "armenian": "hy",
        "assamese": "as",
        "aymara": "ay",
        "azerbaijani": "az",
        "bambara": "bm",
        "basque": "eu",
        "belarusian": "be",
        "bengali": "bn",
        "bhojpuri": "bho",
        "bosnian": "bs",
        "bulgarian": "bg",
        "catalan": "ca",
        "cebuano": "ceb",
        "chichewa": "ny",
        "chinese (simplified)": "zh-CN",
        "chinese (traditional)": "zh-TW",
        "corsican": "co",
        "croatian": "hr",
        "czech": "cs",
        "danish": "da",
        "dhivehi": "dv",
        "dogri": "doi",
        "dutch": "nl",
        "english": "en",
        "esperanto": "eo",
        "estonian": "et",
        "ewe": "ee",
        "filipino": "tl",
        "finnish": "fi",
        "french": "fr",
        "frisian": "fy",
        "galician": "gl",
        "georgian": "ka",
        "german": "de",
        "greek": "el",
        "guarani": "gn",
        "gujarati": "gu",
        "haitian creole": "ht",
        "hausa": "ha",
        "hawaiian": "haw",
        "hebrew": "iw",
        "hindi": "hi",
        "hmong": "hmn",
        "hungarian": "hu",
        "icelandic": "is",
        "igbo": "ig",
        "ilocano": "ilo",
        "indonesian": "id",
        "irish": "ga",
        "italian": "it",
        "japanese": "ja",
        "javanese": "jw",
        "kannada": "kn",
        "kazakh": "kk",
        "khmer": "km",
        "kinyarwanda": "rw",
        "konkani": "gom",
        "korean": "ko",
        "krio": "kri",
        "kurdish (kurmanji)": "ku",
        "kurdish (sorani)": "ckb",
        "kyrgyz": "ky",
        "lao": "lo",
        "latin": "la",
        "latvian": "lv",
        "lingala": "ln",
        "lithuanian": "lt",
        "luganda": "lg",
        "luxembourgish": "lb",
        "macedonian": "mk",
        "maithili": "mai",
        "malagasy": "mg",
        "malay": "ms",
        "malayalam": "ml",
        "maltese": "mt",
        "maori": "mi",
        "marathi": "mr",
        "meiteilon (manipuri)": "mni-Mtei",
        "mizo": "lus",
        "mongolian": "mn",
        "myanmar": "my",
        "nepali": "ne",
        "norwegian": "no",
        "odia (oriya)": "or",
        "oromo": "om",
        "pashto": "ps",
        "persian": "fa",
        "polish": "pl",
        "portuguese": "pt",
        "punjabi": "pa",
        "quechua": "qu",
        "romanian": "ro",
        "russian": "ru",
        "samoan": "sm",
        "sanskrit": "sa",
        "scots gaelic": "gd",
        "sepedi": "nso",
        "serbian": "sr",
        "sesotho": "st",
        "shona": "sn",
        "sindhi": "sd",
        "sinhala": "si",
        "slovak": "sk",
        "slovenian": "sl",
        "somali": "so",
        "spanish": "es",
        "sundanese": "su",
        "swahili": "sw",
        "swedish": "sv",
        "tajik": "tg",
        "tamil": "ta",
        "tatar": "tt",
        "telugu": "te",
        "thai": "th",
        "tigrinya": "ti",
        "tsonga": "ts",
        "turkish": "tr",
        "turkmen": "tk",
        "twi": "ak",
        "ukrainian": "uk",
        "urdu": "ur",
        "uyghur": "ug",
        "uzbek": "uz",
        "vietnamese": "vi",
        "welsh": "cy",
        "xhosa": "xh",
        "yiddish": "yi",
        "yoruba": "yo",
        "zulu": "zu",
    }
    a = wifi.wifi()
    if a != True:
        return
    testo = []
    while True:
        lingua = input(colorama.Fore.RESET + "scegli in che lingua tradurre\n").lower()
        if lingua == "darling.close":
            return
        fine = False
        for language, abbreviazione in lingue.items():
            if abbreviazione == lingua:
                print(colorama.Fore.GREEN + "lingua trovata (" + language + ")" + colorama.Fore.RESET)
                fine = True
        if fine == False:
            print(colorama.Fore.RED + "lingua non trovata vuoi vedere l'elenco di quelle disponibili (s)" + colorama.Fore.RESET)
        else:
            break
        dec = input().lower()
        if dec == "s":
            for language, abbreviation in lingue.items():
                print(f"{colorama.Fore.RESET+language}: {colorama.Fore.YELLOW+abbreviation}")
        else:
            pass
    print("per tradurre un file premi 1 altrimenti premi un tasto a caso")
    dec = input()
    if dec == "1":
        while True:
            file = input("inserisci il nome del file\n")
            if file == "daling.close":
                return
            if os.path.exists(file):
                contenuto = open(file, "r")
                testo = contenuto.read()
                print(colorama.Fore.YELLOW + "_" * (len(testo[0]) // 2) + "TESTO ORIGINALE" + "_" * (len(testo[0]) // 2) + colorama.Fore.LIGHTBLACK_EX)
                print(testo)
                print(colorama.Fore.YELLOW + "_" * (len(testo[-1]) // 2) + "TRADUZIONE" + "_" * (len(testo[-1]) // 2))
                traduzione = GoogleTranslator(source="auto", target=lingua).translate(testo)
                print(colorama.Fore.RESET + traduzione)
                break
            else:
                print(colorama.Fore.RED + "file non trovato" + colorama.Fore.RESET)
    else:
        print("scrivi il testo da tradurre\nPer confermare il contenuto scrivi 'darling.ready'")
        while True:
            b = input()
            if b.lower() == "darling.ready":
                break
            if b.lower().count("darling.") > 0:
                print(colorama.Fore.RED + "comando non trovato" + colorama.Fore.RESET)
            testo.append(b)
        print(colorama.Fore.YELLOW + "_" * (len(testo[0]) // 2) + "TESTO ORIGINALE" + "_" * (len(testo[0]) // 2) + colorama.Fore.LIGHTBLACK_EX)

        print(testo)
        print(colorama.Fore.YELLOW + "_" * (len(testo[-1]) // 2) + "TRADUZIONE" + "_" * (len(testo[-1]) // 2))
        for i in range(len(testo)):
            traduzione = GoogleTranslator(source="auto", target=lingua).translate(testo[i])
            print(colorama.Fore.RESET + traduzione)

    s = input("").lower
    if s.count("darling.") > 0:
        print(colorama.Fore.RED + "comando non trovato" + colorama.Fore.RESET)
    if s == "darling.copy":
        with open("filessenziali/cache.txt", "w") as copia:
            copia.writelines(traduzione)
        print(colorama.Fore.LIGHTBLACK_EX + "testo copiato negli appunti")


translator()
