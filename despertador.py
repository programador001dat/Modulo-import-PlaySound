import time
from playsound import playsound



def __despertador__(definir_hora_alarme):
    print(f"[+]Definido para tocar as: ",definir_hora_alarme)

    while True:


        hora_atual = time.strftime("%H:%M:%S")          # DEFINIR O MODO DE HORA, PADRÃO DA LIB TIME É %H:%M:%S maiusculo
        if hora_atual == definir_hora_alarme:
            print(">> Tocar som << ")
            playsound("play.wav")                       # REPRODUZIR A MIDIA, O FORMATO PADRÃO DA LIB PLAYSOUND É .WAV SE NÃO OCORERÁ UMA EXCESÃO
            break
        time.sleep(1)

definir_hora_alarme = input(">> Horario para despertar (HH:MM:SS)\n#: ")


__despertador__(definir_hora_alarme)