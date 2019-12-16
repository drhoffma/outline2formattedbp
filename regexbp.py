# import the necessary packages
import argparse
import re

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--format", type=str, required=True,
	choices=["txt2wp", "md2wp", "md2latex", "temp"])
ap.add_argument("-i", "--input", type=str, required=True,
	help="path to input text file")
ap.add_argument("-o", "--output", type=str, required=True,
	help="path to output text file"),
ap.add_argument("-t", "--title", type=str, default=None,
	help="the blog post title")
args = vars(ap.parse_args())

# handle the type of config to import

# Markdown -> wp html
if args["format"] == "md2wp":
	import config_md2wp as config
	if args["title"] == "":
		print("[ERROR] you are formatting a blog post and you didn't "
			"provide a title")
		sys.exit(1)

# Dropbox paper md export -> LaTeX book chapter
elif args["format"] == "md2latex":
	import config_md2latex as config

# WP (evernote PDF outline -> text -> wp html)
elif args["format"] == "txt2wp":
	import config_txt2wp as config
	if args["title"] == "":
		print("[ERROR] you are formatting a blog post and you didn't "
			"provide a title")
		sys.exit(1)

elif args["format"] == "temp":
	import config_temp  as config

# catch all (but arg parser should have caught it already with
# *choices*)
else:
	print("[ERROR] your format is invalid")

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

			# print("DEBUG")
			# print(rs)

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
	lines = re.sub(r"\.\n([A-Z])", ".\n\n\g<1>", lines)

	if args["format"] == "latex":
		lines = re.sub(r"[\s-]*COMMAND[\s-]*OUTPUT",
			r"\n\n\\begin{minted}[xleftmargin=15pt,frame=lines,framesep=1mm]{console}\nCOMMAND + OUTPUT\n\\end{minted}\n",
			lines)

	elif args["format"] == "wp":
		lines = re.sub(r"[\s-]*COMMAND[\s-]*OUTPUT",
			r"""\n<pre class="start-line:1 lang:sh decode:true " title="@TITLE@">COMMAND OUTPUT</pre>\n""",
			lines)

	if args["title"] is not None:
		# add the title to code blocks (a hack...see the config.py)
		lines = re.sub(r"@TITLE@", args["title"], lines)


# open the file for writing and write the lines
o = open(args["output"], "w")
o.write(lines)

# close the file
o.close()
