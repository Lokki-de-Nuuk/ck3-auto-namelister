# Function for extracting names
def extract_names(content, start_marker, end_marker, is_list_format):
    extracted_names = []
    start_index = content.find(start_marker) + len(start_marker)
    end_index = content.find(end_marker, start_index)
    extracted_parts = content[start_index:end_index].strip()

    for line in extracted_parts.split('\n'):
        line = line.strip()
        # Ignore comment lines
        if line and not line.startswith('#'):
            if is_list_format:
                # If a line is in brackets then remove them
                if line.startswith('{') and line.endswith('}'):
                    extracted_names.extend(line[1:-1].strip().split())
            else:
                extracted_names.append(line)

    return extracted_names


# File path goes here, make sure to replace \ with \\. Double it up essentially.
file_path = "D:\\L\\Projects and adventures\\CK3\\Workshop\\00_mayan.txt"

# Output file is txt paste the contents yourself to the appropriate file.
new_file = "D:\\L\\Projects and adventures\\CK3\\Workshop\\name_listed_mayan.txt"

# Extracting specific parts from the file
with open(file_path, "r") as file:
    content = file.read()

    # Cadet dynasty names
    cadet_dynasty_names = extract_names(content, "cadet_dynasty_names =", "}", True)

    # Dynasty names
    dynasty_names = extract_names(content, "dynasty_names =", "}", True)

    # Male names
    male_names = extract_names(content, "male_names =", "}", False)

    # Female names
    female_names = extract_names(content, "female_names =", "}", False)

    # Combine all extracted names
    extracted_names = sorted(set(cadet_dynasty_names + dynasty_names + male_names + female_names))

# Writing the extracted names to the new file
with open(new_file, "w") as file:
    for name in extracted_names:
        file.write(f'{name}:0 "{name}"\n')
