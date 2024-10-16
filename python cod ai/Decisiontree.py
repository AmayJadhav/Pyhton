import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_graphviz
import graphviz

# Load and preprocess data
PlayTennis = pd.read_csv('bar.csv').apply(LabelEncoder().fit_transform)

# Display the processed dataset
print(PlayTennis)

# Train decision tree classifier
x, y = PlayTennis.drop('play', axis=1), PlayTennis['play']
clf = DecisionTreeClassifier(criterion='entropy').fit(x, y)

# Visualize decision tree
plot_tree(clf)
dot_data = export_graphviz(clf, out_file=None)  # Export as dot data
graph = graphviz.Source(dot_data)  # Create a graphviz source object
graph.render("decision_tree")  # Save the visualization
graph.view()  # Open the saved file

# Predict and compare predictions
print(clf.predict(x) == y)
