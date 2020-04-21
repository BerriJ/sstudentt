=====
Usage
=====

To use the distribution in a project::

    # Import SST class directly
    from sstudentt import SST

First create an instance of the :class:`SST` class as follows::

    dist = SST(mu = 1, sigma = 1, nu = 1, tau = 5)

Note that tau must be > 2.

Now you can draw random numbers, or get specific quantiles::

    # Draw 5 random realizations
    dist.r(5)

    # Calculate the Median
    dist.q(0.5)
