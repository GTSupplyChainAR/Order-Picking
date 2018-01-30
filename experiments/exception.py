try:
    if 1 < 10:
        raise Con("1 < 10")
except ValueError as ve:
    print(ve.args)
    raise
