import tensorflow as tf 
import os 

class restore_model(object):
	"""
	run a stored model
	"""
	def __init__(self, model_folder, model_name):
		super(restore_model, self).__init__()
		self.model_name=os.path.join(model_folder, model_name)
		self.model_folder=model_folder

	def run_model(self, feature):
		with tf.Session() as sess_run:
			new_saver=tf.train.import_meta_graph(self.model_name)
			new_saver.restore(sess_run, tf.train.latest_checkpoint(self.model_folder+'/.'))

			graph=tf.get_default_graph()
			feature_in_restore=graph.get_tensor_by_name('beat:0')
			predict_restore=graph.get_tensor_by_name('output:0')
			feed_dict={feature_in_restore: feature}
			output=sess_run.run([predict_restore], feed_dict)
		return output
