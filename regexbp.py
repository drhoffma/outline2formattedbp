# import the necessary packages
import argparse
import sys
import re

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--format", type=str, required=True,
	choices=["txt2wp", "md2wp-crayon", "md2wp-enlighter", "md2latex", "temp"])
ap.add_argument("-i", "--input", type=str, required=True,
	help="path to input text file")
ap.add_argument("-o", "--output", type=str, required=True,
	help="path to output text file"),
ap.add_argument("-t", "--title", type=str, default="",
	help="the blog post title")
args = vars(ap.parse_args())

# handle the type of config to import

# Markdown -> wp html ****CRAYON****
if args["format"] == "md2wp-crayon":
	import config_md2wp as config
	if args["title"] == "":
		print("[ERROR] you are formatting a blog post and you didn't "
			"provide a title")
		sys.exit(1)

# Markdown -> wp html ****ENLIGHTER****
elif args["format"] == "md2wp-enlighter":
	import config_md2wp_enlighter as config
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

	if args["format"] == "md2latex":
		lines = re.sub(r"[\s-]*COMMAND[\s-]*OUTPUT",
			r"\n\n\\begin{minted}[xleftmargin=15pt,frame=lines,framesep=1mm]{console}\nCOMMAND + OUTPUT\n\\end{minted}\n",
			lines)

	# elif args["format"] == "md2wp-crayon" or args["format"] == "md2wp-enlighter":
	# 	lines = re.sub(r"[\s-]*COMMAND[\s-]*OUTPUT",
	# 		r"""\n<pre class="start-line:1 lang:sh decode:true " title="@TITLE@">COMMAND OUTPUT</pre>\n""",
	# 		lines)

	# add the title to code blocks (a hack...see the config.py)
	if args["title"] is not None:
		lines = re.sub(r"@TITLE@", args["title"], lines)


# open the file for writing and write the lines
o = open(args["output"], "w")
o.write(lines)

# close the file
o.close()

# here begins the unique group number for enlighter blocks
# each enligher block has a comment and the codeblock with a group number
# regex above replaces  with @GROUPA@ and @GROUPAA@ <-- these correspond
# in the loop below, we'll make the unique group number the line number
# of the HTML file but we have to ensure that we maintain the number
# to associate A with AA, B with BB, C with CC and so on

if args["format"] == "md2wp-enlighter":
	# open just the output file
	with open(args["output"], "r") as o:
		# read the whole file
		lines = o.readlines()
		lastI = None

		print(lines[1])

		for (i, line) in enumerate(lines):

			if "@GROUPA1@" in line or "@GROUPB1@" in line or "@GROUPC1@" in line or "@GROUPD1@" in line:
				lastI = i
				line = re.sub(r"@GROUPA1@", str(i), line)
				line = re.sub(r"@GROUPB1@", str(i), line)
				line = re.sub(r"@GROUPC1@", str(i), line)
				line = re.sub(r"@GROUPD1@", str(i), line)

			elif "@GROUPA2@" in line or "@GROUPB2@" in line or "@GROUPC2@" in line or "@GROUPD2@" in line:
				line = re.sub(r"@GROUPA2@", str(lastI), line)
				line = re.sub(r"@GROUPB2@", str(lastI), line)
				line = re.sub(r"@GROUPC2@", str(lastI), line)
				line = re.sub(r"@GROUPD2@", str(lastI), line)
				lastI = None

			lines[i] = line


	# open the file for writing and write the lines
	with open(args["output"], "w") as o:
		for item in lines:
			o.write("%s\n" % item)


