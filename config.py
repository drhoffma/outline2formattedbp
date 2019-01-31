# NOTE: in Sublime Text, "(groups) in regex" are "$1 in regex".
#             in Python, "(groups) in regex" are "\g<1> in regex".


# regular expression strings in format [(find, replace), (find2, replace2)...]
regexStrings = [

	(r"Codeblock #([0-9].*): Lines (.*)-(.*) (.*)",
	 r"""\n<pre class="start-line:\g<2> lang:python decode:true " title="@TITLE@">Codeblock \g<1> Lines \g<2>-\g<3></pre>\n\n\g<4>"""),

	(r"</*div.*",
	 r""),

	(r"JUMP TO CODE DOWNLOAD",
	 r"[jump_to_code_download]"),

	(r"To learn (.*), just keep reading!",
	 r"<strong>To learn \g<1>, <em>just keep reading!</em></strong>"),

	(r"Review project structure",
	 r"""Review project structure\n\n<pre class="start-line:1 lang:shell decode:true " title="@TITLE@">$ tree --dirsfirst --filelimit 10
output</pre>\n\n...\n"""),

	(r"(.*), (.*) in the form below!",
	 r"<strong>\g<1>, <em>\g<2> in the form below!</em></strong>"),

	(r"—",
	 r"--"),

	(r"Figure X",
	 r"<strong>Figure X</strong>"),

	(r"Downloads",
	 r"""<strong><em>"Downloads"</em></strong>"""),

	(r"`(.*).py`",
	 r"""<span class="lang:sh decode:true crayon-inline">\g<1>.py</span>"""),

	(r" `(.*)` ",
	 r""" <span class="lang:python decode:true  crayon-inline ">\g<1></span> """),

	(r"Summary",
	 r"<h2>Summary</h2>"),

	(r"Project structure",
	 r"<h3>Project structure</h3>"),

	(r"<li>([1-9]*)\. (.*)</li>",
	 r"<li><\g<2></li>"),

	(r"([1-9])x([1-9])",
	 r"<em>\g<1>x\g<2></em>")

]