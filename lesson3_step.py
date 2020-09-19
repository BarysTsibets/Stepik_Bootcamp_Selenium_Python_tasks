# def test_input_text(expected_result, actual_result):
#     assert expected_result == actual_result, \
#         f"expected {expected_result}, got {actual_result}"
#     if True:
#         return f"{expected_result} {actual_result}"
#
#
# print(test_input_text(11, 12))


def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f'expected {expected_result}, got {actual_result}'

test_input_text(9, 9)