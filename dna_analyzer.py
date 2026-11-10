
# DNA SEQUENCE ANALYZER
# B.Tech Bioinformatics + AI Project

# -----------------------------------------
# FEATURE 1: VALIDATE DNA SEQUENCE
# -----------------------------------------

def validate_dna(sequence):

    sequence = sequence.upper().strip()

    valid_bases = {"A", "T", "G", "C"}

    if not sequence:
        raise ValueError("DNA sequence cannot be empty.")

    if not set(sequence).issubset(valid_bases):
        raise ValueError(
            "Invalid DNA sequence! Only A, T, G, C are allowed."
        )

    return sequence


# -----------------------------------------
# FEATURE 2: CALCULATE GC CONTENT
# -----------------------------------------

def calculate_gc_content(sequence):

    sequence = validate_dna(sequence)

    g = sequence.count("G")
    c = sequence.count("C")

    gc_content = ((g + c) / len(sequence)) * 100

    return round(gc_content, 2)


# -----------------------------------------
# FEATURE 3: FIND COMPLEMENTARY DNA
# -----------------------------------------

def get_complement(sequence):

    sequence = validate_dna(sequence)

    base_pairs = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    complement = ""

    for base in sequence:
        complement += base_pairs[base]

    return complement


# -----------------------------------------
# FEATURE 4: FIND REVERSE COMPLEMENT
# -----------------------------------------

def get_reverse_complement(sequence):

    complement = get_complement(sequence)

    reverse_complement = complement[::-1]

    return reverse_complement


# -----------------------------------------
# FEATURE 5: ANALYZE DNA
# -----------------------------------------

def analyze_dna(sequence, name="DNA Sequence"):

    sequence = validate_dna(sequence)

    length = len(sequence)

    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")

    gc_content = calculate_gc_content(sequence)

    complement = get_complement(sequence)

    reverse_complement = get_reverse_complement(sequence)

    # Display results

    print("\n========== DNA ANALYSIS ==========")

    print("Sequence Name:", name)

    print("Original DNA:", sequence)

    print("Sequence Length:", length, "bp")

    print("\nNucleotide Count:")

    print("Adenine (A):", a)
    print("Thymine (T):", t)
    print("Guanine (G):", g)
    print("Cytosine (C):", c)

    print("\nGC Content:", gc_content, "%")

    print("\nComplementary DNA:", complement)

    print("Reverse Complement:", reverse_complement)

    print("==================================")

    # Return results for comparison

    return {
        "name": name,
        "length": length,
        "gc_content": gc_content,
        "complement": complement,
        "reverse_complement": reverse_complement
    }


# -----------------------------------------
# FEATURE 6: READ FASTA FILE
# -----------------------------------------

def read_fasta(filename):

    sequences = []

    name = ""
    sequence = ""

    try:

        with open(filename, "r") as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                if line.startswith(">"):

                    # Save previous sequence

                    if name and sequence:
                        sequences.append((name, sequence))

                    name = line[1:].strip()

                    sequence = ""

                    if not name:
                        raise ValueError(
                            "FASTA header cannot be empty."
                        )

                else:

                    if not name:
                        raise ValueError(
                            "FASTA sequence must start with a header (>)."
                        )

                    sequence += line

            # Save the final sequence

            if name and sequence:
                sequences.append((name, sequence))

    except FileNotFoundError:

        print("Error: FASTA file not found!")

        return []

    except ValueError as error:

        print("Error:", error)

        return []

    return sequences


# -----------------------------------------
# FEATURE 7: COMPARE DNA SEQUENCES
# -----------------------------------------

def compare_sequences(results):

    if not results:

        print("No valid sequences to compare.")

        return

    # Highest GC content

    highest_gc = max(
        results,
        key=lambda item: item["gc_content"]
    )

    # Lowest GC content

    lowest_gc = min(
        results,
        key=lambda item: item["gc_content"]
    )

    # Longest sequence

    longest = max(
        results,
        key=lambda item: item["length"]
    )

    # Average GC content

    average_gc = sum(
        item["gc_content"] for item in results
    ) / len(results)

    # Display comparison

    print("\n========== SEQUENCE COMPARISON ==========")

    print("\nHighest GC Content:")

    print(highest_gc["name"])

    print(highest_gc["gc_content"], "%")

    print("\nLowest GC Content:")

    print(lowest_gc["name"])

    print(lowest_gc["gc_content"], "%")

    print("\nLongest Sequence:")

    print(longest["name"])

    print(longest["length"], "bp")

    print("\nAverage GC Content:")

    print(round(average_gc, 2), "%")

    print("=========================================")


# -----------------------------------------
# FEATURE 8: GC CONTENT VISUALIZATION
# -----------------------------------------

def plot_gc_content(results):

    if not results:

        print("No valid sequences to plot.")

        return

    # Import Matplotlib only when plotting

    import matplotlib.pyplot as plt

    names = [
        item["name"] for item in results
    ]

    gc_values = [
        item["gc_content"] for item in results
    ]

    plt.figure(figsize=(10, 6))

    plt.bar(names, gc_values)

    plt.title("GC Content Comparison")

    plt.xlabel("DNA Sequences")

    plt.ylabel("GC Content (%)")

    plt.ylim(0, 100)

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()


# -----------------------------------------
# MAIN PROGRAM
# -----------------------------------------

def main():

    print("===================================")

    print("       DNA SEQUENCE ANALYZER")

    print("===================================")

    filename = input("\nEnter FASTA filename: ")

    sequences = read_fasta(filename)

    if not sequences:

        print("No sequences found.")

        return

    print("\nTotal sequences found:", len(sequences))

    results = []

    # Analyze each DNA sequence

    for name, sequence in sequences:

        try:

            result = analyze_dna(sequence, name)

            results.append(result)

        except ValueError as error:

            print("\nSkipping sequence:", name)

            print("Reason:", error)

    # Compare sequences

    compare_sequences(results)

    # Display graph

    if results:

        plot_gc_content(results)


# -----------------------------------------
# RUN PROGRAM
# -----------------------------------------

if __name__ == "__main__":

    main()
