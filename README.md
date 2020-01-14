[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Welcome

This is GUI app with the following features:
- Reads/tokenizes words from sentences in text files.
- Cleans and prunes words.
- Finds occurrences of words along with lines of sentences in which they occurred.
- Pytest for Unit Tests (if I have time)

Project Structure
--------

  ```sh
  ├── README.md
  ├── requirements.txt
  ├── utils
      ├── classes
      │   └── __init__.py
      └── __init__.py
  
  ```



### Quick Start

1. Clone the repo
  ```
  $ git clone https://github.com/neguskay/slovo-tokenizator.git
  $ cd slovo-tokenizator
  ```

2. Initialize and activate a virtualenv:
  ```
  $ virtualenv --no-site-packages env
  $ source env/bin/activate
  ```

3. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

5. Run the development server:
  ```
  $ python __init__.py
  ```

6. Navigate to [http://localhost:5000](http://localhost:5000)



