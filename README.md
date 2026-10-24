# ranked-recall-stability

## Français

Distinguer changements de rappel et permutations de résultats ex æquo.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m ranked_recall_stability examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Compare des préfixes de rang capturés, leurs révisions de banque et empreintes de contexte. Les inversions de préférence excluent les ex æquo explicitement fournis ; une absence hors top-k ne devient pas une erreur de mémoire.

### Limites

Diagnostic descriptif de captures, sans exécuter Hindsight ni évaluer la vérité des souvenirs. Empreintes et scores déclarés, sans preuve de provenance ; pas de garantie de stabilité du moteur.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Distinguish recall changes from permutations of tied results.

Synthetic data; no network access or secret required.

```sh
python -m ranked_recall_stability examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Compares captured rank prefixes, bank revisions and context digests. Preference inversions exclude explicitly supplied score ties; absence outside top-k is not treated as a memory error.

### Limits

Descriptive capture diagnostic, without running Hindsight or assessing memory truth. Digests and scores are declared, not authenticated; no engine-stability guarantee.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Distinguir cambios de recuperación y permutaciones de resultados empatados.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m ranked_recall_stability examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Compara prefijos de clasificación capturados, revisiones y resúmenes de contexto. Las inversiones excluyen empates declarados; una ausencia fuera de top-k no se trata como error de memoria.

### Límites

Diagnóstico descriptivo de capturas, sin ejecutar Hindsight ni evaluar verdad de recuerdos. Resúmenes y puntuaciones declarados, no autenticados; sin garantía de estabilidad del motor.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://github.com/vectorize-io/hindsight/issues/6056
