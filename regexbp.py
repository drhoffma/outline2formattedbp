# import the necessary packages
import config
import argparse
import re

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str,
	help="path to input text file")
ap.add_argument("-t", "--title", type=str,
	help="the blog post title")
ap.add_argument("-o", "--output", type=str,
	help="path to output text file")
args = vars(ap.parse_args())

# regex strings
regexStrings = config.regexStrings

# open the file for writing
o = open(args["output"], "w")

# open the file for reading
with open(args["input"], "r+") as f:
	# read lines one at a time
	for line in f.readlines():
		# loop over regular expression strings
		for rs in regexStrings:
			# extract the find/replace patterns
			findPattern = rs[0]
			replacePattern = rs[1]

			# perform the regex replacement
			line = re.sub(findPattern, replacePattern, line)

		# write the line to the output file
		o.write(line)

# close the files
f.close()
o.close()

# open just the output file
with open(args["output"], "r") as o:
	# read the whole file
	lines = o.read()

	# remove double blanks
	lines = re.sub(r"\n\s*\n", "\n\n", lines)

	# new lines for the start of sentences (Wordpress spacing)
	lines = re.sub(r".\n([A-Z])", ".\n\n\g<1>", lines)

	# add the title to code blocks (a hack...see the config.py)
	lines = re.sub(r"@TITLE@", args["title"], lines)


# open the file for writing and write the lines
o = open(args["output"], "w")
o.write(lines)

# close the file
o.close()