import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')

if response.status_code == 200:
    users = response.json()
    
    print("📋 User List:")
    for user in users:
        print(f"- {user['name']} ({user['email']})")
else:
    print(f"❌ Error: {response.status_code}")