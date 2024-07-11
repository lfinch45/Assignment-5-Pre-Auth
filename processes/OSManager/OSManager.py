import os

class OSManager:
    
    def __init__(self, directory):
        self.directory = directory

    def read_files(self):
        items = os.listdir(self.directory)

        files = []
        for item in items:
            item_path = os.path.join(self.directory, item)
            if os.path.isfile(item_path):
                files.append(item)

        file_contents = {}

        for file in files:
            file_path = os.path.join(self.directory, file)
            try:
                with open(file_path, 'r') as f:
                    file_contents[file] = f.read()
            except Exception as e:
                print(f"Couldn't read file {file}: {e}")
            
        
        return file_contents


    def get_most_recent_element(self):
        
        items = os.listdir(self.directory)
        
        files = []
        for item in items:
            item_path = os.path.join(self.directory, item)
            if os.path.isfile(item_path):
                files.append(item)
        
        file_contents = {} 
        for file in files:
            file_path = os.path.join(self.directory, file)
            try:
                with open(file_path, 'r') as f:
                    file_contents[file] = f.read()
            except Exception as e:
                print(f"Couldn't read file {file}: {e}")
        
        last_element = list(file_contents.items())[-1]
        return last_element

    def rename(self, file_name, new_file_name):
        file_path = os.path.join(self.directory, file_name)
        new_file_path = os.path.join(self.directory, new_file_name + '.txt')
        
        try:
            os.rename(file_path, new_file_path)
            return new_file_name + '.txt'
        except OSError as e:
            return None
        
    def delete_file(self, file_name):
        file_path = os.path.join(self.directory, file_name)
        os.remove(file_path)

    def add_file(self, new_file_name, content):
        file_path = os.path.join(self.directory, new_file_name)
        with open(file_path, 'w') as file:
            file.write(content)

    def add_text_to_file(self, file_name, new_content):
        file_path = os.path.join(self.directory, file_name)
        with open(file_path, 'a') as file:
            file.write(new_content)
        
    def remove_text_from_file(self, file_name, text_to_remove):
        file_path = os.path.join(self.directory, file_name)

        with open(file_path, 'r') as file:
            contents = file.read()
        
        new_contents = contents.replace(text_to_remove, '')

        with open(file_path, 'w') as file:
            file.write(new_contents)

    def find_line_number(self, file_name, substring):
        file_path = os.path.join(self.directory, file_name)

        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if substring in line:
                    return line_number
        return None

    def find_text_in_file(self, file_name, text_to_find) -> bool:
        file_path = os.path.join(self.directory, file_name)
        with open(file_path, 'r') as file:
            contents = file.read()
        
        if text_to_find in contents:
            print(f"The text: '{text_to_find}' is on line {self.find_line_number(file_name, text_to_find)}.")