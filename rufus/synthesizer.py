import json

class DocumentSynthesizer:
    def synthesize(self, content):
        # Structure content into JSON
        structured_document = {
            "data": content,
        }
        return json.dumps(structured_document)
