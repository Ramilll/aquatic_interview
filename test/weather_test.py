from interview import weather
from utils.utils import read_file
import io

def baseline_test(test_number):
    reader = io.StringIO(read_file("test/{}/input.txt".format(test_number)))
    writer = io.StringIO()
    weather.process_csv(reader, writer)
    assert writer.getvalue() == read_file("test/{}/output.txt".format(test_number)), "incorrect output on test number {}".format(test_number)

def test_zero():
    baseline_test(0)

def test_one():
    baseline_test(1)

def test_two():
    baseline_test(2)

def test_three():
    baseline_test(3)

def test_four():
    baseline_test(4)