from flask import Flask, render_template, request

app = Flask(__name__)

def generate_custom_plan(weight, height):
    intensity = "High" if weight > 70 and height > 170 else "Moderate"
    return intensity

def calculate_bmi(weight, height):
    bmi = weight / (height / 100) ** 2
    return bmi

def evaluate_health_status(bmi):
    if bmi < 18.5:
        return "Subponderal", "Ai un indice de masă corporală subponderal. Consultă un specialist pentru a menține o greutate sănătoasă."
    elif 18.5 <= bmi < 24.9:
        return "Normal", "Felicitări! Ai un indice de masă corporală normal. Continuă să ai grijă de sănătatea ta."
    elif 25 <= bmi < 29.9:
        return "Supraponderal", "Ai un indice de masă corporală supraponderal. Explorează opțiuni pentru a menține o greutate sănătoasă."
    elif 30 <= bmi < 34.9:
        return "Obezitate gradul I", "Te afli în categoria de obezitate gradul I. Consultă un specialist pentru a-ți îmbunătăți sănătatea."
    elif 35 <= bmi < 39.9:
        return "Obezitate gradul II", "Te afli în categoria de obezitate gradul II. Acționează pentru a îmbunătăți starea ta de sănătate."
    else:
        return "Obezitate gradul III", "Ai un indice de masă corporală extrem de mare. Consultă imediat un specialist pentru asistență medicală."

def generate_exercises(intensity):
    if intensity == "High":
        return [
            "1. Sprints: Sprint for a short distance, then rest and repeat.",
            "2. Burpees: Combine a squat, push-up, and jump in one fluid motion.",
            "3. Box Jumps: Jump onto and off a sturdy box or platform.",
            "4. Skippings: Perform high-knee skipping in place for a cardio boost.",
            "5. Mountain Climbers: Start in a plank position and alternate bringing knees to the chest rapidly."
        ]
    elif intensity == "Moderate":
        return [
            "1. Brisk Walking: Walk at a brisk pace to elevate your heart rate.",
            "2. Cycling: Ride a bicycle at a moderate speed, either outdoors or on a stationary bike.",
            "3. Yoga: Engage in a yoga session focusing on flexibility and balance.",
            "4. Swimming: Swim laps at a steady pace for a full-body workout.",
            "5. Biking or Elliptical: Use a stationary bike or elliptical machine for low-impact cardio."
        ]
    else:
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_plan', methods=['POST'])
def generate_plan():
    if request.method == 'POST':
        age = request.form.get('age')
        height = request.form.get('height')
        weight = request.form.get('weight')

        custom_intensity = generate_custom_plan(float(weight), float(height))
        bmi = calculate_bmi(float(weight), float(height))
        health_status = evaluate_health_status(bmi)

        exercise_plan = {
            "age": age,
            "height": height,
            "weight": weight,
            "bmi": bmi,
            "exercise_type": "Cardio",
            "intensity": custom_intensity,
            "frequency": 3,
            "health_status": health_status,
            "exercises": generate_exercises(custom_intensity)
        }

        return render_template('result.html', exercise_plan=exercise_plan)

if __name__ == '__main__':
    app.run(debug=True)
