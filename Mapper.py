import serial
import time
import matplotlib.pyplot as plt
import numpy as np

# Initialize serial connection to Arduino
ser = serial.Serial('COM3', 9600)  # Adjust 'COM3' to your Arduino's port
time.sleep(2)  # Give time for the connection to initialize

# Variables to store positions and depths
positions = []
depths = []

def start_measurement():
    ser.write(b'start\n')
    print("Measurement started")

def fire_measurement():
    depth_readings = []
    lat_readings = []
    lon_readings = []
    
    for _ in range(5):  # Take 5 readings for averaging
        ser.write(b'fire\n')
        line = ser.readline().decode().strip()
        if "Depth:" in line:
            parts = line.split(";")
            depth = float(parts[0].split(":")[1].strip())
            coordinates = parts[1].split(":")[1].strip()
            lat, lon = map(float, coordinates.split(","))
            
            depth_readings.append(depth)
            lat_readings.append(lat)
            lon_readings.append(lon)
        
        time.sleep(0.5)  # Slight delay to allow for stable measurements

    # Calculate averages
    avg_depth = sum(depth_readings) / len(depth_readings)
    avg_lat = sum(lat_readings) / len(lat_readings)
    avg_lon = sum(lon_readings) / len(lon_readings)
    
    positions.append((avg_lat, avg_lon))
    depths.append(avg_depth)
    print(f"Averaged Coordinates ({avg_lat}, {avg_lon}): Averaged Depth {avg_depth} cm")

def end_measurement():
    ser.write(b'end\n')
    print("Measurement ended")

def create_depth_map():
    # Prepare positions for plotting
    latitudes = [pos[0] for pos in positions]
    longitudes = [pos[1] for pos in positions]
    
    # Create a grid based on unique coordinates
    unique_lat = sorted(set(latitudes))
    unique_lon = sorted(set(longitudes))
    
    lat_map = {lat: i for i, lat in enumerate(unique_lat)}
    lon_map = {lon: i for i, lon in enumerate(unique_lon)}
    
    grid_size = (len(unique_lat), len(unique_lon))
    depth_map = np.zeros(grid_size)

    for (lat, lon), depth in zip(positions, depths):
        x = lat_map[lat]
        y = lon_map[lon]
        depth_map[x, y] = depth

    depth_map = depth_map.T
    
    # Plot the depth map
    plt.imshow(depth_map, cmap='coolwarm', origin='lower', vmin=0, vmax=max(depths))
    plt.colorbar(label="Depth (cm)")
    plt.xlabel("Latitude Index")
    plt.ylabel("Longitude Index")
    plt.title("2D Depth Map of Water Body")
    plt.show()

# Start measurements
start_measurement()

try:
    while True:  # Continuously take measurements until interrupted
        fire_measurement()
except KeyboardInterrupt:
    end_measurement()
    print("\nMeasurement loop interrupted by user.")

# Generate the depth map after all measurements
create_depth_map()

# Close the serial connection
ser.close()
