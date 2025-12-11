import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class MLGuiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Machine Learning Project GUI")
        self.root.geometry("500x400")

        self.df = None

        # Buttons
        tk.Button(root, text="Load Dataset", command=self.load_dataset).pack(pady=10)
        tk.Button(root, text="Show Head", command=self.show_head).pack(pady=10)
        tk.Button(root, text="Summary Stats", command=self.summary_stats).pack(pady=10)
        tk.Button(root, text="Plot Distribution", command=self.plot_distribution).pack(pady=10)
        tk.Button(root, text="Correlation Heatmap", command=self.corr_heatmap).pack(pady=10)
        tk.Button(root, text="Run ML Model", command=self.run_model).pack(pady=10)

    def load_dataset(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")]
        )
        if file_path:
            try:
                if file_path.endswith(".csv"):
                    self.df = pd.read_csv(file_path)
                else:
                    self.df = pd.read_excel(file_path)
                messagebox.showinfo("Success", "Dataset loaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load dataset: {e}")

    def show_head(self):
        if self.df is not None:
            print(self.df.head())
        else:
            messagebox.showwarning("Warning", "No dataset loaded!")

    def summary_stats(self):
        if self.df is not None:
            print(self.df.describe())
        else:
            messagebox.showwarning("Warning", "No dataset loaded!")

    def plot_distribution(self):
        if self.df is not None:
            col = self.ask_column()
            if col and col in self.df.columns:
                plt.figure(figsize=(6,4))
                sns.histplot(self.df[col], kde=True)
                plt.title(f"Distribution of {col}")
                plt.show()
        else:
            messagebox.showwarning("Warning", "No dataset loaded!")

    def corr_heatmap(self):
        if self.df is not None:
            plt.figure(figsize=(8,6))
            sns.heatmap(self.df.corr(), annot=True, cmap="coolwarm")
            plt.title("Correlation Heatmap")
            plt.show()
        else:
            messagebox.showwarning("Warning", "No dataset loaded!")

    def run_model(self):
        if self.df is not None:
            # Placeholder for ML logic
            messagebox.showinfo("ML Model", "Run your ML pipeline here!")
        else:
            messagebox.showwarning("Warning", "No dataset loaded!")

    def ask_column(self):
        # Simple input dialog for column name
        col_win = tk.Toplevel(self.root)
        col_win.title("Select Column")
        tk.Label(col_win, text="Enter column name:").pack(pady=5)
        col_entry = tk.Entry(col_win)
        col_entry.pack(pady=5)

        def submit():
            self.selected_col = col_entry.get()
            col_win.destroy()

        tk.Button(col_win, text="Submit", command=submit).pack(pady=5)
        self.root.wait_window(col_win)
        return getattr(self, "selected_col", None)

if __name__ == "__main__":
    root = tk.Tk()
    app = MLGuiApp(root)
    root.mainloop()