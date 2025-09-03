import os

input_folder = "results/plasmid_hits_250501"
output_file = "results/cpe_plasmid_search_winner_summary.tsv"

# Open output file for writing
with open(output_file, "w") as out:
    # Write header
    out.write("sample\tcpe_on_plasmid\tidentity\tshared_hashes\tp_value\tcpe_plasmid_match\n")

    # Loop over all Mash result files
    for filename in os.listdir(input_folder):
        if filename.endswith("_mash_screen.tsv"):
            filepath = os.path.join(input_folder, filename)
            sample = filename.replace("_contigs_cpe_contig_mash_screen.tsv", "")

            with open(filepath, "r") as f:
                lines = f.readlines()

                if lines:
                    # Take first line (top hit)
                    cols = lines[0].strip().split("\t")
                    identity = cols[0]
                    shared_hashes = cols[1]
                    p_value = cols[3]
                    match = cols[5] if len(cols) > 5 else "N/A"
                    cpe_on_plasmid = "Yes"
                else:
                    identity = shared_hashes = p_value = match = "N/A"
                    cpe_on_plasmid = "No"

                # Write to output file
                out.write(f"{sample}\t{cpe_on_plasmid}\t{identity}\t{shared_hashes}\t{p_value}\t{match}\n")

print(f"Summary saved to {output_file}")

