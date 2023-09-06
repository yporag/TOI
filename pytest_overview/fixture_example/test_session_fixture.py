import pytest

# Define a fixture with session scope for setup
@pytest.fixture(scope="session")
def setup_state():
    # Perform setup actions, e.g., setting up a database connection
    print("Setting up state SESSION")
    
    # This can include yielding values or objects that will be used by the tests
    yield  # This is where the tests will run
    
    # Perform teardown actions, e.g., closing the database connection
    print("Tearing down state")

# Test functions that use the setup state
def test_function1(setup_state):
    print("performing test1")
    # Test code that relies on the setup state

def test_function2(setup_state):
    print("performing test2")
    # Test code that relies on the setup state

# More test functions...

# Finalize teardown after all tests have run (optional)
def test_teardown(setup_state):
    # You can add additional tests for teardown purposes if needed
    print("teardown state SESSION")
    pass