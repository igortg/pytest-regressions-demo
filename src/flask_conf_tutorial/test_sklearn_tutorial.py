from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def test_kneighbours(num_regression):
    dataset = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(
        dataset.data, dataset.target, stratify=dataset.target, random_state=0
    )
    # Training
    knn = KNeighborsClassifier(3, weights='distance')
    knn.fit(X_train, y_train)
    # Test with splitted dataset
    y_predict = knn.predict(X_test)
    num_regression.check({'predict': y_predict})
