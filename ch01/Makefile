all: dump-pickle

people-pickle: 
	python make_db_pickle.py
dump-pickle: people-pickle
	python dump_db_pickle.py
clean:
	rm -f people-pickle
	rm -rf __pycache__
