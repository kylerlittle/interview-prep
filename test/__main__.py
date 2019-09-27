import unittest
import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../study'
# Make sure our src code directory is in PATH variable.
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

def main():
    loader = unittest.TestLoader()
    tests = loader.discover(start_dir='.', pattern='test_*.py')
    test_runner = unittest.runner.TextTestRunner()
    test_runner.run(tests)

if __name__ == "__main__":
    main()