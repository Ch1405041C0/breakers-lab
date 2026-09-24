# Catálogo de hallazgos esperados

Baseline inicial de BREAKERS LAB.

| ID | Categoría | Severidad esperada | Evidencia | Motor candidato |
|---|---|---:|---|---|
| BL-001 | Secreto hardcodeado | HIGH | `SECRET_KEY` en app.py | Gitleaks / Semgrep |
| BL-002 | Credencial falsa expuesta | HIGH | `.env.example` | Gitleaks / Trivy |
| BL-003 | SQL inseguro | HIGH | concatenación en /login | Semgrep / SonarQube |
| BL-004 | XSS reflejado | HIGH | /search concatena input en HTML | Semgrep / ZAP |
| BL-005 | Path traversal / file access | HIGH | /download usa input como ruta | Semgrep / ZAP |
| BL-006 | Debug habilitado | MEDIUM | `debug=True` | Semgrep / SonarQube |
| BL-007 | Dependencia antigua vulnerable | HIGH | requests==2.19.1 | Trivy |
| BL-008 | Dependencia antigua | MEDIUM | PyYAML==5.3.1 | Trivy |
| BL-009 | Información sensible expuesta | MEDIUM | /debug devuelve secreto y rutas | Semgrep / ZAP |
| BL-010 | Contraseñas en texto plano | HIGH | SQLite guarda password sin hash | Semgrep / SonarQube |
| BL-011 | Sin headers de seguridad | LOW/MEDIUM | app Flask sin CSP/HSTS/etc. | ZAP |
| BL-012 | Accesibilidad básica | LOW | inputs sin labels adecuados / estructura mínima | axe-core |

## Criterio de la primera prueba

Para la primera corrida queremos comparar:
- esperados detectados;
- esperados no detectados;
- hallazgos adicionales;
- duplicados entre motores;
- severidad asignada;
- score final.

No buscamos “100% detectado” todavía. Buscamos entender cómo razona BREAKERS frente a un baseline conocido.
