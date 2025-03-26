import argparse


def nbib_to_bib(nbib_file, bib_file):
    with open(nbib_file, "r", encoding="utf-8") as f:
        nbib_data = f.read()

    entries = []
    for entry in nbib_data.strip().split("\n\n"):
        lines = entry.split("\n")
        bib_entry = "@article{"
        pmid = None  # Initialize PMID for unique key
        for line in lines:
            if line.startswith("PMID-"):
                pmid = line.split("- ")[1].strip()
            elif line.startswith("TI  -"):
                bib_entry += f"  title = {{{line[6:].strip()}}},\n"
            elif line.startswith("AU  -"):
                bib_entry += f"  author = {{{line[6:].strip()}}},\n"
            elif line.startswith("DP  -"):
                bib_entry += f"  year = {{{line[6:].strip()}}},\n"

        if pmid:
            bib_entry = f"@article{{{pmid},\n" + bib_entry[9:]  # Replace placeholder
        bib_entry += "}"
        entries.append(bib_entry)

    with open(bib_file, "w", encoding="utf-8") as f:
        f.write("\n\n".join(entries))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a .nbib file to .bib format.")
    parser.add_argument("input_file", help="Path to the input .nbib file")
    parser.add_argument("output_file", help="Path to save the output .bib file")

    args = parser.parse_args()

    nbib_to_bib(args.input_file, args.output_file)
    print(f"Conversion completed: {args.input_file} -> {args.output_file}")
