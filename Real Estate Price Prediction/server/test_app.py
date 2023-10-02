import requests
import unittest

# Define the URL of your Flask server
url = 'http://127.0.0.1:5000/predict_home_price'  # Update with the actual server URL

# Sample data for testing
data = {
    'total_sqft': 1500.0,
    'location': 'Rajaji Nagar',
    'bhk': 3,
    'bath': 2
}

# Send a POST request with the sample data
response = requests.post(url, data=data)

# Check the response
if response.status_code == 500:
    result = response.json()
    estimated_price = result.get('estimated_price')
    print(f'Estimated Price: {estimated_price}')
else:
    print(f'Failed to get estimated price. Status code: {response.status_code}')


class TestYourApp(unittest.TestCase):

    def test_predict_home_price(self):
        # Define test data
        test_data = {
            'total_sqft': 1500.0,
            'location': 'Rajaji Nagar',  # Correct the location name to match your sample data
            'bhk': 3,
            'bath': 2
        }

        # Send a POST request to your Flask server
        response = requests.post(url, data=test_data)

        # Check the response status code
        self.assertEqual(response.status_code, 500)

        # Check the response content
        response_data = response.json()
        self.assertIn('estimated_price', response_data)
        estimated_price = response_data['estimated_price']
        self.assertIsInstance(estimated_price, (int, float))

if __name__ == '__main__':
    unittest.main()