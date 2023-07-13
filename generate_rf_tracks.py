import argparse
import os
import subprocess

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Convert a BED file to bigBed and BED3+9 formats')
    parser.add_argument('-i', '--input', dest='bed_file', required=True, help='Path to input BED file')
    parser.add_argument('-c', '--chrom', dest='chrom_sizes_file', required=True, help='Path to chromosome sizes file')
    parser.add_argument('-o', '--output', dest='output_file', required=True, help='Path to output files (without extension)')
    args = parser.parse_args()

    # Prompt user for track line information
    track_name = input("Please enter the track name: ")
    track_description = input("Please enter the track description: ")
    track_url = "URL_TO_THE_bigBed_FILE"

    # Define output file names
    output_bed_file = args.output_file + ".bed"
    output_bigbed_file = args.output_file + ".bb"

    # Sort the input BED file by chromosome and start position
    try:
        subprocess.run(["sort", "-k1,1", "-k2,2n", "--field-separator", "\t", "--output", args.bed_file, args.bed_file], check=True, env=dict(os.environ, LC_COLLATE='C'))
    except FileNotFoundError:
        # Print warning message to user
        print("Warning: sort not found on your system. Please ensure that the input BED file is sorted by chromosome and start position.")
        print("Alternatively, you can download and install sort from the following link to use this script:")
        print("http://ftp.gnu.org/gnu/coreutils/")
        return
    except:
        print("Error: Failed to sort input BED file.")
        return
    
    # Convert BED file to BED3+9 format
    item_rgb_values = ["0,0,0", "150,150,150"]  # Define the two itemRgb values
    item_rgb_index = 0  # Initialize the itemRgb index
    try:
        with open(args.bed_file, "r") as input_file, open(output_bed_file, "w") as output_file:
            for line in input_file:
                # Split the line into its 6 columns
                chrom, start, end, name, score, strand = line.strip().split("\t")
                strand = "."
                # Add the additional columns to the line
                thick_start = start
                thick_end = end
                item_rgb = item_rgb_values[item_rgb_index]
                block_count = "1"
                block_sizes = str(int(end) - int(start))
                block_starts = "0"

                # Write the modified line to the output file in BED3+9 format
                output_file.write("\t".join([chrom, start, end, name, score, strand, thick_start, thick_end, item_rgb, block_count, block_sizes, block_starts]) + "\n")
             # Update the itemRgb index
                item_rgb_index = (item_rgb_index + 1) % len(item_rgb_values)
    except FileNotFoundError:
        print("Error: One or more of the input files does not exist.")
        return
    except:
        print("Error: Failed to convert BED file to BED3+9 format.")
        return
    
    # Print track line to standard output
    print('## The following track line should be added to the trackDb.txt file:')
    print('## --------------------------------------------------------------------')
    print('## track type=bigBed name="{}" description="{}" bigDataUrl="{}"'.format(track_name, track_description, track_url))
    print('## --------------------------------------------------------------------')
    print('## Note: Please copy and modify the track line as needed.')
    
    # Convert BED file to bigBed format
    try:
        subprocess.run(["bedToBigBed", output_bed_file, args.chrom_sizes_file, output_bigbed_file], check=True)
    except FileNotFoundError:
        # Print warning message to user
        print("Warning: bedToBigBed not found on your system. Please download and install it from the following link to use this script:")
        print("http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/bedToBigBed")
        print("After downloading, please ensure that the file has execute permissions by running the following command:")
        print("chmod +x bedToBigBed")
    except:
        print("Error: Failed to convert BED3+9 file to bigBed format.")
        return
    
main()