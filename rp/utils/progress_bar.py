
def prog_bar(current_value: int, max_value: int, bar_width: int=20, config=None):
    DEFAULT_FILL = "*"
    DEFAULT_SPACE = " "
    DEFAULT_SIDE = "|"
    if config is None:
        config = {
            "fill": DEFAULT_FILL,
            "space": DEFAULT_SPACE,
            "side": DEFAULT_SIDE
        }

    ratio = current_value/max_value
    fill_width = int(ratio * bar_width)
    if current_value > 0:
        fill_width = max(fill_width, 1)

    space_width = bar_width - fill_width

    return f"{config.get('side', DEFAULT_SIDE)}{config.get('fill', DEFAULT_FILL) * fill_width}{config.get('space', DEFAULT_SPACE) * space_width}{config.get('side', DEFAULT_SIDE)}"
