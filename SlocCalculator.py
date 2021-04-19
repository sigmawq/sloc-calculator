import glob
import os

class SlocCalculator:
    def __init__(self, target_folder: str, excluded_files: list, excluded_folders: list):
        if not os.path.exists(target_folder) or not os.path.isdir(target_folder):
            raise Exception("Target location does not exist/is not a folder")

        self.file_count = 0
        self.files = {}
        self.restricted_files = excluded_files
        SlocCalculator.ensure_allowed_files_have_dot(self)
        self.excluded_folders = excluded_folders
        self.target_folder = target_folder

        self.form_file_sloc_dictionary()

    def get_base_report(self):
        sloc_total = 0
        for filename in self.files:
            try:
                sloc_total = sloc_total + self.files[filename]
            except:
                pass

        print(sloc_total, 'SLOC')


    def get_detailed_report(self):
        sloc_total = 0
        for filename in self.files:
            try:
                sloc_total = sloc_total + self.files[filename]
            except:
                pass

        print(sloc_total, 'SLOC')
        self.state_all_file_statistics()

    def state_all_file_statistics(self):
        for filename in self.files:
            print(filename, ':', self.files[filename])

    def add_file(self, file: str):
        if file in self.files:
            file = file + " - duplicate"
        else:
            self.files[file] = 0

    def form_file_sloc_dictionary(self):
        for root, subFolder, files in os.walk(self.target_folder):
            subFolder[:] = [d for d in subFolder if d not in self.excluded_folders]
            for item in files:
                if self.file_is_allowed(item):
                    filename = os.path.join(root, item)
                    self.add_file(filename)
                    self.files[filename] = SlocCalculator.get_sloc_count(filename)

    def file_is_allowed(self, filename: str) -> bool:
        ftype: str
        for ftype in self.restricted_files:
            if filename.endswith(ftype):
                return False
        return True

    def ensure_allowed_files_have_dot(self):
        for i in range(len(self.restricted_files)):
            self.restricted_files[i] = SlocCalculator.add_dot_to_file_type_if_needed(self.restricted_files[i])

    @staticmethod
    def get_sloc_count(filename: str):
        try:
            file = open(filename)
            line_count = 0
            while True:
                if file.readline() != "":
                    line_count += 1
                else:
                    break

            return line_count
        except:
            print('Cannot read: ', filename)

    @staticmethod
    def add_dot_to_file_type_if_needed(filename: str) -> str:
        if not filename.startswith('.'):
            filename = '.' + filename
        return filename

