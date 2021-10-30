def get_profile(name="julian", profession="programmer"):
    try:
        isinstance(name, str) & isinstance(profession, str)
    except:
        raise
    return f"{name} is a {profession}"
    