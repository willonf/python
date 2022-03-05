def soma(a: int, b: int) -> int:  # Type hinting: especificar os tipos dos parametros e retorno
    return a + b


def soma2(a, b):  # Sem type hinting
    return a + b


def produto(a, b):  # Type hinting no comentário
    # type: (float, float) -> float
    return a + b


def produto2(
        a,  # type: float
        b  # type: float
):
    # type: (...) -> float
    return a + b


nome = 'Willon'  # type: str

print(produto(5, 2))
print(produto(5, 'a'))
print(soma2(4, 5))
