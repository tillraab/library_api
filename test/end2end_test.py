
"""End-to-end test for the Books API.

Use the tasks to build and run the Docker container before executing this script.
"""
import requests
print("\n Checking if the API is running...")
response = requests.get("http://127.0.0.1:8000/")
print("Status code:", response.status_code)
print("Response JSON:", response.json())

print("\n Running general GET request to /library endpoint...")
response = requests.get("http://127.0.0.1:8000/library")
print("Status code:", response.status_code)
print("Response JSON:", response.json())

print("\n Running specific GET request to /library endpoint...")
response = requests.get("http://127.0.0.1:8000/library", params={"author": "J.K. Rowling"})
print("Status code:", response.status_code)
print("Response JSON:", response.json())

print("\n Running PUT request to /library endpoint...")
response = requests.post("http://127.0.0.1:8000/library", json={
    "author": "T. Raab",
    "name": "My Book"
})
print("Status code:", response.status_code)
print("Response JSON:", response.json())

print("\n Running specific GET request to to verify successful PUT request...")
response = requests.get("http://127.0.0.1:8000/library", params={"author": "T. R"})
print("Status code:", response.status_code)
print("Response JSON:", response.json())


