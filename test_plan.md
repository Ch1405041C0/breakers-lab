# Plan de prueba — BREAKERS vs BREAKERS LAB

## Objetivo
Validar el flujo completo de SCAN contra un baseline conocido.

## Precondiciones
- BREAKERS SCAN ejecutándose.
- BREAKERS LAB clonado localmente.
- Motores disponibles identificados en /api/tools.

## Ejecución
1. Clonar este repo.
2. Ejecutar BREAKERS SCAN sobre la carpeta local.
3. Guardar scan_id.
4. Comparar preview y reporte persistido con KNOWN_FINDINGS.md.
5. Registrar:
   - TP: hallazgos esperados detectados;
   - FN: esperados no detectados;
   - FP: hallazgos sin correspondencia;
   - duplicados;
   - severidad;
   - motor;
   - score.

## Resultado esperado
BREAKERS debe:
- completar el análisis sin caerse aunque falle un motor;
- generar scan_id;
- persistir el reporte;
- mostrar solo preview antes del desbloqueo;
- permitir recuperar el preview por scan_id.
