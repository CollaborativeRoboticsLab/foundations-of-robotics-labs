OK_FORMAT = True

test = {
    "name": "q_reverse_string",
    "points": 1,
    "suites": [
        {
            "cases": [
                {"code": """
                >>> reverse_string("abc")
                'cba'
                >>> reverse_string("")
                ''
                >>> reverse_string("racecar")
                'racecar'
                """}
            ]
        }
    ]
}
