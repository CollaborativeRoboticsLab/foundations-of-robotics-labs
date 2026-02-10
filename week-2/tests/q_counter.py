OK_FORMAT = True

test = {
    "name": "q_counter",
    "points": 1,
    "suites": [
        {
            "cases": [
                {"code": """
                >>> c = Counter()
                >>> c.value
                0
                >>> c.inc()
                >>> c.value
                1
                >>> c.inc(3)
                >>> c.value
                4
                >>> c.reset()
                >>> c.value
                0
                """}
            ]
        }
    ]
}
