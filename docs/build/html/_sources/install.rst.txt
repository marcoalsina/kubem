How to install
==============

If you have `Conda <https://docs.conda.io/en/latest/>`_ installed (Anaconda or Miniconda), be sure to activate your environment before installing ``kubem``:

.. code-block:: bash

   name@machine:~$ conda activate <yourenvironment>


``kubem`` can be installed with ``pip``, which conveniently checks and downloads the required dependencies. The following install options are curently available:

Install with Git
----------------

If you have `Git <https://git-scm.com/>`_ in your machine, you can install directly by executing the following command in a terminal:

.. code-block:: bash

   name@machine:~$ pip install git+https://github.com/marcoalsina/kubem.git

Install with http
-----------------

Alternatively, you can download the source code and install ``kubem`` directly.
Open up a terminal and execute the following commands:

.. code-block:: bash

    name@machine:~$ wget https://github.com/marcoalsina/kubem/archive/master.zip
    name@machine:~$ unzip master.zip
    name@machine:~$ cd kubem-master
    name@machine:~$ pip install .
