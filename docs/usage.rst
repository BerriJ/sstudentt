=====
Usage
=====

This page demonstrates the usage of the :class:`sstudentt.SST` Class.

Importing the Class
-------------------

.. code-block:: python

    >>> from sstudentt import SST


Initialize a Class Instance
---------------------------

Now, create an instance of the :class:`sstudentt.SST` class as follows:

.. code-block:: python

    >>> dist = SST(mu = 1, sigma = 1, nu = 1, tau = 5)

.. note::

   This distribution is only defined for tau > 2 it will return NaN if you set tau to <= 2.

Calculate Densities
-------------------

You can evaluate the density of your distribution using the .d method:

.. code-block:: python

    >>> dist.d(5)
    array(0.00192913)


Calculate Probabilities
-----------------------

To evaluate the cumulative distribution function use .p:

.. code-block:: python

    >>> dist.p(5)
    array(0.99821359)

Calculate quantiles
-------------------

Calculate quantiles with the .q method as follows:

.. code-block:: python

    # Calculate the Median
    >>> dist.q(0.5)
    array(1.)

.. note::

   Since dist.nu equals 1 we have defined a symmetric distribution. That is, the median equals the mean (dist.mu).

Draw Random Numbers
-------------------

.. code-block:: python

    # Draw 5 random realizations
    >>> dist.r(5)
    array([3.05375391, 1.34209471, 1.01463769, 1.87961664, 1.58893329])

.. note::

   You can also define the shape of the return array to draw multiple random numbers as follows.
   Note that this only works when all class parameters (mu, sigma, nu tau) are defined as scalars. If (some of them) are arrays .r will always return an array of random values that matches the respective input shape

.. code-block:: python

    # Draw 5 random realizations
    >>> dist.r((4,5))
    array([[ 1.92072641,  0.60935071,  2.13692281,  0.66015911,  3.11887499],
          [ 2.08452098, -0.3657303 ,  0.95636288,  2.67946154,  0.89610456],
          [ 1.13357025, -0.26609876,  2.32864548,  0.79109498,  2.00020994],
          [ 0.64556586,  1.32889601, -0.49943665, -0.14925501,  1.11598305]])

Use an array of parameter values
--------------------------------

It's possible to intialize the distribution using arrays for the parameters.

For demonstration purposes we will define 2 arrays:

.. code-block:: python

    >>> arr_1 = np.array([[1, 3], [3, 7]])
    >>> arr_2 = np.array([[7, 3], [3, 1]])

You can use these arrays to instantiate a distribution as follows:

.. code-block:: python

    >>> dist2 = SST(mu = arr_1, sigma = arr_2, nu = 2, tau = 4)

As you can see, it's possible to mix arrays (of equal size) with scalars.

The methods will now return an array of the same shape:

.. code-block:: python

    >>> dist2.p(2)
    array([[6.63755107e-01, 4.35802430e-01],
           [4.35802430e-01, 1.21990298e-05]])

Its even possible to use an array (of the same shape) as method input:

.. code-block:: python

    >>> dist2.p(arr_2)
    array([[8.57842312e-01, 6.04032453e-01],
           [6.04032453e-01, 5.29846717e-06]])

This does not work with the .r method.

.. warning::

   The functions are relatively robust against arrays of different sizes because it uses the numpy broadcasting for casting arrays together.
   This can, however, create results which might be hard to interpret.
   Therefore, I strongly recommend sticking to one of the following for parameter definition:

    * Scalars for all parameters
    * Arrays of the same shape for all parameters
    * A mixture of scalars and same shaped arrays


