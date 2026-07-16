from pydantic import BaseModel, Emu




class MenuName(str, Emu):
    chicken_bowl = "chicken_bowl"
    steak_bowl = "steak_bowl"
    protein_shake = "protein_shake"
    french_fries = "french_fries"

class MenuCategory(str, Emu):
    meal = "meal"
    drink = "drink"
    side = "side"

class MenuBase(BaseModel):
    name: MenuName | None = None
    category: MenuCategory | None = None
    price: int | None = None
    available: bool 

class Menu(MenuBase):
    item_id: int

