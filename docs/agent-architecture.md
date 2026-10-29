# Arquitectura propuesta
Diseño conceptual; no hay agentes desplegados. Los roles pueden compartir implementación. Empezar con un flujo sencillo antes de separar múltiples agentes.

| Rol | Entrada | Salida permitida |
|---|---|---|
| Asistente | Fuentes autorizadas | Extractos, metadatos y tablas conservando referencias |
| Analista | Evidencia estructurada y criterios comunes | Comparaciones, hipótesis provisionales, alternativas y vacíos |
| Orquestador | Pregunta y estado del proyecto | Asignaciones, dependencias, integración y solicitudes de revisión |
| Guardián | Entradas, salidas y reglas | Bloqueo, escalamiento o advertencia registrada |
| Ejecutor | Artefacto autorizado y versión aprobada | Actualización de fichas en espacio de borradores |

## Orquestación
Primero una secuencia de permisos y comparabilidad. Después, como máximo dos líneas analíticas iniciales: comportamiento comercial y desempeño operativo. Finalmente, integración y revisión humana antes del workshop.

Solo abrir una nueva línea si responde a la pregunta acordada, usa fuentes autorizadas y cabe en el presupuesto de tiempo/costo fijado. Si cambia alcance, requiere nuevas fuentes o supera ese presupuesto, solicitar revisión.

## Contrato mínimo de traspaso
project_id, source_ids, periodo, segmento, definición, tipo de afirmación, limitaciones, versión, estado de revisión y siguiente acción. Un resultado sin fuente identificable no pasa a material del cliente.

## Estados de una hipótesis
Borrador → pendiente de revisión → aprobada para discusión → discutida → reformulada/descartada/pendiente de validación.
Aprobada para discusión no significa verdadera ni prioridad aprobada.

Nueva evidencia relevante, una contradicción material o un cambio de definición invalida la aprobación dependiente y reabre revisión. Registrar quién aprobó, cuándo y qué versión.

## Implementación candidata
SharePoint o OneDrive como repositorio segregado; Lists o Excel para registros; Power Automate para condiciones y aprobaciones; Copilot Studio como interfaz/orquestación. Es una opción futura sujeta a permisos, licencias y pruebas; no una integración existente.

La recuperación de fuentes, las verificaciones deterministas y los permisos deben respaldar las instrucciones al modelo. Un prompt o un agente Guardián por sí solos no garantizan calidad.
