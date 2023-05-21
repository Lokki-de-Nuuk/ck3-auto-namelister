# File path goes here, make sure to replace \ with \\. Double it up essentially.
file_path = "D:\\L\\Projects and adventures\\CK3\\Workshop\\00_mayan.txt"

# Output file is txt paste the contents yourself to the appropriate file.
new_file = "D:\\L\\Projects and adventures\\CK3\\Workshop\\name_listed_mayan.txt"

# Extracting specific parts from the file
with open(file_path, "r") as file:
    content = file.read()

    # Cadet dynasty names
    start_marker = "cadet_dynasty_names = {"
    end_marker = "}"
    start_index = content.index(start_marker) + len(start_marker)
    end_index = content.index(end_marker, start_index)
    extracted_parts = content[start_index:end_index].strip()

    # Creates empty thing, which gets filled with stuff later on
    extracted_names = []

    # Write down the names and remove comment lines
    for line in extracted_parts.split('\n'):
        line = line.strip()
        if line.startswith('{') and line.endswith('}'):
            extracted_names.append(line[1:-1].strip())

    # Dynasty names
    start_marker = "dynasty_names = {"
    end_marker = "}"
    start_index = content.index(start_marker) + len(start_marker)
    end_index = content.index(end_marker, start_index)
    extracted_parts = content[start_index:end_index].strip()

    # Processing
    for line in extracted_parts.split('\n'):
        line = line.strip()
        if line.startswith('{') and line.endswith('}'):
            extracted_names.append(line[1:-1].strip())
    
    
    # Male names
    start_marker = "male_names = {"
    end_marker = "}"
    start_index = content.index(start_marker) + len(start_marker)
    end_index = content.index(end_marker, start_index)
    extracted_parts = content[start_index:end_index].strip()

    # Processing
    for line in extracted_parts.split('\n'):
        line = line.strip()
        if line and not line.startswith('#'):
            extracted_names.extend(line.split())

    # Female names
    start_marker = "female_names = {"
    end_marker = "}"
    start_index = content.index(start_marker) + len(start_marker)
    end_index = content.index(end_marker, start_index)
    extracted_parts = content[start_index:end_index].strip()

    # Processing
    for line in extracted_parts.split('\n'):
        line = line.strip()
        if line and not line.startswith('#'):
            extracted_names.extend(line.split())

    # Remove duplicates and alphabetise the names
    extracted_names = sorted(set(extracted_names))

# Writing the extracted names to the new file
with open(new_file, "w") as file:
    for name in extracted_names:
        file.write(f'{name}:0 "{name}"\n')
