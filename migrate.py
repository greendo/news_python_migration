import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('news-e631a-firebase-adminsdk-lzc29-4c40c2e993.json')
firebase_admin.initialize_app(cred)

# 1 batch may hold up to 500 operations, complete migration might require richer logic, including multiple batches
db = firestore.client()

cache_ref = db.collection(u'cache')
docs = cache_ref.stream()

batch = db.batch()

for doc in docs:
    s = doc.get('description').lower()
    batch.update(doc.reference, {u'description': s})

batch.commit()
