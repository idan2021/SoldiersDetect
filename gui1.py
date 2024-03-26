import tkinter as tk
from tkinter import ttk
import folium
from folium.plugins import MarkerCluster

def commit_report():
    # This function will be called when the "Commit Report" button is clicked
    # You can implement the functionality to save the report here
    print("Report Committed")

def show_map_with_comments():
    # Create a Tkinter window
    window = tk.Tk()
    window.title("Map with Comments")

    # Create a Frame to hold the map and the button
    frame = ttk.Frame(window)
    frame.grid(row=0, column=0, sticky="nsew")

    # Create a Folium Map
    m = folium.Map(location=[37.7749, -122.4194], zoom_start=10)

    # Add marker with popup
    tooltip = "Click me!"
    folium.Marker(
        location=[37.7749, -122.4194],
        popup="<b>Comment:</b> This is a comment",
        tooltip=tooltip
    ).add_to(m)

    # Add Marker Cluster to the map
    marker_cluster = MarkerCluster().add_to(m)

    # Add map to the frame
    map_frame = ttk.Frame(frame)
    map_frame.grid(row=0, column=0, padx=10, pady=10)
    map_html = m.repr_html()

    browser = ttk.Label(map_frame)
    browser.grid(row=0, column=0)
    browser.configure(text=map_html)

    # Create a "Commit Report" button
    commit_button = ttk.Button(frame, text="Commit Report", command=commit_report)
    commit_button.grid(row=1, column=0, pady=10)

    # Start the Tkinter event loop
    window.mainloop()

#if _name_ == "_main_":
show_map_with_comments()