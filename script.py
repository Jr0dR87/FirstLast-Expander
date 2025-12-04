import sys
import string

def generate_names(first_last: str):
    first_last = first_last.strip()
    if "." not in first_last:
        return []
    
    first, last = first_last.split(".", 1)
    f = first[0].lower()
    last = last.lower()
    # This is for a - z
    return [f"{f}{n}{last}" for n in string.ascii_lowercase]

def main():
    if len(sys.argv) != 4:
        print("Usage: python file_io_namegen.py <input_file> <output_file> <domain>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    domain = sys.argv[3]

    all_results = []

    with open(input_file, "r") as infile:
        for line in infile:
            line = line.strip()
            if line:
                all_results.extend(generate_names(line))

    with open(output_file, "w") as outfile:
        for item in all_results:
            outfile.write(item + "@" + domain + "\n")

    print(f"Generated {len(all_results)} items and saved to {output_file}")

if __name__ == "__main__":
    main()
