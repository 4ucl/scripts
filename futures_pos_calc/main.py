def introduction():
    return {
        "name": "Futures Position Calculator",
        "desc": "合约仓位计算器",
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
            "key": "risk_amount",
            "name": "止损金额",
            "detail": None,
            "position": 0,
            "required": True,
            "uiComponentSchema": {
                "type": "inputNumber",
            },
            "jsonSchema": {
                "type": "number"
            }
        },
        {
            "key": "entry_price",
            "name": "开仓点位",
            "detail": None,
            "position": 1,
            "required": True,
            "uiComponentSchema": {
                "type": "inputNumber",
            },
            "jsonSchema": {
                "type": "number"
            }
        },
        {
            "key": "stop_loss_price",
            "name": "止损点位",
            "detail": None,
            "position": 2,
            "required": True,
            "uiComponentSchema": {
                "type": "inputNumber",
            },
            "jsonSchema": {
                "type": "number"
            }
        },
    ]


def run(risk_amount: float, entry_price: float, stop_loss_price: float):
    """
        根据给定的风险金额、开仓点位和止损点位，计算交易参数。

        这个计算器假设风险回报比 (Risk/Reward Ratio) 为 1:1。

        Args:
            risk_amount (float): 愿意承担的总止损金额 (Amount to Risk)。
            entry_price (float): 计划的开仓点位 (Entry Price)。
            stop_loss_price (float): 计划的止损点位 (Stop Loss Price)。

        Returns:
            dict: 一个包含计算结果的字典，包括买入数量、止盈点位和止盈金额。
                  如果输入无效（例如开仓价等于止损价），则返回一个包含错误信息的字典。
        """
    # 检查输入是否有效，防止除以零的错误
    if entry_price == stop_loss_price:
        return {
            "data": "开仓点位不能等于止损点位。",
            "type": "plaintext"
        }

    # 1. 计算每单位的风险（开仓价和止损价之间的绝对差值）
    # |开仓点位 - 止损点位|
    risk_per_unit = abs(entry_price - stop_loss_price)

    # 2. 计算买入数量 (Position Size)
    # 买入数量 = 止损金额 / 每单位的风险
    # 按照要求，结果保留小数点后六位
    position_size = round(risk_amount / risk_per_unit, 6)

    # 3. 计算止盈点位 (Take Profit Price)
    # 止盈点位 = 开仓点位 + (开仓点位 - 止损点位)
    # 这个公式同时适用于做多（entry > stop_loss）和做空（entry < stop_loss）
    take_profit_price = entry_price + (entry_price - stop_loss_price)

    # 4. 计算止盈金额 (Take Profit Amount)
    # 因为这是一个 1:1 的风险回报比，所以止盈金额等于止损金额。
    # 也可以通过公式验证: (止盈点位 - 开仓点位) * 买入数量
    # take_profit_amount = abs(take_profit_price - entry_price) * position_size
    # 简化后，它就等于 risk_amount
    take_profit_amount = round(risk_amount, 6)

    # 整理并返回结果
    data = f"""
    买入数量 (Position Size): {position_size}\n
    止盈点位 (Take Profit Price): {take_profit_price}\n
    止盈金额 (Take Profit Amount): {take_profit_amount}\n
    """

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
