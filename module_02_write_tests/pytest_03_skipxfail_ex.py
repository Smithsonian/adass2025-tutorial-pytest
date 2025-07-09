# Exercise: Using a pytest annotation, mark a test case to be skipped and provide a reason
def test_skip():
    assert False


# Exercise: Using a pytest annotation, mark a test case to xfail and provide a reason
def test_xfail():
    assert 1 / 0 == 1


# Exercise: Use a programmatic addition of a test marker,
# to conditionally mark a test to xfail if server != "bar"
# We might read 'server' from an environment variable in real life
# but we can hardcode in the test for the workshop.
#
# 'request' is a pytest fixture.
# Example useage:
# request.node.add_marker(pytest.mark.xfail(reason=reason))


def test_foobar(request):
    server = "foo"
    # server = "bar
    if server != "bar":
        pass

    assert server == "bar"
