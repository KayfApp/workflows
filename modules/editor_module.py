import requests
from credentials import EditorCredentials

class EditorModule:
    def __init__(self, credentials: EditorCredentials):
        self.credentials = credentials

    def list_documents(self):
        """Fetches all top-level documents from the editor API"""
        url = f"{self.credentials.base_url}/api/pages"
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"[EditorModule] Fehler beim Abrufen der Dokumentliste: {e}")
            return []

    def get_document(self, doc_id: str):
        """Fetches a specific document's metadata by ID"""
        url = f"{self.credentials.base_url}/api/pages/{doc_id}"
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"[EditorModule] Fehler beim Abrufen von Dokument {doc_id}: {e}")
            return None

    def delete_document(self, doc_id: str):
        """Deletes a document by ID"""
        url = f"{self.credentials.base_url}/api/pages/{doc_id}"
        try:
            response = requests.delete(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"[EditorModule] Fehler beim Löschen von Dokument {doc_id}: {e}")
            return None

    def rename_document(self, doc_id: str, new_name: str):
        """Updates the document name"""
        url = f"{self.credentials.base_url}/api/pages/{doc_id}"
        try:
            response = requests.patch(
                url,
                json={"name": new_name},
                timeout=5
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"[EditorModule] Fehler beim Umbenennen von Dokument {doc_id}: {e}")
            return None

