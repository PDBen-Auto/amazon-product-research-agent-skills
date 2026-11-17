# Suite de investigación de productos Amazon

`amazon-product-research-suite` · Español

## Objetivo y alcance

Dirigir decisiones que abarcan dos o más dominios al mínimo conjunto de Skills especialistas; una tarea concreta va directamente al especialista.

## Fundamento y dependencias

Entorno Agent Skills y especialistas seleccionados instalados. Los datos aportados permiten trabajo sin conexión; recopilar en vivo exige red y permiso. Python 3.10+ para herramientas opcionales.

## Entradas

Decisión de producto obligatoria; según tarea ASIN/identidad, mercado, jurisdicción, periodo y permisos. Opcionales CSV/JSON/XLSX/PDF/imágenes, presupuestos y restricciones. Lo desconocido sigue siendo una carencia.

## Salidas

route-plan.json, contrato común de pruebas, Skills/orden, entradas ausentes y destinos. El enrutamiento no instala ni contacta servicios.

## Procedimiento

1. Definir decisión/alcance
2. elegir y comprobar Skills
3. crear ruta/contrato
4. ejecutar solo etapas autorizadas
5. distinguir observado/calculado/modelado/inferido/supuesto
6. validar schemas y archivos
7. conservar resultados parciales ante bloqueos.

## Límites y condiciones de parada

No inventar denominadores, tarifas, promesas de proveedores, conclusiones jurídicas ni puntuaciones privadas. CAPTCHA, acceso ausente, envío sensible o supuestos financieros insuficientes detienen la etapa afectada.

## Ejemplo de solicitud

Usa `$amazon-product-research-suite` — Evaluar un soporte para coche mediante mercado, reseñas, diferenciación, proveedor y economía, añadiendo revisión de diseños si hay imágenes; responde en español y conserva pruebas, datos desconocidos y límites de autorización.

## Especificación completa

[Entrada del Skill y referencias detalladas](../../SKILL.md).

Usa el idioma solicitado expresamente; si no se indica, sigue el de la petición. Conserva comandos, identificadores, claves JSON, valores enumerados, unidades y citas originales. Separa traducciones y originales. No deduzcas país, moneda ni jurisdicción por el idioma. Lee las referencias detalladas pertinentes y conserva todos los controles y permisos existentes.

Antes de entregar, concilia entradas, pruebas, valores ausentes, archivos y criterios de finalización originales. Marca como no verificados los pasos no ejecutados; el éxito de un script no valida conclusiones comerciales.

## Cobertura lingüística y validación

Esta guía localizada cubre objetivo, requisitos, entradas, salidas, pasos, ejemplos y límites; no traduce línea por línea todas las referencias. La documentación técnica detallada, los casos históricos, errores de scripts, interfaces de ejemplo e imágenes mantienen su idioma original y pueden explicarse a petición. Se comprueban estructura, enlaces y restricciones esenciales; no se afirma una revisión por hablantes nativos de cada idioma.

