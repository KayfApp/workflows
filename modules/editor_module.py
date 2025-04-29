from fastapi import FastAPI, HTTPException, Depends, Header
from typing import List, Dict
from editor_credentials import EditorCredentials

app = FastAPI()

# API-Zugangsdaten
CREDENTIALS = EditorCredentials(api_token="your-secure-api-token")

# Simulierte Datenbank mit Dokumenten
documents = {
    1: {
        "id": 1,
        "title": "Strategiepapier Q1",
        "content": "Detaillierte Analyse und Maßnahmen für das kommende Quartal...",
        "created_at": "2025-03-11T10:00:00Z",
        "updated_at": "2025-03-11T12:30:00Z",
        "comments": [
            {
                "id": "c1",
                "author": "Projektleiter",
                "message": "Bitte diesen Abschnitt präzisieren.",
                "created_at": "2025-03-11T12:35:00Z"
            }
        ]
    },
    2: {
        "id": 2,
        "title": "Technische Spezifikation",
        "content": "Diese Spezifikation definiert die Architektur der neuen Plattform...",
        "created_at": "2025-03-10T08:20:00Z",
        "updated_at": "2025-03-11T14:00:00Z",
        "comments": []
    }
}

# Authentifizierungsfunktion
def authenticate(api_token: str = Header(...)):
    if api_token != CREDENTIALS.api_token:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return True

@app.get("/list-docs", dependencies=[Depends(authenticate)])
def list_docs():
    """Gibt eine Liste aller gespeicherten Dokumente mit Metadaten zurück."""
    return [
        {
            "id": doc["id"],
            "name": doc["title"],
            "description": doc["content"][:30] + "...",  # Gekürzte Vorschau des Inhalts
            "last_updated": doc["updated_at"]
        }
        for doc in documents.values()
    ]

@app.get("/doc-info/{doc_id}", dependencies=[Depends(authenticate)])
def get_doc_info(doc_id: int):
    """Gibt die Metadaten eines bestimmten Dokuments zurück, ohne den vollständigen Inhalt."""
    if doc_id not in documents:
        raise HTTPException(status_code=404, detail="Dokument nicht gefunden")
    doc = documents[doc_id]
    return {
        "id": doc["id"],
        "name": doc["title"],
        "description": doc["content"][:30] + "...",
        "last_updated": doc["updated_at"]
    }

@app.get("/doc-content/{doc_id}", dependencies=[Depends(authenticate)])
def get_doc_content(doc_id: int):
    """Gibt den vollständigen Inhalt eines Dokuments zurück."""
    if doc_id not in documents:
        raise HTTPException(status_code=404, detail="Dokument nicht gefunden")
    return {"content": documents[doc_id]["content"]}
