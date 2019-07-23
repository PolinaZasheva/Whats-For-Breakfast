# Whats-For-Breakfast

Definition: 
---
Multiclass Classification using Keras and TensorFlow on Food-101 Dataset

Overview:
---
 * Download and extract Food 101 dataset
 * Understand dataset structure and files
 * Visualize random image from three of the classes
 * Create a subset of data with few classes(3) – french toast, omelet, waffle
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
 * For computational efficiency, limited the dataset to 3 classes to develop the multiclass classification model
 * Generated separate data folders for each class
 * Fine tuned Inception Pretrained model 
    *Use Keras to provide pretrained model* . 
    *Using the pretrained model, we were able to use the already learned weights and add few layers on top to finetune the model to our new data* . 
    *This helps in faster convergence and saves time and computation when compared to models trained from scratch* . 
 * Visualized the accuracy of the model
 * Predicted classes for new images from internet using the best trained model
 * Set compile=False and clearing the session leads to faster loading of the saved model


  
  
  
  
  
 Findings: 
 ---
   * Challenge: The data files and model code was too large to host on the standard GitHub Repository. 
   * Solution: We used GitHub LFS to load the large file into our GitHub Repository
 
