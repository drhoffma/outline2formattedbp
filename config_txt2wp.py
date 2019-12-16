# -*- coding: utf-8 -*-
# NOTE: in Sublime Text, "(groups) in regex" are "$1 in regex".
#             in Python, "(groups) in regex" are "\g<1> in regex".


# regular expression strings in format [(find, replace), (find2, replace2)...]
regexStrings = [

	(r"""\<div.*?\>""",
	 r""""""),

	(r"""\<\/div.*?\>""",
	 r""""""),

	(r"""(.*)Codeblock \#(\d*): Lines (\d*)-(\d*)(.*)""",
	 r"""\g<1>\n\n<pre class="start-line:\g<3> lang:python decode:true " title="@TITLE@">Codeblock \g<2> Lines \g<3>-\g<4></pre>\n\n\g<5>"""),

	(r"JUMP TO CODE DOWNLOAD",
	 r"[jump_to_code_download]"),

	(r"To learn (.*), just keep reading!",
	 r"<strong>To learn \g<1>, <em>just keep reading!</em></strong>"),

	(r"Review project structure",
	 r"""Review project structure\n\n<pre class="start-line:1 lang:sh decode:true " title="@TITLE@">$ tree --dirsfirst --filelimit 10
output</pre>\n\n...\n"""),

	(r"""(.*), (.*) in the form below!""",
	 r"""<strong>\g<1>, <em>\g<2> in the form below!</em></strong>\n\n[code_download_form action="" formid=""]"""),

	(r"—",
	 r"--"),

	(r"Figure X",
	 r"<strong>Figure X</strong>"),

	(r""""(.*?) section""",
	 r"""<em>"\g<1>"</em> section"""),

	(r"""DOWNLOAD FORM""",
	 r"""[code_download_form action="" formid=""]"""),

	(r"`(.*?).py`",
	 r"""<span class="lang:sh decode:true crayon-inline">\g<1>.py</span>"""),

	(r"""`(.*?)`""",
	 r"""<span class="lang:python decode:true  crayon-inline ">\g<1></span>"""),

	(r"Summary",
	 r"<h2>Summary</h2>"),

	(r"Project structure",
	 r"<h3>Project structure</h3>"),

	(r"<li>([1-9]*)\. (.*)</li>",
	 r"<li><\g<2></li>"),

	(r"([1-9]+)x([1-9]+)",
	 r"<em>\g<1>x\g<2></em>"),

	(r"""\<i\>(.*)\<\/i\>""",
	r"""<em>\g<1></em>"""),

	(r"""\<p .*?\>(.*)\<\/p\>""",
	r"""\g<1>"""),

	(r"""\<b\>(.*)\<\/b\>""",
	r"""<strong>\g<1></strong>"""),

	(r"""\<b\>\<em\>(.*)\<\/em\><\/b\>""",
	r"""<strong><em>\g<1></em></strong>"""),

	(r"""\<a href="(.*?)"\>(.*\>)\<\/a\>""",
	 r"""\<a href="\g<1>" target="_blank" rel="noopener">\g<2>\<\/a\>"""),

	# (r"""\<span class.*?\>(.*)\<\/span\>""",
	# r"""\g<1>"""),

	# (r"""\<span class.*?\>(.*)\<\/span\>""",
	# r"""\g<1>"""),

	(r"""\<span style="font-weight: bold;"\>(.*?)\<\/span\>""",
	 r"""\<strong\>\g<1>\<\/strong\>"""),

	(r"""\<span style="font-style: italic;"\>(.*?)\<\/span\>""",
	 r"""\<em>\g<1></em>"""),

	(r"""\<span style="font-weight: bold; font-style: italic;"\>(.*?)\<\/span\>""",
	 r"""<strong><em>\g<1></em></strong>"""),

	(r"""\<span style="font-weight: bold; font-size: 24px;"\>(.*?)\<\/span\>""",
	 r"""\n<h2>\g<1></h2>\n"""),

	(r"""\<span style="font-weight: bold; font-size: 18px;"\>(.*?)\<\/span\>""",
	 r"""\n\<h3\>\g<1>\<\/h3\>\n"""),

	(r"""COMMAND""",
	 r"""\n<pre class="start-line:1 lang:sh decode:true " title="@TITLE@">COMMAND OUTPUT</pre>\n\n\g<2>"""),

	(r"""\(x, y\)-(.*) """,
	 r"""<em>(x, y)</em>-\g<1> """),

	(r"""Line (\d*)""",
	 r"""<strong>Line \g<1></strong>"""),

	(r"""Lines (\d*)-(\d*)""",
	 r"""<strong>Lines \g<1>-\g<2></strong>"""),

	(r"""Lines (\d*) and (\d*)""",
	 r"""<strong>Lines \g<1> and \g<2></strong>""")


]
