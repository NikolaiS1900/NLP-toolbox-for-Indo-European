import os, re, glob

CWD = os.getcwd()
# Går i overmappen.
PATH = os.path.dirname(CWD)

# The full path to the folder preprocessed_text in preprocess
PATH_PRE_PROC_TXT = PATH+"/Target_text"

# An empty container for the texts
CORPUS = []

EXAMPLES = []

# List all the files in PATH_PRE_PROC_TXT
FILE_LIST = os.listdir(PATH_PRE_PROC_TXT)

# Write your search word here.
# Remember the quotation marks
WORD = "bonde"


# This function can be called on a text file, and then it will find all lines
# containing the search word, and then tell the name of the text file
# and show each line with their line number.
def find_lines_and_number(file):
    with open(PATH_PRE_PROC_TXT+"/"+file, "r", encoding="utf8") as F:
        READ_F = F.read()

    lines = READ_F.split("\n")

    # A container for all findings
    findings_list = []

    # Find all examples of the search word, while ignoring case.
    find_word = re.findall(WORD, READ_F, re.IGNORECASE)
    # Removes all duplicates.
    find_word_uniq = set(find_word)

    # Goes through each example word in find_word_uniq.
    for word in find_word_uniq:
        # And then goes through each line number and line.
        for number, line in enumerate(lines, 1):
            if word in line:
                findings_list.append(f"\n\t{number}    {line}")

    # Formats the list in findings_list
    nice_list = '\n'.join(findings_list)

    # Combines the filetered data.
    result = (f"{file}\n{nice_list}\n\n")

    return result

# Container for the results
RESULTS = []
# This for loop gooes through each file in FILE_LIST and calls the function
# find_lines_and_number(file) on them. It saves the results in the RESULTS container (as a list).
for file in FILE_LIST:
    RESULTS.append(find_lines_and_number(file))

# The RESULTS list need to be converted into a string, and there need to be a division of two line shitfs
# between each result (\n\n).
NICE_LIST = '\n\n'.join(RESULTS)

# An empty text file with a name containing the search word is created,
# and stored in the Result directory.
EXAMPLES = open(f'{CWD}/Result/{WORD}_examples.txt', 'w', encoding='utf8')
# Writes the content of NICE_LIST to the text file.
EXAMPLES.write('' +  NICE_LIST)
# Closes the text file neatly in order to avoid data corruption.
EXAMPLES.close()

print(f"""
whereis.py     done running:

{WORD}_examples.txt is ready in the Result directory.

Visit my GitHub at: https://github.com/NikolaiS1900
I can be contacted via: sandbecks_github@protonmail.com

Kind regards
- Nikolai Sandbeck
""")
