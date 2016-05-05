from setuptools import setup, find_packages

setup(name='mortals',
      version='0.1',
      description='Humans of planet earth.',
      author='Brahma',
      author_email='four@faces.com',
      license='MIT',
      keywords=['mammals', 'bipedal', 'sentient'],
      packages=find_packages(),
      install_requires=['funniest'],
      entry_points={'console_scripts':
                    ['wisdom = humans.tupac:spout_wisdom']})
