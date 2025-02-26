from flask import Flask, jsonify
import socket
import concurrent.futures

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Scanner de ports opérationnel 🚀"})

@app.route('/scan/<target>')
def scan_ports(target):
    """Scanne les ports d'une cible et retourne les résultats en JSON"""
    ports = range(1, 1025)
    open_ports = []

    def scan_port(port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((target, port))
                if result == 0:
                    return port
        except:
            return None
        return None

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(scan_port, port): port for port in ports}
        for future in concurrent.futures.as_completed(futures):
            port = futures[future]
            if future.result() is not None:
                open_ports.append(port)

    return jsonify({"target": target, "open_ports": open_ports})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
