import pytest

@pytest.fixture()
def setup_state():
    # Perform setup actions, e.g., setting up a database connection
    print("Setting up state GLOBAL ")
    
    # This can include yielding values or objects that will be used by the tests
    yield  # This is where the tests will run
    
    # Perform teardown actions, e.g., closing the database connection
    print("Tearing down state GLOBAL")

@pytest.fixture(scope="session")
def setup_state_session():
    # Perform setup actions, e.g., setting up a database connection
    print("Setting up state session GLOBAL ")
    
    # This can include yielding values or objects that will be used by the tests
    yield  # This is where the tests will run
    
    # Perform teardown actions, e.g., closing the database connection
    print("Tearing down state session GLOBAL")