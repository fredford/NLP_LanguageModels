import nltk
from nltk.lm import Vocabulary
from nltk.tokenize import word_tokenize
from collections import Counter
import numpy as np
import random

class Interpolation:
	'''
	This class creates an object that runs an interpolation model
	'''

	def __init__ (self, n):

		self.n = n
		self.data = [[0, 0 , 0, 0]]
		self.dist = {}
		self.counter = {}
		self.vocabulary = {}
		self.filenames = {}
		self.length = {}
		self.perplexity = {}
		self.filenames = []

	def process_train(self, dataFile, filename):
		'''
		This method takes a training datafile and its filename, processes all of the text for a vocabulary, distribution and counter

		Arguments:
			dataFile -- text file object
			filename -- string with the filename to be stored in dictionaries

		Return:
			None
		'''

		# Read the text file into a single string while stripping the newline characters
		lines = ""
		for line in dataFile:
			lines = lines + " "+ line.strip('\n')
		
		# Tokenize the provided string
		line_tokens = word_tokenize(lines)

		# Set the tokenized list into a vocabulary
		vocabulary = Vocabulary(line_tokens, unk_cutoff=1)

		tokens = []
		# In case any words not in the vocabulary are tokenized set them to <UNK>
		for token in line_tokens:
			if token not in vocabulary or token == "<UNK>":
				tokens.append("<UNK>")
			else:
				tokens.append(token)

		# Set the length of tokens for the file
		self.length[filename] = len(tokens)

		# Acquire the ngrams of the tokens
		grams = nltk.ngrams(tokens, self.n)

		# Store the frequency distribution, counts and vocabulary into dictionaries for use
		self.dist[filename] = nltk.FreqDist(grams)
		self.counter[filename] = Counter(line_tokens)
		self.vocabulary[filename] = Vocabulary(tokens)
		self.filenames.append(filename)
		self.lambdas = {}

	def process_interpolate(self, testFile, testFileName):
		'''
		This method takes a test datafile and its filename, processes all of the text for a vocabulary, distribution and counter

		Arguments:
		dataFile -- text file object
		filename -- string with the filename to be stored in dictionaries

		Return:
		None
		'''

		# Generate 3 random numbers between 0 and 1
		#l1, l2, l3 = np.random.dirichlet(np.ones(3), size=1)[0]

		# Read the text file into a single string while stripping the newline characters
		lines = ""
		for line in testFile:
			lines = lines + " "+ line.strip('\n')

		# Tokenize the provided string
		line_tokens = word_tokenize(lines)
		
		tokens = []
		perplexities = {}

		# Compare the test file data to each training data set
		for filename in self.filenames:
			for token in line_tokens:
				if token not in self.vocabulary[filename] or token == "<UNK>":
					tokens.append("<UNK>")
				else:
					tokens.append(token)

			#threshold = random.random()

			#if threshold <= l1:
			#	self.n = 1
			#elif threshold > l2 and threshold < l3:
			#	self.n = 2
			#else:
			#	self.n = 3

			grams = nltk.ngrams(tokens, self.n)

			log_probability = 0

			# For each token calculate the probability and sum the result
			for token in grams:
				log_probability += self.probability(token, filename)

			# Store the perplexity calculated into a temporary dictionary
			perplexities[filename] = np.power(2, - (log_probability / len(tokens)))

		# Find the best matching training file to the test file
		min_file = min(perplexities.keys(), key=(lambda k: perplexities[k]))
		
		#self.lambdas[testFileName] = [l1, l2, l3, accuracy]

		# Store the results
		self.data = [testFileName, min_file, perplexities[min_file], self.n]


	def process_test(self, testFile, testFileName):
		'''
		This method takes a test datafile and its filename, processes all of the text for a vocabulary, distribution and counter

		Arguments:
		dataFile -- text file object
		filename -- string with the filename to be stored in dictionaries

		Return:
		None
		'''

		# Read the text file into a single string while stripping the newline characters
		lines = ""
		for line in testFile:
			lines = lines + " "+ line.strip('\n')

		# Tokenize the provided string
		line_tokens = word_tokenize(lines)
		
		tokens = []
		perplexities = {}

		# Compare the test file data to each training data set
		for filename in self.filenames:
			for token in line_tokens:
				if token not in self.vocabulary[filename] or token == "<UNK>":
					tokens.append("<UNK>")
				else:
					tokens.append(token)

			grams = nltk.ngrams(tokens, self.n)

			log_probability = 0

			# For each token calculate the probability and sum the result
			for token in grams:
				log_probability += self.probability(token, filename)

			# Store the perplexity calculated into a temporary dictionary
			perplexities[filename] = np.power(2, - (log_probability / len(tokens)))

		# Find the best matching training file to the test file
		min_file = min(perplexities.keys(), key=(lambda k: perplexities[k]))
		
		# Store the results
		self.data = [testFileName, min_file, perplexities[min_file], self.n]

	def probability(self, token, filename):
		'''
		This method calculates the probability of the token being in the provided training file given.

		Arguments:
			token 	 -- object of type `token` that provides information on the word being observed
			filename -- string filename of the file being compared against
		'''
		return self.dist[filename].freq(token)

	def get_data(self):
		'''
		This method gets the calculated data from the unsmoothed object

		Return:
			self.data -- list containing the file names of the test and predicted files, perplexity, and n value
		'''
		return self.data










