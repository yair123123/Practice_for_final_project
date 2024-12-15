from typing import Generator
import pandas as pd

def load_data(filename,chunk_size=1000) -> Generator:
    for chunk in pd.read_csv(filename, chunksize=chunk_size):
        yield chunk
