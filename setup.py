from setuptools import setup

requires = [
    'pyramid',
    'waitress',
]

setup(name='Api',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = Api:main
      """,
)
