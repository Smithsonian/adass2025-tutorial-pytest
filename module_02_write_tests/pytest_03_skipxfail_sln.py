import pytest


@pytest.mark.skip(reason="Feature under development")
def test_skip():
    assert False


@pytest.mark.xfail(reason="Known bug with negative input")
def test_xfail():
    assert 1 / 0 == 1


def test_foobar(request):
    """Try changing the hardcoded server value from server='foo' to 'bar'"""
    server = "foo"
    # server = "bar
    if server != "bar":
        reason = "Require bar. All other servers violate requirements."
        request.node.add_marker(pytest.mark.xfail(reason=reason))

    assert server == "bar"
