from bridge_the_gap import SampleClassName


def test_calculate_answer():
    sample = SampleClassName('some', 1773, ['values'])
    assert sample.calculate_answer(0) == 42
