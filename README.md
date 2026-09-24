# BREAKERS LAB

Laboratorio controlado para validar BREAKERS SCAN.

Este repositorio contiene una aplicación deliberadamente defectuosa, creada exclusivamente para pruebas de calidad y seguridad dentro de un entorno autorizado.

## Objetivo

Medir:
- cuántos hallazgos conocidos detecta BREAKERS;
- qué motores los detectan;
- falsos negativos y falsos positivos;
- duplicados;
- calidad de la priorización y del Quality Score.

## Stack

- Flask
- SQLite
- HTML/CSS/JS

## Hallazgos sembrados

La versión inicial contiene problemas deliberados de distintas categorías:
- credencial falsa hardcodeada;
- dependencia vulnerable fijada;
- debug habilitado;
- consulta SQL insegura;
- manejo inseguro de archivos;
- validación insuficiente de entrada;
- encabezados de seguridad ausentes;
- secreto de ejemplo expuesto;
- mala gestión de errores;
- problemas básicos de accesibilidad.

Ver `KNOWN_FINDINGS.md` para el catálogo esperado.

## Ejecución local

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Abrir: http://127.0.0.1:5000

> No desplegar esta aplicación en Internet. Está construida para ser insegura a propósito.
