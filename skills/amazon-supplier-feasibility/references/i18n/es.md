# Viabilidad de proveedores y muestras

`amazon-supplier-feasibility` · Español

## Objetivo y alcance

Preparar RFQ, presupuestos comparables y aceptación de muestras con pruebas; por defecto no contactar fábricas ni comprar.

## Fundamento y dependencias

Especificación obligatoria; comparación con presupuestos fechados equivalentes. Cumplimiento, acceso a muestras y comunicación son condicionales. Contactar requiere autorización aparte.

## Entradas

Especificación/plano con unidades/tolerancias y supuestos de cantidad/demanda; moneda, Incoterm, herramientas y pagos según necesidad; presupuestos PDF/XLSX/CSV y calidad opcionales.

## Salidas

RFQ, comparación coste/plazo, registro de riesgos y plan de muestras. Estados READY_FOR_RFQ, READY_FOR_SAMPLE, CONDITIONAL o INSUFFICIENT_EVIDENCE.

## Procedimiento

1. Revisar carencias y requisitos innegociables
2. preparar campos RFQ
3. alinear cantidad, moneda, Incoterm, inclusiones y fecha
4. revisar herramientas/capacidad/calidad/cumplimiento/logística
5. fijar pruebas antes de recibir
6. comparar viabilidad total y transferir costes al modelo económico.

## Límites y condiciones de parada

No clasificar presupuestos incomparables ni aceptar certificación sin documentos. Un fallo crítico no se compensa con precio. No enviar, negociar ni pedir sin permiso.

## Ejemplo de solicitud

Usa `$amazon-supplier-feasibility` — Alinear imán, adhesivo, par, ensayo térmico, propiedad de moldes y embalaje antes de comparar soportes; responde en español y conserva pruebas, datos desconocidos y límites de autorización.

## Especificación completa

[Entrada del Skill y referencias detalladas](../../SKILL.md).

Usa el idioma solicitado expresamente; si no se indica, sigue el de la petición. Conserva comandos, identificadores, claves JSON, valores enumerados, unidades y citas originales. Separa traducciones y originales. No deduzcas país, moneda ni jurisdicción por el idioma. Lee las referencias detalladas pertinentes y conserva todos los controles y permisos existentes.

Antes de entregar, concilia entradas, pruebas, valores ausentes, archivos y criterios de finalización originales. Marca como no verificados los pasos no ejecutados; el éxito de un script no valida conclusiones comerciales.

## Cobertura lingüística y validación

Esta guía localizada cubre objetivo, requisitos, entradas, salidas, pasos, ejemplos y límites; no traduce línea por línea todas las referencias. La documentación técnica detallada, los casos históricos, errores de scripts, interfaces de ejemplo e imágenes mantienen su idioma original y pueden explicarse a petición. Se comprueban estructura, enlaces y restricciones esenciales; no se afirma una revisión por hablantes nativos de cada idioma.

