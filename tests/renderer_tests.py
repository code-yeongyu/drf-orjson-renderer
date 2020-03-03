import pytest
import orjson

from drf_orjson.renderers import ORJSONRenderer


@pytest.fixture()
def uut():
    return ORJSONRenderer()


@pytest.fixture()
def data():
    return {
        "a": [1, 2, 3],
        "b": True,
        "c": 1.23,
        "d": "test",
        "e": {"foo": "bar"},
    }


def test_basic_data_structures_rendered_correctly(uut, data):
    rendered = uut.render(data)
    reloaded = orjson.loads(rendered)

    assert reloaded == data


def test_renderer_works_correctly_when_media_type_and_context_provided(uut, data):
    rendered = uut.render(
        data=data, accepted_media_type="application/json", renderer_context={}
    )
    reloaded = orjson.loads(rendered)

    assert reloaded == data


def test_renderer_gets_no_data_returns_empty_bytes(uut):
    rendered = uut.render(None)

    assert rendered == b""
