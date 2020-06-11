from distutils.core import setup
setup(
  name = 'robotframework-nsm',
  packages = ['nsm'],
  version = '0.11',
  license='MIT',
  description = 'Robotframework library for NSM',
  author = 'Adam Przybyla',
  author_email = 'adam.przybyla@gmail.com',
  url = 'https://github.com/AdamPrzybyla/robotframework-nsm',
  download_url = 'https://github.com/AdamPrzybyla/robotframework-nsm/archive/v_11.tar.gz',
  keywords = ['robotframework', 'nsm', 'automatisation', 'tests'],
  install_requires=[
          'robotframework',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 2',
  ],
)
