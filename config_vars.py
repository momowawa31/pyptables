import os

home_dir = os.path.expanduser("~")

config_dir = os.path.join(home_dir, ".config", "pyptables")
if not os.path.exists(config_dir):
    os.makedirs(config_dir)
rules_file = os.path.join(config_dir, "rules.v4")
if not os.path.exists(rules_file):
    with open(rules_file, "w") as f:
        f.write("# Fichier de configuration de pyptables")
        
conf_file = os.path.join(config_dir, "config")
lines_to_write_conf = [
    "# Fichier de configuration de pyptables",
    "# Toutes modifications pourrait etre dangereuse",
    "# -------PRUDENCE--------",
]
if not os.path.exists(conf_file):
    with open(conf_file, "a") as file:
        for line in lines_to_write_conf:
            file.write(line + "\n")

readme_file = os.path.join(config_dir, "readme")
lines_to_write_about = [
    "Bla bla bla bla",
    "TUTU TU TU TU TU ",
    "LO lop pol lop pol",
]
if not os.path.exists(readme_file):
    with open(readme_file,"a") as file:
        for line in lines_to_write_about:
                file.write(line + "\n")