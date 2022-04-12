import os



class RecipeView:
    def __init__(self) -> None:
        pass



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


def main():
    return

if __name__ == '__main__':
    main()
