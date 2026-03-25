# SOP: Migrazione Fedele da Spring Boot a FastAPI

**Ruolo dell'Agente:** Esperto in migrazione software Java-Python.
**Modulo di Riferimento:** `parking_spot_reservation`.
**Obiettivo:** Convertire il progetto mantenendo una corrispondenza strutturale **1 a 1**.

---

## 1. Requisiti di Sistema e Ambiente
* **Versione Python:** Deve essere utilizzato esclusivamente **Python 3.11**.
* **Root Directory:** Tutto il progetto convertito deve risiedere all'interno di una cartella chiamata `parking_spot_reservation/`.
* **Entry Point:** Il progetto deve essere avviabile tramite il comando `python main.py`. 
    * *Nota per l'Agente:* Inserire nel file `main.py` il blocco `if __name__ == "__main__": uvicorn.run(...)`.
* **Dipendenze:** Deve essere generato un file `requirements.txt` completo.
* **Versione Control:** Deve essere generato un file `.gitignore` specifico per progetti Python (escludendo `__pycache__`, `.venv`, `.env`, ecc.).

---

## 2. Regole di Mapping Strutturale (1:1)

L'agente deve mappare i componenti Java nei corrispettivi Python mantenendo la stessa gerarchia di cartelle originale:

| Componente Java (Spring) | Corrispettivo Python (FastAPI/Pydantic) |
| :--- | :--- |
| **Package** (`com.api.parkingcontrol...`) | **Directory** (con file `__init__.py`) |
| `@RestController` / `@RequestMapping` | Classe con istanza di `APIRouter` |
| `@Service` / `@Component` | Classe Python (es: `class ParkingSpotService`) |
| `@Entity` / `@Table` | Classe `SQLModel` o SQLAlchemy `Base` |
| `@Repository` / `JpaRepository` | Classe Repository con sessione DB (SQLAlchemy) |
| **DTO / Request / Response** | Classi **Pydantic** (`BaseModel`) |
| `@Autowired` / Iniezione da costruttore | Dependency Injection tramite `Depends()` di FastAPI |

---

## 3. Gestione dei File di Configurazione

L'agente deve creare i seguenti file di supporto nella root:
1.  **requirements.txt**: Analizzando le necessità (DB drivers, validation, FastAPI core).
2.  **.gitignore**: Includendo i pattern standard per Python (venv, pycache, log, file di database locali).
3.  **.env**: Per mappare le variabili presenti in `application.properties`.

---

## 4. Direttive di Conversione (Logica e Firme)

1.  **Nomi dei File:** Converti il PascalCase originale in snake_case.
2.  **Firme dei Metodi:** Mantieni gli stessi nomi e parametri per non alterare la logica originale.
3.  **Gestione Dati:** Usa i Type Hints di Python 3.11 e converti le validazioni Bean in vincoli `Field` di Pydantic.
4.  **Sincronicità:** Usa funzioni `def` standard per riflettere il comportamento bloccante di Spring MVC.

---

## 5. Workflow Operativo (Ordine di Esecuzione)

1.  **Setup Struttura:** Crea la cartella root `parking_spot_reservation/` e i file `.gitignore` e `requirements.txt`.
2.  **Models & DTOs:** Converti prima tutto ciò che definisce i dati.
3.  **Repositories & Services:** Traduci la logica di accesso ai dati e di business riga per riga.
4.  **Controllers & Main:** Crea le rotte FastAPI e il file `main.py` per l'avvio manuale.

---

**Istruzione Finale per l'Agente:** "Analizza il modulo `parking_spot_reservation`. Prima di scrivere il codice, presenta la lista delle dipendenze per il `requirements.txt`, il contenuto del `.gitignore` e la struttura delle cartelle."