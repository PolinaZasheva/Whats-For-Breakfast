# Whats-For-Breakfast

Definition: 
---
Multiclass Classification using Keras and TensorFlow on Food-101 Dataset

Overview:
---
 * Download and extract Food 101 dataset
 * Understand dataset structure and files
 * Visualize random image from three of the classes
 * Create a subset of data with few classes(9) – waffles, omelet, French toast, breakfast burrito, donuts, pancakes, deviled eggs, huevos rancheros, “not breakfast food”
 * Train the Model
 * Fine tune Inception Pretrained model
 * Predicting classes for new images from internet
 * Reformatted data as HDF5 to enable easier handling without compromising the model from a computational perspective
 * Scale up the model utilizing GitHub LFS,  Flask & Keras, Tensorflow
 * Create a user interface that allows someone to upload an image of a food to be recognized by the machine learning algorithm
 
Model Outline:
---
 * Split the image data into train and test
 * Prepared “Training” dataset
 * Prepared “Testing” dataset
 * For computational efficiency, limited the dataset to 9 classes to develop the multiclass classification model
 * Generated separate data folders for each class
 * Fine tuned Inception Pretrained model 
 * Use Keras to provide pretrained model
 * Using the pretrained model, we were able to use the already learned weights and add few layers on top to finetune the model to our new data
 * This helps in faster convergence and saves time and computation when compared to models trained from scratch* . 
 * Visualized the accuracy of the model
 * Predicted classes for new images from internet using the best trained model
 * Set compile=False and clearing the session leads to faster loading of the saved model
 
 Deployment: 
 ---
 * Created a directory of the model
 * Created a python script to build and train the model and run that script
 * Created directory for the Flask App
 * Copy the pre-trained model to the root of the Flask app
 * Set up virtual hosting for Flask
 * Create and HTML script that enables image interaction with model on app
 
 Challenges: 
 ---
   * Challenge: The data files and model code was too large to host on the standard GitHub Repository. 
   * Solution: We used GitHub LFS to load the large file into our GitHub Repository
   
Future Works:
 ---
 * Currently our model is able to accurately predict the outcome from nine classes of food – waffles, omelet, French toast, breakfast burrito, donuts, pancakes, deviled eggs, huevos rancheros, “not breakfast food”
 * With more time and more computational power, we would like to add more classes to it and expand it’s usefulness by offering additional detail about each food selection– such as closes location to buy, nutritional fact, etc. 
 * Currently our model is housed on a traditional website where the user is asked to upload an image in order to receive a response
 * With more time, we would like to turn this functionality into an application that enables the end user to use the camera on their phone to take a picture of a food and receive a response 

 
