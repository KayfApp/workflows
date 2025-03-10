from dataclasses import dataclass

@dataclass
class EmailCredentials:
    smtp_server: str
    smtp_port: int
    username: str
    password: str
