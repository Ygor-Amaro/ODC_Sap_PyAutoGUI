import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
excel_base_sap = os.getenv("excel_base_sap")
login_sap = os.getenv("login_sap")
senha_sap = os.getenv("senha_sap")

def ler_excel_sap():
    # Lê o arquivo Excel diretamente do link fornecido
    df = pd.read_excel(excel_base_sap, engine='openpyxl')
    return df

ler_excel_sap()