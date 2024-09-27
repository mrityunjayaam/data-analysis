import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class CovidDataAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("COVID-19 Data Analyzer")
        
        self.upload_button = tk.Button(root, text="Upload CSV", command=self.upload_csv)
        self.upload_button.pack(pady=20)

        self.state_button = tk.Button(root, text="Show Bar Graphs", command=self.show_statistics)
        self.state_button.pack(pady=20)

        self.data = None

    def upload_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                self.data = pd.read_csv(file_path)
                messagebox.showinfo("Success", "CSV file uploaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def show_statistics(self):
        if self.data is not None:
            required_columns = ['state', 'month', 'total_cases', 'total_deaths', 'total_recoveries']
            if all(col in self.data.columns for col in required_columns):
                self.plot_data()
            else:
                messagebox.showerror("Error", "CSV must contain 'state', 'month', 'total_cases', 'total_deaths', and 'total_recoveries' columns.")
        else:
            messagebox.showwarning("Warning", "No data uploaded!")

    def plot_data(self):
        states = ['Kerala', 'Karnataka', 'Andhra Pradesh', 'Tamil Nadu', 'Odisha','Nepal']
        months = self.data['month'].unique()

        for state in states:
            state_data = self.data[self.data['state'] == state]
            if not state_data.empty:
                # Create a single figure
                fig, ax = plt.subplots(figsize=(12, 6))

                # Set x positions for each month
                x = np.arange(len(state_data['month']))

                # Bar width
                width = 0.2

                # Bar graphs for total cases, deaths, and recoveries
                ax.bar(x - width, state_data['total_cases'], width, label='Total Cases', color='blue')
                ax.bar(x, state_data['total_deaths'], width, label='Total Deaths', color='red')
                ax.bar(x + width, state_data['total_recoveries'], width, label='Total Recoveries', color='green')

                # Title and labels
                ax.set_title(f"{state} - COVID-19 Statistics per Month")
                ax.set_xlabel("Month")
                ax.set_ylabel("Count")
                ax.set_xticks(x)
                ax.set_xticklabels(state_data['month'], rotation=45)
                ax.legend()
                plt.grid(axis='y')
                plt.tight_layout()
                plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = CovidDataAnalyzer(root)
    root.mainloop()
