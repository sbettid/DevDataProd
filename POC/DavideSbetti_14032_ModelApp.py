import tensorflow as tf
from os import path
import numpy as np

# class used for the POC application of the model
class ModelApp: 

	#constructor, we need the path to the model
	def __init__(self, modelPathInit):
		
		#save it inside the object	
		self.modelPath = modelPathInit
		
		#check if the directory exists
		if path.exists(self.modelPath):
			self.model = tf.keras.models.load_model(self.modelPath)
			print("Model loaded")
 # if success load the model
		else: #else give error
			print("Model could not be loaded")
			self.model = None

	#function used to retrieve classification of a post		
	def classifyPost(self, post):
		
		#if the model is valid
		if self.model is not None:
			
			new_x = tf.data.Dataset.from_tensor_slices([post])

			prediction = np.argmax(self.model.predict(new_x.batch(32)))

			return int(prediction)

		return None



#am = ModelApp("model")
#answer = am.classifyPost("text text and some other text")
#print("Classification: ", answer)