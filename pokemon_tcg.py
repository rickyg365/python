import requests
from typing import Dict, List, Any

def prettify(raw_data: Dict[str, Any], depth: int=0) -> str:
    txt = ""
    spacer = f"{depth*'    '}"
 
    if not isinstance(raw_data, dict):
        return f"{spacer}{raw_data}"

    for k, v in raw_data.items():
        if isinstance(v, list):
            v = "\n" + "\n".join([prettify(x, depth + 1) for x in v])
        
        if isinstance(v, dict):
            v = "\n" + prettify(v, depth + 1)

        txt += f"""{spacer}{k}: {v}
"""
    return txt

def setup_card(level, name, types, hp, subtypes, evolvesFrom, abilities, attacks, weaknesses, retreatCost, convertedRetreatCost, flavorText, artist, number, rarity, **kwargs):
    MAX_LENGTH = 42
    LINE_BREAK = f"{MAX_LENGTH*'_'}"

    ABILITY_TEXT = '\n'.join([f"{a['name']}[{a['type']}]: {a['text']}" for a in abilities])
    ATTACK_TEXT = '\n'.join([f"{atk['damage']}dmg - {atk['name']}[{atk['convertedEnergyCost']}]: {atk['text']}" for atk in attacks])
    WEAKNESS_TEXT = '\n'.join([f"{w['type']} {w['value']}" for w in weaknesses])
    
    card_txt = f"""
lvl.{level} {name}  {hp} HP  [{' '.join(types)}]
{' '.join(subtypes)}: Evolves from {evolvesFrom}
{'ABILITIES':-^{MAX_LENGTH}}
{ABILITY_TEXT}
{'ATTACKS':-^{MAX_LENGTH}}
{ATTACK_TEXT}
{LINE_BREAK}
weaknesses: {WEAKNESS_TEXT}
retreat cost: {retreatCost} x{convertedRetreatCost}
{LINE_BREAK}
{flavorText}
{LINE_BREAK}
{artist}
{number:02}/102 {rarity}
"""

    return card_txt


def get_data(url) -> Any:
    if url.split(".")[-1] != "json":
        return None

    response = requests.get(url)

    raw_data = response.json()

    return raw_data

def main():
    DATA_URL_1 = "https://raw.githubusercontent.com/PokemonTCG/pokemon-tcg-data/master/cards/en/base1.json"
    DATA_URL_2 = "https://raw.githubusercontent.com/PokemonTCG/pokemon-tcg-data/master/cards/en/base2.json"
    data = get_data(DATA_URL_1)
    data_point = data[0]
    data_point_2 = data[24]

    # print("\n".join([prettify(d) for d in data]))
    print(prettify(data_point))

    print(setup_card(**data_point))
    print(setup_card(**data_point_2))


if __name__ == "__main__":
    main()


