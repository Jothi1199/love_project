import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time
import random


class LoveApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Love Story ❤️")
        self.root.geometry("800x600")
        self.root.configure(bg="#ffe6f2")

        self.pages = []
        self.current_page = 0
        self.create_heart_animation()
        self.create_pages()
        self.show_page(0)



    # ------------------ HEART ANIMATION ------------------ #
    def create_heart_animation(self):
        self.canvas = tk.Canvas(self.root, bg="#ffe6f2", highlightthickness=0)
        self.canvas.place(relwidth=1, relheight=1)

        self.hearts = []
        for _ in range(20):
            x = random.randint(0, 900)
            y = random.randint(0, 650)
            heart = self.canvas.create_text(
                x, y, text="❤️", font=("Arial", random.randint(15, 25))
            )
            self.hearts.append(heart)

        self.animate_hearts()

    def animate_hearts(self):
        for heart in self.hearts:
            self.canvas.move(heart, 0, -2)
            x, y = self.canvas.coords(heart)
            if y < 0:
                self.canvas.coords(heart, random.randint(0, 900), 650)
        self.root.after(100, self.animate_hearts)

    def create_pages(self):
        # Page 1 - Welcome
        page1 = tk.Frame(self.root, bg="#ffe6f2")
        tk.Label(page1, text="Happy Valentine's Day ❤️",
                 font=("Helvetica", 24, "bold"),
                 bg="#ffe6f2", fg="#d63384").pack(pady=20)

        tk.Label(page1,
                 text="To My Loving Husband & My Sweet Son 💕",
                 font=("Helvetica", 18),
                 bg="#ffe6f2").pack(pady=10)

        self.pages.append(page1)

        # Page 2 - Husband Love
        page2 = tk.Frame(self.root, bg="#fff0f5")

        tk.Label(page2, text="My Dear Husband 💖",
                 font=("Helvetica", 22, "bold"),
                 bg="#fff0f5", fg="#c2185b").pack(pady=20)

        message = """You are my strength, my happiness,
my forever and always.
Since 16.11.2024 our reception,
and 17.11.2024 our marriage,
my life became complete.

Happy Birthday (02.12.1998) to the love of my life ❤️"""

        tk.Label(page2, text=message,
                 font=("Helvetica", 16),
                 bg="#fff0f5",
                 justify="center").pack(pady=20)

        self.pages.append(page2)

        # Page 3 - Son Love
        page3 = tk.Frame(self.root, bg="#e6f7ff")

        tk.Label(page3, text="My Little Prince 👶💙",
                 font=("Helvetica", 22, "bold"),
                 bg="#e6f7ff", fg="#0066cc").pack(pady=20)

        message2 = """My sweet baby boy ❤️
Born on 23.10.2025,
you are the greatest blessing in my life.

You made me a proud mother.
Happy Birthday my sunshine 🌞"""

        tk.Label(page3, text=message2,
                 font=("Helvetica", 16),
                 bg="#e6f7ff",
                 justify="center").pack(pady=20)

        self.pages.append(page3)

        # Page 4 - Important Dates
        page4 = tk.Frame(self.root, bg="#f9f2ff")

        tk.Label(page4, text="Our Beautiful Timeline 💕",
                 font=("Helvetica", 22, "bold"),
                 bg="#f9f2ff", fg="#800080").pack(pady=20)

        dates = """💍 Reception: 16.11.2024
💒 Marriage: 17.11.2024
🎂 Husband Birthday: 02.12.1998
🎂 My Birthday: 01.01.1999
👶 Son Birthday: 23.10.2025"""

        tk.Label(page4, text=dates,
                 font=("Helvetica", 16),
                 bg="#f9f2ff",
                 justify="center").pack(pady=20)

        self.pages.append(page4)

        # Page 5 - Photos
        page5 = tk.Frame(self.root, bg="#fff5e6")

        tk.Label(page5, text="My World 🌍❤️",
                 font=("Helvetica", 22, "bold"),
                 bg="#fff5e6", fg="#ff6600").pack(pady=20)

        try:
            husband_img = Image.open("husband.jpeg").resize((200, 250))
            son_img = Image.open("son.jpeg").resize((200, 250))

            self.husband_photo = ImageTk.PhotoImage(husband_img)
            self.son_photo = ImageTk.PhotoImage(son_img)

            tk.Label(page5, image=self.husband_photo, bg="#fff5e6").pack(side="left", padx=40)
            tk.Label(page5, image=self.son_photo, bg="#fff5e6").pack(side="right", padx=40)
        except:
            tk.Label(page5, text="Add husband.jpg and son.jpg to display photos ❤️",
                     font=("Helvetica", 14),
                     bg="#fff5e6").pack(pady=20)

        self.pages.append(page5)

        # Navigation Buttons
        nav_frame = tk.Frame(self.root, bg="#ffe6f2")
        nav_frame.pack(side="bottom", fill="x", pady=10)

        tk.Button(nav_frame, text="⬅ Previous", command=self.prev_page,
                  bg="#ff99cc", font=("Helvetica", 12)).pack(side="left", padx=20)

        tk.Button(nav_frame, text="Next ➡", command=self.next_page,
                  bg="#ff99cc", font=("Helvetica", 12)).pack(side="right", padx=20)

    def show_page(self, page_number):
        for page in self.pages:
            page.pack_forget()
        self.pages[page_number].pack(fill="both", expand=True)

    def next_page(self):
        if self.current_page < len(self.pages) - 1:
            self.current_page += 1
            self.show_page(self.current_page)

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.show_page(self.current_page)


if __name__ == "__main__":
    root = tk.Tk()
    app = LoveApp(root)
    root.mainloop()