from dataclasses import dataclass
from typing import Optional


@dataclass
class Teacher:
    id : str
    name : str
    department : str
    title : str
    office: str
    email : str

