# Strategic Sensemaking MCP — Evidence to Decisions

Servidor MCP local y de solo lectura para apoyar el diagnóstico previo a un workshop. **Datos totalmente ficticios.** El servidor consulta evidencia estructurada; no ejecuta un modelo de IA, no valida causas ni toma decisiones. Cline actúa como cliente y aporta el modelo seleccionado por el usuario.

## Qué incluye
- Cinco fuentes sintéticas con localizadores S1–S5.
- Tres hipótesis provisionales sobre entregas, precio y seguimiento comercial.
- Cuatro herramientas: `search_evidence`, `get_source`, `check_comparability`, `get_hypothesis`.
- Aislamiento por ID de proyecto; rechazo de fuentes desconocidas y rutas arbitrarias.
- Pruebas de lógica y un cliente que comprueba el protocolo real por stdio.

## Instalar
Python 3.10 o superior. Desde esta carpeta:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m unittest -v
.\.venv\Scripts\python.exe smoke_mcp.py
```

Se usa el SDK oficial MCP 1.30.0, en su línea v1 de mantenimiento, fijado para reproducibilidad. Las dependencias transitivas están en requirements-lock.txt cuando se genera la instalación verificada. No se necesitan claves para el servidor. El modelo de Cline tiene sus propias condiciones de uso.

## Conectar a Cline
En MCP Servers → Configure MCP Servers, fusionar este bloque con la configuración existente; no reemplazar otros servidores. Sustituir ambas rutas por rutas absolutas reales:

```json
{"mcpServers":{"strategic-sensemaking":{"command":"C:/ruta/strategic-sensemaking-mcp/.venv/Scripts/python.exe","args":["C:/ruta/strategic-sensemaking-mcp/server.py"],"disabled":false,"autoApprove":[]}}}
```

`cline.local.json` contiene las rutas de esta computadora y no debe publicarse. La configuración del usuario no se modifica automáticamente.

## Primera consulta
“Usa strategic-sensemaking para buscar evidencia de seguimiento. Recupera S5 y compara S2 con S5; después consulta H3. Cita ID y localizador, distingue asociación de causalidad y propone tres preguntas para el workshop. No ejecutes comandos ni modifiques archivos.”

## Límites
La búsqueda es literal normalizada, no semántica. Las reglas comparan metadatos y escalan discrepancias; no hacen homologación inteligente. Incluso metadatos alineados requieren revisión antes de combinar datos. Los controles de ID son límites del ejemplo, no autenticación multiusuario. No añadir datos reales sin rediseñar autorización, almacenamiento, privacidad y evaluación.

El Space público sigue siendo una simulación independiente: no se conecta al servidor local. H3/S5 están disponibles aquí; incorporarlas a la interfaz es un cambio separado.

## Referencias
- Método: https://github.com/Jguthaaz/ai-augmented-strategic-sensemaking
- SDK oficial v1: https://py.sdk.modelcontextprotocol.io/v1/
- Configuración de Cline: https://docs.cline.bot/mcp/mcp-overview

No se ha elegido una licencia de redistribución para estos materiales.
