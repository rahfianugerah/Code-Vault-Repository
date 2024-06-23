from sklearn.ensemble import RandomForestClassifier

# Model fitting and prediction for Random Forest
rf = RandomForestClassifier(n_estimators=10, random_state=42) # n_estimators default values is 100 or 10
rf.fit(x_train, y_train)
ypred_train_rf = rf.predict(x_train)
ypred_test_rf = rf.predict(x_test)

# Calculating metrics for Random Forest
accuracy_rf, f1_rf, precision_rf, recall_rf = calculate_metrics(y_test, ypred_test_rf)

# Storing the results in a DataFrame
model_results = pd.DataFrame({
    'RF Accuracy': [accuracy_rf],
    'RF F1': [f1_rf],
    'RF Precision': [precision_rf],
    'RF Recall': [recall_rf]
}, index=['Test'])

# Display the results
model_results.head()
