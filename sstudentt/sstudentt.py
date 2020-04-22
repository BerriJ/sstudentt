"""Main module."""

import numpy as np
from scipy import stats
from scipy.special import beta


class SST:
    # Init Parameters
    def __init__(self, mu, sigma, nu, tau):
        """
        Creates an Instance of the Skewed Student T Distribution.
        In this parameterization the expectation equals mu and standard
        deviation equals sigma.

        :param mu: mu parameter
        :type mu: scalar or array_like
        :param sigma: sigma parameter
        :type sigma: scalar or array_like
        :param nu: nu parameter
        :type nu: scalar or array_like
        :param tau: tau parameter
        :type tau: scalar or array_like
        """
        self.mu = np.asarray(mu).astype(float)
        self.sigma = np.asarray(sigma).astype(float)
        self.nu = np.asarray(nu).astype(float)
        self.tau = np.asarray(tau).astype(float)
        self.c = 2 * self.nu * ((1 + self.nu ** 2) *
                                beta(0.5, self.tau / 2) *
                                self.tau ** 0.5) ** -1
        self.m = ((2 * self.tau ** 0.5) * (self.nu - self.nu ** -1)) / (
                (self.tau - 1) * beta(0.5, 0.5 * self.tau))
        self.s2 = ((self.tau / (self.tau - 2)) * (
                self.nu ** 2 + self.nu ** -2 - 1) - self.m ** 2)
        self.mu_0 = self.mu - (self.sigma * self.m / np.sqrt(self.s2))
        self.sigma_0 = self.sigma / np.sqrt(self.s2)

    # Density Function
    def d(self, y):
        """Density Function

        :param y: distribution values
        :type y: scalar or array_like
        :return: density at the specified y values
        :rtype: array
        """
        mu_0 = self.mu_0
        sigma_0 = self.sigma_0
        c = self.c
        nu = self.nu
        tau = self.tau
        z = (y - mu_0) / sigma_0
        p = np.where(y < mu_0,
                     (c / sigma_0) * (1 + ((nu ** 2) * (z ** 2)) / tau) ** (
                             -(tau + 1) / 2),
                     (c / sigma_0) * (1 + (z ** 2) / ((nu ** 2) * tau)) ** (
                             -(tau + 1) / 2))
        return p

    def q(self, p):
        """Quantile Function / Inverse CDF / Percent Point Function

        :param p: probabilities
        :type p: scalar or array_like
        :return: Quantile values corresponding to the specified probabilities.
        :rtype: array
        """
        p = np.asarray(p).astype(float)
        mu_0 = self.mu_0
        sigma_0 = self.sigma_0
        nu = self.nu
        tau = self.tau
        # Calculate quantile
        quantile = np.where(p <= (1 + nu ** 2) ** -1,
                            mu_0 + (sigma_0 / nu) * stats.t.ppf(
                                (p * (1 + nu ** 2)) * 0.5, tau),
                            mu_0 + sigma_0 * nu * stats.t.ppf(
                                (p * (1 + nu ** 2) - 1 + nu ** 2) / (
                                        2 * nu ** 2), tau)
                            )
        return quantile

    # Cumulative Distribution Function
    def p(self, q):
        """Distribution Function

        :param q: value
        :type q: scalar or array_like
        :return: The probability that the SST distributed variable will take
        a value less than or equal to q.
        :rtype: array
        """
        nu = self.nu
        mu_0 = self.mu_0
        tau = self.tau
        sigma_0 = self.sigma_0
        # Calculate CDF
        prob = np.where(q < mu_0,
                        (2 / (1 + nu ** 2)) * stats.t.cdf(
                            x=(nu * (q - mu_0) / sigma_0), df=tau),
                        (1 / (1 + nu ** 2)) * (
                            1 + 2 * nu ** 2 * (
                                stats.t.cdf(x=(q - mu_0) / (sigma_0 * nu),
                                            df=tau) - 0.5))
                        )
        return prob

    # Draw Random Numbers using Inversion Sampling
    def r(self, n=1):
        """Draws Random Numbers which Follow the SST Distribution

        :param n: sample size
        :type n: int or tuple of return shape, optional
        :return: random sample drawn from the SST distribution
        :rtype: array

        .. note::
           n is ignored if the distribution parameters are provided as
           arrays. In that case, a sample with the shape of the provided arrays
           will be drawn. i.e. n = 1.

        """
        return self.q(p=np.random.random(size=n))
