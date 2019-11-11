# -*- coding: utf-8 -*-
# NOTE: in Sublime Text, "(groups) in regex" are "$1 in regex".
#             in Python, "(groups) in regex" are "\g<1> in regex".


# regular expression strings in format [(find, replace), (find2, replace2)...]
regexStrings = [



	# preformatted filename
	(r"`(.*?).py`",
	 r"""<span class="lang:sh decode:true crayon-inline">\g<1>.py</span>"""),

	# preformatted
	(r"""`(.*?)`""",
	 r"""<span class="lang:python decode:true  crayon-inline ">\g<1></span>""")
]