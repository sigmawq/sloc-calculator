import argparse
import SlocCalculator

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("location", help="Location to calculate SLOC count in")
    parser.add_argument("--fe", '--files-exclude', nargs="+", help="File types to exclude")
    parser.add_argument("--de", '--dir-exclude', nargs="+", help="Directories to exclude")
    args = parser.parse_args()

    excluded_files = []
    excluded_directories = []
    if (args.fe):
        excluded_files = args.fe

    if (args.de):
        excluded_directories = args.de

    try:
        sloc_calculator = SlocCalculator.SlocCalculator(args.location, excluded_files, excluded_directories)
        sloc_calculator.get_detailed_report()
    except Exception as e:
        print(str(e))

main()

