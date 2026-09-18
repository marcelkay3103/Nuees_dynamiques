# Nuées Dynamiques — Implémentation from scratch

Implémentation en Python (from scratch, sans scikit-learn) de l'algorithme
des **Nuées Dynamiques** (Diday, 1971), pour le TP du cours *Science des
données et Big Data* — UNIKIN.

## Contenu
- `nuees_dynamiques.py` : implémentation de l'algorithme (classe `NueesDynamiques`) + démo sur données synthétiques (150 individus, 3 groupes).
- `images/clusters_nuees_dynamiques.png` : partition finale obtenue (3 classes + prototypes).
- `images/convergence_nuees_dynamiques.png` : courbe de convergence du critère de coût.
- `rapport_nuees_dynamiques.pdf` / `.tex` : rapport complet (théorie + implémentation + résultats expérimentaux).

## Utilisation
```bash
pip install numpy matplotlib
python nuees_dynamiques.py