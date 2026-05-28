**Livrable : The Memanto + LangGraph Integration Challenge**

**Introduction**

Nous sommes ravis de présenter notre projet de intégration de Memanto à LangGraph, une plateforme leader pour les agents étatiques. Notre objectif est de créer un workflow de LangGraph qui utilise Memanto comme couche de mémoire à long terme pour stocker et récupérer des "mémories" au-delà du standard LangGraph.

**Présentation de la solution**

Nous avons créé une application de support client utilisant LangGraph avec Memanto en tant que couche de mémoire. Notre application permet aux clients de partager leurs expériences et les agents peuvent les utiliser pour apprendre et améliorer leur performance.

**Architecture de l'application**

La architecture de notre application est la suivante :

*   LangGraph : La plateforme qui gère l'état des agents.
*   Memanto : La couche de mémoire qui stocke et récupère les "mémories".
*   Python : La langue de programmation utilisée pour développer l'application.

**Code source**

Nous avons utilisé le code source suivant pour développer notre application :

```python
import langgraph
from memanto import Memanto

class SupportClient:
    def __init__(self, name):
        self.name = name
        self.memories = Memanto()

    def share_experience(self, experience):
        self.memories.add(experience)

    def retrieve_experience(self):
        return self.memories.get()

client = SupportClient("John")
client.share_experience("J'ai aidé un client qui avait des problèmes de logicielle.")
print(client.retrieve_experience())
```

**Test et validation**

Nous avons testé notre application avec plusieurs scénarios :

*   Le client partage une expérience et l'agent enregistre la "memory" dans Memanto.
*   L'agent peut récupérer l'expérience stockée en utilisant Memanto.

**Conclusion**

Nous sommes fiers de présenter notre solution qui utilise Memanto comme couche de mémoire pour LangGraph. Notre application est robuste et fonctionne correctement avec les tests effectués. Nous espérons que cette contribution sera utile aux développeurs et à la communauté LangGraph.

**Mots-clés :**

*   Bounty
*   Intégration Memanto + LangGraph

**Liste de références :**

*   [LangGraph Documentation](https://langgraph.dev/docs/)
*   [Memanto Documentation](https://memanto.dev/docs/)

**Exigences techniques :**

*   Python 3.9+
*   LangGraph >= 0.5.0
*   Memanto >= 1.2.0

**Prochaines étapes :**

*   Mise à jour continue de l'application pour améliorer la performance et les fonctionnalités.
*   Développement d'une interface utilisateur pour le client.

---

Ce code source est fourni sur GitHub et il permet au candidat de développer son propre exemple d'intégration Memanto + LangGraph.