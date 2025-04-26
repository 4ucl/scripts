def introduction():
    return {
        "name": "Hacker name generator",
        "desc": "转换为特定格式的名字",
        "author":
        [
            "L"
        ],
        "category":
        [
            "工具"
        ]
    }


def params():
    return [
        {
            "key": "source_input",
            "name": "源输入",
            "detail": None,
            "position": 0,
            "required": True,
            "uiComponentSchema": {
                "type": "inputText",
            },
            "jsonSchema": {
                "type": "string"
            }
        },
        {
            "key": "forward",
            "name": "正逆向",
            "detail": "true: 正向, false: 逆向",
            "position": 1,
            "required": True,
            "uiComponentSchema": {
                "type": "selectButton",
                "options": [
                    {
                        "value": True,
                        "name": "正向"
                    },
                    {
                        "value": False,
                        "name": "逆向"
                    }
                ],
                "defaultValue": True
            },
            "jsonSchema": {
                "type": "boolean"
            }
        },
        # {
        #     "name": "input_files",
        #     "desc": "文件列表",
        #     "detail": "",
        #     "type": "files",
        #     "position": 1,
        #     "required": True,
        #     "default": True,
        #     "option": {
        #         "maxLength": 2
        #     }
        # }
    ]


def run(source_input: str, forward: bool = True):
    # 26 English letters in hacker style
    letters_in_hacker_style = "48cd3f6h1jklmn0pqr57uvwxyz"
    # The unicode code point of letter a
    ord_a = ord('a')

    data = None
    if forward:
        data = "".join([char if not char.isalpha() else letters_in_hacker_style[ord(char) - ord_a]
                   for char in list(source_input.lower())]).upper()
    else:
        data = "".join([char if letters_in_hacker_style.find(char) == -1 else chr(ord_a + letters_in_hacker_style.find(char))
                   for char in list(source_input.lower())]).lower()

    return {
        "data": data,
        "type": "plaintext"
    }


if __name__ == '__main__':
    import argparse
    import json

    parser = argparse.ArgumentParser()
    parser.add_argument('func', type=str, help='The function name')
    parser.add_argument('--args', nargs='?', required=False)
    _args = parser.parse_args()

    func = globals().get(_args.func)
    result = func(**json.loads(_args.args)) if _args.args else func()

    print(json.dumps(result, ensure_ascii=False))
