from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'super_secret_music_key_123'

# Mock user credentials for validation
MOCK_USER = {
    "email": "you@example.com",
    "password": "password123"
}

# Sample available media tracklist
TRACKS = [
    {"id": 1, "title": "Acoustic Melody", "artist": "Guitar Master", "filename": "track1.mp3"},
    {"id": 2, "title": "Electronic Beats", "artist": "Synthwave Kid", "filename": "track2.mp3"},
    {"id": 3, "title": "Ambient Ambient Sky", "artist": "Lo-Fi Dreamer", "filename": "track3.mp3"}
]

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if email == MOCK_USER["email"] and password == MOCK_USER["password"]:
            return redirect(url_for('player'))
        else:
            flash('Invalid credentials. Please try again.')
            return redirect(url_for('login'))
            
    return render_template('login.html')

@app.route('/player')
def player():
    return render_template('player.html', tracks=TRACKS)

if __name__ == '__main__':
    app.run(debug=True)
