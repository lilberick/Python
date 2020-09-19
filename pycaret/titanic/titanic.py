#binary classification
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O
data = pd.read_csv('titanic/train.csv')
data.head()
# setting up environment in pycaret
import pycaret
from pycaret.classification import *
clf1 = setup(data, target = 'Survived', ignore_features = ['Ticket', 'Name', 'PassengerId'], silent = True, session_id = 786) 
# comparing all models
#best_model = compare_models()
best_model = compare_models(verbose = False)
print(best_model)
models()
# create a model: random forest classifier
rf = create_model('rf',verbose=False)
# tune a model: random forest classifier
tuned_rf = tune_model(rf,verbose=False)
print(tuned_rf)
# plot a model
# plot a model: auc plot
plot_model(tuned_rf, plot = 'auc')
# plot a model: precision-recall curve
plot_model(tuned_rf, plot = 'pr')
# plot a model: feature importance plot
plot_model(tuned_rf, plot='feature')
# plot a model: confusion matrix
plot_model(tuned_rf, plot = 'confusion_matrix')
# all available plots
evaluate_model(tuned_rf)
# predict on test/hold-out sample
predict_model(tuned_rf);
# finalize model for deployment
final_rf = finalize_model(tuned_rf)
print(final_rf)
predict_model(final_rf);
# predict on unseen data
data_unseen = pd.read_csv('titanic/test.csv')
data_unseen.head()
unseen_predictions = predict_model(final_rf, data=data_unseen)
unseen_predictions.head()
# saving the model
save_model(final_rf,'Final RF Model 12Set2020')
# loading the saved model
saved_final_rf = load_model('Final RF Model 12Set2020')
new_prediction = predict_model(saved_final_rf, data=data_unseen)
new_prediction.head()

