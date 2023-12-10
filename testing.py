from utils import helpers as helpers
import numpy as np

arrayA = np.array([1, 0, -1])
arrayB = np.array([2, 8, 1])
arrayC = np.array([3, 1, 4])
print("Sim between A - C"+str(helpers.cosine_similarity(arrayA, arrayC)))
print("Sim between B - C"+str(helpers.cosine_similarity(arrayB, arrayC)))
print("Sim between A - B"+str(helpers.cosine_similarity(arrayA, arrayB)))