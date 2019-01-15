# Unix Exercises

* Make a directory (in this directory) called "files" and download the following files in there:
	* Download the following using their existing filenames (i.e., you will have "usdeclar.txt", etc.):
		* https://www.constitution.org/usdeclar.txt
		* https://www.usconstitution.net/const.txt
	* Download https://www.gutenberg.org/files/25344/25344-0.txt as "scarlet.txt" (in one line, i.e., do not download and then rename -- how can you specify the download filename?)
* Show a long listing of the files
* Show a command to count the number of lines in each file and a total count of all lines
* Show a command that will find the files in this directory which are larger than 50k
* Show a command that will tell you what kind of file that Unix considers "const.txt"
* Show a single command that will print the MD5 sum of all the text files (without mentioning each file individually)
* Show a single command that will calculate the number of words in the files that start with either "c" or "s"; the command must use a pattern and not list the files individually
* Show the output of a command that will tell you how much disk space in kilobytes (K) is being used
* Show a command to count how many times you can find the word "judge" (irrespective of case)
* Show a command that will display only the names of the files that contain the word "human" 
* Show a command that will show the lines that begin with "Article" followed by a space and a number
* Show a command that will count the number of empty lines in "const.txt"
* Show a single command that will count the number of times the word "scarlet" appears in "scarlet.txt" (case-insensitive); that is, not the number of lines that contain "scarlet" but each occurrence of the word
* Show a single command that will take the first 15 lines from each file and append them into a new file called "foo"
* Show a command that shows how many lines are in "foo"
* Remove the file called "foo"
* Show a command that will find all the lines in "scarlet.txt" that begin with a vowel (case-insensitive) and shows you a count by letter like the output in Table 1
* Do "history > cmds"
* "git add -A files" and then commit and push. Ensure you can see your new files on Github.

Table 1: Expected output for "scarlet.txt" lines beginning with a vowel:

	  59 A
	  10 E
	  91 I
	  20 O
	   6 U
	 651 a
	 199 e
	 356 i
	 358 o
	 106 u