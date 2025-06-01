from flask import Flask, render_template
import random
from questions import questions

app = Flask(__name__)

@app.route('/')
def index():
    # Вопрос 1 из ПАХТ
    q1_discipline = 'ПАХТ'
    q1 = random.choice(questions[q1_discipline])
    q1_number = q1.split('. ')[0]
    q1_text = q1[len(q1_number) + 2:]

    # Вопрос 2 из МАХП
    q2_discipline = 'МАХП'
    q2 = random.choice(questions[q2_discipline])
    q2_number = q2.split('. ')[0]
    q2_text = q2[len(q2_number) + 2:]

    # Вопрос 3 из других дисциплин
    excluded = ['ПАХТ', 'МАХП']
    other_disciplines = [d for d in questions if d not in excluded]
    q3_discipline = random.choice(other_disciplines)
    q3 = random.choice(questions[q3_discipline])
    q3_number = q3.split('. ')[0]
    q3_text = q3[len(q3_number) + 2:]

    return render_template('index.html',
                           q1_number=q1_number, q1_text=q1_text, q1_discipline=q1_discipline,
                           q2_number=q2_number, q2_text=q2_text, q2_discipline=q2_discipline,
                           q3_number=q3_number, q3_text=q3_text, q3_discipline=q3_discipline)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
