
import random
from datetime import datetime


def read_sensor_data():
    """Generate simulated sensor readings for Aerolytix."""

    return {
        "timestamp": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "MQ2": round(random.uniform(100, 500), 2),
        "MQ3": round(random.uniform(100, 500), 2),
        "MQ7": round(random.uniform(100, 500), 2),
        "MQ135": round(random.uniform(100, 500), 2),
        "temperature": round(random.uniform(25, 35), 2),
        "humidity": round(random.uniform(40, 75), 2),
    }


if __name__ == "__main__":
    print(read_sensor_data())
