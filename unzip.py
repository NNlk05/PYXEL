import zip

def unzip(zip_file, extract_to):
    with zip.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        file_list = zip_ref.namelist()
    file_structure = {}
    for file_name in file_list:
        if file_name.endswith('/'):
            file_structure[file_name] = {}
        else:
            with zip_ref.open(file_name) as file:
                file_structure[file_name] = file.read()
    return file_structure