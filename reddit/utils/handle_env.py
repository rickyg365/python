import os
from typing import List


def load_env_var(env_path: str, key_list: List[str], show_status: bool=True) -> List[str]:
    """ Load env var from a file, then add them to a list """
    # Imports
    from dotenv import load_dotenv
    
    # Load ENV file
    load_dotenv(env_path)

    # Get Variables
    extracted_data = []
    
    for key in key_list:
        new_val = os.getenv(key)

        if show_status:
            status = f"[ {key} Not Found! ]" if new_val is None else f"[ {key} Loaded ]"

            print(status)  
        
        extracted_data.append(new_val)

    return extracted_data
