# new_project.py - Server educational complet
from flask import Flask, request, jsonify
import datetime
import json

app = Flask(__name__)

# Stocare pentru datele primite (în memorie)
received_data = []

@app.route('/')
def home():
    """Pagina principală cu formular de test"""
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Server Educational - Test Phishing Simulat</title>
        <style>
            body { font-family: Arial; padding: 20px; max-width: 600px; margin: 0 auto; }
            .warning { background: #fff3cd; border: 1px solid #ffc107; padding: 15px; border-radius: 5px; margin: 20px 0; }
            input, button { width: 100%; padding: 10px; margin: 8px 0; box-sizing: border-box; }
            .result { background: #e8f5e9; padding: 15px; border-radius: 5px; margin: 15px 0; display: none; }
            pre { background: #f5f5f5; padding: 10px; overflow: auto; }
        </style>
    </head>
    <body>
        <h1>🔐 Server Educational Cybersecurity</h1>
        <p>Server rulează pe: <strong>http://localhost:5000</strong></p>
        
        <div class="warning">
            <h3>⚠️ ATENȚIE: SIMULARE EDUCAȚIONALĂ</h3>
            <p>Acest server este pentru învățarea tehnologiilor web.</p>
            <p><strong>Folosește DOAR date false pentru test:</strong></p>
            <ul>
                <li>test@example.com</li>
                <li>parola_test123</li>
                <li>orice date imaginare</li>
            </ul>
        </div>
        
        <h2>Testează trimiterea datelor</h2>
        
        <form id="testForm">
            <input type="email" id="email" placeholder="Email (folosește fals)" required>
            <input type="password" id="password" placeholder="Parolă (folosește falsă)" required>
            <button type="submit">📤 Trimite date de test</button>
        </form>
        
        <div class="result" id="result"></div>
        
        <h3>Accesează și:</h3>
        <ul>
            <li><a href="/view-data" target="_blank">/view-data</a> - Vezi toate datele primite</li>
            <li><a href="/stats" target="_blank">/stats</a> - Statistici server</li>
            <li><a href="/api/test" target="_blank">/api/test</a> - Test API</li>
        </ul>
        
        <script>
        document.getElementById('testForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            // Validare simplă pentru date "reale"
            const realDomains = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'];
            const domain = email.split('@')[1];
            
            if (domain && realDomains.includes(domain.toLowerCase())) {
                if (!confirm('⚠️ Ai introdus un domeniu real (' + domain + ').\\n\\nFolosește doar date false pentru test!\\nEx: test@example.com\\n\\nContinui?')) {
                    return;
                }
            }
            
            const data = {
                email: email,
                password: password,
                educational: true,
                source: 'browser_test'
            };
            
            try {
                const response = await fetch('/collect', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(data)
                });
                
                const result = await response.json();
                
                document.getElementById('result').innerHTML = `
                    <h4>✅ Date trimise cu succes!</h4>
                    <p><strong>Status:</strong> ${result.status}</p>
                    <p><strong>Mesaj:</strong> ${result.message}</p>
                    <p><strong>Timestamp:</strong> ${result.timestamp}</p>
                    <p><strong>Total înregistrări:</strong> ${result.total_records}</p>
                    <p><strong>Date trimise:</strong></p>
                    <pre>${JSON.stringify(data, null, 2)}</pre>
                    <p><a href="/view-data" target="_blank">👉 Vezi toate datele primite</a></p>
                `;
                document.getElementById('result').style.display = 'block';
                
                // Curăță formularul
                document.getElementById('email').value = '';
                document.getElementById('password').value = '';
                
                console.log('📊 Date trimise:', data);
                console.log('📥 Răspuns server:', result);
                
            } catch (error) {
                document.getElementById('result').innerHTML = `
                    <h4>❌ Eroare la trimitere</h4>
                    <p>${error.message}</p>
                    <p>Verifică dacă serverul rulează.</p>
                `;
                document.getElementById('result').style.display = 'block';
            }
        });
        
        // Mesaj în consolă
        console.log('%c🔐 SERVER EDUCAȚIONAL CYBERSECURITY', 'color: blue; font-size: 16px; font-weight: bold;');
        console.log('Acest server rulează local pentru învățare.');
        console.log('Folosește DOAR date false pentru test!');
        </script>
    </body>
    </html>
    '''

@app.route('/collect', methods=['POST'])
def collect_data():
    """Endpoint care primește date (educațional)"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "Nu sunt date"}), 400
        
        # Adaugă metadata
        record = {
            "timestamp": datetime.datetime.now().isoformat(),
            "ip_address": request.remote_addr,
            "user_agent": request.headers.get('User-Agent', ''),
            "data": data
        }
        
        # Adaugă în listă
        received_data.append(record)
        
        # Afișează în terminal (pentru vizibilitate)
        print(f"\n{'='*50}")
        print(f"📥 DATE PRIMITE ({len(received_data)})")
        print(f"IP: {record['ip_address']}")
        print(f"Timp: {record['timestamp']}")
        if 'email' in data:
            print(f"Email: {data['email']}")
        if 'password' in data:
            masked_pw = '*' * len(data['password']) if data['password'] else '[empty]'
            print(f"Parolă: {masked_pw}")
        print(f"{'='*50}\n")
        
        return jsonify({
            "status": "success",
            "message": "Date primite (simulare educațională)",
            "timestamp": record['timestamp'],
            "total_records": len(received_data),
            "note": "Datele sunt stocate doar în memorie și se vor pierde la oprirea serverului"
        }), 200
        
    except Exception as e:
        print(f"❌ Eroare: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/view-data')
def view_data():
    """Pagina pentru vizualizarea datelor primite"""
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Date primite - Server Educational</title>
        <style>
            body { font-family: Arial; padding: 20px; }
            .record { border: 1px solid #ddd; padding: 15px; margin: 15px 0; border-radius: 5px; }
            .warning { background: #fff3cd; padding: 15px; border-radius: 5px; margin: 20px 0; }
            pre { background: #f5f5f5; padding: 10px; overflow: auto; font-size: 14px; }
            .password { color: red; font-weight: bold; }
        </style>
    </head>
    <body>
        <h1>📊 Date primite - Server Educational</h1>
        <div class="warning">
            <h3>⚠️ SIMULARE EDUCAȚIONALĂ</h3>
            <p>Aceste date sunt pentru învățarea tehnologiei web.</p>
            <p><strong>Nu sunt date reale!</strong> Toate datele sunt stocate doar în memorie.</p>
        </div>
    '''
    
    if not received_data:
        html += "<p>Nu au fost primite date încă.</p>"
        html += '<p><a href="/">← Înapoi la formular</a></p>'
    else:
        html += f'<p><strong>Total înregistrări:</strong> {len(received_data)}</p>'
        html += '<p><a href="/">← Înapoi la formular</a> | '
        html += '<a href="javascript:location.reload()">⟳ Reîncarcă</a></p><hr>'
        
        for i, record in enumerate(reversed(received_data), 1):
            # Mask password in display
            display_data = record['data'].copy()
            if 'password' in display_data and display_data['password']:
                display_data['password'] = '*' * len(display_data['password'])
            
            html += f'''
            <div class="record">
                <h3>Înregistrare #{len(received_data) - i + 1}</h3>
                <p><strong>📅 Timp:</strong> {record['timestamp']}</p>
                <p><strong>🌐 IP:</strong> {record['ip_address']}</p>
                <p><strong>🖥️ Browser:</strong> {record['user_agent'][:80]}...</p>
                <p><strong>📝 Date trimise:</strong></p>
                <pre>{json.dumps(display_data, indent=2, ensure_ascii=False)}</pre>
            </div>
            <hr>
            '''
    
    html += '''
        <div class="warning">
            <p><strong>Informație tehnică:</strong></p>
            <ul>
                <li>Datele sunt stocate în lista <code>received_data</code></li>
                <li>La oprirea serverului, toate datele se pierd</li>
                <li>Serverul rulează pe <code>localhost:5000</code></li>
                <li>Endpoint API: <code>POST /collect</code></li>
            </ul>
        </div>
    </body>
    </html>
    '''
    
    return html

@app.route('/stats')
def stats():
    """Pagina cu statistici"""
    stats_info = {
        "server_running_since": datetime.datetime.now().isoformat(),
        "total_requests": len(received_data),
        "unique_ips": len(set(r['ip_address'] for r in received_data)) if received_data else 0,
        "requests_per_minute": "N/A",  # Simplificat
        "memory_usage": f"{len(str(received_data))} bytes"
    }
    
    return jsonify(stats_info)

@app.route('/api/test')
def api_test():
    """Endpoint de test API"""
    return jsonify({
        "status": "active",
        "service": "Educational Cybersecurity Server",
        "version": "1.0",
        "timestamp": datetime.datetime.now().isoformat(),
        "endpoints": {
            "GET /": "Pagina principală cu formular",
            "POST /collect": "Primește date (JSON)",
            "GET /view-data": "Vizualizează datele primite",
            "GET /stats": "Statistici server",
            "GET /api/test": "Acest endpoint"
        },
        "note": "Server educational pentru învățare"
    })

@app.route('/clear-data', methods=['POST'])
def clear_data():
    """Endpoint pentru ștergerea datelor (educațional)"""
    global received_data
    count = len(received_data)
    received_data = []
    
    return jsonify({
        "status": "success",
        "message": f"Șterse {count} înregistrări",
        "remaining": 0
    })

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 SERVER EDUCAȚIONAL CYBERSECURITY")
    print("="*60)
    print("\n📋 ACCESEAZĂ ÎN BROWSER:")
    print("   • http://localhost:5000")
    print("   • http://127.0.0.1:5000")
    print("\n🔐 SCOPE EDUCAȚIONAL:")
    print("   • Înțelegerea fluxului de date client-server")
    print("   • Cum funcționează formularele web")
    print("   • Protejarea datelor personale")
    print("\n⚠️ ATENȚIE:")
    print("   • Folosește DOAR date false pentru test!")
    print("   • Serverul rulează DOAR local")
    print("   • Datele se pierd la oprirea serverului")
    print("\n🛑 OPREȘTE SERVERUL: Ctrl+C")
    print("="*60 + "\n")
    
    app.run(debug=True, host='127.0.0.1', port=5000)