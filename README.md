# Movie Recommendation System

## Overview

This project is a movie recommendation system built using Flask for the backend and HTML/CSS/JavaScript for the frontend. It allows users to input a movie name and receive recommendations based on a precomputed dataset of movie ratings.

## Features

- **Search for Movies**: Users can enter a movie name to search for it.
- **Movie Recommendations**: Based on the input movie, the system provides recommendations for similar movies.
- **Autocomplete Search**: Integrated autocomplete for movie names to improve user experience.
- **Responsive Design**: The application is designed to be responsive and accessible on various devices.

## Project Structure

- `app.py`: Flask application for handling routes and logic.
- `recommendations.csv`: Precomputed movie recommendations data.
- `templates/index.html`: Main page where users can input movie names.
- `templates/result.html`: Page displaying recommended movies based on user input.

## Setup

### Prerequisites

- Python 3.x
- Flask
- Pandas

## Usage
- On the main page (/), enter a movie name and click "Get Recommendations."
- The system will display a list of recommended movies based on the input movie.

## Contributing
Feel free to submit issues or pull requests if you have suggestions or improvements for the project.
