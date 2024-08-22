from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the recommendations data
df = pd.read_csv('recommendations.csv')
df['title'] = df['title'].str.strip().str.lower()  # Normalize movie titles

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        movie_name = request.form.get('movie_name').strip().lower()  # Normalize input
        print(f"Searching for movie: {movie_name}")  # Debug print
        
        # Search for the movie in the DataFrame
        result = df[df['title'].str.contains(movie_name, case=False, regex=False, na=False)]
        if not result.empty:
            movie_data = result.iloc[0].to_dict()  # Convert Series to dictionary
            print(f"Found movie data: {movie_data}")  # Debug print
            return render_template('result.html', movie_data=movie_data)
        else:
            print("Movie not found in DataFrame")  # Debug print
            return render_template('index.html', error="Movie not found.")
    return render_template('index.html')

@app.route('/movies')
def movies():
    movie_titles = df['title'].tolist()
    return jsonify(movie_titles)

if __name__ == '__main__':
    app.run(debug=True)
