from flask import request as FlaskRequest
from typing import Dict, List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator2:
    """
    * N números são enviados
    * Todos esses N números são multiplicados por 11 e elevados a potência de 0.95.
    * Por fim, é retirado o desvio padrão desses resultados e retornado o inverso desse valor (1/result).
    """
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)

        first_process_result = self.__first_process(input_data)
        calc_result = self.__second_process(first_process_result)

        response = self.__format_response(calc_result)
        return response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Invalid body!")

        input_data = body["numbers"]
        return input_data

    def __first_process(self, input_data: List[float]) -> List[float]:
        first_part = [num * 11 for num in input_data]
        second_part = [num ** 0.95 for num in first_part]
        return second_part

    def __second_process(self, first_process_result: List[float]) -> float:
        result = self.driver_handler.standard_derivation(first_process_result)
        return (1/result)

    def __format_response(self, calc_result: float) -> Dict:
        return {
            "data": {
                "Calculator": 2,
                "result": round(calc_result, 2)
            }
        }