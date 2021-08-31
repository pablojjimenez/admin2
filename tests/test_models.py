import pytest
from src.model.model import Model


class ExampleModel(Model):
    def __init__(self, data):
        super().__init__(data)


class TestModel:
    def test_empty_model(self):
        with pytest.raises(TypeError):
            ExampleModel()

    def test_model(self):
        c = ExampleModel({
            'attr1': 10,
            'attr2': [10, 0],
            'attr3': 'bye'
        })
        assert c.attr1 == 10
        assert c.attr2 == [10, 0]
        assert c.attr3 == 'bye'

    def test_model_dir(self):
        c = ExampleModel({
            'attr1': 10,
            'attr2': [10, 0],
            'attr3': 'bye'
        })
        assert str(c._dir()) == "['attr1', 'attr2', 'attr3']"