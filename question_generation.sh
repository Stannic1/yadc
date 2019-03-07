#! /bin/bash
echo -e "Inserting question records into database ..."
sqlite3 serverapp/db.sqlite3 <<END_SQL
DELETE FROM core_question;
INSERT INTO core_question(rowid, text, solution, contest_id) VALUES(NULL, "Test 3", "3", 1);
INSERT INTO core_question(rowid, text, solution, contest_id) VALUES(NULL, "Test", "1", 1);
INSERT INTO core_question(rowid, text, solution, contest_id) VALUES(NULL, "Test 4", "4", 1);
END_SQL
echo -e "Values successfully inserted"
