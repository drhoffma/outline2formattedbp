# -*- coding: utf-8 -*-
# NOTE: in Sublime Text, "(groups) in regex" are "$1 in regex".
#             in Python, "(groups) in regex" are "\g<1> in regex".


# regular expression strings in format [(find, replace), (find2, replace2)...]
regexStrings = [

	# minted Codeblock Python
	(r"""(.*)Codeblock \#(\d*): Lines (\d*)-(\d*)(.*)""",
	 r"""\\begin{minted}\[xleftmargin=15pt,frame=lines,framesep=1mm,firstnumber=\g<3>,linenos\]{python}\nCodeblock \g<2>: Lines \g<3>-\g<4>\n\\end{minted}"""),

	# Project Structure
	(r"\\section\{Project Structure\}",
	 r"""\\section{Project Structure}\n\nReview project structure\n\n\\begin{minted}\[xleftmargin=15pt,frame=lines,framesep=1mm\]{console}\nPROJECT STRUCTURE\n\\end{minted}\n"""),

	(r"—",
	 r"--"),

	# Figure reference
	(r"Figure X",
	 r"Figure \\ref{fig:bundle:TBD}"),

	# (r"Summary",
	 # r"\\section\{Summary\}"),

	(r""" \_(.*?)\_ """,
	 r""" \\textit{\g<1>} """),

	# console COMMAND OUTPUT
	(r"""COMMAND( ?\n?)OUTPUT ?(.*)""",
	 r"""\\begin{minted}\[xleftmargin=15pt,frame=lines,framesep=1mm\]{console}\n\n\\end{minted}\n"""),

	# italics (x, y)-coordinates
	(r"""\(x, y\)-(.*) """,
	 r"""\\textit{\(x, y\)}-\g<1> """),

	# bold Line X
	(r"""\*\*Line (\d*)\*\*""",
	 r"""\\textbf{Line \g<1>}"""),

	# bold Lines X-X
	(r"""\*\*Lines (\d*)-(\d*)\*\*""",
	 r"""\\textbf{Lines \g<1>-\g<2>}"""),

	# bold Lines X and X
	(r"""\*\*Lines (\d*) and (\d*)\*\*""",
	 r"""\\textbf{Lines \g<1> and \g<2>}"""),

	# bold generic
	(r""" \*\*(.*?)\*\* """,
	 r""" \\textbf{\g<1>} """),

	# must be under the double stars
	(r""" \*(.*?)\* """,
	 r""" \\textit{\g<1>} """),

	# preformatted CL arg
	(r""" `--(.*?)` """,
	 r""" \\texttt{-{}-\g<1>} """),

	# preformatted filename
	(r"`(.*?).py`",
	 r"""\\texttt{\g<1>.py}"""),

	# preformatted
	(r""" `(.*?)` """,
	  """ \\texttt{\g<1>} """)

]