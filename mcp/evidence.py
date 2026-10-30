"""Fictional, project-scoped evidence. No file paths or remote URLs accepted."""
import copy
import unicodedata

PROJECT = 'horizonte-demo'
DISCLAIMER = 'Datos ficticios. Asociación no demuestra causalidad. Requiere revisión humana.'

def source(sid, title, locator, excerpt, period, definition, population, kind='observado', tags=()):
    return dict(source_id=sid, project_id=PROJECT, title=title, locator=locator,
                excerpt=excerpt, period=period, definition=definition,
                population=population, unit='porcentaje de cuentas', claim_type=kind,
                authorized=True, synthetic=True, tags=list(tags), version='1')

SOURCES = {
    'S1': source('S1', 'Cohortes comerciales', 'tabla de cohortes, filas 1–2',
        'Enero–marzo: 20/100 cuentas sin recompra en 90 días. Abril–junio: 30/100. Ventanas completas; composición no ajustada.',
        'dos cohortes: enero–marzo y abril–junio', 'sin recompra en 90 días', 'B2B recurrente', tags=('recompra', 'fuga', 'cohortes')),
    'S2': source('S2', 'Entregas y recompra', 'tabla operativa, filas 1–2',
        'Cohorte abril–junio: con retrasos, 20/40 sin recompra (50%); sin retrasos, 10/60 (16.7%). Revisar secuencia temporal y factores de confusión.',
        'cohorte abril–junio', 'sin recompra en 90 días', 'B2B recurrente', tags=('entregas', 'retrasos', 'recompra', 'fuga')),
    'S3': source('S3', 'Nota comercial', 'párrafo 1',
        '6 de 10 conversaciones seleccionadas mencionan precio. Muestra por conveniencia; no representa la cartera.',
        'no documentado', 'mención de precio en entrevista', '10 conversaciones seleccionadas', 'afirmación', ('precio', 'entrevistas', 'fuga')),
    'S4': source('S4', 'Tablero anual', 'indicador 1',
        '12% de bajas contractuales anuales en todo B2B. No equivale a falta de recompra en 90 días.',
        'año completo', 'baja contractual', 'todo B2B', tags=('fuga', 'bajas', 'anual')),
    'S5': source('S5', 'Seguimiento comercial', 'registro ficticio, filas 1–2',
        'Mismas 100 cuentas de abril–junio: sin seguimiento registrado, 18/40 sin recompra (45%); con seguimiento registrado, 12/60 (20%). Ausencia de registro no prueba ausencia de contacto; grupos pueden diferir.',
        'cohorte abril–junio', 'sin recompra en 90 días', 'B2B recurrente', tags=('seguimiento', 'contacto', 'recompra', 'fuga')),
}
HYPOTHESES = {
    'H1': dict(title='Las entregas contribuyen a la menor recompra', supporting=['S2'], alternatives=['S3','S5'],
               pending=['Confirmar que retrasos preceden a la menor recompra', 'Controlar diferencias de cuenta y producto']),
    'H2': dict(title='El precio explica principalmente la pérdida', supporting=['S3'], alternatives=['S2','S5'],
               pending=['Recoger motivos consistentemente', 'Comparar precios y valor percibido; evitar extrapolar 10 entrevistas']),
    'H3': dict(title='La falta de seguimiento contribuye a la menor recompra', supporting=['S5'], alternatives=['S2','S3'],
               pending=['Verificar calidad del registro y temporalidad', 'Contrastar si se contactó más a cuentas con mayor probabilidad de recompra']),
}

def validate_project(project_id):
    if project_id != PROJECT:
        raise ValueError('Proyecto no autorizado. Solo se admite horizonte-demo.')

def normalize(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text.casefold()) if unicodedata.category(c) != 'Mn')

def get_source(source_id: str, project_id: str = PROJECT) -> dict:
    """Return one authorized synthetic source and its exact locator; IDs only."""
    validate_project(project_id)
    if source_id not in SOURCES:
        raise ValueError('Fuente desconocida; use S1–S5.')
    return dict(source=copy.deepcopy(SOURCES[source_id]), disclaimer=DISCLAIMER)

def search_evidence(query: str, project_id: str = PROJECT) -> dict:
    """Keyword search, not semantic ranking. Empty query lists the five demo sources."""
    validate_project(project_id)
    if len(query) > 500:
        raise ValueError('Consulta demasiado larga; máximo 500 caracteres.')
    terms=normalize(query).split()
    results=[]
    for item in SOURCES.values():
        corpus=normalize(' '.join([item['title'],item['excerpt'],*item['tags']]))
        if all(term in corpus for term in terms):
            results.append(copy.deepcopy(item))
    return dict(results=results, method='coincidencia literal normalizada; todos los términos', disclaimer=DISCLAIMER)

def check_comparability(source_a: str, source_b: str, project_id: str = PROJECT) -> dict:
    """Conservative metadata check. Partial or incompatible sources never authorize pooling."""
    a=get_source(source_a,project_id)['source']; b=get_source(source_b,project_id)['source']
    differences=[dict(field=k,left=a[k],right=b[k]) for k in ('definition','period','population','unit') if a[k]!=b[k]]
    critical=any(d['field'] in ('definition','population','unit') for d in differences)
    status='incompatible' if critical else 'partial' if differences else 'metadata_aligned'
    return dict(status=status, can_pool=False, requires_human_review=True, differences=differences,
                sources=[dict(source_id=x['source_id'],locator=x['locator']) for x in (a,b)],
                reason='No combinar automáticamente. Metadatos alineados tampoco garantizan independencia, comparabilidad causal ni ausencia de duplicación.', disclaimer=DISCLAIMER)

def get_hypothesis(hypothesis_id: str, project_id: str = PROJECT) -> dict:
    """Retrieve a provisional hypothesis; never approve it or select a strategic priority."""
    validate_project(project_id)
    if hypothesis_id not in HYPOTHESES:
        raise ValueError('Hipótesis desconocida; use H1, H2 o H3.')
    h=copy.deepcopy(HYPOTHESES[hypothesis_id])
    return dict(hypothesis_id=hypothesis_id,project_id=project_id,**h,
                sources=[get_source(s,project_id)['source'] for s in dict.fromkeys(h['supporting']+h['alternatives'])],
                status='provisional_not_human_approved', disclaimer=DISCLAIMER)
