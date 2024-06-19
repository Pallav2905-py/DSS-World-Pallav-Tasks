import random
import time
import sqlite3


class PassengerCounter:
    def __init__(self):
        self.passenger_count = 0
        self.infant_count = 0
        self.conn = sqlite3.connect("passenger_data.db")
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS counts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    passenger_count INTEGER NOT NULL,
                    infant_count INTEGER NOT NULL
                )
            """
            )

    def detect_passenger(self):
        # Simulate passenger detection (1 means passenger detected, 0 means no passenger)
        return random.choice([0, 1])

    def detect_infant(self):
        # Simulate infant detection (1 means infant detected, 0 means no infant)
        return random.choice([0, 1])

    def update_counts(self):
        if self.detect_passenger():
            self.passenger_count += 1
        if self.detect_infant():
            self.infant_count += 1
        self.store_counts()
        return self.passenger_count, self.infant_count

    def store_counts(self):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with self.conn:
            self.conn.execute(
                """
                INSERT INTO counts (timestamp, passenger_count, infant_count)
                VALUES (?, ?, ?)
            """,
                (timestamp, self.passenger_count, self.infant_count),
            )

    def close(self):
        self.conn.close()


counter = PassengerCounter()

# Simulate data collection
try:
    for _ in range(100):  # Simulate 100 detection attempts
        passenger_count, infant_count = counter.update_counts()
        print(f"Passenger count: {passenger_count}, Infant count: {infant_count}")
        time.sleep(0.1)  # Simulate time delay between detections
finally:
    counter.close()