import math
import speedtest
from datetime import date, datetime

wifi = speedtest.Speedtest()

# Converting our measurement speeds from bits to mb's
def bytes_to_mb(size_bytes):

    # Mathematical logic
    i = int(math.floor(math.log(size_bytes, 1024)))
    power = math.pow(1024, i)
    size = round(size_bytes / power, 2)

    return f"{size} Mbps"

# Progress displaying, takes awhile to measure.
print("Measuring Download speed...")
download_speed = wifi.download()

print("Measuring Upload speed...")
upload_speed = wifi.upload()

# Displaying results
print("Download:", bytes_to_mb(download_speed))
print("Upload:", bytes_to_mb(upload_speed))

# Speedtest data collection and logging
def data_logging():
    with open("speedtest_log.txt", "a") as file:

        # Data aggregation, logging date, time, and speeds
        date_time = f"[{date.today():%d/%m/%Y}, {datetime.now():%H:%M}] "
        speeds = f"Down: {bytes_to_mb(download_speed)}, Up: {bytes_to_mb(upload_speed)}"

        # Writing log and appending to file.
        file.write(f"{date_time} {speeds} \n")
    print("Speed test logged.")

data_logging()