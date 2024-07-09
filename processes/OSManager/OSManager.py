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

    def rename(self, file_name, account_number):
        file_path = os.path.join(self.directory, file_name)
        new_file_path = os.path.join(self.directory, str(account_number) + ".txt")
        
        try:
            os.rename(file_path, new_file_path)
            return str(account_number) + ".txt"
        except OSError as e:
            return None