  
from status_monitor import Status_Monitor


if __name__ == "__main__":
    url = "https://catfact.ninja/fact"
    Monitor_the_status = Status_Monitor()
    result = Monitor_the_status.get(url)
    print(result)
