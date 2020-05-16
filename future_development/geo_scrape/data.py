import pickle

def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

buckets = load_obj("buckets")

def update(status,score, name):
	loc = status.user.location
	if loc not in buckets:
		buckets[loc] = [score]
	else:
		buckets[loc].append(score)
	save_obj(buckets, name)
