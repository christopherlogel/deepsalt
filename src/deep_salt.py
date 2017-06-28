# -----------------------------------------------------------------------------
# Name:        deep_salt.py
# Purpose:     This is the main Deep Salt script
#
# Author:      Christopher Logel
#
# Created:     6/9/2017
# Copyright:   (c) Christopher Logel
# -----------------------------------------------------------------------------

# Imports
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm

# Import data
match_dict_list = pickle.load(open("match_data.p", "rb"))

# Process Data
match_heroes = []
match_results = []

false_list = []

for i in range(228):
    false_list.append(0)


for match in match_dict_list:
    heroes_list = list(false_list)

    # Parse Heroes
    radiant_heroes = match["radiant_team"].split(",")
    dire_heroes = match["dire_team"].split(",")

    for hero in radiant_heroes:
        heroes_list[int(hero)-1] = 1

    for hero in dire_heroes:
        heroes_list[(int(hero) * 2)-1] = 1

    match_heroes.append(heroes_list)
    match_results.append(match["radiant_win"])


# Evaluation Data
eval_heroes = []
eval_results = []

# Split Data
for i in xrange(len(match_heroes) / 3):
    eval_heroes.append(match_heroes.pop())
    eval_results.append(match_results.pop())

####

# clf = LogisticRegression(max_iter=300, solver="sag")
#clf = LogisticRegression(max_iter=1000, solver="sag")
#clf = MLPClassifier()
#clf = GaussianNB()
#clf = RandomForestClassifier()
#clf = GradientBoostingClassifier(n_estimators=300, learning_rate=1.0, max_depth=2, random_state=0)
#clf = KNeighborsClassifier(n_neighbors=10)
clf = svm.SVC()
clf.fit(match_heroes, match_results)

predictions = clf.predict(eval_heroes)

print accuracy_score(eval_results, predictions)