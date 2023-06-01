import sys
from codeowners import CodeOwners
filepath = sys.argv[1]
fileContents = open('CODEOWNERS', "r")
codeowners = CodeOwners(fileContents.read())
print(codeowners.of(filepath))