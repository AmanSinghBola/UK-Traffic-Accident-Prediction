import tkinter as tk
from tkinter import ttk, messagebox
from accident_functions import *
from predictions_functions import train_random_forest, predict_severity
import pandas as pd

class AccidentAnalysisApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Traffic Accident Data Analysis Tool")
        self.geometry('800x600')
        self.configure(background='lightblue')

        # Load the traffic data
        self.df_traffic = load_and_clean_data('data/dft-road-casualty-statistics-collision-provisional-mid-year-unvalidated-2023.csv')

        self.style = ttk.Style()
        self.style.configure('Red.TButton', background='#ff6347', foreground='black')

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Select a graph type:", bg='lightblue', fg='black', font=("Arial", 12))
        self.label.pack(pady=10)

        self.graph_options = [
            "Select Graphs", "Accidents by Month", "Accidents by Day of Week", "Accidents by Hour",
            "Accidents by Severity", "Accidents by Road Type", "Accidents by Weather",
            "Accidents by Speed Limit", "Accidents by Casualties", "Accidents by Day and Weather",
            "Predict Severity (Random Forest)"
        ]
        self.graph_type_var = tk.StringVar(self)
        self.graph_type_var.set(self.graph_options[0])  # Default to "Select Graphs"

        self.graph_type_menu = ttk.OptionMenu(self, self.graph_type_var, *self.graph_options)
        self.graph_type_menu.pack(pady=10)

        self.plot_button = ttk.Button(self, text="Plot Graph", command=self.plot_graph, style='Red.TButton')
        self.plot_button.pack(pady=10)

        self.exit_button = ttk.Button(self, text="Exit", command=self.destroy, style='Red.TButton')
        self.exit_button.pack(pady=10)

    def plot_graph(self):
        graph_type = self.graph_type_var.get()

        if graph_type == "Accidents by Month":
            plot_accidents_by_month(self.df_traffic)
        elif graph_type == "Accidents by Day of Week":
            plot_accidents_by_day_of_week(self.df_traffic)
        elif graph_type == "Accidents by Hour":
            plot_accidents_by_hour(self.df_traffic)
        elif graph_type == "Accidents by Severity":
            plot_accidents_by_severity(self.df_traffic)
        elif graph_type == "Accidents by Road Type":
            plot_accidents_by_road_type(self.df_traffic)
        elif graph_type == "Accidents by Weather":
            plot_accidents_by_weather(self.df_traffic)
        elif graph_type == "Accidents by Speed Limit":
            plot_accidents_by_speed_limit(self.df_traffic)
        elif graph_type == "Accidents by Casualties":
            plot_accidents_by_casualties(self.df_traffic)
        elif graph_type == "Accidents by Day and Weather":
            plot_accidents_by_day_and_weather(self.df_traffic)
        elif graph_type == "Predict Severity (Random Forest)":
            self.run_random_forest()

    def run_random_forest(self):
        def submit_prediction():
            try:
                input_data = pd.DataFrame([{
                    'weather_conditions': weather_var.get(),
                    'speed_limit': int(speed_entry.get()),
                    'hour': int(hour_entry.get()),
                    'day_of_week': day_map[day_var.get()],
                    'road_type': road_var.get()
                }])

                model = train_random_forest(self.df_traffic)
                prediction = predict_severity(model, input_data)
                messagebox.showinfo("Prediction Result", f"Predicted Severity: {prediction}")
                input_window.destroy()

            except Exception as e:
                messagebox.showerror("Input Error", str(e))

        # Mapping day names to numbers
        day_map = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}

        input_window = tk.Toplevel(self)
        input_window.title("Enter Accident Conditions")
        input_window.geometry("400x400")
        input_window.configure(background='lightblue')

        # Weather dropdown
        tk.Label(input_window, text="Weather Conditions:", bg='lightblue').pack(pady=5)
        weather_var = tk.StringVar()
        weather_choices = [
            'Fine without high winds', 'Raining without high winds',
            'Snowing without high winds', 'Fine with high winds',
            'Raining with high winds', 'Other'
        ]
        weather_var.set(weather_choices[0])
        tk.OptionMenu(input_window, weather_var, *weather_choices).pack()

        # Road type dropdown
        tk.Label(input_window, text="Road Type:", bg='lightblue').pack(pady=5)
        road_var = tk.StringVar()
        road_choices = ['Single carriageway', 'Dual carriageway', 'Roundabout', 'One way street', 'Other']
        road_var.set(road_choices[0])
        tk.OptionMenu(input_window, road_var, *road_choices).pack()

        # Day of week dropdown
        tk.Label(input_window, text="Day of Week:", bg='lightblue').pack(pady=5)
        day_var = tk.StringVar()
        day_choices = list(day_map.keys())
        day_var.set(day_choices[0])
        tk.OptionMenu(input_window, day_var, *day_choices).pack()

        # Speed limit entry
        tk.Label(input_window, text="Speed Limit (e.g. 30):", bg='lightblue').pack(pady=5)
        speed_entry = tk.Entry(input_window)
        speed_entry.pack()

        # Hour entry
        tk.Label(input_window, text="Hour of Day (0–23):", bg='lightblue').pack(pady=5)
        hour_entry = tk.Entry(input_window)
        hour_entry.pack()

        # Submit button
        tk.Button(input_window, text="Predict Severity", command=submit_prediction, bg='#ff6347', fg='black').pack(
            pady=20)


if __name__ == "__main__":
    app = AccidentAnalysisApp()
    app.mainloop()
