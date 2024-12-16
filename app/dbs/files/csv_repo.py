import os
from typing import Generator
import pandas as pd

def load_data(filename,chunk_size=1000) -> Generator:
    file_path = os.path.join(os.path.dirname(__file__), '..','..','..','data', filename)
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        yield chunk
