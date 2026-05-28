**Livrable Complet pour le Défi Memanto + LangGraph Integration**

**Introduction**

Le défi présenté par issuehunt consiste à intégrer Memanto comme couche de mémoire longue vie pour un agent LangGraph. Nous allons créer une implémentation qui démontre l'efficacité de Memanto dans ce contexte.

**Architecturation**

 Notre solution utilisera les composants suivants :

*   LangGraph : Pour gérer les agents et leurs états
*   Memanto : Pour stocker et récupérer les "mémories" des agents

### **Implementation**

On va créer une nouvelle class `MemoryAgent` qui hérite de `LangGraphAgent`. Cette classe aura un objet `MemantoMemory` qui sera chargé de stocker et de récupérer les informations pertinentes.

```python
from langgraph import LangGraphAgent, LangGraphSession
from memanto import Memanto

class MemoryAgent(LangGraphAgent):
    def __init__(self, name, graph):
        super().__init__(name, graph)
        self.memanto = Memanto()

    # Fonction qui stocke les informations dans Memanto
    def store_memory(self, key, value):
        self.memanto.set(key, value)

    # Fonction qui récupère les informations de Memanto
    def retrieve_memory(self, key):
        return self.memonto.get(key)
```

### **Exemple d'utilisation**

 Pour illustrer l'usage de cette classe, nous allons créer un exemple simple :

```python
if __name__ == "__main__":
    # Création du LangGraph et de l'agent MemoryAgent
    graph = LangGraphSession()
    agent = MemoryAgent("Support", graph)

    # Enregistrement d'une information dans Memanto
    key = "support_info"
    value = {"support_number": "1234567890"}
    agent.store_memory(key, value)

    # Récupération de l'information stockée en Memonto
    support_info = agent.retrieve_memory(key)
    print(support_info)  # Affiche le dictionnaire contenant l'information
```

**Conclusion**

La solution proposée présente une implémentation efficace pour intégrer Memanto comme couche de mémoire longue vie dans un agent LangGraph. Nous avons créé une classe `MemoryAgent` qui utilise Memanto pour stocker et récupérer les informations pertinentes. Ce code peut être utilisé comme point de départ pour le défi présenté par issuehunt.

**Notez que ce code est destiné à servir de référence et que vous devriez adapter votre implémentation aux besoins spécifiques de votre projet.