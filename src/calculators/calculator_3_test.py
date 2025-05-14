from typing import Dict, List
from pytest import raises
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from .calculator_3 import Calculator3

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandlerError(DriverHandlerInterface):
    def standard_derivation(self, numbers: List[float]) -> None:
        pass
    
    def variance(self, numbers: List[float]) -> float:
        return 3

class MockDriverHandler(DriverHandlerInterface):
    def standard_derivation(self, numbers: List[float]) -> None:
        pass
    
    def variance(self, numbers: List[float]) -> float:
        return 100000

def test_calculate_with_variance_error():
    mock_request = MockRequest({
        "numbers": [
            1, 2, 3, 4, 5
        ]
    })

    calculator_3 = Calculator3(MockDriverHandlerError())

    with raises(Exception) as exc_info:
        calculator_3.calculate(mock_request)

    assert str(exc_info.value) == "Process failure: Variance less than multiplication"

def test_calculate():
    mock_request = MockRequest({
        "numbers": [
            1, 1, 1, 1, 100
        ]
    })

    calculator_3 = Calculator3(MockDriverHandler())
    response = calculator_3.calculate(mock_request)
    
    # Formato da resposta
    assert isinstance(response, dict)
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "variance" in response["data"]
    assert "Success" in response["data"]

    # Assertividade da resposta
    assert response["data"]["variance"] == 100000
    assert response["data"]["Calculator"] == 3