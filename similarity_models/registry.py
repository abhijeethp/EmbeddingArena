from similarity_models.cosine_similarity import CosineSimilarity

class _Registry:
    def __init__(self):
        pass

    def _models(self):
        return [
            CosineSimilarity()
        ]

    def models(self):
        return {m.name(): m for m in self._models()}

registry = _Registry()
