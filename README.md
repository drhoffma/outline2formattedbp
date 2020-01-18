# README `outline2formattedbp`


This project takes advantage of regular expressions to format a blog post from a given outline.

The process is partly manual and partly automated as it currently stands (this may change in the future).

## Cloning the repo

pass

It is a private GitHub repo right now and it probably will stay that way.  I might post the non-specific regex config on public GitHub in the future.

## Features

**Currently the script works like this:**

* Accepts an input txt file of jacked-up WP formatting.
* Removes `<div>` tags and other junk.
* Codeblocks with title, line numbers, and syntax type:
 * Formats Python codeblocks
 * Formats Project Structure Shell blocks
 * Formats command + output Shell blocks
* Preformatted text:
 * Formats preformatted text in `` marks as Python syntax
 * Filenames are automatically formatted as Shell syntax
* Formats some headings that it recognizes
 * TODO recognize Title and format as H2 (easy)
* Formats the "just keep reading" with bold/italics followed by the "jump to code download"
* Formats the ending "just enter your email address" with bold/italics followed by the code download form

**The following items are on the TODO list:**

* Format numerical lists (bulleted lists will be hard because the outline is in bulleted format to begin with...unless we switch the process of creating the input text file).
* Put the code in the codeblocks (easy, but will take about 1-2 hours to code + test). This involves making a CL arg to the code path and then finding/opening all files necessary and extracting the relevant lines + putting them into the codeblocks.
* Bold/italics/links. This sounds easy and I really, really want this feature because it would reduce 10-20 minutes down to sub-second. The problem is that when I copy/paste from the outline in MacOS's Preview app, the formatting is lost. There's nothing to parse for, so it's impossible with the current process (see the process below).  I've explored outputting to the Evernote .enex and then converting to HTML, but honestly it makes it even more difficult because then line breaks are not captured and there are `<div>` tags all over the fucking place.
* Extract the title to eliminate a CL argument.  This is easy, but I keep forgetting to do it.

## Process

I have a local WordPress server running on a MacOS laptop with MAMP. I'm using the same version of Apache, PHP, MySQL, Wordpress, Theme, Crayon, and Shortcodes (or whatever it is called) as of January 2019.  I haven't queried the server lately to see if any versions have changed.  MAMP will also run nginx and I think we're switching to that soon.

Here is the process I'm currently following:

* Start MAMP and navigate to my dev Wordpress server.
* Open an outline and copy/paste it into Wordpress WYSIWYG view.
* Switch to code view and then copy/paste all the code into a text file.
* Save the text file in the input folder in the `outline2formattedbp` directory.
* Run the script with command line arguments (see below).
* Open the output file, inspect it, and then copy/paste all back into Wordpress code view.
* Save the draft
* At this point, I look for any improvements I can make to the regular expressions. I either (a) note them to do next month when we batch blog posts, or (b) make a quick change and try again.  I try to prevent myself from investing too much time in (b).
* I use regex101.com to make my regular expressions and put them in the config file.
* Then I do all of the bold/italic/links manually (see previous section TODO).  I loathe this so I use a focus timer and good music.
* Then I put in all the code manually into the already formatted code blocks.  This will be automated soon pretty easily.
* Then I generate the Project Structure using `tree` and paste it into the Shell block.  Sometimes I run my `pyclean` bash command to remove `.pyc` and `__pycache__` if they are present.  I don't plan to automate this because I always make some manual changes to the `tree` output so it is better for the post and the files are in the order of appearance in the blog post. Automation wouldn't be worth it here.
* Finally, I copy the code into the live server and save as draft + schedule.
* I can batch this process pretty quickly and have 3-4 formatted blog posts ready in about 1 hour if I'm not doing any code/regex updates.

## Running the script:

``` 
$ python regex2bp.py --input input/breast_cancer.txt \
	--title "Breast cancer classification with Keras and Deep Learning" \
	--output output/out_breast_cancer.txt
```