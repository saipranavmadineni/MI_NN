# MI_NN
PES University
Machine Intelligence 
Assignment- 3

Name: Sai Pranav M          Name: Rohan Bennur
SRN: PES1201800296	        SRN: PES1201801718

Problem Statement:
Low Birth weight (LBW) acts as an indicator of sickness in new born babies. LBW is closely
associated with infant mortality as well as various health outcomes later in life. Various studies
show strong correlation between maternal health during pregnancy and the child’s birth weight.
We use health indicators of pregnant women such as age, height, weight, community etc in order
for early detection of potential LBW cases. This detection is treated as a classification problem
between LBW and not-LBW classes
You have been provided with a Dataset consisting of data collected from a hospital which
classifies the patient as cases of LBW and cases of non-LBW.


About the Dataset:
The Dataset consists of 10 columns
1. Community - Information about the patient’s community
a. SC - 1
b. ST - 2
c. BC - 3
d. OC - 4
2. Age - Patients age in years
3. Weight - Weight in Kg during Trimester
4. Delivery Phase -
a. 1 - Before 37 weeks
b. 2 - After 42 weeks
5. HB - Haemoglobin content
6. IFA - determines if the patient took Folic acid or not
a. 1 - patient consumed Folic acid
b. 0 - patient did not consume Folic acid
7. BP - Blood Pressure during Trimester
8. Education - Educational Qualification of the patient on a scale of 0-10
9. Residence - indicates whether the patient is resident of the town or village in which the
study was conducted (indicated by 1) or if the patient is a non-resident (indicated by 2)
10. Result - Label 1 indicates case of LBW, Label 0 indicates non LBW case


Data Pre-processing : 
	Dataset that is given for this assignment had a lot of NaN values and the presence of these values leads to bad performance of a neural network hence this stage is very necessary before we train the neural network.

	def clean_df(file):
    df = pd.read_csv(file)
    df['Education'].fillna(5.0, inplace=True)
    df['Residence']=df['Residence'].fillna(method='ffill')a
    df['Weight']=df['Weight'].fillna(df['Weight'].mean())
    df['BP']=df['BP'].fillna(df['BP'].mean())
    df['HB']=df['HB'].fillna(df['HB'].mean())
    df['Delivery phase']=df['Delivery phase'].fillna(method='ffill')
    df['Age']=df['Age'].fillna(df['Age'].mean())

The above code depicts the changes made in each column and how we handled it to replace the Nan values.

Training and Testing dataset: 
	Using the sklearn’s traintestsplit, the dataset was split into x_train,x_test,y_train and y_test respectively. 
All of these were split in the fit function before training the neural network.
x_train, x_test, y_train, y_test = train_test_split(X.T, y.T, test_size=validation_split, )

This way we split the training and test data by using validation split to be 0.2


Design:
This neural consisted of 5 layers which are as follows :
1.	Input layer : 9 nodes (9 features from the dataset)
2.	Hidden layer 1 : 18 nodes 
3.	Hidden layer 2 : 9 nodes
4.  Hidden layer 3 : 9 nodes
5.	Output layer : 1 node (binary classification since the output is either 1 or 0 )
This combination of layers and nodes resulted in a 95% accuracy.




Out of the box implementation: 
	Usually the neural networks are built using the following :
	Activation functions : ReLu and the output activation to be Sigmoid 

	We've used sigmoid function for all the nodes, instead of just for the output layer. Although ReLu introduces non-linearity, there's a disadvantage pf vanishing gradient.
	So, we've bought out of the box thinking by using sigmoid function for all the layers.

	Loss function : Binary_CrossEntory(BCE) is used as a loss function in neural networks.

	In this assignment we implemented mean_squared_error as a loss function to update the weights such that the loss is minimized.


Experimental Results: 
	 Precision: 100%
	 Accuracy: 95%
	 Recall: 95%
	 F1 SCORE: 97%
	 This shows the confusion metric and also shows the result of the evaluation metrics such as Accuracy, Precision, Recall, F1 Score.


Steps to run files:
1. execute preprocessing.py for preprocessing the dataset
2. execute Neural_Net.py for running the model on the preprocessed dataset


Conclusion: 
	Neural network uses linear combination of multiple variables to form complex variables and help us in doing regression as well as categorical tasks. In this assignment we changed the default activation and loss function to see how the neural network performs and we observed that with a certain configuration of layers and number of nodes in each layer the network performed good with an accuracy of 95%. The dataset was highly imbalanced so that also caused the predictions to be a little inaccurate. 
	With more data, the results would’ve been much more interesting and accurate nevertheless even 96 samples helped us get good results. 

