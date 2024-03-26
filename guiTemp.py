import tkinter as tk
from folium import Map, Marker
from io import BytesIO
from PIL import Image, ImageTk


class MapWindow(tk.Tk):
    def __init__(self, locations):
        super().__init__()
        self.title("Interactive OpenStreetMap")
        self.locations = locations
        self.zoom_level = 2

        # Create the initial map
        self.create_map()

    def create_map(self):
        # Create a Folium Map
        self.m = Map(location=[0, 0], zoom_start=self.zoom_level)

        # Add markers for each location
        for loc in self.locations:
            Marker(
                location=loc,
                popup="Marker",
                tooltip="Click me!"
            ).add_to(self.m)

        # Convert the Folium map to an image
        img_data = self.m._to_png()
        img = Image.open(BytesIO(img_data))

        # Convert the image to Tkinter format
        self.img_tk = ImageTk.PhotoImage(img)

        # Create a label to display the map image
        self.label = tk.Label(self, image=self.img_tk)
        self.label.pack()

        # Create zoom in button
        self.zoom_in_button = tk.Button(self, text="Zoom In", command=self.zoom_in)
        self.zoom_in_button.pack(side=tk.LEFT, padx=10)

        # Create zoom out button
        self.zoom_out_button = tk.Button(self, text="Zoom Out", command=self.zoom_out)
        self.zoom_out_button.pack(side=tk.LEFT, padx=10)

    def zoom_in(self):
        self.zoom_level += 1
        self.update_map()

    def zoom_out(self):
        if self.zoom_level > 1:
            self.zoom_level -= 1
            self.update_map()

    def update_map(self):
        # Update the map with new zoom level
        self.m.options['zoom'] = self.zoom_level

        # Update markers
        self.m = Map(location=[0, 0], zoom_start=self.zoom_level)
        for loc in self.locations:
            Marker(
                location=loc,
                popup="Marker",
                tooltip="Click me!"
            ).add_to(self.m)

        # Convert the updated Folium map to an image
        img_data = self.m._to_png()
        img = Image.open(BytesIO(img_data))

        # Convert the updated image to Tkinter format
        self.img_tk = ImageTk.PhotoImage(img)

        # Update the label with the new map image
        self.label.config(image=self.img_tk)


# Example usage
if __name__ == "__main__":
    # Example locations
    locations = [
        (37.7749, -122.4194),  # San Francisco
        (34.0522, -118.2437),  # Los Angeles
        (40.7128, -74.0060)  # New York
    ]

    # Create and run the MapWindow
    app = MapWindow(locations)
    app.mainloop()
