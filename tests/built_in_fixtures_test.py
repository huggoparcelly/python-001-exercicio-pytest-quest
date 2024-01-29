import pytest

from src.hex_converter import (  # noqa: F401
    main,
    print_hexadecimal_to_decimal,
    write_hexadecimal_to_decimal,
)

# aplica o marcador de dependency para todos os testes do arquivo
pytestmark = pytest.mark.dependency  # NÃO REMOVA ESSA LINHA


def test_monkeypatch(monkeypatch):

    def mock_input(_):
        return "a"
    
    monkeypatch.setattr("builtins.input", mock_input)
    output = main()

    assert output == 10


def test_capsys(capsys):
    input = "a"
    expected_output = "10\n"
    expected_err = ""
    print_hexadecimal_to_decimal(input)
    capture = capsys.readouterr()
    assert capture.out == expected_output
    assert capture.err == expected_err


def test_tmp_path(tmp_path):
    input_hexa = "a"
    output_path = tmp_path / "output.txt"

    write_hexadecimal_to_decimal(input_hexa, output_path)
    with open(output_path) as file:
        assert file.read() == "10"