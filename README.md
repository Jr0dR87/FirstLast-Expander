# FirstLast Username Generator

This script takes names in the format `first.last` and generates all username variations in the format:
Made this script to take in a list of users and create a list for a format that includes a middle initial. 

Where:
- **f** = first initial  
- **n** = each letter of the alphabet (a–z)  
- **last** = full last name
- Then appends domain name

Example:  
`john.smith` → `jasmith`, `jbsmith`, `jcsmith`, … `jzsmith`
Then appends the domain provided.


## Usage

Run the script with an input file (containing one `first.last` entry per line) and specify an output file and provide a domain.
Example: script.py users.txt emails.txt example.com
