# Strategic Sensemaking Lab — arquitectura, funcionamiento y avances

Actualización: 29 de octubre de 2026. Autor del proyecto: Jorge Alberto Gutierrez Haaz.

## 1. Qué estamos construyendo y para qué

Una metodología y un prototipo de consultoría aumentada por IA para llegar mejor preparados a workshops de planeación estratégica. El caso inicial es la fuga de clientes: contrastar explicaciones sobre entregas, precio y seguimiento comercial antes de decidir qué intervención merece una prueba.

El valor buscado es mejorar la conexión entre evidencia, hipótesis y decisión. No se ha demostrado todavía una mejora de productividad, calidad decisional o retención en clientes reales.

El consultor define la pregunta, revisa interpretaciones, facilita el diálogo y conserva desacuerdos. Los directivos deciden. La IA puede ampliar la exploración y reducir coordinación manual sin asumir esa responsabilidad.

## 2. Estado real de cada componente

| Componente | Implementado y observado | Límite actual |
|---|---|---|
| GitHub | Playbook, plantillas, caso ficticio y código MCP | Portafolio en desarrollo; sin resultados de negocio validados |
| Hugging Face | Space estático con dos hipótesis, comparación, preguntas y ficha descargable | Contenido predefinido; no llama a modelos ni al MCP local |
| VS Code | Carpeta de la demostración abierta para trabajar con Cline | Guardar localmente no publica automáticamente |
| Cline | Modelo conectado; servidor MCP detectado con cuatro herramientas; consulta completada | La síntesis depende del modelo y requiere revisión |
| Servidor MCP | Código Python real, transporte stdio y datos sintéticos S1–S5/H1–H3 | Búsqueda literal, reglas de metadatos; solo un proyecto de demostración |
| Orquestación multiagente | Roles definidos conceptualmente | No hay cinco agentes especializados desplegados |

## 3. Arquitectura explicada de forma sencilla

### Flujo que ya funciona

```text
CONSULTOR: pregunta estratégica y límites
                   |
                   v
VS CODE + CLINE + MODELO DE IA
Interpreta la solicitud y elige herramientas
                   |
          aprobación de la llamada
                   |
                   v
MCP LOCAL (stdio: comunicación entre procesos)
  search_evidence     -> buscar evidencia
  get_source          -> recuperar fuente y localizador
  check_comparability -> contrastar metadatos
  get_hypothesis      -> recuperar hipótesis provisional
                   |
                   v
DATOS FICTICIOS EN evidence.py: S1–S5 y H1–H3
                   |
                   v
Respuesta estructurada -> Cline sintetiza con referencias
                   |
                   v
CONSULTOR REVISA -> WORKSHOP -> DIRECTIVOS DECIDEN
```

MCP es el contrato de comunicación, no el modelo de IA. El servidor es como una mesa de consulta organizada: entrega fuentes y controles definidos. Cline es el cliente que solicita esas consultas; su modelo prepara la síntesis. La aprobación manual sigue activa.

### Componentes complementarios, sin conexión automática

```text
GITHUB: documentación + código + historial de versiones
    |                                  |
    | consulta o actualización manual   | instalación local
    v                                  v
HUGGING FACE                        MCP EN LA COMPUTADORA
demostración estática                consultado por Cline
```

Actualmente no hay un enlace operativo entre el Space y el servidor local. GitHub conserva materiales, pero tampoco sincroniza por sí solo los cambios del disco, el Space y Cline.

## 4. Descripción funcional de las herramientas

| Herramienta | Entrada de ejemplo | Qué devuelve | Qué no hace |
|---|---|---|---|
| search_evidence | query: seguimiento comercial | Fuentes coincidentes con los términos normalizados | No hace búsqueda semántica ni investiga la web |
| get_source | source_id: S5 | Extracto, ID, localizador y límites | No abre archivos arbitrarios |
| check_comparability | source_a: S2; source_b: S5 | Diferencias de definición, periodo, población y unidad | No prueba causalidad ni autoriza combinar datos |
| get_hypothesis | hypothesis_id: H3 | Sustento, alternativas y validaciones pendientes | No aprueba hipótesis ni decide prioridades |

Todas aceptan únicamente el proyecto ficticio horizonte-demo. El control de ID limita este ejemplo; no sustituye autenticación o autorización multiusuario para un producto real.

## 5. Ejemplo ejecutado de principio a fin

Se envió a Cline una solicitud para buscar evidencia de seguimiento comercial, recuperar S5, comparar S2 con S5 y consultar H3, sin comandos ni modificaciones de archivos.

La tarea en Cline produjo resultados para las cuatro herramientas y una síntesis en español con referencias.

- **S5, registro ficticio, filas 1–2:** sin seguimiento registrado, 18 de 40 cuentas no recompraron (45%); con seguimiento registrado, 12 de 60 (20%). Total: 100 cuentas y 30 sin recompra.
- **S2, tabla operativa, filas 1–2:** aparecen diferencias de recompra asociadas a retrasos de entrega, una explicación alternativa.
- **S2 frente a S5:** metadatos alineados, pero can_pool=false y requires_human_review=true. Son las mismas 100 cuentas; no representan 200 observaciones independientes.
- **H3:** la falta de seguimiento podría contribuir a la menor recompra. Permanece provisional y no aprobada por un humano.

La diferencia de 25 puntos porcentuales en S5 no demuestra un efecto del seguimiento. Un contacto puede no haberse registrado; los grupos pueden ser diferentes; el seguimiento pudo ocurrir después del resultado. Las cifras son ficticias.

Preguntas útiles para el workshop:

1. ¿Qué evidencia permitiría distinguir ausencia de contacto de ausencia de registro?
2. ¿Se dio seguimiento preferentemente a cuentas con mayor probabilidad de recompra?
3. ¿Cómo contrastar la explicación de seguimiento frente a entregas y precio antes de elegir una intervención?

## 6. Qué se verificó y qué falta verificar

**Verificado:** ocho pruebas de lógica; descubrimiento de cuatro herramientas y llamadas mediante un cliente SDK real; rechazo de un proyecto distinto; conexión visible en Cline; consulta completa en Cline con síntesis y localizadores. La demostración web también se probó en contraste, bloqueo, registro, descarga y revalidación.

**No verificado todavía:** desempeño en datos reales, mejoras frente a un diagnóstico manual, confiabilidad sostenida con consultas variadas, costos completos de revisión y utilidad para participantes de un workshop real.

No confundir una llamada exitosa al protocolo con una respuesta analítica correcta en cualquier situación. La revisión humana sigue siendo necesaria.

## 7. Gobierno y límites de delegación

- El servidor solo devuelve datos sintéticos incluidos en el código; no contiene claves ni fuentes de clientes.
- No publica, escribe documentos ni modifica sistemas de negocio.
- autoApprove está vacío; no se activó aprobación automática.
- Las fuentes se tratan como datos, no como instrucciones operativas.
- El resultado de comparabilidad nunca autoriza combinar automáticamente.
- La hipótesis no hereda certeza por venir de una herramienta.
- Los roles Asistente, Analista, Orquestador, Guardián y Ejecutor son un diseño futuro; el control actual se implementa con funciones y revisión humana.

## 8. Aprendizajes del desarrollo

Se pasó de una metodología documentada a una demostración visual y después a una integración real entre Cline y un servidor MCP propio. El activo diferenciador está en convertir criterios consultivos en estructuras verificables: fuentes, preguntas, reglas y límites.

En la configuración se identificó una migración: el Cline activo usa .cline/data/settings/cline_mcp_settings.json, mientras la instalación anterior conservaba otra ubicación. Se configuró la ruta activa, se retiró únicamente la entrada recién añadida al archivo antiguo y se conservaron respaldos. No publicar archivos de configuración con rutas personales.

## 9. Próximos pasos, en orden

1. Incorporar H3/S5 en la interfaz de Hugging Face y probar su integración con la ficha y revalidación. Aún no se confirma ese cambio en la interfaz actual.
2. Agregar casos de evaluación: fuente inexistente, términos sin coincidencias, periodos incompatibles y preguntas que intenten convertir asociación en causalidad.
3. Revisar calidad semántica de metadatos y evidencias, además de que el protocolo responda.
4. Medir esfuerzo total y utilidad de una síntesis asistida frente a una preparación manual comparable.
5. Considerar una aplicación conectada a MCP remoto con autenticación, permisos y límites de uso. El Space estático no se convierte en servidor Python por subir estos archivos.
6. Solo después, preparar un piloto autorizado con un cliente y fuentes segregadas.

## 10. Enlaces y uso práctico

- [Proyecto en GitHub](https://github.com/Jguthaaz/ai-augmented-strategic-sensemaking)
- [Módulo MCP](https://github.com/Jguthaaz/ai-augmented-strategic-sensemaking/tree/main/mcp)
- [Demostración en Hugging Face](https://huggingface.co/spaces/jguthaaz/strategic-sensemaking-lab)
- [Código del servidor](https://github.com/Jguthaaz/ai-augmented-strategic-sensemaking/blob/main/mcp/server.py)
- [Pruebas](https://github.com/Jguthaaz/ai-augmented-strategic-sensemaking/blob/main/mcp/test_evidence.py)

Primera consulta reusable: “Usa las cuatro herramientas de strategic-sensemaking para explorar H3. Cita fuentes y localizadores, explica límites y propone preguntas de contraste. No ejecutes comandos ni modifiques archivos.”

**Estado de cierre:** integración local Cline–MCP funcional con evidencia ficticia; metodología y demostración pública disponibles; impacto consultivo pendiente de evaluación.