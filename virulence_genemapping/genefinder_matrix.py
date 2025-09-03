import os
import xml.etree.ElementTree as Eltree
import csv
from collections import defaultdict


# Store data: {isolate_id: {gene_name: detection_value}}
all_data = defaultdict(dict)

# Track all unique gene names
all_genes = set()

# Walk through directories and parse XML files
for subdir, _, files in os.walk("Burhan_MSc_Work"):
    for file in files:
        if file.endswith(".xml"):
            filepath = os.path.join(subdir, file)

            try:
                tree = Eltree.parse(filepath)
                root = tree.getroot()

                isolate_id = root.attrib.get("id", os.path.basename(filepath))

                for result in root.findall(".//result[@type='gene']"):
                    gene = result.attrib.get("value", "Unknown")

                    detection = "NA"
                    for res_data in result.findall("result_data"):
                        if res_data.attrib.get("type") == "detection":
                            detection = res_data.attrib.get("value", "NA")
                            break

                    all_data[isolate_id][gene] = detection
                    all_genes.add(gene)

            except Exception as e:
                print(f"Error processing {filepath}: {e}")

# Prepare output CSV
output_file = "gene_detection_matrix.csv"
gene_list = sorted(all_genes)

with open(output_file, mode="w", newline="") as f:
    writer = csv.writer(f)
    header = ["sample_id"] + gene_list
    writer.writerow(header)

    for sample_id, gene_data in all_data.items():
        row = [sample_id] + [gene_data.get(g, "NA") for g in gene_list]
        writer.writerow(row)

print(f"CSV created: {output_file}")

