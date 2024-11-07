import tkinter as tk
from tkinter import ttk
import random
import math

class Building:
    def __init__(self, x, y, width, height, building_type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.building_type = building_type

class CityBuilder(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Procedural Fantasy City Builder")
        self.geometry("800x600")

        self.canvas = tk.Canvas(self, width=600, height=650)
        self.canvas.pack(side=tk.LEFT, padx=20, pady=20)

        self.control_panel = tk.Frame(self)
        self.control_panel.pack(side=tk.LEFT, padx=20, pady=20)

        self.generate_button = ttk.Button(self.control_panel, text="Generate City", command=self.generate_city)
        self.generate_button.pack(pady=10)

        self.city_size_label = ttk.Label(self.control_panel, text="City Size:")
        self.city_size_label.pack(pady=5)

        self.city_size_slider = ttk.Scale(self.control_panel, from_=50, to=200, orient=tk.HORIZONTAL, command=self.update_city_size)
        self.city_size_slider.set(100)
        self.city_size_slider.pack(pady=5)

        self.generate_city()

    def generate_city(self, event=None):
        self.canvas.delete("building")
        city_size = int(self.city_size_slider.get())
        buildings = self.generate_buildings(city_size)
        for building in buildings:
            self.draw_building(building)

    def generate_buildings(self, city_size):
        buildings = []
        for i in range(city_size):
            for j in range(city_size):
                building_type = random.choice(["house", "shop", "temple", "castle"])
                width = random.randint(10, 50)
                height = random.randint(10, 50)
                x = i * (width + 5) + random.randint(0, 5)
                y = j * (height + 5) + random.randint(0, 5)
                building = Building(x, y, width, height, building_type)
                buildings.append(building)
        return buildings

    def draw_building(self, building):
        building_colors = {
            "house": "#8B4513",
            "shop": "#FF7F50",
            "temple": "#FFD700",
            "castle": "#A9A9A9"
        }
        color = building_colors[building.building_type]
        self.canvas.create_rectangle(building.x, building.y, building.x + building.width, building.y + building.height, fill=color, tags="building")

    def update_city_size(self, value):
        self.generate_city()
#////////////////////////////
if __name__ == "__main__":
    app = CityBuilder()

    app.mainloop()
