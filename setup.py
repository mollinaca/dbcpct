from setuptools import setup, find_packages

setup(
    name="dblpct",
    version="1.20220102",
    description="Reduce % to two.",
    url="https://github.com/mollinaca/dblpct",
    author="mollinaca",
    author_email="mail@mollinaca.dev",
    license="CC0",
    packages=find_packages(),
    entry_points="""
      [console_scripts]
      dblpct = dblpct.dblpct:main
    """,
)
