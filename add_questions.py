#! /usr/bin/env python3
# This script adds questions to the question_generation.sh script

# Dictionaries for yes/no
yes = {'yes','y', 'ye', ''}
no = {'no','n'}

# Function to build question_generation.sh
def build_script():
    output = open("question_generation.sh", "w")
    sql_lines = open("question_list.txt", "r")

    # Place correct header lines
    output.write('#! /bin/bash\n')
    output.write('echo -e "Inserting question records into database ..."\n')
    output.write('sqlite3 serverapp/db.sqlite3 <<END_SQL\n')
    output.write('DELETE FROM core_question;\n')

    # Place all user lines
    for line in sql_lines.readlines():
        output.write(line)
    sql_lines.close()

    # Place correct footer lines
    output.write('END_SQL\n')
    output.write('echo -e "Values successfully inserted"\n')
    output.close()    

def main():
    # File to edit
    questions = open("question_list.txt", "a")

    # Condition to stop looping
    continue_adding = True
    while continue_adding:
        choice = input("\nAdd a question? (y/n): ")
        if choice in yes:
            # Add question
            question_name = input("Enter question name: ")
            question_solution = input("Enter the question solution: ")
            question_contest = input("Enter the contest ID the question is being added to: ")

            # Write question to list of questions
            questions.write('INSERT INTO core_question(rowid, text, solution, contest_id) VALUES(NULL, "%s", "%s", %s);\n' % (question_name, question_solution, question_contest))
            questions.close()

            # Changes were made, rebuild script.
            build_script()
        else:
            # End program safely
            continue_adding = False

if __name__ == "__main__":
    main()
