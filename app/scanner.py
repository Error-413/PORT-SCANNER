import socket
import concurrent.futures

def scan_port(target, port):
    """Tente de se connecter à un port spécifique et retourne s'il est ouvert."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Temps d'attente pour la connexion
            result = s.connect_ex((target, port))  # Retourne 0 si le port est ouvert
            if result == 0:
                return port
    except Exception:
        return None
    return None

def scan_ports(target, ports):
    """Scanne une liste de ports en parallèle pour un gain de performance."""
    print(f"🔎 Scan des ports de {target}...")
    open_ports = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(scan_port, target, port): port for port in ports}
        for future in concurrent.futures.as_completed(futures):
            port = futures[future]
            if future.result() is not None:
                open_ports.append(port)

    return open_ports

if __name__ == "__main__":
    target = input("Entrez l'IP ou le domaine cible : ")
    ports = range(1, 1025)  # Scanner les ports bien connus (1-1024)

    open_ports = scan_ports(target, ports)

    if open_ports:
        print("\n✅ Ports ouverts trouvés :")
        for port in open_ports:
            print(f" - Port {port} ouvert")
    else:
        print("\n❌ Aucun port ouvert trouvé.")
