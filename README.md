# Análisis de Ventas por Categoría

Pipeline reproducible de carga, limpieza, análisis y visualización de datos de ventas.

---

## Estructura del proyecto

```
proyecto_reproducible/
├── data/
│   └── resumen_ventas_preparado.csv   # Dataset de ventas (fuente)
├── notebooks/
│   └── analisis_ventas.ipynb          # Notebook principal (limpio y comentado)
├── outputs/
│   └── *.png                          # Gráficos generados automáticamente
├── scripts/
│   └── utils.py                       # Funciones reutilizables (carga, limpieza, análisis, viz)
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Requisitos previos

- Python >= 3.10
- `pip` actualizado

---

## Instalación rápida

```bash
# 1. Clona el repositorio
git clone <URL-del-repositorio>
cd proyecto_reproducible

# 2. (Opcional) Crea un entorno virtual
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux / macOS:
source .venv/bin/activate

# 3. Instala las dependencias
pip install -r requirements.txt
```

---

## Reproducir el análisis

```bash
# Desde la raíz del proyecto, abre el notebook
jupyter notebook notebooks/analisis_ventas.ipynb
```

Ejecuta las celdas en orden (**Kernel → Restart & Run All**).  
Los gráficos se guardarán automáticamente en la carpeta `outputs/`.

---

## Dataset

| Columna | Tipo | Descripción |
|---------|------|-------------|
| `Categoria` | str | Categoría del producto (`Hogar`, `Tech`, …) |
| `Precio_Medio` | float | Precio promedio de venta en la categoría |
| `Total_Ventas_Acumuladas` | float | Suma total de ventas registradas |

El archivo fuente se encuentra en `data/resumen_ventas_preparado.csv`.

---

## Funciones reutilizables (`scripts/utils.py`)

| Función | Descripción |
|---------|-------------|
| `cargar_csv(ruta)` | Carga un CSV y devuelve un DataFrame |
| `limpiar_dataframe(df)` | Elimina duplicados y filas vacías |
| `convertir_tipos(df, cols)` | Convierte columnas a tipo numérico |
| `resumen_estadistico(df, col)` | Media, mediana, std, min, max |
| `ventas_por_categoria(df, cat, val)` | Agrupación total/promedio/cantidad |
| `grafico_barras(df, x, y, ...)` | Genera y guarda un gráfico de barras PNG |

---

## Control de versiones

El repositorio usa **Git**. Convención de mensajes de commit:

```
feat: <descripción breve de la nueva funcionalidad>
fix:  <descripción del error corregido>
docs: <cambios en documentación>
data: <actualización del dataset>
```

---

## Licencia

MIT — libre para uso educativo y profesional.
