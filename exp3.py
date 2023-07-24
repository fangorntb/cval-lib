import random

from cval_lib.connection import CVALConnection
from cval_lib.models.embedding import FrameEmbeddingModel, EmbeddingModel


user_api_key = '50b524bcae7b7bf77e2fcd34fefaf6c7192cbeef1ea55939d5f86a88f42bc809'
cval = CVALConnection(user_api_key)
ds1 = cval.dataset().create()
emb = cval.embedding(ds1, part_of_dataset='training')

embs = []

for i in range(1000):
    embs += [FrameEmbeddingModel(frame_id=f'{i}', embeddings=[
        EmbeddingModel(embedding=list(map(lambda x: random.random(), range(100))), embedding_id=f'{i}')
    ])]
    cval.detection().on_premise_sampling()


emb.upload_many(embeddings=embs, )
