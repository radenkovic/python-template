from app.main import SampleApp


def test_app():
    app = SampleApp()
    assert app.dummy_value == 10


def test_app_with_param():
    app = SampleApp(dummy_value=100)
    assert app.dummy_value == 100
