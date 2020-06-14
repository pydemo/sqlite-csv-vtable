i./sqlite3 '' '.load ./csv' 'CREATE VIRTUAL TABLE temp.t1 USING csv(filename="sample.csv", header='YES');' 'PRAGMA table_info(t1);' 'SELECT col_int FROM t1;'
