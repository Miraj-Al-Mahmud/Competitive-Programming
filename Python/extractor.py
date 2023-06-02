import os, sys
from distutils.dir_util import copy_tree


snippet_dir = "D:\\Python\\CompetitiveProgramming\\Portable\\MAVERICK\\Data\\Packages\\User\\Snippets"
to_directory = "D:\\Python\\CompetitiveProgramming\\Portable\\UserFiles\\Python\\Snippets"
text_file = "D:\\Python\\CompetitiveProgramming\\Portable\\UserFiles\\Python\\gathered.txt"


import textwrap
from fpdf import FPDF

def text_to_pdf(text, filename):
    a4_width_mm = 210
    pt_to_mm = 0.35
    fontsize_pt = 8
    fontsize_mm = fontsize_pt * pt_to_mm
    margin_bottom_mm = 10
    character_width_mm = 7 * pt_to_mm
    width_text = a4_width_mm / character_width_mm

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(True, margin=margin_bottom_mm)
    pdf.add_page()
    pdf.set_font(family='Courier', size=fontsize_pt)
    splitted = text.split('\n')

    for line in splitted:
        lines = textwrap.wrap(line, width_text)

        if len(lines) == 0:
            pdf.ln()

        for wrap in lines:
            pdf.cell(0, fontsize_mm, wrap, ln=1)

    pdf.output(filename, 'F')

def main() -> None:
	copy_tree(snippet_dir, to_directory) # copy the files
	all_files = os.listdir(to_directory) # list to an array
	with open(text_file, 'w') as f1: # open the text file
		f1.write(f"Total number of snippets >>> {len(all_files)}")
		for idx0,every_snippet in enumerate(all_files): # for every snippet
			complete_path = f"{to_directory}\\{every_snippet}" # join the paths
			with open(complete_path, 'r') as f2: # open the snipet as the text file is already opened
				lines = f2.readlines()
				for idx,line in enumerate(lines):
					if line.startswith("]]></content>"): break
					if idx == 1: # decorator at the beginning of the snippet writing or documentation
						f1.write("\n************************************************************************\n")
						f1.write(f"{idx0+1}th Snippet -> Name {every_snippet[:-16]} \n")
					if idx > 1:	f1.write(line)
	
	
	
	input_filename = text_file
	output_filename = 'C:\\Users\\miraj\\OneDrive\\Desktop\\output.pdf'
	file = open(input_filename)
	text = file.read()
	file.close()
	text_to_pdf(text, output_filename)
	


if __name__ == "__main__": main()