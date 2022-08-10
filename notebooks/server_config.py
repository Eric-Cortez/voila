## The common section includes global server parameters and parameters
## reused in multiple other classes
[common]
parnames = [par1, par2]     # names of the parameters
lb = [0, 0]     # lower bouns of the parameters, in the same order as above
ub = [10, 10]   # upper bounds of parameter, in the same order as above
stimuli_per_trial = 1   # the number of stimuli shown in each trial; 1 for single, or 2 for pairwise experiments
outcome_types = [continuous]    # the type of response given by the participant; can be [binary] or [continuous]
strategy_names = [init_strat, opt_strat] # The strategies that will be used, corresponding to the named sections below

# Configuration for the initialization strategy, which we use to gather initial points
# before we start doing model-based acquisition
[init_strat]
min_asks = 10   # number of sobol trials to run
# The generator class used to generate new parameter values
generator = SobolGenerator

#  Configuration for the optimization strategy, our model_based acquisition
[opt_strat]
min_asks = 40   # number of model-based trials to run
generator = OptimizeAcqfGenerator   # The generator class used to generate new parameter values

# The model, which must conform to the stimuli_per_trial and outcome_types settings above.
#  Use GPClassificationModel or GPRegressionModel for single or PairwiseProbitModel for pairwise.
model = GPRegressionModel

# Acquisition function: the objective we use to decide where to simple next. We recommend
# MonotonicMCLSE for threshold finding, MonotonicMCPosteriorVariance for global exploration,
# qNoisyExpectedImporvement for optimization. For other options, check out the botorch and
# aepsych docs
acqf = qNoisyExpectedImprovement

## OptimizeAcqfGenerator model settings.
[OptimizeAcqfGenerator]
restarts = 10   # number of restarts for acquisition functions optimization
samps = 1000    # number of samples for quasi-random initialization of the acquisition function optimizer
