def get_profile(*name="julian", *profession="programmer"):
    if not (isinstance(name, str) & isinstance(profession, str)):
        raise TypeError
    return f"{name} is a {profession}"