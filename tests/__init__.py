"""
    To run all test case:
    python manage.py test tests
"""

from accounts.tests.token_tests import *
from accounts.tests.user_tests import *
from accounts.tests.profile_tests import *
from weather.tests import *
from products.tests.product_tests import *
from products.tests.product_type_tests import *
from products.tests.customer_tests import *
