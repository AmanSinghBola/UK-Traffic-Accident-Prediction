import pandas as pd
import matplotlib.pyplot as plt

# Load and clean data
def load_and_clean_data(filepath):
    """Loads the dataset and performs basic cleaning."""
    # Load the dataset
    df = pd.read_csv(filepath)

    # Drop rows where location data (longitude and latitude) is missing
    df.dropna(subset=['longitude', 'latitude'], inplace=True)

    # Convert 'date' column to datetime format
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Extract month and day of the week
    df['month'] = df['date'].dt.month
    df['day_of_week'] = df['date'].dt.dayofweek  # 0 = Monday, 6 = Sunday

    # Convert 'time' to datetime and extract hour
    if 'time' in df.columns:
        df['hour'] = pd.to_datetime(df['time'], format='%H:%M', errors='coerce').dt.hour

    return df

# Existing plot functions
def plot_accidents_by_month(df):
    """Plots the number of accidents by month (Bar Chart)."""
    accidents_per_month = df.groupby('month').size()

    plt.figure(figsize=(10, 5))
    accidents_per_month.plot(kind='bar', color='lightblue')
    plt.title("Number of Accidents Per Month in 2023")
    plt.xlabel("Month")
    plt.ylabel("Number of Accidents")
    plt.xticks(ticks=range(12),
               labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.show()

def plot_accidents_by_day_of_week(df):
    """Plots the number of accidents by day of the week (Bar Chart)."""
    accidents_per_day = df.groupby('day_of_week').size()

    plt.figure(figsize=(8, 5))
    accidents_per_day.plot(kind='bar', color='orange')
    plt.title("Number of Accidents Per Day of the Week")
    plt.xlabel("Day of the Week")
    plt.ylabel("Number of Accidents")
    plt.xticks(ticks=range(7), labels=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    plt.show()

def plot_accidents_by_hour(df):
    """Plots the number of accidents by hour of the day (Bar Chart)."""
    if 'hour' in df.columns:
        accidents_per_hour = df.groupby('hour').size()

        plt.figure(figsize=(10, 5))
        accidents_per_hour.plot(kind='bar', color='green')
        plt.title("Number of Accidents Per Hour of the Day")
        plt.xlabel("Hour of the Day")
        plt.ylabel("Number of Accidents")
        plt.show()
    else:
        print("No time data available to plot accidents by hour.")

# New plot functions with different chart types
def plot_accidents_by_severity(df):
    """Plots the number of accidents by severity (Pie Chart)."""
    accidents_by_severity = df['legacy_collision_severity'].value_counts()

    plt.figure(figsize=(10, 5))
    plt.pie(accidents_by_severity, labels=accidents_by_severity.index, autopct='%1.1f%%', colors=['red', 'blue', 'green'])
    plt.title('Accidents by Severity')
    plt.show()

def plot_accidents_by_road_type(df):
    """Plots the number of accidents by road type (Pie Chart)."""
    accidents_by_road_type = df['road_type'].value_counts()

    plt.figure(figsize=(10, 5))
    plt.pie(accidents_by_road_type, labels=accidents_by_road_type.index, autopct='%1.1f%%', colors=['purple', 'yellow', 'pink', 'cyan', 'orange'])
    plt.title('Accidents by Road Type')
    plt.show()

def plot_accidents_by_weather(df):
    """Plots the number of accidents by weather conditions (Bar Chart)."""
    accidents_by_weather = df['weather_conditions'].value_counts()

    plt.figure(figsize=(10, 5))
    accidents_by_weather.plot(kind='bar', color='blue')
    plt.title('Accidents by Weather Conditions')
    plt.xlabel('Weather Conditions')
    plt.ylabel('Number of Accidents')
    plt.show()

def plot_accidents_by_speed_limit(df):
    """Plots the number of accidents by speed limit (Scatter Plot)."""
    accidents_by_speed_limit = df['speed_limit'].value_counts()

    plt.figure(figsize=(10, 5))
    plt.scatter(accidents_by_speed_limit.index, accidents_by_speed_limit.values, color='orange')
    plt.title('Accidents by Speed Limit')
    plt.xlabel('Speed Limit')
    plt.ylabel('Number of Accidents')
    plt.show()

def plot_accidents_by_casualties(df):
    """Plots the number of accidents by number of casualties (Line Plot)."""
    accidents_by_casualties = df['number_of_casualties'].value_counts().sort_index()

    plt.figure(figsize=(10, 5))
    accidents_by_casualties.plot(kind='line', color='brown')
    plt.title('Accidents by Number of Casualties')
    plt.xlabel('Number of Casualties')
    plt.ylabel('Number of Accidents')
    plt.show()

def plot_accidents_by_day_and_weather(df):
    """Plots the number of accidents by day of the week and weather conditions (Stacked Bar Chart)."""
    accidents_by_day_and_weather = df.groupby(['day_of_week', 'weather_conditions']).size().unstack()

    accidents_by_day_and_weather.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='rainbow')
    plt.title('Accidents by Day of Week and Weather Conditions')
    plt.xlabel('Day of the Week')
    plt.ylabel('Number of Accidents')
    plt.xticks(ticks=range(7), labels=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    plt.show()
