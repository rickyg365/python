import json
from textwrap import indent
from typing import List, Dict
from dataclasses import dataclass

from utils.text_formatter import parse_paragraph


@dataclass
class Recipe:
    name: str
    description: str
    ingredients: Dict[str, str]
    steps: List[str]
    max_width: int = 45
    detail: bool = True

    def __str__(self) -> str:
        # Detailed view
        if self.detail:
            return self.full_str()

        # Define Seperators
        sep1 = f"{self.max_width*'-'}"
        sep2 = f"{self.max_width*'_'}"

        # Name and Description
        header=f"\n{self.name}:\n{sep2}\n{parse_paragraph(self.description, self.max_width)}\n{sep2}"

        return header
    
    def set_detail_level(self, detailed: bool):
        self.detail = detailed
    
    def full_str(self) -> str:
        # Define Seperators
        sep1 = f"{self.max_width*'-'}"
        sep2 = f"{self.max_width*'_'}"

        # Name and Description
        header=f"{self.name}:\n{sep2}\n{parse_paragraph(self.description, self.max_width)}\n{sep2}"
        
        # Ingredients
        ingredients_text = f"\nIngredients:\n{sep1}"
        for name, quantity in self.ingredients.items():
            ingredients_text += f"\n  {name.title()}: {quantity.upper()}"
        ingredients_text += f"\n{sep1}"

        # Steps
        steps_text = f"\nInstructions:\n{sep1}"
        for _, step in enumerate(self.steps, start=1):
            steps_text += f"\n  {_}. {parse_paragraph(step, self.max_width)}"
        steps_text += f"\n{sep1}"
        
        final_text = f"""
{header}
{ingredients_text}
{steps_text}
"""

        return final_text

    def export(self) -> Dict[str, any]: 
        return {
            "name": self.name,
            "description": self.description,
            "ingredients": self.ingredients,
            "steps": self.steps,
            "max_width": self.max_width
        }

def main():
    # Sample Recipe Data
    test_recipe_data = {
        "name": "Philly CheeseSteak",
        "description": "A delicious blend of steak and cheese grilled with peppers and enjoyed on a nice bread roll.",
        "ingredients": {
            "salt": "1 teaspoon",
            "pepper": "1 teaspoon",
            "Steak": "1 lb",
            "Cheese": "1/2 lb",
            "Onion": "1 whole",
            "Bell Peppers": "2 whole",
            "French Roll": "1 loaf"
    },
        "steps": [
            "Chop Onion, Bell Peppers, and Steak",
            "Grill and season Veggies",
            "Grill and season Steak",
            "Top Steak with Cheese",
            "Toast French Roll",
            "Assemble",
            "Enjoy"
        ]
    }
    # Create Recipe Object
    new_recipe = Recipe(**test_recipe_data)

    # Display | str() Method
    # print(json.dumps(new_recipe.export(), indent=4))
    print(new_recipe)

if __name__ == '__main__':
    main()
