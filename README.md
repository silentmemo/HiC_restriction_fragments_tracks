# Hi-C restriction fragments visualization

## Motivation

In restriction enzyme digestion Hi-C experiments, restriction fragments is one of the factor that limits the resolutions of the Hi-C matrix. When display in 1-D tracks, it may be informative to show the individual restriction fragments. 

* this repo is written with the help of AI.  

***
## Directions
1. Generate a restriction fragments bed file, each record is a restriction fragment
2. convert that into a bed3+9 format
3. change the color to interleave black and  gray
4. generate a track line description for copy and paste
5. provide instruction to convert to bigbed format

Define user input:
1. path to restriction fragments bed file
2. track line descriptions
3. output name 

Expected output:
1. bigbed file
2. trackline description

Make it interactive for better user experience. It is likely that this script will only be used once.
***

## Description of the function of the python script

This script is a command-line tool that converts a BED file to both BED3+9 and bigBed formats. The tool takes three required arguments: the path to the input BED file, the path to a chromosome sizes file, and the path to the output files (without extension).

After parsing the command-line arguments, the tool prompts the user to enter a track name and description. It then converts the input BED file to BED3+9 format and writes the result to an output BED file. The tool then prints a track line, and converts the output BED file to bigBed format using the bedToBigBed command.

If the bedToBigBed command is not found on the user's system, the tool prints a warning message and provides a link to download the command. The tool also provides instructions on how to ensure that the downloaded command has execute permissions.

### To run the script
Suppose we have a BED file called my_bed_file.bed and a chromosome sizes file called chrom_sizes.txt, and we want to convert the BED file to both BED3+9 and bigBed formats with output files named my_output_files.

We would run the following command:
```{python}
python generate_rf_tracks.py -i my_bed_file.bed -c chrom_sizes.txt -o my_output_files
```
