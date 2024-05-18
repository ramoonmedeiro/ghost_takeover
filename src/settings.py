from enum import Enum
from colorama import Fore


class Settings(Enum):

    APP_NAME = "GHOST TAKEOVER"
    APP_VERSION = "0.1.0"

    BANNER = f"""
{Fore.BLACK}

              ('-. .-.                .-')     .-') _    
             ( OO )  /               ( OO ).  (  OO) )   
  ,----.     ,--. ,--.  .-'),-----. (_)---\_) /     '._  
 '  .-./-')  |  | |  | ( OO'  .-.  '/    _ |  |'--...__) 
 |  |_( O- ) |   .|  | /   |  | |  |\  :` `.  '--.  .--' 
 |  | .--, \ |       | \_) |  |\|  | '..`''.)    |  |    
(|  | '. (_/ |  .-.  |   \ |  | |  |.-._)   \    |  |    
 |  '--'  |  |  | |  |    `'  '-'  '\       /    |  |    
  `------'   `--' `--'      `-----'  `-----'     `--'    
{Fore.RESET}

                  {Fore.YELLOW}Coded by RAMONSTRO{Fore.RESET}
"""

    USER_AGENT = [
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    ]
