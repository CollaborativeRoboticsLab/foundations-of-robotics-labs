OK_FORMAT = True

test = {
    "name": "q_merge_dicts",
    "points": 1,
    "suites": [
        {
            "cases": [
                {"code": """
                >>> a = {'x': 1, 'z': 0}
                >>> b = {'x': 2, 'y': 3}
                >>> out = merge_dicts(a, b)
                >>> out['x']
                2
                >>> out['y']
                3
                >>> out['z']
                0
                """}
            ]
        }
    ]
}
