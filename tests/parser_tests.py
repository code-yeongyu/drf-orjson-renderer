from io import BytesIO

import pytest
import orjson
from rest_framework.exceptions import ParseError

from drf_orjson.parsers import ORJSONParser


@pytest.fixture()
def uut():
    return ORJSONParser()


@pytest.fixture()
def data():
    return {
        "a": [1, 2, 3],
        "b": True,
        "c": 1.23,
        "d": "test",
        "e": {"foo": "bar"},
    }


def test_basic_data_structure_parsed_correctly(uut, data):
    dumped = orjson.dumps(data)
    parsed = uut.parse(BytesIO(dumped))

    assert parsed == data


def test_parser_works_correctly_when_media_type_and_context_provided(uut, data):
    dumped = orjson.dumps(data)

    parsed = uut.parse(
        BytesIO(dumped),
        media_type="application/json",
        parser_context={},
    )

    assert parsed == data


def test_parser_catches_value_error_and_reraises_parse_error(uut, data, mocker):
    mock_ujson = mocker.patch("drf_orjson.parsers.orjson")
    mock_ujson.loads.side_effect = [ValueError("hello")]

    dumped = orjson.dumps(data)
    with pytest.raises(ParseError, match="hello"):
        uut.parse(BytesIO(dumped))
