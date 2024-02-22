from dataclasses import dataclass

@dataclass
class Version:
    id:int
    name: str

@dataclass
class Character:
    id: int
    name: str

@dataclass
class CharacterUsage:
    character_id: int
    version_id: int
    rate: float
    rank: int

@dataclass
class CharacterAppearance:
    character_id: int
    version_id: int
    rate: float
    rank: int

@dataclass
class CharacterFullStar:
    character_id: int
    version_id: int
    rate: float
    rank: int