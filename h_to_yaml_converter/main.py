import re

class Converter:
    def __init__(self):
        self.file_content = None
        self.define_finder = re.compile(r'#define\s+(?P<word>\w+)\s+(?P<data>\w+)')
        self.define_finder_operators = re.compile(r'#define\s+(?P<word>\w+)\s+\((?P<data>[^\)]+)\)')

    def file_opener(self, file_path):
        with open(file_path, 'r') as file:
            file_contents = file.read()
        self.file_content = file_contents

    def conv_h_yaml(self, path_h, path_yaml):
        self.file_opener(path_h)
        defines = self.defines_finder_fun()
        self.defines_formatter_yaml(path_yaml, defines)
        
    def defines_finder_fun(self):
        define_finder_matches = self.define_finder.finditer(self.file_content)
        define_finder_matches_oper = self.define_finder_operators.finditer(self.file_content)
        return_list = []
        for match in define_finder_matches:
            word = match.group('word')
            data = match.group('data')
            return_list.append((word,data))
        for match in define_finder_matches_oper:
            word = match.group('word')
            data = match.group('data')
            data = f'({data})'
            return_list.append((word,data))
        return return_list
    
    def defines_formatter_yaml(self, file_path, defines_list):
        with open(file_path, 'w') as file:
            #everything in define will come under the common label
            file.write("common:\n")
            #write all the defines in the encodings.h
            for define in defines_list:
                file.write(f' {define[0]}: {define[1]}\n')
file_path_header = '/home/hammad/USEFUL_SCRIPTS/Useful-Scipts/h_to_yaml_converter/encodings.h'
file_path_yaml = '/home/hammad/USEFUL_SCRIPTS/Useful-Scipts/h_to_yaml_converter/encodings.yaml'
conv = Converter()
conv.conv_h_yaml(file_path_header, file_path_yaml)
