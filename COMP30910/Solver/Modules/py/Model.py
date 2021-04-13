#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


from sklearn.model_selection import train_test_split, GroupShuffleSplit
from sklearn.preprocessing import MinMaxScaler 
from sklearn.metrics import precision_recall_curve, precision_score, recall_score

from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier
# In[3]:

import seaborn as sns
from sklearn.model_selection import GridSearchCV, StratifiedKFold
import re, sys, os

from linecache import getline
from pathlib import Path
from sklearn.preprocessing import MinMaxScaler 

from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFECV

from sklearn.feature_selection import mutual_info_classif, mutual_info_regression
from sklearn.naive_bayes import GaussianNB
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from sklearn.pipeline import Pipeline

sys.path.append(str(Path(os.getcwd()).parent) + '\py')
print(os.getcwd())


# In[4]:


import Constants as c


# In[5]:

def prune_instance():
    path = "COMP30910/Solver/Data/"
    cvrp = pd.read_csv(path + 'data.csv', index_col=0)
    cvrp


    # In[6]:


    cvrp.pop(c.U_NODE_ID)
    cvrp.pop(c.V_NODE_ID)
    cvrp.pop(c.U_Y)
    cvrp.pop(c.U_X)
    cvrp.pop(c.V_X)
    cvrp.pop(c.V_Y)


    # In[7]:


    cvrp['FILE_NAME'].nunique()


    # In[8]:


    file_names = cvrp['FILE_NAME'].unique()
    count = len(file_names)

    idx_training = round(count * 2/3) - 1
    training_file_name = file_names[idx_training]
    training_ratio = cvrp.index[cvrp['FILE_NAME'] == training_file_name].tolist()[0]
    file_names = file_names[idx_training + 1:]

    idx_validation = round(count * 0.16666666666) - 1
    validation_file_name = file_names[idx_validation]
    validation_ratio = cvrp.index[cvrp['FILE_NAME'] == validation_file_name].tolist()[0]


    # In[9]:


    train, validate, test = np.split(cvrp, [int(training_ratio), int(validation_ratio)])


    # In[10]:


    # print(train)
    file_names = train['FILE_NAME'].unique()
    print(file_names)
    train.pop('FILE_NAME')


    # In[11]:


    # print(validate)
    file_names = validate['FILE_NAME'].unique()
    print(file_names)
    validate.pop('FILE_NAME')


    # In[12]:


    # print(test)
    file_names = test['FILE_NAME'].unique()
    print(file_names)
    test.pop('FILE_NAME')


    # In[13]:


    cvrp.pop('FILE_NAME')


    # In[14]:


    y_train = train.pop('IS_OPTIMAL_EDGE')
    X_train = train.values

    y_val = validate.pop('IS_OPTIMAL_EDGE')
    X_val = validate.values

    y_test = test.pop('IS_OPTIMAL_EDGE')
    X_test = test.values

    cvrp.pop('IS_OPTIMAL_EDGE')

    scaler = MinMaxScaler()

    X_train = scaler.fit_transform(X_train)
    X_val = scaler.fit_transform(X_val)
    X_test = scaler.fit_transform(X_test)


    # # RandomForest

    # In[15]:


    clf = RandomForestClassifier()

    clf.fit(X_train, y_train)
    feat_labels = list(cvrp.columns)
    for feature in sorted(zip(feat_labels, clf.feature_importances_)):
        print(feature)

    sfm = SelectFromModel(clf)

    sfm.fit(X_train, y_train)
    print()
    for feature_list_index in sfm.get_support(indices=True):
        print(feat_labels[feature_list_index])

    X_important_train = sfm.transform(X_train)
    X_important_val = sfm.transform(X_val)
    X_important_test = sfm.transform(X_test)


    # In[16]:



    lr = RandomForestClassifier()

    lr.fit(X_important_train, y_train)

    #Setting the range for class weights
    weights = np.linspace(0.0,0.99,200)

    #Creating a dictionary grid for grid search
    param_grid = {'class_weight': [{0:x, 1:1.0-x} for x in weights]}

    #Fitting grid search to the train data with 5 folds
    gridsearch = GridSearchCV(estimator = lr, 
                              param_grid= param_grid,
                              cv=StratifiedKFold(), 
                              n_jobs=-1, 
                              scoring='recall', 
                              verbose=2).fit(X_important_val, y_val)

    #Ploting the score for different values of weight
    sns.set_style('whitegrid')
    plt.figure(figsize=(12,8))
    weigh_data = pd.DataFrame({ 'score': gridsearch.cv_results_['mean_test_score'], 'weight': (1- weights)})
    sns.lineplot(weigh_data['weight'], weigh_data['score'])
    plt.xlabel('Weight for class 1')
    plt.ylabel('F1 score')
    plt.xticks([round(i/10,1) for i in range(0,11,1)])
    plt.title('Scoring for different class weights', fontsize=24)


    # In[17]:


    # model, features = train_model(RandomForestClassifier(class_weight={0: 0, 1: 1}))
    clf_important = RandomForestClassifier(class_weight='balanced')
    clf_important.fit(X_important_train, y_train)


    # In[18]:


    y_pred = clf.predict(X_test)

    # View The Accuracy Of Our Full Feature (4 Features) Model
    print(recall_score(y_test, y_pred))

    y_important_pred = clf_important.predict(X_important_test)

    # View The Accuracy Of Our Limited Feature (2 Features) Model
    print(recall_score(y_test, y_important_pred))


    # In[19]:


    decision_function = clf_important.predict_proba(X_important_test)[:,1]


    # In[20]:


    start = 0
    step = 0.1
    thresholds = [start + (x * step) for x in range(0, 11)]

    def calc_recall_ratio_ground_truth_count(decision_function, y):
        ground_truth_count = []
        recall = []
        ratios = []

        for t in thresholds:   
            # Set the value of decision threshold. 
            decision_threshold = t

            # Desired prediction to increase precision value. 
            desired_predict = [] 

            for i in decision_function: 
                if i < decision_threshold: 
                    desired_predict.append(0) 
                else: 
                    desired_predict.append(1) 

            count = 0
            for e in desired_predict:
                if e == 1:
                    count += 1

            ratio = count / len(desired_predict)
            prune_ratio = 1 - ratio
            non_pruning_ratio = 1 - prune_ratio   

            ratios.append(non_pruning_ratio)
            ground_truth_count.append(count)  
            recall.append(recall_score(y, desired_predict))

        return recall, ratios, ground_truth_count

    def plot_recall_threshold_ground_truth(recall, ground_truth_count):        
        plt.rcParams["figure.figsize"] = [16, 9]
        fig, host = plt.subplots()
        fig.subplots_adjust(right=0.75)

        par1 = host.twinx()

        p1, = host.plot(thresholds, recall, "b-", label="Recall")
        p2, = par1.plot(thresholds, ground_truth_count, "r-", label="Ground Truth Count")

        plt.xticks(np.arange(0, 1.1, 0.1))

        host.set_xlim(0, 1)
        host.set_ylim(0, 1)

        host.set_xlabel("Threshold")
        host.set_ylabel("Recall")
        par1.set_ylabel("Ground Truth Count")

        host.yaxis.label.set_color(p1.get_color())
        par1.yaxis.label.set_color(p2.get_color())

        host.set_title('Threshold vs Recall and Ground Truth Count')

        tkw = dict(size=4, width=1.5)
        host.tick_params(axis='y', colors=p1.get_color(), **tkw)
        par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
        host.tick_params(axis='x', **tkw)

        lines = [p1, p2]

        host.legend(lines, [l.get_label() for l in lines])

    def plot_ratio_recall(ratio, recall):
        plt.rcParams["figure.figsize"] = [16, 9]
        plt.figure()
        plt.plot(ratio, recall, c ='b') 
        plt.xlabel("Recall")
        plt.ylabel("Non-Pruning Ratio")
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.title('Non-Pruning Ratio vs Recall')
        plt.show() 


    # In[21]:


    recall, ratio, ground_truth_count = calc_recall_ratio_ground_truth_count(decision_function, y_test)


    # In[22]:


    plot_recall_threshold_ground_truth(recall, ground_truth_count)


    # In[23]:


    plot_ratio_recall(ratio, recall)


    # # Logistic Regression

    # In[24]:





    # In[25]:


    logreg = LogisticRegression(solver='newton-cg', max_iter=5000)
    selector = RFECV(logreg, step=1, cv=10, n_jobs=-1, verbose=1, scoring='recall')


    # In[26]:


    selector = selector.fit(X_train, y_train)


    # In[27]:


    for feature_list_index in selector.get_support(indices=True):
        print(feat_labels[feature_list_index])

    X_important_train = selector.transform(X_train)
    X_important_val = selector.transform(X_val)
    X_important_test = selector.transform(X_test)


    # In[28]:


    c_values = [100, 10, 1.0, 0.1, 0.01]
    intercept = [True, False]
    weight = ['balanced', None]

    logreg = LogisticRegression(solver='newton-cg', max_iter=5000)
    logreg.fit(X_important_train, y_train)
    # define grid search
    grid = dict(C=c_values, fit_intercept=intercept, class_weight=weight)
    grid_search = GridSearchCV(estimator=logreg, param_grid=grid, n_jobs=-1, cv=10, scoring='recall', error_score=0)
    grid_result = grid_search.fit(X_important_val, y_val)

    # summarize results
    print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
    means = grid_result.cv_results_['mean_test_score']
    stds = grid_result.cv_results_['std_test_score']
    params = grid_result.cv_results_['params']
    for mean, stdev, param in zip(means, stds, params):
        print("%f (%f) with: %r" % (mean, stdev, param))


    # In[29]:


    clf_important = LogisticRegression(solver='newton-cg', max_iter=5000, C=grid_result.best_params_['C'], class_weight=grid_result.best_params_['class_weight'], fit_intercept=grid_result.best_params_['fit_intercept'])
    clf_important.fit(X_important_train, y_train)


    # In[30]:


    y_pred = selector.predict(X_test)

    # View The Accuracy Of Our Full Feature (4 Features) Model
    print(recall_score(y_test, y_pred))

    y_important_pred = clf_important.predict(X_important_test)

    # View The Accuracy Of Our Limited Feature (2 Features) Model
    print(recall_score(y_test, y_important_pred))


    # In[31]:


    decision_function = clf_important.decision_function(X_important_test) 


    # In[32]:


    recall, ratio, ground_truth_count = calc_recall_ratio_ground_truth_count(decision_function, y_test)


    # In[33]:


    plot_recall_threshold_ground_truth(recall, ground_truth_count)


    # In[34]:


    plot_ratio_recall(ratio, recall)


    # # Naiive Bayes

    # In[35]:

    i_scores = mutual_info_classif(X_train, y_train)

    X_train_df = pd.DataFrame(data=X_train, columns=list(cvrp.columns))
    X_train_df

    FS_DF = pd.DataFrame(i_scores, index = X_train_df.columns, columns = ['I-Gain'])
    FS_DF.sort_values(by=['I-Gain'], ascending=False, inplace=True)
    FS_DF


    # In[36]:


    gnb = GaussianNB()


    # In[37]:


    sbs = SFS(gnb, 
              k_features=3, 
              forward=False, 
              floating=False, 
              scoring='recall',
              cv=10,
              n_jobs=-1)
    sbs = sbs.fit(X_train, y_train)


    # In[38]:


    pipe = Pipeline([('sfs', sbs), 
                     ('gnb', gnb)])

    param_grid = [
      {'sfs__k_features': [x for x in range(1, len(cvrp.columns) + 1)]
        }
      ]

    gs = GridSearchCV(estimator=pipe, 
                      param_grid=param_grid, 
                      scoring='recall', 
                      n_jobs=-1, 
                      cv=10,
                      refit=False)

    # run gridearch
    gs = gs.fit(X_train, y_train)


    # In[39]:


    for i in range(len(gs.cv_results_['params'])):
        print(gs.cv_results_['params'][i], 'test acc.:', gs.cv_results_['mean_test_score'][i])


    # In[40]:


    print("Best parameters via GridSearch", gs.best_params_)


    # In[41]:


    sbs = SFS(gnb, 
              k_features=gs.best_params_['sfs__k_features'], 
              forward=False, 
              floating=False, 
              scoring='recall',
              cv=10,
              n_jobs=-1)
    sbs = sbs.fit(X_train, y_train)


    # In[42]:


    for feature_list_index in sbs.k_feature_names_:
        print(feat_labels[int(feature_list_index)])

    X_important_train = sbs.transform(X_train)
    X_important_val = sbs.transform(X_val)
    X_important_test = sbs.transform(X_test)


    # In[43]:


    gnb_test = GaussianNB()
    gnb_test.fit(X_train, y_train)
    y_pred_test = gnb_test.predict(X_test)

    gnb.fit(X_important_train, y_train)
    y_pred = gnb.predict(X_important_test)

    # Compute the accuracy of the prediction
    acc = float((y_test == y_pred).sum()) / y_pred.shape[0]
    print('Test set accuracy: %.2f %%' % (acc * 100))


    # In[44]:


    print(recall_score(y_test, y_pred))

    print(recall_score(y_test, y_pred_test))


    # In[45]:


    decision_function = gnb.predict_proba(X_important_test)[:,1]


    # In[46]:


    recall, ratio, ground_truth_count = calc_recall_ratio_ground_truth_count(decision_function, y_test)


    # In[47]:


    plot_recall_threshold_ground_truth(recall, ground_truth_count)


    # In[48]:


    plot_ratio_recall(ratio, recall)


    # # Prune

    # In[62]:


    df_prune = pd.read_csv(path + 'data_prune.csv', index_col=0)


    # In[63]:


    df_prune


    # In[64]:


    y_prune = df_prune.pop('IS_OPTIMAL_EDGE')


    # In[65]:


    feats = [feat_labels[int(feature_list_index)] for feature_list_index in sbs.k_feature_names_]

    for feat in feats:
        print(feat)


    # In[66]:


    extracted_X_val = df_prune[feats]


    # In[67]:


    yhat = gnb.predict(extracted_X_val)


    # In[68]:


    pruned = pd.DataFrame(yhat)
    df_prune['IS_OPTIMAL_EDGE_PRUNE'] = pruned


    # In[69]:


    df_prune


    # In[70]:


    df_prune[df_prune['IS_OPTIMAL_EDGE_PRUNE'] == 1]


    # In[73]:


    decision_function = gnb.predict_proba(extracted_X_val)[:,1]
    recall, ratio, ground_truth_count = calc_recall_ratio_ground_truth_count(decision_function, y_prune)


    # In[74]:


    plot_recall_threshold_ground_truth(recall, ground_truth_count)


    # In[75]:


    plot_ratio_recall(ratio, recall)


    # In[72]:


    df_prune.to_csv(path + 'data_pruned.csv', index = True)


    # In[ ]:





    # In[ ]:




