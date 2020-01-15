# -*- coding: utf-8 -*-
# NOTE: in Sublime Text, "(groups) in regex" are "$1 in regex".
#             in Python, "(groups) in regex" are "\g<1> in regex".


# regular expression strings in format [(find, replace), (find2, replace2)...]
regexStrings = [

	(r" *\- ",
	 r"""\n"""),

	(r"""(.*)Codeblock \#(\d*): Lines (\d*)-(\d*)(.*)""",
	 r"""\g<1>\n\n<pre class="start-line:\g<3> lang:python decode:true " title="@TITLE@">Codeblock \g<2> Lines \g<3>-\g<4></pre>\n\n\g<5>"""),

	(r"""(.*)COMMAND OUTPUT(.*)""",
	 r"""\g<1>\n\n<pre class="start-line:1 lang:sh decode:true " title="@TITLE@">COMMAND OUTPUT</pre>\n\n\g<2>"""),

	(r"Review project structure",
	 r"""Review project structure\n\n<pre class="start-line:1 lang:sh decode:true " title="@TITLE@">$ tree --dirsfirst --filelimit 10
output</pre>\n\n...\n"""),

	(r"Figure X",
	 r"<strong>Figure X</strong>"),

	# bold italics
	(r"""\*\*\*(.*?)\*\*\*""",
	 r"""<strong><em>\g<1></em></strong>"""),

	# bold generic
	(r"""\*\*(.*?)\*\*""",
	 r"""<strong>\g<1></strong>"""),

	# ##### must be under **double** stars #####
	# italics
	(r"""\*{1}(.*?)\*{1}""",
	 r"""<em>\g<1></em>"""),

	(r"""—""",
	 r"""--"""),

	# italics
	#(r"""\_(.*?)\_""",
	# r"""<em>\g<1></em>"""),

	# italics (x, y)-coordinates
	(r""" \(x, y\)-(.*) """,
	 r""" <em>\(x, y\)</em>-\g<1> """),

	(r"JUMP TO CODE DOWNLOAD",
	 r"[jump_to_code_download]"),

	(r"""DOWNLOAD FORM""",
	 r"""[code_download_form action="" formid=""]"""),

	# preformatted filename
	(r"`(.*?).py`",
	 r"""<span class="lang:sh decode:true crayon-inline">\g<1>.py</span>"""),

	# preformatted
	(r"""`(.*?)`""",
	 r"""<span class="lang:python decode:true  crayon-inline ">\g<1></span>"""),

	# fix preformatted inline zero
	(r""">0<""",
	 r"""> 0<"""),

	(r""".Downloads.""",
	 r"""<strong><em>"Downloads"</em></strong>"""),

# 	(r"""\(x, y\)-(.*) """,
# 	 r"""<em>(x, y)</em>-\g<1> """),

# 	(r"""Line (\d*)""",
# 	 r"""<strong>Line \g<1></strong>"""),

# 	(r"""Lines (\d*)-(\d*)""",
# 	 r"""<strong>Lines \g<1>-\g<2></strong>"""),

# 	(r"""Lines (\d*) and (\d*)""",
# 	 r"""<strong>Lines \g<1> and \g<2></strong>"""),

# 	# MARKDOWN

# 	# be careful with this one -- if there is a comment in a code block, it fails
	(r"""^# (.*)""",
	 r"""<h2>\g<1></h2>"""),

	(r"""^## (.*)""",
	 r"""<h3>\g<1></h3>"""),

	(r"""^### (.*)""",
	 r"""<h4>\g<1></h2>"""),

	# (r"""_(.*)_""",
	#  r"""<em>\g<1></em>"""),

	# (r""" \*([a-zA-Z].*?)\* """,
	#  r"""<em>\g<1></em>"""),

	# (r"""\*\*(.*)\*\*""",
	#  r"""<strong>\g<1></strong>"""),

	(r"""\[(.*?)\]\((.*?)\)""",
	 r"""<a href="\g<2>" target="_blank" rel="noopener">\g<1></a>"""),

	(r"""^(```)\n((.*\n)*?)^(```)""",
	 r"""\n<pre class="start-line:1 lang:sh decode:true " title="@TITLE@">\g<2></pre>\n\n""")

	# (r"\`(.*?).py\`",
	#  r"""<span class="lang:sh decode:true crayon-inline">\g<1>.py</span>"""),

	# (r"""\`(.*?)\`(.?)""",
	#  r"""<span class="lang:sh decode:true  crayon-inline ">\g<1></span>\g<2>""")


]