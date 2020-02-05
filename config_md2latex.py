# -*- coding: utf-8 -*-
# NOTE: in Sublime Text, "(groups) in regex" are "$1 in regex".
#             in Python, "(groups) in regex" are "\g<1> in regex".
# IMPORTANT: the \t in \textXX must be double escaped to escape the \ and the \t to prevent a tab from being inserted!
#				*\\\\t*


# regular expression strings in format [(find, replace), (find2, replace2)...]
regexStrings = [

	# minted Codeblock Python
	(r"""(.*)Codeblock \#(\d*): Lines (\d*)-(\d*)(.*)""",
	 r"""\n\\begin{minted}[xleftmargin=15pt,frame=lines,framesep=1mm,firstnumber=\g<3>,linenos]{python}\nCodeblock \g<2>: Lines \g<3>-\g<4>\n\\end{minted}\n"""),

# 	# MARKDOWN

# 	# be careful with this one -- if there is a comment in a code block, it fails
	(r"""^# (.*)""",
	 r"""\n%------------------------------------------------------------------------------------\n\n\\section{\g<1>}"""),

	(r"""^## (.*)""",
	 r"""\n%------------------------------------------------------------------------------------\n\n\\subsection{\g<1>}"""),

	(r"""^### (.*)""",
	 r"""\n%------------------------------------------------------------------------------------\n\n\\subsubsection{\g<1>}"""),

	# Project Structure
	(r"PROJECT STRUCTURE}",
	 r"""\n\nReview project structure\n\n\\begin{minted}[xleftmargin=15pt,frame=lines,framesep=1mm]{text}\nPROJECT STRUCTURE\n\\end{minted}\n"""),

	# long dash
	(r" -- ",
	 r" — "),

	# Figure reference
	(r"Figure X",
	 r"Figure \\ref{fig:bundle:TBD}"),

	# console COMMAND OUTPUT
	(r"""[\s-]*COMMAND[\s-]*OUTPUT""",
	 r"""\n\\begin{minted}[xleftmargin=15pt,frame=lines,framesep=1mm]{console}\nCOMMAND + OUTPUT\n\\end{minted}\n"""),

	# bold + italics
	(r"""\*\*\*(.*?)\*\*\*""",
	 r"""\\textbf{\\textit{\g<1>}}"""),

	# ##### must be under ***triple*** stars #####
	# bold Line X
	(r"""\*\*Line (\d*)\*\*""",
	 r"""\\textbf{Line \g<1>}"""),

	# bold Lines X-X
	(r"""\*\*Lines (\d*)-(\d*)\*\*""",
	 r"""\\textbf{Lines \g<1>-\g<2>}"""),

	# bold Lines X and X
	(r"""\*\*Lines (\d*) and (\d*)\*\*""",
	 r"""\\textbf{Lines \g<1> and \g<2>}"""),

	# bold italics
	(r"""\*\*\*(.*?)\*\*\*""",
	 r"""\\textbf{\\textit{\g<1>}}"""),

	# bold generic
	(r"""\*\*(.*?)\*\*""",
	 r"""\\textbf{\g<1>}"""),

	# ##### must be under **double** stars #####
	# italics
	(r"""\*{1}(.*?)\*{1}""",
	 r"""\\textit{\g<1>}"""),

	# italics (x, y)-coordinates
	(r""" \(x, y\)-(.*) """,
	 r""" \\textit{\(x, y\)}-\g<1> """),

	# preformatted CL arg
	(r"""`--(.*?)`""",
	 r"""\\texttt{-{}-\g<1>}"""),

	# preformatted filename
	(r"`(.*?).py`",
	 r"""\\texttt{\g<1>.py}"""),

	# preformatted
	(r"""`(.*?)`""",
	 r"""\\texttt{\g<1>}""")

]