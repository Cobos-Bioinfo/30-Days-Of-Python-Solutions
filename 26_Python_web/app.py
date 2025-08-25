# Day 26 - 30DaysOfPython Challenge
# Python Web

from flask import Flask, render_template, request, redirect, url_for
import os

app: Flask = Flask(__name__)

# to stop caching static file
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/') # this decorator create the home route
def home ():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name = name, title = 'Home')

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name = name, title = 'About Us')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/post', methods=['GET', 'POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html', name=name, title=name)

    if request.method == 'POST':
        content = request.form['content']

        # Analyze text
        char_count = len(content)
        word_count = len(content.split())
        sentence_count = content.count('.') + content.count('!') + content.count('?')

        # Most frequent word
        words = [word.strip('.,!?";:') for word in content.lower().split() if word.strip('.,!?";:')]
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        most_frequent = ""
        freq = 0
        if word_freq:
            most_frequent = max(word_freq, key=word_freq.get)
            freq = word_freq[most_frequent]

        # Render result with data
        return render_template(
            'result.html',
            content=content,
            char_count=char_count,
            word_count=word_count,
            sentence_count=sentence_count,
            most_frequent=most_frequent,
            freq=freq,
            title="Analysis Result"
        )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)