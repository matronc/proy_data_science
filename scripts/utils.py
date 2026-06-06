"""
utils.py
--------
Funciones reutilizables para el pipeline de análisis de ventas.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os


# ---------------------------------------------------------------------------
# Carga de datos
# ---------------------------------------------------------------------------

def cargar_csv(ruta: str, **kwargs) -> pd.DataFrame:
    """Carga un archivo CSV y devuelve un DataFrame.

    Parameters
    ----------
    ruta : str
        Ruta al archivo CSV.
    **kwargs
        Argumentos adicionales para ``pd.read_csv``.

    Returns
    -------
    pd.DataFrame
    """
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta}")
    df = pd.read_csv(ruta, **kwargs)
    print(f"[INFO] Archivo cargado: {ruta}  |  filas={len(df)}, columnas={len(df.columns)}")
    return df


# ---------------------------------------------------------------------------
# Limpieza de datos
# ---------------------------------------------------------------------------

def limpiar_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Elimina duplicados y filas con todos los valores nulos.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame limpio
    """
    filas_antes = len(df)
    df = df.drop_duplicates()
    df = df.dropna(how="all")
    filas_despues = len(df)
    print(f"[INFO] Limpieza: {filas_antes - filas_despues} filas eliminadas. Quedan {filas_despues}.")
    return df.reset_index(drop=True)


def convertir_tipos(df: pd.DataFrame, columnas_numericas: list[str]) -> pd.DataFrame:
    """Convierte columnas especificadas a tipo numérico.

    Parameters
    ----------
    df : pd.DataFrame
    columnas_numericas : list[str]
        Nombres de las columnas a convertir.

    Returns
    -------
    pd.DataFrame
    """
    for col in columnas_numericas:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


# ---------------------------------------------------------------------------
# Análisis
# ---------------------------------------------------------------------------

def resumen_estadistico(df: pd.DataFrame, columna: str) -> dict:
    """Calcula estadísticas básicas de una columna numérica.

    Parameters
    ----------
    df : pd.DataFrame
    columna : str

    Returns
    -------
    dict con media, mediana, std, min, max
    """
    serie = df[columna].dropna()
    return {
        "media": round(serie.mean(), 2),
        "mediana": round(serie.median(), 2),
        "std": round(serie.std(), 2),
        "min": round(serie.min(), 2),
        "max": round(serie.max(), 2),
    }


def ventas_por_categoria(df: pd.DataFrame,
                          col_categoria: str,
                          col_valor: str) -> pd.DataFrame:
    """Agrupa ventas por categoría y calcula total y promedio.

    Parameters
    ----------
    df : pd.DataFrame
    col_categoria : str
        Nombre de la columna de categorías.
    col_valor : str
        Nombre de la columna numérica a agregar.

    Returns
    -------
    pd.DataFrame con columnas [col_categoria, 'total', 'promedio', 'cantidad']
    """
    resumen = (
        df.groupby(col_categoria)[col_valor]
        .agg(total="sum", promedio="mean", cantidad="count")
        .round(2)
        .reset_index()
        .sort_values("total", ascending=False)
    )
    return resumen


# ---------------------------------------------------------------------------
# Visualización
# ---------------------------------------------------------------------------

def grafico_barras(df: pd.DataFrame,
                   col_x: str,
                   col_y: str,
                   titulo: str = "Ventas por Categoría",
                   carpeta_salida: str = "outputs") -> str:
    """Genera un gráfico de barras y lo guarda como imagen PNG.

    Parameters
    ----------
    df : pd.DataFrame
    col_x : str
        Columna del eje X (categorías).
    col_y : str
        Columna del eje Y (valores).
    titulo : str
    carpeta_salida : str
        Directorio donde se guardará la imagen.

    Returns
    -------
    str  ruta del archivo guardado
    """
    os.makedirs(carpeta_salida, exist_ok=True)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(df[col_x], df[col_y], color="steelblue", edgecolor="white")
    ax.set_title(titulo, fontsize=14, fontweight="bold")
    ax.set_xlabel(col_x)
    ax.set_ylabel(col_y)
    plt.tight_layout()
    nombre_archivo = os.path.join(carpeta_salida, f"{titulo.replace(' ', '_').lower()}.png")
    fig.savefig(nombre_archivo, dpi=150)
    plt.close(fig)
    print(f"[INFO] Gráfico guardado en: {nombre_archivo}")
    return nombre_archivo
