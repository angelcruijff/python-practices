import textwrap

texto = """
Texto de muestra para mostrar la funcionalidad
de acortar el texto. Esto puede ser util en
determinadas situaciones, como un preview de un
articulo o texto especial para base de datos.
"""

"""
La funcion shorten de textwrap acorta el texto
y no muestra palabras parciales, es por eso que
no muestra la cantidad exacta de caracteres
solicitados.
"""
texto_corto = textwrap.shorten(texto, 50)

"""
Por default, el metodo shorten utiliza el placeholder
[...] al final de cada cadena pero puede ser reemplazado
si usamos el parametro 'placeholder'. 
Los caracteres usados en el placeholder tambien son 
considerados en la cantidad del texto acortado
"""
texto_corto_placeholder = textwrap.shorten(texto, 50, placeholder='>>>>>')

print(texto)
print("\n\n")
print(texto_corto)
print("\n\n")
print(texto_corto_placeholder)
