OK_FORMAT = True

test = {
    "name": "q_is_even",
    "points": 1,
    "suites": [
        {
            "cases": [
                {"code": """
                >>> is_even(0)
                True
                >>> is_even(1)
                False
                >>> is_even(-2)
                True
                """}
            ]
        }
    ]
}
