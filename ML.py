import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


dataset_japanese = pd.read_csv('./data/dataset_japanese.csv', sep ='\t')


X = dataset_japanese['text']
y = dataset_japanese['source']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crea una rappresentazione numerica dei testi utilizzando TfidfVectorizer
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Crea e valuta i modelli di classificazione
models = [
    LogisticRegression(),
    DecisionTreeClassifier(),
    RandomForestClassifier(),
    SVC(),
    KNeighborsClassifier(),
    GradientBoostingClassifier(),
    MLPClassifier()
]

accuracies = []
best_model = None
best_accuracy = 0.0

for model in models:
    # Addestra il modello
    model.fit(X_train_vec, y_train)

    # Effettua le predizioni sul test set
    y_pred = model.predict(X_test_vec)

    # Calcola l'accuratezza
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)

    # Verifica se è il modello migliore fino ad ora
    if accuracy > best_accuracy:
        best_model = model
        best_accuracy = accuracy

    # Stampa l'accuratezza del modello corrente
    print(f"Accuratezza del modello {type(model).__name__}: {accuracy}")

# Trova l'indice del modello con l'accuratezza migliore
best_model_index = accuracies.index(best_accuracy)

# Stampa il modello migliore e la sua accuratezza
print(f"\nIl modello migliore è {type(models[best_model_index]).__name__} con un'accuratezza di {best_accuracy}")
