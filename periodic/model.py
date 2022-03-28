import os
from dataclasses import dataclass


@dataclass
class PeriodicElement:
    name: str
    symbol: str
    atomic_number: int
    atomic_mass: float = None
    chemical_group_block: str = None
    density: float = None
    electron_configuration: str = None
    electro_negativity: float = None
    cpk_hex_color: str = None
    atomic_radius: int = None
    ionization_energy: float = None
    electron_affinity: float = None
    oxidation_states: str = None
    standard_state: str = None
    melting_point: float = None
    boiling_point: float = None
    year_discovered: int = None

    width: int = 0
    string_cache: str = None
    recache: bool = True

    def __post_init__(self):
        self.width = min(len(self.name) + 2, 15)

    def __str__(self):
        if self.string_cache is not None and not self.recache:
            return self.string_cache

        wanted_display_values = [self.atomic_number, f"[{self.symbol}]", self.name, "", self.atomic_mass]

        element_txt = f"╭{'─'*self.width}╮\n"
        for display_val in wanted_display_values:
            # print(type(display_val) is str, type(display_val))
            if type(display_val) is float:
                element_txt += f"│{display_val:^{self.width}.3f}│\n"
            else:
                element_txt += f"│{display_val:^{self.width}}│\n"
                
        element_txt += f"╰{'─'*self.width}╯"
        
        self.string_cache = element_txt
        return element_txt
    
    def to_dict(self):
        new_dict = {
            "atomic_number": self.atomic_number,
            "symbol": self.symbol,
            "name": self.name,
            "atomic_mass": self.atomic_mass,
            "cpk_hex_color": self.cpk_hex_color,
            "electron_configuration": self.electron_configuration,
            "electro_negativity": self.electro_negativity,
            "atomic_radius": self.atomic_radius,
            "ionization_energy": self.ionization_energy,
            "electron_affinity": self.electron_affinity,
            "oxidation_states": self.oxidation_states,
            "standard_state": self.standard_state,
            "melting_point": self.melting_point,
            "boiling_point": self.boiling_point,
            "density": self.density,
            "chemical_group_block": self.chemical_group_block,
            "year_discovered": self.year_discovered
        }

        return new_dict

