from scipy import stats
import numpy as np


def make_dirichlet_distribution(tuples, concentration):
    alpha = np.array([old_value for (obj, metric, old_value) in tuples])
    rv = stats.dirichlet(alpha * concentration)
    def _sample_dirichlet():
        return rv.rvs(size=1)[0]
    return _sample_dirichlet
    
def make_uniform_distribution(lower, upper):
    assert upper >= lower
    loc = lower
    scale = upper - lower
    rv = stats.uniform(loc, scale)
    def _sample_uniform():
        return rv.rvs(size=1)[0]
    return _sample_uniform

def make_normal_distribution(mean, sd):
    loc = mean
    scale = sd
    rv = stats.norm(loc, scale)
    def _sample_normal():
        return rv.rvs(size=1)[0]
    return _sample_normal


def make_normal_distribution_recipe(mean, sd):
    loc =  np.array([old_value for (obj, metric, old_value) in mean])
    scale = sd
    rv = stats.norm(loc, scale)
    def _sample_normal():
        return rv.rvs
    return _sample_normal