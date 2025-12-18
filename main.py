import importlib
import sys
import os

# Konfigurasi
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# Impor file konfigurasi
config = importlib.import_module('config')

# Impor file fungsi
functions = {
    'aim_lock': importlib.import_module('functions.aim_lock'),
    'bot': importlib.import_module('functions.bot'),
    'anti_ban': importlib.import_module('functions.anti_ban'),
    'tesks_akar': importlib.import_module('functions.tesks_akar'),
    'tesks_bergantian': importlib.import_module('functions.tesks_bergantian'),
    'bermain_akar': importlib.import_module('functions.bermain_akar'),
    'bermain_bergantian': importlib.import_module('functions.bermain_bergantian'),
}

# Jalankan fungsi
if config.AIM_LOCK:
    functions['aim_lock'].aim_lock()
if config.BOT:
    functions['bot'].bot()
if config.ANTI_BAN:
    functions['anti_ban'].anti_ban()