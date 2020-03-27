# -*- coding: utf-8 -*-
# NOTE: in Sublime Text, "(groups) in regex" are "$1 in regex".
#             in Python, "(groups) in regex" are "\g<1> in regex".


# regular expression strings in format [(find, replace), (find2, replace2)...]
regexStrings = [

	# codeblocks are assumed to be Python and the start line number is set from the outline "Codeblock #1: Lines 42-58"
	(r"""(.*)Codeblock \#(\d*): Lines (\d*)-(\d*)(.*)""",
	 r"""\g<1>\n\n<!-- wp:enlighter/codeblock {"linenumbers":"true","group":@GROUPA1@,"language":"python","lineoffset":"\g<3>","title":"@TITLE@"} -->\n<pre class="EnlighterJSRAW" data-enlighter-language="python" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="true" data-enlighter-lineoffset="\g<3>" data-enlighter-title="@TITLE@" data-enlighter-group="@GROUPA2@">\nCodeblock \g<2> Lines \g<3>-\g<4></pre>\n<!-- /wp:enlighter/codeblock -->\n\n\g<5>"""),

	# # preformatted blocks in Notion are assumed to be "shell" format and start at line number 1
	# (r""":\s*?^    (.*)""",
	#  r"""\n\nBEGINSHELLBLOCK\n\g<1>"""),

	# # preformatted blocks in Notion are assumed to be "shell" format and start at line number 1
	# (r"""^    (.*)\n\s*<p>""",
	#  r"""\n\nENDSHELLBLOCK\n\g<1>"""),


#<!-- wp:enlighter/codeblock {"linenumbers":"true","group":@GROUPA1@,"language":"shell","lineoffset":"1","title":"@TITLE@"} -->\n<pre class="EnlighterJSRAW" data-enlighter-language="shell" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="true" data-enlighter-lineoffset="1" data-enlighter-title="@TITLE@" data-enlighter-group="@GROUPA2@">\g<1></pre>\n<!-- /wp:enlighter/codeblock -->\n\n


	# command output block
	(r"""(.*)COMMAND OUTPUT(.*)""",
	 r"""\g<1>\n\n<!-- wp:enlighter/codeblock {"linenumbers":"true","group":@GROUPB1@,"language":"shell","lineoffset":"1","title":"@TITLE@"} -->\n<pre class="EnlighterJSRAW" data-enlighter-language="shell" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="true" data-enlighter-lineoffset="1" data-enlighter-title="@TITLE@" data-enlighter-group="@GROUPB2@">\nCOMMAND OUTPUT</pre>\n<!-- /wp:enlighter/codeblock -->\n\n\g<2>"""),

	(r"Review project structure",
	 r"""Review project structure\n\n<!-- wp:enlighter/codeblock {"linenumbers":"true","group":@GROUPC1@,"language":"shell","lineoffset":"1","title":"@TITLE@"} -->\n<pre class="EnlighterJSRAW" data-enlighter-language="shell" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="true" data-enlighter-lineoffset="1" data-enlighter-title="@TITLE@" data-enlighter-group="@GROUPC2@">\n$ tree --dirsfirst --filelimit 10</pre>\n<!-- /wp:enlighter/codeblock -->\n\n...\n"""),

	# (r"""^(```)\n((.*\n)*?)^(```)""",
	#  r"""<!-- wp:enlighter/codeblock {"linenumbers":"true","group":@GROUPD1@,"language":"shell","lineoffset":"1","title":"@TITLE@"} -->\n\n<pre class="EnlighterJSRAW" data-enlighter-language="shell" data-enlighter-theme="" data-enlighter-highlight="" data-enlighter-linenumbers="true" data-enlighter-lineoffset="1" data-enlighter-title="@TITLE@" data-enlighter-group="@GROUPD2@">\n\g<2></pre>\n<!-- /wp:enlighter/codeblock -->\n\n"""),


	# (r"Figure X",
	#  r"<strong>Figure X</strong>"),

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

	(r"""CODE DOWNLOAD FORM""",
	 r"""[code_download_form action="" formid=""]"""),

	(r"""DOWNLOAD FORM""",
	 r"""[code_download_form action="" formid=""]"""),

	# preformatted filename .py
	(r"`(.*?).py`",
	 r"""<code class="EnlighterJSRAW" data-enlighter-language="shell">\g<1>.py</code>"""),

	# preformatted filename .zip
	(r"`(.*?).zip`",
	 r"""<code class="EnlighterJSRAW" data-enlighter-language="shell">\g<1>.zip</code>"""),

	# preformatted filename .json
	(r"`(.*?).json`",
	 r"""<code class="EnlighterJSRAW" data-enlighter-language="shell">\g<1>.json</code>"""),

	# preformatted filename .png
	(r"`(.*?).png`",
	 r"""<code class="EnlighterJSRAW" data-enlighter-language="shell">\g<1>.png</code>"""),

	# preformatted filename .h5
	(r"`(.*?).h5`",
	 r"""<code class="EnlighterJSRAW" data-enlighter-language="shell">\g<1>.h5</code>"""),

	# preformatted filename .txt
	(r"`(.*?).txt`",
	 r"""<code class="EnlighterJSRAW" data-enlighter-language="shell">\g<1>.txt</code>"""),

	# preformatted filename .avi
	(r"`(.*?).avi`",
	 r"""<code class="EnlighterJSRAW" data-enlighter-language="shell">\g<1>.avi</code>"""),

	# preformatted filename .hdf5
	(r"`(.*?).hdf5`",
	 r"""<code class="EnlighterJSRAW" data-enlighter-language="shell">\g<1>.hdf5</code>"""),

	# preformatted filename .gz
	(r"`(.*?).gz`",
	 r"""<code class="EnlighterJSRAW" data-enlighter-language="shell">\g<1>.gz</code>"""),

	# preformatted filename .pdf
	(r"`(.*?).pdf`",
	 r"""<code class="EnlighterJSRAW" data-enlighter-language="shell">\g<1>.pdf</code>"""),

	# preformatted filename .tflite
	(r"`(.*?).tflite`",
	 r"""<code class="EnlighterJSRAW" data-enlighter-language="shell">\g<1>.tflite</code>"""),

	# preformatted filename .pb
	(r"`(.*?).pb`",
	 r"""<code class="EnlighterJSRAW" data-enlighter-language="shell">\g<1>.pb</code>"""),

	# preformatted
	(r"""`(.*?)`""",
	 r"""<code class="EnlighterJSRAW" data-enlighter-language="python">\g<1></code>"""),

	# (r""".Downloads.""",
	#  r"""<strong><em>"Downloads"</em></strong>"""),

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

	# hyperlinks open in new tab
	(r"""\[(.*?)\]\((.*?)\)""",
	 r"""<a href="\g<2>" target="_blank" rel="noopener">\g<1></a>"""),


	## NUMBERED LISTS   *****DON'T FOR GET TO CLOSE WITH <ol> MANUALLY*****
	# numbered lists start with 1
	(r"""^1\. (.*)""",
	 r"""<ol>\n\t<li>\g<1></li>"""),

	# numbered lists 2-onward
	(r"""^[\d*]\. (.*)""",
	 r"""\t<li>\g<1></li>"""),

	## BULLETS   *****DON'T FOR GET TO OPEN and CLOSE WITH <ul> MANUALLY*****
	(r"""^- (.*)""",
	 r"""\t<li>\g<1></li>"""),


	# with gutenberg and enlighter, all paragraphs get open and close <p> tags
	(r"""^([A-Z\d\*\[].*)""",
	 r"""<p>\g<1></p>"""),

	# ...continuing, we then need to go back and remove the paragraph tags for codeblocks
	(r"""^<p>(Codeblock.*)</p>""",
	 r"""\g<1>""")


]