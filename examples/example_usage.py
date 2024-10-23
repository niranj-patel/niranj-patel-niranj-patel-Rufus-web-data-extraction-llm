from rufus.client import RufusClient

if __name__ == "__main__":
    key = 'your_api_key'
    client = RufusClient(api_key=key)

    instructions = "Find information about product features and customer FAQs."
    documents = client.scrape("https://example.com", instructions)
    print(documents)
