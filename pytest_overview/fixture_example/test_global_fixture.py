import pytest

# Define a fixture with session scope for setup

# Test functions that use the setup state
def test_function1(setup_state):
    print("performing test1")
    # Test code that relies on the setup state

def test_function2(setup_state):
    print("performing test2")
    # Test code that relies on the setup state

# Test functions that use the setup state
def test_function3(setup_state_session):
    print("performing test1")
    # Test code that relies on the setup state

def test_function4(setup_state_session):
    print("performing test2")
    # Test code that relies on the setup state

# More test functions...

def test_teardown(setup_state):
    # You can add additional tests for teardown purposes if needed
    print("teardown state")

# Finalize teardown after all tests have run (optional)
def test_teardown_session(setup_state_session):
    # You can add additional tests for teardown purposes if needed
    print("teardown state")