set curr_dir=%cd%
 
chdir /D test
 
python -i test.py

chdir /D %curr_dir%
