#
#
#
#
"""
Phewas object used to run different phenotype statistical anaylses.

This module is used to execute a variety of different analyses on large sets of patient phenotype data.

"""

import pyPhewaslog, pyPhewaslin

class Phewas:

	"""
	The Phewas object is used to run different types of Phewas regressions and plots.

	"""

	def __init__(self, inputfile, groupfile, path='', covariates='genotype', reg_type=0, save='', output=''):
		"""
		Creates a Phewas object with the given parameters.

		:param inputfile: the name of the phenotype file (no path)
		:param groupfile: the name of the genotype file (no path)
		:param path: the path to the inputfile and groupfile, this path will be used for all outputs as well. Defaults to empty path (i.e. current directory)
		:param covariates: the covariates that want to be run by pyPhewas, each additional covariate must be delimited by a *+* sign (i.e 'genotype+age')
		:param save: the filename to save the generated plot. The default is an empty string. This will result in the plot being displayed.
		:param output: the filename to save the regression data. The default is an empty string.

		"""
		self.pargs = [path, inputfile, groupfile, covariates, save, output]
		self.results = None
	def run_lin(self):
		"""
		Runs a linear regression on the current arguments.

		Upon completion, the results of the regression are saved by the object so that they can be used without creating a new regression.

		"""
		self.result = (pyPhewaslin.phewas(*self.pargs))
	def run_log(self):
		"""
		Runs a logarithmic regression on the current arguments.

		Upon completion, the results of the regression are saved by the object so that they can be used without creating a new regression.

		"""
		self.result = (pyPhewaslog.phewas(*self.pargs))
	def replot(self):
		"""
		Replots the regression that was execut