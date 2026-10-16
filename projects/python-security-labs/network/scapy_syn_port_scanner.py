from scapy.all import IP, TCP, sr1


def escanear_host(host, puertos):
    print(f"Escaneando host: {host}")
    for puerto in puertos:
        paquete = IP(dst=host) / TCP(dport=puerto, flags="S")
        respuesta = sr1(paquete, timeout=1, verbose=0)

        if respuesta is None:
            print(f"Puerto {puerto}: No responde (posiblemente filtrado)")
        elif respuesta.haslayer(TCP):
            if respuesta.getlayer(TCP).flags == 0x12:
                print(f"Puerto {puerto}: Abierto")
                rst_paquete = IP(dst=host) / TCP(dport=puerto, flags="R")
                sr1(rst_paquete, timeout=1, verbose=0)
            elif respuesta.getlayer(TCP).flags == 0x14:
                print(f"Puerto {puerto}: Cerrado")
        else:
            print(f"Puerto {puerto}: Estado desconocido")


if __name__ == "__main__":
    host = "127.0.0.1"
    puertos = range(1, 65536)
    escanear_host(host, puertos)
