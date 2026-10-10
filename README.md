
# UK Traffic Accident Analysis & Severity Prediction

**Final Year Project | BSc (Hons) Computer Science | Nottingham Trent University | 2025**

## Project Overview

This project explores UK road traffic accident data using Python, data visualisation and machine learning. The aim was to develop an interactive application that allows users to identify accident patterns, investigate contributing factors and predict accident severity.

The system combines a Tkinter graphical user interface, Matplotlib visualisations and a Random Forest classification model.

## Key Results

- **Random Forest model accuracy: 75.82%** (as reported in the final-year project).
- Developed an interactive Python application for exploring traffic accident statistics.
- Analysed accident trends by month, day, time, weather conditions and speed limits.
- Implemented user-input-based accident severity predictions.
- Applied the CRISP-DM methodology throughout the project.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core application development |
| Pandas | Data cleaning and manipulation |
| NumPy | Numerical processing |
| Matplotlib | Data visualisation |
| Scikit-learn | Random Forest model development and evaluation |
| Tkinter | Graphical user interface |
| CSV | Storage and loading of historical accident data |

## Features

### 1. Data Cleaning and Preparation
- Processed UK government road traffic accident data.
- Handled missing values and inconsistent records.
- Prepared variables for analysis and machine learning.

### 2. Interactive Data Visualisation
Created visualisations to explore:
- Accidents by month and day of the week.
- Accident frequency by time of day.
- Distribution of accident severity.
- Accidents by speed limit and number of casualties.
- Weather conditions and accident trends.

### 3. Accident Severity Prediction
- Developed a Random Forest classification model using Scikit-learn.
- Used historical accident data to train and evaluate the model.
- Allowed users to enter accident conditions through the graphical interface.
- Displayed predicted severity results.

## Dataset

The project uses historical UK road collision data from the Department for Transport, including the 2023 road casualty statistics dataset.

## Project Structure

- `main.py` — Main application entry point.
- `accident_functions.py` — Accident data analysis and visualisation functions.
- `predictions_functions.py` — Machine learning prediction functions.
- `data/` — Road accident dataset, where applicable.

## Methodology

The project followed the **CRISP-DM** framework:

1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Modelling
5. Evaluation
6. Deployment

## Limitations and Future Improvements

- The model achieved 75.82% accuracy, leaving room for improvement.
- Historical data limits the ability to make real-time predictions.
- Further model tuning and additional datasets could improve performance.
- Future development could explore alternative algorithms and real-time traffic data integration.

## Skills Demonstrated

Python Programming | Data Cleaning | Exploratory Data Analysis | Data Visualisation | Machine Learning | Model Evaluation | GUI Development | CRISP-DM

## Author

Developed as a final-year Computer Science project at Nottingham Trent University in 2025.
  
