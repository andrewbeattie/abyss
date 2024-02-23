import pandas as pd
from abyss.ambr.characters import get_character_name

def main():
    data = get_character_name()
    df = pd.DataFrame(data)
    df.to_csv(r"./data/character_name.csv", index=False)

if __name__ == "__main__":
    main()