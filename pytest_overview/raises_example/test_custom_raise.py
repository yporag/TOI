import pytest

def function_that_raises_exception(input):
    if (input < 5):
        raise ValueError("Still bad, but you should continue")
    
    raise ValueError("Very bad, everything is on fire")

@pytest.mark.parametrize("input",[3,10])
def test_exception_handling(input):
    with pytest.raises(ValueError) as exc_info:
        function_that_raises_exception(input)
        
    # Now you can make assertions about the raised exception
    assert str(exc_info.value) == "Still bad, but you should continue"
