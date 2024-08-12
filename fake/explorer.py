from model.explorer import Explorer

#fake data, replaced in chapter 10 by a real database and SQL

_explorers = [
    Explorer(
        name='Claud Hande',
        country='FR',
        description="Scarce during full moons"
    ),
    Explorer(
        name="Noah Weiser",
        country="DE",
        description="Myopic mchete man"
    ),
]

def get_all() -> list[Explorer]:
    """Return all explorers"""
    return _explorers

def get_one(name: str)-> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None

# The following are nonfunctional for now,
# so they just act like they work, without modifying
# the actual fake _explorere list:
def create(explorer: Explorer) -> Explorer:
    """Add an exploerer"""
    return explorer

def modify(explorer: Explorer) -> Explorer:
    """Partially moify an exploerer"""
    return explorer

def replace(explorer: Explorer) -> Explorer:
    """Completely replace an exploerer"""
    return explorer

def delete(explorer: Explorer) -> Explorer:
    """Delete an exploerer"""
    return explorer