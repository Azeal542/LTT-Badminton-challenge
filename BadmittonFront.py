import csv
import tkinter as tk
from tkinter import simpledialog, messagebox
import PlayerManagement

class BadmintonApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Badminton Challenge")
        self.geometry("300x150")

        add_player_btn = tk.Button(self, text="Add Player", command=self.open_add_player)
        add_player_btn.pack(pady=10)

        record_game_btn = tk.Button(self, text="Record Game", command=self.open_record_game)
        record_game_btn.pack(pady=10)

        show_data_btn = tk.Button(self, text="Show Player Data", command=self.show_player_data)
        show_data_btn.pack(pady=10)

    def open_add_player(self):
        def submit():
            name = name_entry.get()
            if name:
                PlayerManagement.create_user(name)
                messagebox.showinfo("Player Added", f"Player '{name}' added!")
                add_player_win.destroy()
            else:
                messagebox.showwarning("Input Error", "Please enter a name.")

        add_player_win = tk.Toplevel(self)
        add_player_win.title("Add Player")
        tk.Label(add_player_win, text="Player Name:").pack(padx=10, pady=5)
        name_entry = tk.Entry(add_player_win)
        name_entry.pack(padx=10, pady=5)
        tk.Button(add_player_win, text="Add", command=submit).pack(pady=10)

    def open_record_game(self):
        def submit():
            win = player1_entry.get()
            los = player2_entry.get()
            if win and los:
                try:
                    PlayerManagement.elo_calc(win, los)
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {e}")
                    return
                messagebox.showinfo("Game Recorded", f"Game between '{win}' and '{los}' recorded with winner '{win}'!")
                record_game_win.destroy()
            else:
                messagebox.showwarning("Input Error", "Check all fields.")

        record_game_win = tk.Toplevel(self)
        record_game_win.title("Record Game")
        tk.Label(record_game_win, text="Winner:").pack(padx=10, pady=5)
        player1_entry = tk.Entry(record_game_win)
        player1_entry.pack(padx=10, pady=5)
        tk.Label(record_game_win, text="Loser:").pack(padx=10, pady=5)
        player2_entry = tk.Entry(record_game_win)
        player2_entry.pack(padx=10, pady=5)
        tk.Button(record_game_win, text="Record", command=submit).pack(pady=10)
    
    def show_player_data(self):
        try:
            with open("Player sheet.csv", newline='') as csvfile:
                reader = csv.reader(csvfile)
                data = list(reader)
        except Exception as e:
            messagebox.showerror("Error", f"Could not read Player sheet.csv: {e}")
            return

        data_win = tk.Toplevel(self)
        data_win.title("Player Data")

        if not data:
            tk.Label(data_win, text="No data found.").pack(padx=10, pady=10)
            return

        for i, row in enumerate(data):
            for j, value in enumerate(row):
                e = tk.Label(data_win, text=value, borderwidth=1, relief="solid", padx=10, pady=5)
                e.grid(row=i, column=j, sticky="nsew")

if __name__ == "__main__":
    app = BadmintonApp()
    app.mainloop()