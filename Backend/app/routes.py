from flask import request, jsonify, render_template
from app.attacks import ping_flood, stop_flood
from app import app
import threading

# Sledování aktivních ping floodů
active_threads = {}


# API endpoint pro spuštění ping floodu
@app.route('/api/start_flood', methods=['POST'])
def start_flood():
    target_ip = request.json.get('target_ip')
    countdown_seconds = request.json.get('countdown_seconds')

    if not target_ip:
        return jsonify({"error": "IP adresa není poskytnuta"}), 400

    if not countdown_seconds:
        return jsonify({"error": "Odpočet není poskytnut"}), 400

    # Spuštění ping floodu ve vláknu
    ping_thread = ping_flood(target_ip)
    thread_id = threading.get_ident()  # identifikátor vlákna
    active_threads[thread_id] = ping_thread

    # Zpráva o zahájení ping floodu
    return jsonify({"message": f"Ping flood běží na {target_ip}...", "thread_id": thread_id})

# API endpoint pro zastavení ping floodu
@app.route('/api/stop_flood/<int:thread_id>', methods=['POST'])
def stop_flood_route(thread_id):
    ping_thread = active_threads.get(thread_id)
    
    if not ping_thread:
        return jsonify({"error": "Vlákno nenalezeno"}), 404
    
    stop_flood(ping_thread)
    del active_threads[thread_id]

    # Zpráva o zastavení ping floodu
    return jsonify({"message": "Ping flood byl zastaven."})