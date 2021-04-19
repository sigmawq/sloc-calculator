import argparse
import SlocCalculator

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("location", help="Location to calculate SLOC count in")
    parser.add_argument("--fe", '--files-exclude', nargs="+", help="File types to exclude")
    parser.add_argument("--de", '--dir-exclude', nargs="+", help="Directories to exclude")
    parser.add_argument("--d", action='store_true', help="Show detailed output")
    parser.add_argument("--debug", action='store_true', help="Show debug info")
    args = parser.parse_args()

    excluded_files = []
    excluded_directories = []
    if args.fe:
        excluded_files = args.fe

    if args.de:
        excluded_directories = args.de

    if args.debug:
        print("Target location:", args.location)
        print("File type excluded:", args.fe)
        print("Directories excluded:", args.de)

    try:
        sloc_calculator = SlocCalculator.SlocCalculator(args.location, excluded_files, excluded_directories)
        if (args.d):
            sloc_calculator.get_detailed_report()
        else:
            sloc_calculator.get_base_report()
    except Exception as e:
        print(str(e))

main()

