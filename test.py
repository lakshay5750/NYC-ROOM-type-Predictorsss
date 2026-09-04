

import joblib
import lzma

with lzma.open("Model_pipeline.pkl.xz", "rb") as f:
    model = joblib.load(f)
    


import joblib
import lzma

with lzma.open("model.pkl.xz", "wb", preset=9) as f:
    joblib.dump(model, f)
    
import os

size = os.path.getsize("model.pkl.xz") / (1024**2)
print(f"Size: {size:.2f} MB")