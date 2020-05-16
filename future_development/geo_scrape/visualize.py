import pickle
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


name = input("Input the name of the project for which you would like to visualize data.\n")


def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

buckets = load_obj(name)
objects = []
places = []
performance = []
i = 0
for place in buckets:
	if 'NY' not in place:
		continue
	objects.append(i)
	places.append(place)
	i += 1
	performance.append(sum(buckets[place])/len(buckets[place]))

print(list(enumerate(places)))

y_pos = np.arange(len(objects))
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')

plt.show()


