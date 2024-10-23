from flask import Flask, request, jsonify
from rufus.client import RufusClient
import os

# Create the Flask app
app = Flask(__name__)

# Initialize Rufus Client
api_key = os.getenv('RUFUS_API_KEY', 'your_default_api_key')
client = RufusClient(api_key=api_key)

@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        # Get the JSON data from the request
        data = request.json
        url = data.get('https://www.sfgov.com')
        instructions = data.get("We're making a chatbot for the HR in San Francisco.")

        if not url or not instructions:
            return jsonify({'error': 'URL and instructions are required'}), 400

        # Use Rufus to scrape the data
        documents = client.scrape(url, instructions)

        # Return the result as JSON
        return jsonify({'status': 'success', 'documents': documents})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
