import requests

def StoreMosque(name, address, latitude, longitude):
    mosque = {
        'name': name,
        'address': address,
        'latitude': latitude,
        'longitude': longitude
    }
    
    try:
        response = requests.post(
            'https://vfyiwfmxnm.ap-southeast-1.awsapprunner.com/v1/admin/mosque',
            json=mosque,
            headers={
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        )
        print("request\n")
        print(mosque)
        print("response\n")
        print(response.json())
        print("\n")
        
        if response.status_code == 200:
            return True
        else:
            error_data = response.json()
            if 'error' in error_data and error_data['error'] == 'mosque with same name and address already exists':
                print(f"Mosque already exists: {name} at {address}")
                return False
        
        response.raise_for_status()
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"Error storing mosque: {str(e)}")
        return False
    