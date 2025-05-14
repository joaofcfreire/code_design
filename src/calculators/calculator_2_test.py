from typing import Dict, List
from .calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler(DriverHandlerInterface):
    def standard_derivation(self, numbers: List[float]) -> float:
        return 3

# Integração entre NumpyHandler e Calculator2
def test_calculate_integration():
    mock_request = MockRequest({
        "numbers": [
            2.123, 4.62, 1.32
        ]
    })

    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)
    response = calculator_2.calculate(mock_request)

    # Formato da resposta
    assert isinstance(response, dict)
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    # Assertividade da resposta
    assert response["data"]["result"] == 0.08
    assert response["data"]["Calculator"] == 2

# Teste unitário de fato do Calculator2
def test_calculate():
    mock_request = MockRequest({
        "numbers": [
            2.123, 4.62, 1.32
        ]
    })

    driver = MockDriverHandler()
    calculator_2 = Calculator2(driver)
    response = calculator_2.calculate(mock_request)

    # Formato da resposta
    assert isinstance(response, dict)
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    # Assertividade da resposta
    assert response["data"]["result"] == 0.33
    assert response["data"]["Calculator"] == 2