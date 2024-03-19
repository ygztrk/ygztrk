from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def timer():
    # HTML sayfası ve JavaScript kodu
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Zaman Sayacı</title>
        <script>
            var startTime, interval;
            var running = false;

            function toggleTimer() {
                if (!running) {
                    startTime = new Date();
                    running = true;
                    document.getElementById("startStopBtn").innerText = 'Durdur';
                    interval = setInterval(function() {
                        var now = new Date();
                        var elapsed = now - startTime;
                        var seconds = Math.floor(elapsed / 1000);
                        var milliseconds = elapsed % 1000;
                        document.getElementById("duration").innerText = "Geçen Süre: " + seconds + " saniye " + milliseconds + " salise";
                    }, 1); // Milisaniye olarak süreyi güncelle
                } else {
                    clearInterval(interval);
                    running = false;
                    document.getElementById("startStopBtn").innerText = 'Başlat';
                }
            }
        </script>
    </head>
    <body>
        <h1>Zaman Sayacı Uygulaması</h1>
        <button id="startStopBtn" onclick="toggleTimer()">Başlat</button>
        <p id="duration"></p>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
