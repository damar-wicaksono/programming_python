# update_db_pickle_recs.py
import pickle

# Open a Pickle record
suefile = open("sue.pkl", "rb")
sue = pickle.load(suefile)
suefile.close()

# Update the Pickle record
sue["pay"] *= 1.10
suefile = open("sue.pkl", "wb")
pickle.dump(sue, suefile)
suefile.close()