import random
import time
import json
from datetime import datetime


class SensorSimulator:
    """
    This class simulates sensor data - like a thermometer that
    takes readings every few seconds
    """

    def __init__(self, sensor_type="temperature"):
        self.sensor_type = sensor_type
        self.current_value = 20.0  # Starting temperature

    def generate_reading(self):
        """
        Generate one sensor reading
        Think of this as taking one measurement
        """
        # Add some randomness (real sensors aren't perfectly stable)
        change = random.uniform(-0.5, 0.5)
        self.current_value += change

        # Keep temperature in realistic range
        if self.current_value < -10:
            self.current_value = -10
        elif self.current_value > 40:
            self.current_value = 40

        # Create a data point with timestamp
        reading = {
            "timestamp": datetime.now().isoformat(),
            "sensor_type": self.sensor_type,
            "value": round(self.current_value, 2),
            "sensor_id": "sensor_001"
        }

        return reading

    def stream_data(self, interval=1):
        """
        Continuously generate readings
        interval: seconds between readings
        """
        print(f"Starting {self.sensor_type} sensor stream...")
        print("Press Ctrl+C to stop")

        try:
            while True:
                reading = self.generate_reading()
                print(f"📊 {reading}")
                time.sleep(interval)

        except KeyboardInterrupt:
            print("\n🛑 Sensor stream stopped")


# Test the simulator
if __name__ == "__main__":
    sensor = SensorSimulator("temperature")
    sensor.stream_data(interval=2)  # New reading every 2 seconds