import os

def change_first_number(input_file, output_file, new_number):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        for line in lines:
            parts = line.strip().split()
            if parts:  # Check if line is not empty
                try:
                    parts[0] = str(new_number)  # Change the first number to the new number
                    new_line = ' '.join(parts) + '\n'
                    f.write(new_line)
                except ValueError:
                    # If the first part of the line is not a number, simply write the original line
                    f.write(line)

def change_first_number_in_files(directory, new_number):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            # Modify each file
            change_first_number(filepath, filepath, new_number)

# This next part could definitely be abstracted way better, but it's late and I believe this script will only run maybe twice in its lifetime

# Ammobatoidini
directory1 = '../data/se_us_bee_data/Ammobatoidini/labels/'
change_first_number_in_files(directory1, 0)

# Andrenini
directory2 = '../data/se_us_bee_data/Andrenini/labels/'
change_first_number_in_files(directory2, 1)

# Anthidiini
directory3 = '../data/se_us_bee_data/Anthidiini/labels/'
change_first_number_in_files(directory3, 2)

# Anthophorini
directory4 = '../data/se_us_bee_data/Anthophorini/labels/'
change_first_number_in_files(directory4, 3)

# Apini
directory5 = '../data/se_us_bee_data/Apini/labels/'
change_first_number_in_files(directory5, 4)

# Augochlorini
directory6 = '../data/se_us_bee_data/Augochlorini/labels/'
change_first_number_in_files(directory6, 5)

# Bombini
directory7 = '../data/se_us_bee_data/Bombini/labels/'
change_first_number_in_files(directory7, 6)

# Calliopsini
directory8 = '../data/se_us_bee_data/Calliopsini/labels/'
change_first_number_in_files(directory8, 7)

# Caupolicanini
directory9 = '../data/se_us_bee_data/Caupolicanini/labels/'
change_first_number_in_files(directory9, 8)

# Centridini
directory10 = '../data/se_us_bee_data/Centridini/labels/'
change_first_number_in_files(directory10, 9)

# Ceratinini
directory11 = '../data/se_us_bee_data/Ceratinini/labels/'
change_first_number_in_files(directory11, 10)

# Dasypodaini 
directory12 = '../data/se_us_bee_data/Dasypodaini/labels/'
change_first_number_in_files(directory12, 11)

# Emphorini
directory13 = '../data/se_us_bee_data/Emphorini/labels/'
change_first_number_in_files(directory13, 12)

# Epeolini
directory14 = '../data/se_us_bee_data/Epeolini/labels/'
change_first_number_in_files(directory14, 13)

# Eucerini
directory15 = '../data/se_us_bee_data/Eucerini/labels/'
change_first_number_in_files(directory15, 14)

# Euglossini 
directory16 = '../data/se_us_bee_data/Euglossini/labels/'
change_first_number_in_files(directory16, 15)

# Halictini
directory17 = '../data/se_us_bee_data/Halictini/labels/'
change_first_number_in_files(directory17, 16)

# Megachilini
directory18 = '../data/se_us_bee_data/Megachilini/labels/'
change_first_number_in_files(directory18, 17)

# Melectini
directory19 = '../data/se_us_bee_data/Melectini/labels/'
change_first_number_in_files(directory19, 18)

# Nomadini
directory20 = '../data/se_us_bee_data/Nomadini/labels/'
change_first_number_in_files(directory20, 19)

# Osmiini
directory21 = '../data/se_us_bee_data/Osmiini/labels/'
change_first_number_in_files(directory21, 20)

# Panurgini
directory22 = '../data/se_us_bee_data/Panurgini/labels/'
change_first_number_in_files(directory22, 21)

# Protandrenini
directory23 = '../data/se_us_bee_data/Protandrenini/labels/'
change_first_number_in_files(directory23, 22)

# Sphecodini
directory24 = '../data/se_us_bee_data/Sphecodini/labels/'
change_first_number_in_files(directory24, 23)

# Xylocopini
directory25 = '../data/se_us_bee_data/Xylocopini/labels/'
change_first_number_in_files(directory25, 24)
