from embedding_models import open_ai
class _Registry:
    def __init__(self):
        pass

    def _models(self):
        return [
            open_ai.OpenAIAda002(),
            open_ai.OpenAI3Large()
        ]

    def models(self):
        return {m.name(): m for m in self._models()}

registry = _Registry()
