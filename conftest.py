import pytest

@pytest.fixture(
    params=["https://dog.ceo/api/breed/akita/images/random", "https://dog.ceo/api/breed/hound/images/random", "https://dog.ceo/api/breed/boxer/images/random"])
def pict(request):
    return request.param


@pytest.fixture(
    params=["https://dog.ceo/api/breed/hound/list", "https://dog.ceo/api/breed/briard/list", "https://dog.ceo/api/breed/mastiff/list"])
def per(request):
    return request.param