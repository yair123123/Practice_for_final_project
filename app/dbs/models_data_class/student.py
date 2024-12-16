
from dataclasses import dataclass
from typing import Optional


@dataclass
class Student:
    id : int
    first_name : str
    last_name : str
    age : int
    address : str

