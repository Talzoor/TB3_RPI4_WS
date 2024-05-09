import requests
import datetime
import subprocess

def get_system_time(internet_time_var):
    return datetime.datetime.now(internet_time_var.tzinfo)

def get_internet_time():
    try:
        # Fetch current time from an internet time API
        response = requests.get("http://worldtimeapi.org/api/ip")
        if response.status_code == 200:
            data = response.json()
            internet_time_str = data['datetime']
            internet_time = datetime.datetime.strptime(internet_time_str, '%Y-%m-%dT%H:%M:%S.%f%z')
            return internet_time
        else:
            print("Failed to fetch internet time. Status code:", response.status_code)
            return None
    except Exception as e:
        print("Error fetching internet time:", e)
        return None

def update_system_time(internet_time):
    try:
        # Update system time using subprocess
        subprocess.run(['sudo', 'date', '-s', internet_time.strftime('%Y-%m-%d %H:%M:%S')])
        print("System time updated successfully.")
    except Exception as e:
        print("Error updating system time:", e)

def main():
    internet_time = get_internet_time()
    if internet_time:
        system_time = datetime.datetime.now(internet_time.tzinfo)
        print("Internet time:", internet_time)
        print("System time:", system_time)
        if internet_time != system_time:
            update_system_time(internet_time)
    else:
        print("Failed to retrieve internet time.")

if __name__ == "__main__":
    main()
