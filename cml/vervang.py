import os
import fnmatch

def replace_underscores_in_filenames():
    # Define the patterns to search for .yml and .yaml files
    patterns = ['*.yml', '*.yaml']

    # Walk through the directory tree
    for dirpath, dirnames, filenames in os.walk('.'):
        for pattern in patterns:
            for filename in fnmatch.filter(filenames, pattern):
                if '_' in filename:
                    # Construct the full path to the original file
                    original_file = os.path.join(dirpath, filename)
                    
                    # Replace underscores with hyphens in the file name
                    new_filename = filename.replace('_', '-')
                    new_file = os.path.join(dirpath, new_filename)
                    
                    # Rename the file
                    os.rename(original_file, new_file)
                    print(f'Renamed: {original_file} to {new_file}')
                    
replace_underscores_in_filenames()
