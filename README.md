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
git clone https://github.com/usuario/proy_data_science
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

El repositorio usa **Git** con commits frecuentes y atómicos: cada commit refleja un único avance concreto (una función nueva, un gráfico, una corrección).

### Convención de mensajes

```
<tipo>: <descripción breve en imperativo>
```

| Tipo | Cuándo usarlo |
|------|---------------|
| `feat` | Nueva funcionalidad o análisis |
| `fix` | Corrección de error o resultado incorrecto |
| `docs` | Cambios en README u otra documentación |
| `data` | Actualización o corrección del dataset |
| `refactor` | Mejora interna sin cambio de comportamiento |
| `style` | Formato, limpieza de celdas, sin lógica nueva |
| `chore` | Tareas de mantenimiento (deps, `.gitignore`, etc.) |

### Ejemplos aplicados a este proyecto

```bash
git commit -m "data: agregar resumen_ventas_preparado.csv como fuente principal"
git commit -m "feat: implementar cargar_csv y limpiar_dataframe en utils.py"
git commit -m "feat: añadir análisis de ventas por categoría con agrupación"
git commit -m "feat: generar gráfico de barras por categoría y guardar en outputs/"
git commit -m "fix: corregir conversión de tipos en columna Precio_Medio"
git commit -m "docs: completar README con estructura, instalación y uso"
git commit -m "chore: eliminar dependencias no utilizadas de requirements.txt"
```

### Frecuencia recomendada

- Haz commit al terminar **cada función** en `utils.py`.
- Haz commit al completar **cada sección del notebook** (carga, limpieza, análisis, visualización).
- No acumules varios cambios sin relacionar en un solo commit.

---

## Licencia

MIT — libre para uso educativo y profesional.
