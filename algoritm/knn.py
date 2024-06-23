from sklearn.neighbors import KNeighborsClassifier

# Model fitting and prediction for KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)
ypred_train_knn = knn.predict(x_train)
ypred_test_knn = knn.predict(x_test)

# Calculating metrics for Random Forest
accuracy_knn, f1_knn, precision_knn, recall_knn = calculate_metrics(y_test, ypred_test_knn)

# Storing the results in a DataFrame
model_results = pd.DataFrame({
    'KNN Accuracy': [accuracy_knn],
    'KNN F1': [f1_knn],
    'KNN Precision': [precision_knn],
    'KNN Recall': [recall_knn]
}, index=['Test'])

# Display the results
model_results.head()
