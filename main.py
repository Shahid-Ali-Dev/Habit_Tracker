import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
USERNAME = os.getenv("user")
TOKEN = os.getenv("token")
GRAPH_ID = "graph1"

BASE_URL = "https://pixe.la/v1/users"
HEADERS = {"X-USER-TOKEN": TOKEN}


def create_user():
    """Creates a new Pixela user account."""
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    res = requests.post(url=BASE_URL, json=user_params)
    print(f"[CREATE USER] {res.text}")


def create_graph(name="Sit Ups Graph", unit="Reps", graph_type="int", color="sora"):
    """Creates a new graph for tracking a habit."""
    graph_endpoint = f"{BASE_URL}/{USERNAME}/graphs"
    graph_config = {
        "id": GRAPH_ID,
        "name": name,
        "unit": unit,
        "type": graph_type,
        "color": color
    }
    res = requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS)
    print(f"[CREATE GRAPH] {res.text}")


def add_pixel(date=datetime.now(), quantity="15"):
    """Adds a habit entry for a specific date."""
    pixel_data = {
        "date": date.strftime("%Y%m%d"),
        "quantity": str(quantity)
    }
    pixel_url = f"{BASE_URL}/{USERNAME}/graphs/{GRAPH_ID}"
    res = requests.post(url=pixel_url, json=pixel_data, headers=HEADERS)
    print(f"[ADD PIXEL] {res.text}")


def update_pixel(date, quantity):
    """Updates an existing habit entry."""
    update_data = {"quantity": str(quantity)}
    update_url = f"{BASE_URL}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
    res = requests.put(url=update_url, json=update_data, headers=HEADERS)
    print(f"[UPDATE PIXEL] {res.text}")


def delete_pixel(date):
    """Deletes a habit entry."""
    delete_url = f"{BASE_URL}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
    res = requests.delete(url=delete_url, headers=HEADERS)
    print(f"[DELETE PIXEL] {res.text}")


if __name__ == "__main__":
    # Uncomment any operation you need:

    # create_user()
    # create_graph()

    today = datetime.now()

    # Add new pixel
    add_pixel(today, 20)

    # Update pixel (example date: "20250713")
    # update_pixel("20250713", 30)

    # Delete pixel
    # delete_pixel("20250713")
