from openai import OpenAI

class OpenAIAda002():

    def name(self):
        return "OpenAI/text-embedding-ada-002"

    def embed(self, text):
        client = OpenAI()
        resp = client.embeddings.create(
            input=[text],
            model="text-embedding-ada-002"
        )
        embedding = resp.data[0].embedding
        return embedding

class OpenAI3Large():

    def name(self):
        return "OpenAI/text-embedding-3-large"

    def embed(self, text):
        client = OpenAI()
        resp = client.embeddings.create(
            input=[text],
            model="text-embedding-3-large"
        )
        embedding = resp.data[0].embedding
        return embedding