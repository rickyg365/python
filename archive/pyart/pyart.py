import os

import json
from typing import List, Dict

"""
Duck
  __ 
<(o )__
 ( ._>/ 
  `--' 


▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░║░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░║░╬▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▓░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒╬░░▓░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒░░▐▓▌░░▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒░░▐▓▌░░▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒░░▐▓▌░░▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒░░░░░░▄▓▄░░░╬░░▒▒▒▒▒▒▒▒▒
▒▒▒▒▒╬░░░░░░▄▄█████▄▄░░░░░░░▒▒▒▒▒
▒▒▒▒░░▄▄▄███████████████▄▄▄░░▒▒▒▒
▒▒▒▒░░▐░░░▀▓▓▒▓▓▒▓▓▒▓▓▀░░░▌░░▒▒▒▒
▒▒▒▒░░░░░▄█████████████▄░░░╬░▒▒▒▒
▒▒▒░░▄▄███████████████████▄▄░░▒▒▒
▒▒▒░░▐░░░▀▓▓▒▓▓▓▒▓▓▓▒▓▓▀░░░▌░░▒▒▒
▒▒▒▒░░░▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░▒░░░▒▒▒▒
▒▒▒░╬░░░▄███████████████▄░░░░░▒▒▒
▒▒░░▄▄█████████████████████▄▄░░▒▒
▒▒░░▐░░░▀▓▓▒▓▓▓▓▒▓▓▓▓▒▓▓▀░░░▌░░▒▒
▒▒▒░░░▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▒░░░▒▒▒
▒▒░░░░░▄█████████████████▄░░░░╬▒▒
▒░░▄▄███████████████████████▄▄░░▒
▒░░▐░░░▀▓▓▒▓▓▓▓▓▒▓▓▓▓▓▒▓▓▀░░░▌░░▒
▒▒░░░▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▒░░░▒▒
▒░╬░░░▄███████████████████▄░░░░░▒
░░▄▄█████████████████████████▄▄░░
░░▐░░░▀▓▓▒▓▓▓▓▓▓▒▓▓▓▓▓▓▒▓▓▀░░░▌░░
▒░░▄▄███████████████████████▄▄░░▒
▒▒░░░▓║║▓║║▓║║▓█▓█▓║║▓║║▓║║▓░░░╬▒
▒╬░░▄▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▄░░▒▒
░░▄██████████▓▄▄▄▄▄▓██████████▄░░
▄████████████▓▄▄▄▄▄▓████████████▄


_.█████████████████ 
_ ██████████████████ 
████████████████████ 
█████████████████████ 
_█_________▄▄▄▄_ ▄▄▄▄_█ 
_█__█████_▐▓▓▌_▐▓▓▌_█ 
_█__█████_▐▓▓▌_▐▓▓▌_█ 
_█__█████_▐▓▓▌_▐▓▓▌_█ 
_█__█████_▀▀▀▀_ ▀▀▀ █✿ ✿ 
_█__█████_____________ █(\\|/) 
_____________██ _____________██ 




┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼███
┼┼┼┼┼┼┼┼┼┼┼┼┼███████
┼┼┼┼┼┼┼┼┼┼██████████████
┼┼┼┼┼┼┼████████████████████
┼┼┼┼██████████████████████████
┼████████████████████████████████
██████████████████████████████████
┼████████████████████████████████
┼█░░░░██░░░░██████████░░░░██░░░░█
┼█░░░░██░░░░██████████░░░░██░░░░█
┼████████████████████████████████
┼█░░░░██░░░░██████████░░░░██░░░░█
┼█░░░░██░░░░██████████░░░░██░░░░█
┼████████████████████████████████
┼████████████████████████████████
┼█░░░░██░░░░██████████░░░░██░░░░█
┼█░░░░██░░░░█▒▒▒▒▒▒▒▒█░░░░██░░░░█
┼████████████▒▒▒░░▒▒▒████████████
┼█░░░░██░░░░█▒▒▒▒▒▒▒▒█░░░░██░░░░█
┼█░░░░██░░░░█▒▒▒▒▒▒▒▒█░░░░██░░░░█
┼████████████▒▒▒▒▒▒▒▒████████████
┼████████████▓▓▓▓▓▓▓▓████████████
████████████▓▓▓▓▓▓▓▓▓▓████████████



██████████████████████████
▌════════════════════════▐
▌══▄▄▓█████▓▄═════▄▄▓█▓▄═▐ 
▌═▄▓▀▀▀██████▓▄═▄▓█████▓▌▐
▌═══════▄▓███████████▓▀▀▓▐ 
▌═══▄▓█████████▓████▓▄═══▐
▌═▄▓████▓███▓█████████▓▄═▐ 
▌▐▓██▓▓▀▀▓▓███████▓▓▀▓█▓▄▐
▌▓▀▀════▄▓██▓██████▓▄═▀▓█▐
▌══════▓██▓▀═██═▀▓██▓▄══▀▐
▌═════▄███▀═▐█▌═══▀▓█▓▌══▐ 
▌════▐▓██▓══██▌═════▓▓█══▐
▌════▐▓█▓══▐██═══════▀▓▌═▐
▌═════▓█▀══██▌════════▀══▐
▌══════▀═══██▌═══════════▐ 
▌═════════▐██▌═══════════▐
▌═════════▐██════════════▐
▌═════════███════════════▐
▌═════════███════════════▐ 
▌════════▐██▌════════════▐
▌▓▓▓▓▓▓▓▓▐██▌▓▓▓▓▓▓▓▓▓▓▓▓▐
▌▓▓▓▓▓▓▓▓▐██▌▓▓▓▓▓▓▓▓▓▓▓▓▐
▌▓▓▓▓▓▄▄██████▄▄▄▓▓▓▓▓▓▓▓▐ 
██████████████████████████

░░░░░░███████ ]▄▄▄▄▄▄▄▄
▂▄▅█████████▅▄▃▂
I███████████████████].
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤...


__●__ ●
 _ █___█
  __ █__ █_
   __ █__ █
    __ ███____________█████ 　　　
     _█▒░░█_________██▓▒▒▓██ ☆
      █▒░●░░█___ ██▓▒██▓▒▒▓█　　 ★
       █░█▒░░██_ ██▓▒██▓▒░▒▓█
        _██▒░░██ ██▓▒░██▓▒░▒▓█ 　　　★
         ____█▒░██ ██▓▒░░ ████▓█
          ___█▒░██__██▓▓▒▒░░░██ 　 ★★
           ____█▒░██___████████████
            _____█▒░█▒▒▒▒▒▒▒▒▒▒▒▒█
             ______██████████████████.•°*”~҈.•°*”~҈.



───────█────────────────────────███▓
────█──██──────────────────────███▓
─────██████───────────────────███▓
──────███████────────────────███▓
───── █◉██████───────────────██▓
────██████████───────────────██▓
────██████████────────────────██▓
─────█████████──────────█████████
─────────██████─────██████████████
─────────██████████████████████████
─────────██████████████████████████
─────────██████████████████████████
─────────██████████████████████████
──────────████████████▓▓▓▓█████████
──────────███████▓▓▓▓▓────▓████████
─────────█████▓▓▓──────────▓████████
─────────███▓▓██────────────▓▓██████
────────███▓─███─────────────█▓▓▓████
────────███──███─────────────███──███
───────███────██─────────────███───██
───────██─────███────────────██────██
──────███──────██───────────███────██
─────███───────██───────────██─────██
─────██─────────██─────────██──────██
────███─────────██────────███──────██
─彡███────────彡███──────彡███────彡███




░░▒░░█░ 
░░▒░█ 
░░░█ 
░░█░░░░███████ 
░██░░░██▓▓███▓██▒ 
██░░░█▓▓▓▓▓▓▓█▓████ 
██░░██▓▓▓(◐)▓█▓█▓█ 
███▓▓▓█▓▓▓▓▓█▓█▓▓▓▓█ 
▀██▓▓█░██▓▓▓▓██▓▓▓▓▓█ 
░▀██▀░░█▓▓▓▓▓▓▓▓▓▓▓▓▓█ 
░░░░▒░░░█▓▓▓▓▓█▓▓▓▓▓▓█ 
░░░░▒░░░█▓▓▓▓█▓█▓▓▓▓▓█ 
░▒░░▒░░░█▓▓▓█▓▓▓█▓▓▓▓█ 
░▒░░▒░░░█▓▓▓█░░░█▓▓▓█ 
░▒░░▒░░██▓██░░░██▓▓██


╦╦╦╦╦╦▄▀▀▀▀▀▀▄╦╦╦╦╦╦
▒▓▒▓▒█╗░░▐░░░╔█▒▓▒▓▒
▒▓▒▓▒█║░░▐▄▄░║█▒▓▒▓▒
▒▓▒▓▒█╝░░░░░░╚█▒▓▒▓▒
╩╩╩╩╩╩▀▄▄▄▄▄▄▀╩╩╩╩╩╩

█▀███▀▀███▀▀███▀▀███▀▀███▀█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▒▒█▒▒▒▒▒███▒▒█▒▒▒█▒█████▒█
█▒▒█▒▒▒▒█▒▒▒█▒█▒▒▒█▒█▒▒▒▒▒█
█▒▒█▒▒▒▒█▒▒▒█▒▒█▒█▒▒█████▒█
█▒▒█▒▒▒▒█▒▒▒█▒▒█▒█▒▒█▒▒▒▒▒█
█▒▒████▒▒███▒▒▒▒█▒▒▒█████▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒█
█▒▒▒▒▒▒▒█──█▒████▒█──█▒▒▒▒█
█▒▒▒▒▒▒█──█─█────█─█──█▒▒▒█
█▒▒▒▒▒▒█─██───────███─█▒▒▒█
█▒▒▒▒▒▒█──────────────█▒▒▒█
█▒▒▒▒▒▒▒█────────────█▒▒▒▒█
█▒▒▒▒██▒▒█──██───██──█▒▒▒▒█
█▒▒▒█──█▒█──██───██──█▒▒▒▒█
█▒▒▒█──█▒█────███────█▒▒▒▒█
█▒▒▒█──█▒█───█───█──█▒▒▒▒▒█
█▒▒▒▒█──█─█───███──█▒▒▒▒▒▒█
█▒▒▒▒▒█────██────██▒▒▒▒▒▒▒█
█▒▒▒▒▒█──────████─██▒▒▒▒▒▒█
█▒▒▒▒▒▒█───────────█▒▒▒▒▒▒█
█▒▒▒▒▒▒▒███─────────█▒▒▒▒▒█
█▒▒▒▒▒▒▒▒▒█──────█───█▒▒▒▒█
█▒▒▒▒███▒▒█───────█───█▒▒▒█
█▒▒▒█──████─────████───█▒▒█
█▒▒▒█────█─────█────█─█▒▒▒█
█▒▒▒█─────█────█────██▒▒▒▒█
█▒▒▒█──────█───█──────█▒▒▒█
█▒▒▒▒█─────██████─────█▒▒▒█
█▒▒▒▒▒█──███▒▒▒▒█─────█▒▒▒█
█▒▒▒▒▒▒██▒▒▒▒▒▒▒▒█───█▒▒▒▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒█
█▒▒▒▒█▒▒▒▒█▒▒███▒▒█▒▒▒█▒▒▒█
█▒▒▒▒▒█▒▒█▒▒█▒▒▒█▒█▒▒▒█▒▒▒█
█▒▒▒▒▒▒██▒▒▒█▒▒▒█▒█▒▒▒█▒▒▒█
█▒▒▒▒▒▒█▒▒▒▒█▒▒▒█▒█▒▒▒█▒▒▒█
█▒▒▒▒▒█▒▒▒▒▒▒███▒▒▒███▒▒▒▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▄▄█▄▄██▄▄█▄▄█▄▄█▄▄██▄▄█▄▄█




─────▄───▄
─▄█▄─█▀█▀█─▄█▄
▀▀████▄█▄████▀▀
─────▀█▀█▀


▄───▄
█▀█▀█
█▄█▄█
─███──▄▄
─████▐█─█
─████───█
─▀▀▀▀▀▀▀

──▒▒▒▒▒▒───▄████▄
─▒─▄▒─▄▒──███▄█▀
─▒▒▒▒▒▒▒─▐████──█─█
─▒▒▒▒▒▒▒──█████▄
─▒─▒─▒─▒───▀████▀





────────▄▄▄▄▄▄▄▄▄
────────▌▐░▀░▀░▀▐
────────▌░▌░░░░░▐
────────▌░░░░░░░▐
────────▄▄▄▄▄▄▄▄▄
──▄▀▀▀▀▀▌▄█▄░▄█▄▐▀▀▀▀▀▄
─█▒▒▒▒▒▐░░░░▄░░░░▌▒▒▒▒▒█
▐▒▒▒▒▒▒▒▌░░░░░░░▐▒▒▒▒▒▒▒▌
▐▒▒▒▒▒▒▒█░▀▀▀▀▀░█▒▒▒▒▒▒▒▌
▐▒▒▒▒▒▒▒▒█▄▄▄▄▄█▒▒▒▒▒▒▒▒▌
▐▒▒▒▒▐▒▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒▌
▐▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▌
▐▒▒▒▒▒▐▒▒▒▒▒▒▒▒▒▒▒▌▒▒▒▒▒▌
▐▒▒▒▒▒▒▌▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒▒▌
▐▒▒▒▒▒▒▌▄▄▄▄▄▄▄▄▄▐▒▒▒▒▒▒▌
▐▄▄▄▄▄▄▌▌███████▌▐▄▄▄▄▄▄▌
─█▀▀▀▀█─▌███▌███▌─█▀▀▀▀█
─▐░░░░▌─▌███▌███▌─▐░░░░▌
──▀▀▀▀──▌███▌███▌──▀▀▀▀
────────▌███▌███▌
────────▌███▌███▌
──────▐▀▀▀██▌█▀▀▀▌
▒▒▒▒▒▒▐▄▄▄▄▄▄▄▄▄▄▌▒▒▒▒▒▒▒


───────────────────────────────────────
───▐▀▄───────▄▀▌───▄▄▄▄▄▄▄─────────────
───▌▒▒▀▄▄▄▄▄▀▒▒▐▄▀▀▒██▒██▒▀▀▄──────────
──▐▒▒▒▒▀▒▀▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄────────
──▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒▒▒▒▒▒▒▒▒▀▄──────
▀█▒▒▒█▌▒▒█▒▒▐█▒▒▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌─────
▀▌▒▒▒▒▒▒▀▒▀▒▒▒▒▒▒▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐───▄▄
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌▄█▒█
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒█▀─
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▀───
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌────
─▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐─────
─▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌─────
──▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐──────
──▐▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▌──────
────▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀────────



──▒▒▒▒▒▒───▄████▄
─▒─▄▒─▄▒──███▄█▀
─▒▒▒▒▒▒▒─▐████──█─█
─▒▒▒▒▒▒▒──█████▄
─▒─▒─▒─▒───▀████▀

( ͡° ͜ʖ ͡°( ಠ ͜ʖ ಠ  ) ͡° ͜ʖ ͡° )

───────────────────────────────
───────────────████─███────────
──────────────██▒▒▒█▒▒▒█───────
─────────────██▒────────█──────
─────────██████──██─██──█──────
────────██████───██─██──█──────
────────██▒▒▒█──────────███────
────────██▒▒▒▒▒▒───▒──██████───
───────██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███─
──────██▒▒▒▒─────▒▒▒▒▒▒▒▒▒▒▒▒█─
──────██▒▒▒───────▒▒▒▒▒▒▒█▒█▒██
───────██▒▒───────▒▒▒▒▒▒▒▒▒▒▒▒█
────────██▒▒─────█▒▒▒▒▒▒▒▒▒▒▒▒█
────────███▒▒───██▒▒▒▒▒▒▒▒▒▒▒▒█
─────────███▒▒───█▒▒▒▒▒▒▒▒▒▒▒█─
────────██▀█▒▒────█▒▒▒▒▒▒▒▒██──
──────██▀██▒▒▒────█████████────
────██▀███▒▒▒▒────█▒▒██────────
█████████▒▒▒▒▒█───██──██───────
█▒▒▒▒▒▒█▒▒▒▒▒█────████▒▒█──────
█▒▒▒▒▒▒█▒▒▒▒▒▒█───███▒▒▒█──────
█▒▒▒▒▒▒█▒▒▒▒▒█────█▒▒▒▒▒█──────
██▒▒▒▒▒█▒▒▒▒▒▒█───█▒▒▒███──────
─██▒▒▒▒███████───██████────────
──██▒▒▒▒▒██─────██─────────────
───██▒▒▒██─────██──────────────
────█████─────███──────────────
────█████▄───█████▄────────────
──▄█▓▓▓▓▓█▄─█▓▓▓▓▓█▄───────────
──█▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓█──────────
──█▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓█──────────
──▀████████▀▀███████▀──────────


────────────────────────────────────────
─────────────▄▄██████████▄▄─────────────
─────────────▀▀▀───██───▀▀▀─────────────
─────▄██▄───▄▄████████████▄▄───▄██▄─────
───▄███▀──▄████▀▀▀────▀▀▀████▄──▀███▄───
──████▄─▄███▀──────────────▀███▄─▄████──
─███▀█████▀▄████▄──────▄████▄▀█████▀███─
─██▀──███▀─██████──────██████─▀███──▀██─
──▀──▄██▀──▀████▀──▄▄──▀████▀──▀██▄──▀──
─────███───────────▀▀───────────███─────
─────██████████████████████████████─────
─▄█──▀██──███───██────██───███──██▀──█▄─
─███──███─███───██────██───███▄███──███─
─▀██▄████████───██────██───████████▄██▀─
──▀███▀─▀████───██────██───████▀─▀███▀──
───▀███▄──▀███████────███████▀──▄███▀───
─────▀███────▀▀██████████▀▀▀───███▀─────
───────▀─────▄▄▄───██───▄▄▄──────▀──────
──────────── ▀▀███████████▀▀ ────────────
────────────────────────────────────────

---▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄


────────▄█▀▄
──────▄██▀▀▀▀▄
────▄███▀▀▀▀▀▀▀▄
──▄████▀▀▀▀▀▀▀▀▀▀▄
▄█████▀▀▀▀▀▀▀▀▀▀▀▀▀▄


─────▀▄▀─────▄─────▄
──▄███████▄──▀██▄██▀
▄█████▀█████▄──▄█
███████▀████████▀
─▄▄▄▄▄▄███████▀



░░░░░░░░░░█
░░░░░░░░▄▄█▄▄
░░░░▀▀▀██▀▀▀██▀▀▀
▄▄▄▄▄▄▄███████▄▄▄▄▄▄▄
░░█▄█░░▀██▄██▀░░█▄█



░╔╔╩╩╝
▄██▄
░░██████▄░░░░░░▄▄▄▄▄▄█
░░█▀█▀█▀█░░▄░▄████████
░▄▌▄▌▄▌▄▌░▀▄▄▄▄█▄▄▄▄█▄


─▄▀▀▀▄────▄▀█▀▀█▄
▄▀─▀─▀▄▄▀█▄▀─▄▀─▄▀▄
█▄▀█───█─█▄▄▀─▄▀─▄▀▄
──█▄▄▀▀█▄─▀▀▀▀▀▀▀─▄█
─────▄████▀▀▀▀████─▀▄


░░░░░░░░░░█
░░░░░░░░▄▄█▄▄
░░░░▀▀▀██▀▀▀██▀▀▀
▄▄▄▄▄▄▄███████▄▄▄▄▄▄▄
░░█▄█░░▀██▄██▀░░█▄█



───▄▄─▄████▄▐▄▄▄▌
──▐──████▀███▄█▄▌
▐─▌──█▀▌──▐▀▌▀█▀
─▀───▌─▌──▐─▌
─────█─█──▐▌█


╔══╗░░░░╔╦╗░░╔═════╗
║╚═╬════╬╣╠═╗║░▀░▀░║
╠═╗║╔╗╔╗║║║╩╣║╚═══╝║
╚══╩╝╚╝╚╩╩╩═╝╚═════╝


█▓▒▓█▀██▀█▄░░▄█▀██▀█▓▒▓█
█▓▒░▀▄▄▄▄▄█░░█▄▄▄▄▄▀░▒▓█
█▓▓▒░░░░░▒▓░░▓▒░░░░░▒▓▓█


░░▄█▀▀▀░░░░░░░░▀▀▀█▄
▄███▄▄░░▀▄██▄▀░░▄▄███▄
▀██▄▄▄▄████████▄▄▄▄██▀
░░▄▄▄▄██████████▄▄▄▄
░▐▐▀▐▀░▀██████▀░▀▌▀▌▌


"""

class ArtPiece:
  def __init__(self, title: str, img_data: str=None):
      if img_data is not None:
          img_data = img_data.strip()
      self.title = title
      self.img_data = img_data

      self.width = 0
      self.height = 0

      self.matrix = None
      self.get_matrix()
  
  def __str__(self) -> str:
    image = self.img_data

    if self.img_data is None:
        image = 'emtpy' 
    
    txt = f"""\r
{image}
{self.title} [{self.width}x{self.height}]
"""
    return txt

  def json_that_shit(self):
      output_json = {
          "title": self.title,
          "image_text": self.img_data,
          "image_matrix": self.matrix
      }
      return output_json
  
  def update_image(self, new_img_data:str):
      self.img_data = new_img_data.strip()
      self.get_matrix()

  def set_dimensions(self):
    if self.matrix is None:
        return False
    
    self.width = len(self.matrix[0])
    self.height = len(self.matrix)

  def get_matrix(self) -> List[List[str]]:
    if self.img_data is None:
      return False

    if self.matrix is None:
      self.matrix = []

    lines = self.img_data.split("\n")

    for line in lines:
      chars = list(line)
      self.matrix.append(chars)
    
    # Set Width and Height
    self.set_dimensions()

    return True


class ArtGallery:
    def __init__(self, filepath="default_gallery.json"):
        self.filepath = filepath
        
        self.name = "No Name"
        self.pieces = []

    def __str__(self) -> str:
        txt = f"{self.name}"

        for art_piece in self.pieces:
            txt += f"\n\n{art_piece}"
        return txt

    def load(self):
        with open(self.filepath, 'r') as input_data:
            raw_data = json.load(input_data)
            # Parse data if needed
            self.pieces = raw_data

    
    def save(self):
        new_list = []
        for piece in self.pieces:
            current_data = piece.json_that_shit()
            new_list.append(current_data)
        
        with open(self.filepath, 'w') as out_json:
            json.dump(new_list, out_json, indent=4)
    
    def add_piece(self, new_piece: ArtPiece):
        self.pieces.append(new_piece)


def test_ArtPiece():
  test_piece = f"""
────────▄█▀▄
──────▄██▀▀▀▀▄
────▄███▀▀▀▀▀▀▀▄
──▄████▀▀▀▀▀▀▀▀▀▀▄
▄█████▀▀▀▀▀▀▀▀▀▀▀▀▀▄
"""

  pyramid = ArtPiece("Pyramid")

  print(pyramid)
  pyramid.update_image(test_piece)
  print(pyramid)

  new_gallery = ArtGallery("test_gallery.json")

  new_gallery.add_piece(pyramid)

  new_gallery.save()


def test_Gallery():
    ...


def main():
    # # Make Gallery to hold art pieces
    # main_gallery = Gallery(name)

    # # takes in multiline fstring for img_data
    # new_piece = ArtPiece(title, img_data)
    
    test_ArtPiece()


if __name__ == '__main__':
    main()
