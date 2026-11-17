# Suite de investigación de productos Amazon

[简体中文](README.zh-CN.md) | [English](README.en.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Português](README.pt.md)

Usa el idioma solicitado expresamente; si no se indica, sigue el de la petición. Conserva comandos, identificadores, claves JSON, valores enumerados, unidades y citas originales. Separa traducciones y originales. No deduzcas país, moneda ni jurisdicción por el idioma. Lee las referencias detalladas pertinentes y conserva todos los controles y permisos existentes.

## Instalación y uso

Descarga o clona el repositorio y copia el directorio del Skill indicado, con sus references, scripts, assets y demás dependencias existentes, al directorio de Skills del entorno. Conserva el nombre y SKILL.md. Cambiar el idioma de la documentación no requiere otra instalación. Los comandos son opciones, no pruebas de instalación ni activación.

```sh
git clone https://github.com/PDBen-Auto/amazon-product-research-agent-skills.git
```

## Diferenciación de producto basada en pruebas

`amazon-product-differentiation-rd`

Convertir problemas de clientes en mecanismos, especificaciones medibles, experimentos económicos y criterios de descarte previos.

Directorio del Skill: `skills/amazon-product-differentiation-rd`

**Fundamento y dependencias**

Pruebas trazables, producto de referencia y tarea principal del usuario. Restricciones comerciales para viabilidad; prototipos y revisión de patentes/proveedores según necesidad. Datos aportados sin servicio en vivo.

**Entradas**

Obligatorios: reseñas/entrevistas/devoluciones, imágenes o especificaciones y tarea del usuario. Condicionales precio, coste, dimensiones, materiales, compatibilidad, MOQ y regulación. Umbrales propuestos se marcan como supuestos.

**Salidas**

Mapa prueba-mecanismo, cartera de conceptos, requisitos medibles, experimentos y riesgos abiertos en Markdown/JSON/tablas. Cada recomendación exige prueba, mecanismo, requisito y ensayo.

[Procedimiento · Límites y condiciones de parada · Ejemplo de solicitud](skills/amazon-product-differentiation-rd/references/i18n/es.md)

> Usa `$amazon-product-differentiation-rd` — Para soportes que resbalan, definir retención, liberación, masa del teléfono y pruebas de vibración/temperatura en lugar de solo más magnetismo; responde en español y conserva pruebas, datos desconocidos y límites de autorización.

## Suite de investigación de productos Amazon

`amazon-product-research-suite`

Dirigir decisiones que abarcan dos o más dominios al mínimo conjunto de Skills especialistas; una tarea concreta va directamente al especialista.

Directorio del Skill: `skills/amazon-product-research-suite`

**Fundamento y dependencias**

Entorno Agent Skills y especialistas seleccionados instalados. Los datos aportados permiten trabajo sin conexión; recopilar en vivo exige red y permiso. Python 3.10+ para herramientas opcionales.

**Entradas**

Decisión de producto obligatoria; según tarea ASIN/identidad, mercado, jurisdicción, periodo y permisos. Opcionales CSV/JSON/XLSX/PDF/imágenes, presupuestos y restricciones. Lo desconocido sigue siendo una carencia.

**Salidas**

route-plan.json, contrato común de pruebas, Skills/orden, entradas ausentes y destinos. El enrutamiento no instala ni contacta servicios.

[Procedimiento · Límites y condiciones de parada · Ejemplo de solicitud](skills/amazon-product-research-suite/references/i18n/es.md)

> Usa `$amazon-product-research-suite` — Evaluar un soporte para coche mediante mercado, reseñas, diferenciación, proveedor y economía, añadiendo revisión de diseños si hay imágenes; responde en español y conserva pruebas, datos desconocidos y límites de autorización.

## Viabilidad de proveedores y muestras

`amazon-supplier-feasibility`

Preparar RFQ, presupuestos comparables y aceptación de muestras con pruebas; por defecto no contactar fábricas ni comprar.

Directorio del Skill: `skills/amazon-supplier-feasibility`

**Fundamento y dependencias**

Especificación obligatoria; comparación con presupuestos fechados equivalentes. Cumplimiento, acceso a muestras y comunicación son condicionales. Contactar requiere autorización aparte.

**Entradas**

Especificación/plano con unidades/tolerancias y supuestos de cantidad/demanda; moneda, Incoterm, herramientas y pagos según necesidad; presupuestos PDF/XLSX/CSV y calidad opcionales.

**Salidas**

RFQ, comparación coste/plazo, registro de riesgos y plan de muestras. Estados READY_FOR_RFQ, READY_FOR_SAMPLE, CONDITIONAL o INSUFFICIENT_EVIDENCE.

[Procedimiento · Límites y condiciones de parada · Ejemplo de solicitud](skills/amazon-supplier-feasibility/references/i18n/es.md)

> Usa `$amazon-supplier-feasibility` — Alinear imán, adhesivo, par, ensayo térmico, propiedad de moldes y embalaje antes de comparar soportes; responde en español y conserva pruebas, datos desconocidos y límites de autorización.

## Economía unitaria y efectivo inicial

`amazon-unit-economics-cashflow`

Calcular contribución, ACOS de equilibrio, sensibilidad a devoluciones y efectivo de primer pedido desde supuestos explícitos.

Directorio del Skill: `skills/amazon-unit-economics-cashflow`

**Fundamento y dependencias**

Precios/costes numéricos y tarifas de mercado documentadas. Python 3.10+ para calculadora sin paquetes externos. El efectivo requiere cantidad y calendario de pagos.

**Entradas**

JSON: precio, comisión, logística, coste puesto en destino, devolución/pérdida, ACOS y otros variables. Efectivo: unidades, moldes, inicio, anticipo y reserva. Una moneda y tasas entre0 y1.

**Salidas**

JSON/archivo elegido con contribución/margen, ACOS de equilibrio, pérdida esperada, efectivo inicial y escenarios. Entradas inválidas devuelven error; sin cambios de red/cuenta.

[Procedimiento · Límites y condiciones de parada · Ejemplo de solicitud](skills/amazon-unit-economics-cashflow/references/i18n/es.md)

> Usa `$amazon-unit-economics-cashflow` — Con precios/costes proporcionados, comparar devoluciones/ACOS del soporte y mostrar por separado contribución y efectivo inicial; responde en español y conserva pruebas, datos desconocidos y límites de autorización.

## Cobertura lingüística y validación

Esta guía localizada cubre objetivo, requisitos, entradas, salidas, pasos, ejemplos y límites; no traduce línea por línea todas las referencias. La documentación técnica detallada, los casos históricos, errores de scripts, interfaces de ejemplo e imágenes mantienen su idioma original y pueden explicarse a petición. Se comprueban estructura, enlaces y restricciones esenciales; no se afirma una revisión por hablantes nativos de cada idioma.

Antes de entregar, concilia entradas, pruebas, valores ausentes, archivos y criterios de finalización originales. Marca como no verificados los pasos no ejecutados; el éxito de un script no valida conclusiones comerciales.
