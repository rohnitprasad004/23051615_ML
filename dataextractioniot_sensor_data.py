import time
import random
import pandas as pd
from datetime import datetime

# -----------------------------
# Simulated IoT Sensors
# -----------------------------

def read_temperature():
    return round(random.uniform(20.0, 35.0), 2)

def read_humidity():
    return round(random.uniform(40.0, 90.0), 2)

def read_light_intensity():
    return random.randint(100, 800)

def read_motion():
    return random.choice([0, 1])  # 1 = motion detected, 0 = no motion


# -----------------------------
# Collect Data
# -----------------------------

data_list = []

print("Collecting IoT sensor data...")

for i in range(20):  # reading 20 samples
    data = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Temperature(C)": read_temperature(),
        "Humidity(%)": read_humidity(),
        "Light_Intensity(lx)": read_light_intensity(),
        "Motion": read_motion()
    }
    
    print(data)
    data_list.append(data)

    time.sleep(1)  # simulate 1 sec sensor reading


# Convert to DataFrame
df = pd.DataFrame(data_list)

# Save to CSV
df.to_csv("iot_sensor_data.csv", index=False)

print("\nData saved to: iot_sensor_data.csv")
