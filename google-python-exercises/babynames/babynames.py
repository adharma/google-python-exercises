#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """extract the year_string, and print it"""
  in_file = open(filename)
  contents = in_file.read()
  year_string = re.findall(r'Popularity\sin\s(\d\d\d\d)', contents)
  names_string = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', contents)
  new_list = []

  """store each male name and female name of the names_string list, in a new list"""
  for i in names_string:
    male_entry = str(i[1]) + " " + str(i[0])
    new_list.append(male_entry)
    female_entry = str(i[2]) + " " + str(i[0])
    new_list.append(female_entry)   
  """sort the list. Insert the year_string value, as the first entry"""
  new_list.sort()
  new_list.insert(0, str(year_string[0]))
  text = '\n'.join(new_list) + '\n'
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  return text


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
  # +++your code here+++
  """open a file for writing"""
  
  # the_filename = "test.txt"
  x = 0
  for i in args:
    the_filename = i + ".summary"
    with open(the_filename, 'w') as f:
      for s in extract_names(i):
        f.write(s)
    x += 1

  print extract_names(i)
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  

if __name__ == '__main__':
  main()
