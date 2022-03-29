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

    def __str__(self) -> str:
        max_width = 50
        entry_width = 25
        
        left_header = f"#{self.atomic_number} [{self.symbol}]: {self.name}"
        header = f"""{'-'*50}\n{left_header:<{entry_width}}{f'{self.standard_state}':>{entry_width}}""" 
        
        # Optional Attributes        
        atomic_mass = f"{' Atomic Mass:':<{entry_width}}{f'{self.atomic_mass}':>{entry_width}}"
        group = f"{' Chemical Group Block:':<{entry_width}}{f'{self.chemical_group_block}':>{entry_width}}"
        density = f"{' Density:':<{entry_width}}{f'{self.density} g/L':>{entry_width}}"   # | g/cm^3
        elec_config = f"{' Electron Configuration:':<{entry_width}}{f'{self.electron_configuration}':>{entry_width}}"
        elec_neg = f"{' Electro Negativity:':<{entry_width}}{f'{self.electro_negativity}':>{entry_width}}"
        hex_clr = f"{' CPK Hex Color:':<{entry_width}}{f'#{self.cpk_hex_color}':>{entry_width}}"
        atomic_radius = f"{' Atomic Radius:':<{entry_width}}{f'{self.atomic_radius} pm':>{entry_width}}"  # van der Waals
        ion_energy = f"{' Ionization Energy:':<{entry_width}}{f'{self.ionization_energy} eV':>{entry_width}}"
        elec_affinity = f"{' Electron Affinity:':<{entry_width}}{f'{self.electron_affinity} eV':>{entry_width}}"
        oxi_states = f"{' Oxidation State:':<{entry_width}}{f'{self.oxidation_states}':>{entry_width}}"
        standard_state = f"{' Standard State:':<{entry_width}}{f'{self.standard_state}':>{entry_width}}"
        melt_point = f"{' Melting Point:':<{entry_width}}{f'{self.melting_point} K':>{entry_width}}"
        boil_point = f"{' Boiling Point:':<{entry_width}}{f'{self.boiling_point} K':>{entry_width}}"
        year = f"{' Year Discovered:':<{entry_width}}{f'{self.year_discovered}':>{entry_width}}"
        
        text = f"{header}"
        text += f"""
{'-'*50}
{group}
{hex_clr}

{density}
{atomic_mass}
{atomic_radius}

{elec_config}
{oxi_states}

{elec_neg}
{ion_energy}
{elec_affinity}

{melt_point}
{boil_point}

{standard_state}
{year}
{'-'*50}
"""
        return text

    def card_view(self):
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

