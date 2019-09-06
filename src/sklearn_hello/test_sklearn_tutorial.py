import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor


def train_and_predict(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    # Training
    knn = KNeighborsRegressor(1)
    knn.fit(X_train, y_train)
    # Test with splitted dataset
    y_predict = knn.predict(X_test)
    return y_predict, y_test


def test_kneighbours():
    X, y = make_wave()
    y_predict, y_test = train_and_predict(X, y)

    assert len(y_predict) == 25
    assert round(y_predict[0], 5) == -1.09953
    assert round(y_predict[4], 5) == 1.12868
    assert round(y_predict[10], 5) == 1.70897
    assert round(y_predict[-1], 5) == -0.02249
    assert round(y_test[-1], 5) == -0.3112


def test_kneighbours_regression(num_regression):
    X, y = make_wave()
    y_predict, y_test = train_and_predict(X, y)
    num_regression.check({
        'test': y_test,
        'predicted': y_predict}
    )


def test_kneighbours_regression_tol(num_regression):
    X, y = make_wave()
    y_predict, y_test = train_and_predict(X, y)
    num_regression.check(
        default_tolerance={'atol': 1e-2},
        data={
            'test': y_test,
            'predicted': y_predict
        }
    )


def make_wave(n_samples=100):
    rnd = np.random.RandomState(42)
    x = rnd.uniform(-3, 3, size=n_samples)
    y_no_noise = (np.sin(4 * x) + x)
    y = (y_no_noise + rnd.normal(size=len(x))) / 2
    return x.reshape(-1, 1), y
