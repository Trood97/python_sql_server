import difflib

# Define the two strings
str1 = "Tabak, R. G., Khoong, E. C., Chambers, D. A., & Brownson, R. C. (2012). Bridging research and practice: models for dissemination and implementation research. Am J Prev Med, 43(6), 337-350. doi: 10.1016/j.amepre.2012.05.024"
str2 = "Tabak, R. G., Khoong, E. C., Chambers, D. A., & Brownson, R. C. (2012). <span style = 'normal' >Bridging research and practice: Models for dissemination and implementation research</span>. <span style = 'font-style:italic' >American Journal of Preventive Medicine</span>, <span style='font-style:italic'>43</span>(<span style='normal'>3</span>), <span style='normal'>337</span>–<span style='normal'>350</span>. <span style = 'normal' >10.1016/j.amepre.2012.05.024</span>"

# Split the strings into words for diff comparison
str1_words = str1.split()
str2_words = str2.split()

# Perform the difference comparison
differ = difflib.Differ()
diff = list(differ.compare(str1_words, str2_words))

# Initialize variables to keep track of formatting
output = []
in_bold = False
in_italic = False

# Process the differences and format the output
for word in diff:
    if word.startswith('+ '):  # Insertion
        output.append(f'<span style="color: green"><ins>{word[2:]}</ins></span>')
    elif word.startswith('- '):  # Deletion
        output.append(f'<span style="color: red"><del>{word[2:]}</del></span>')
    elif word.startswith('? '):  # Common
        output.append(word[2:])
    else:  # Unchanged
        output.append(word)

# Combine the words back into a single string
formatted_diff = ' '.join(output)

# Print the formatted difference
print('*****')
print(formatted_diff)
