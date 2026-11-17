# Economía unitaria y efectivo inicial

`amazon-unit-economics-cashflow` · Español

## Objetivo y alcance

Calcular contribución, ACOS de equilibrio, sensibilidad a devoluciones y efectivo de primer pedido desde supuestos explícitos.

## Fundamento y dependencias

Precios/costes numéricos y tarifas de mercado documentadas. Python 3.10+ para calculadora sin paquetes externos. El efectivo requiere cantidad y calendario de pagos.

## Entradas

JSON: precio, comisión, logística, coste puesto en destino, devolución/pérdida, ACOS y otros variables. Efectivo: unidades, moldes, inicio, anticipo y reserva. Una moneda y tasas entre0 y1.

## Salidas

JSON/archivo elegido con contribución/margen, ACOS de equilibrio, pérdida esperada, efectivo inicial y escenarios. Entradas inválidas devuelven error; sin cambios de red/cuenta.

## Procedimiento

1. Validar supuestos, fuentes de tarifas, fecha y unidades
2. ejecutar calculadora o declarar cálculo manual
3. conciliar base
4. variar publicidad/devoluciones/costes
5. separar beneficio unitario y efectivo de inventario, declarar exclusiones.

## Límites y condiciones de parada

No inventar tarifas, demanda, impuestos, flete ni condiciones. Sin calendario, limitar a economía unitaria. No es asesoramiento contable, fiscal ni de inversión.

## Ejemplo de solicitud

Usa `$amazon-unit-economics-cashflow` — Con precios/costes proporcionados, comparar devoluciones/ACOS del soporte y mostrar por separado contribución y efectivo inicial; responde en español y conserva pruebas, datos desconocidos y límites de autorización.

## Especificación completa

[Entrada del Skill y referencias detalladas](../../SKILL.md).

Usa el idioma solicitado expresamente; si no se indica, sigue el de la petición. Conserva comandos, identificadores, claves JSON, valores enumerados, unidades y citas originales. Separa traducciones y originales. No deduzcas país, moneda ni jurisdicción por el idioma. Lee las referencias detalladas pertinentes y conserva todos los controles y permisos existentes.

Antes de entregar, concilia entradas, pruebas, valores ausentes, archivos y criterios de finalización originales. Marca como no verificados los pasos no ejecutados; el éxito de un script no valida conclusiones comerciales.

## Cobertura lingüística y validación

Esta guía localizada cubre objetivo, requisitos, entradas, salidas, pasos, ejemplos y límites; no traduce línea por línea todas las referencias. La documentación técnica detallada, los casos históricos, errores de scripts, interfaces de ejemplo e imágenes mantienen su idioma original y pueden explicarse a petición. Se comprueban estructura, enlaces y restricciones esenciales; no se afirma una revisión por hablantes nativos de cada idioma.

