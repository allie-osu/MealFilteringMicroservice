from setuptools import setup

setup(
      name='mealfilteringservice',
      version='1.0',
      packages=['mealfilteringservice'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            'flask'
      ],
)