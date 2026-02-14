import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import datetime
import random
import pygame
import os

# ------------------ IMPORTANT DATES ------------------ #
RECEPTION_DATE = datetime.date(2024, 11, 16)
MARRIAGE_DATE = datetime.date(2024, 11, 17)
HUSBAND_BDAY = datetime.date(1998, 12, 2)
MY_BDAY = datetime.date(1999, 1, 1)
SON_BDAY = datetime.date(2025, 10, 23)

# ------------------ MAIN CLASS ------------------ #
class LoveApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Forever Love ❤️")
        self.root.geometry("900x650")
        self.root.configure(bg="#ffe6f2")

        pygame.mixer.init()
        if os.path.exists("music.mpeg"):
            pygame.mixer.music.load("music.mpeg")
            pygame.mixer.music.play(-1)

        self.create_heart_animation()
        self.create_main_content()

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

    # ------------------ MAIN CONTENT ------------------ #
    def create_main_content(self):
        self.frame = tk.Frame(self.root, bg="#ffffff", bd=5)
        self.frame.place(relx=0.5, rely=0.5, anchor="center", width=750, height=550)

        title = tk.Label(
            self.frame,
            text="My Beautiful Family 💕",
            font=("Helvetica", 24, "bold"),
            bg="#ffffff",
            fg="#d63384",
        )
        title.pack(pady=10)

        self.message = tk.Label(
            self.frame,
            text="You both are my heart, my world, my everything ❤️",
            font=("Helvetica", 16),
            bg="#ffffff",
        )
        self.message.pack(pady=10)

        self.counter_label = tk.Label(
            self.frame,
            font=("Helvetica", 14),
            bg="#ffffff",
            fg="#800080",
        )
        self.counter_label.pack(pady=10)

        self.update_counters()

        # Slideshow
        self.image_label = tk.Label(self.frame, bg="#ffffff")
        self.image_label.pack(pady=10)

        self.photos = []
        for file in ["husband.jpg", "husband1.jpg", "son.jpg", "son1.jpg"]:
            if os.path.exists(file):
                img = Image.open(file).resize((300, 350))
                self.photos.append(ImageTk.PhotoImage(img))

        self.photo_index = 0
        self.start_slideshow()

        love_note = """
My Dear Husband 💖
You are my strength and forever love.
Since 2016,
my life became magical.

My Little Prince 👶💙
Born on 23.10.2025,
you are my greatest blessing.

I love you both endlessly ❤️
        """

        note_label = tk.Label(
            self.frame,
            text=love_note,
            font=("Helvetica", 14),
            bg="#ffffff",
            justify="center",
        )
        note_label.pack(pady=10)

    # ------------------ COUNTERS ------------------ #
    def update_counters(self):
        today = datetime.date.today()
        days_married = (today - MARRIAGE_DATE).days

        husband_next = HUSBAND_BDAY.replace(year=today.year)
        if husband_next < today:
            husband_next = husband_next.replace(year=today.year + 1)

        son_next = SON_BDAY.replace(year=today.year)
        if son_next < today:
            son_next = son_next.replace(year=today.year + 1)

        reception_next = RECEPTION_DATE.replace(year=today.year)
        if reception_next < today:
            reception_next = reception_next.replace(year=today.year + 1)

        text = f"""
💍 Married for: {days_married} days
🎂 Husband Birthday in: {(husband_next - today).days} days
👶 Son Birthday in: {(son_next - today).days} days
💒 Reception Anniversary in: {(reception_next - today).days} days
        """

        self.counter_label.config(text=text)
        self.root.after(86400000, self.update_counters)

    # ------------------ SLIDESHOW ------------------ #
    def start_slideshow(self):
        if self.photos:
            self.image_label.config(image=self.photos[self.photo_index])
            self.photo_index = (self.photo_index + 1) % len(self.photos)
        self.root.after(3000, self.start_slideshow)


if __name__ == "__main__":
    root = tk.Tk()
    app = LoveApp(root)
    root.mainloop()