import SlocCalculator

excluded_files = [".txt"]
excluded_directories = ["venv", ".idea", "__pycache__"]

test = SlocCalculator.SlocCalculator("./", excluded_files, excluded_directories)
test.get_base_report()
test.get_detailed_report()


