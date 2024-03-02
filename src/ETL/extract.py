import requests
import pandas as pd

def buscar_times_api(league, season, country):
    """
    Faz uma requisição à API de futebol para buscar times com base na liga, temporada e país.
    
    Parâmetros:
    league: O identificador da liga (como uma string ou número).
    season: A temporada (ano) a ser consultada.
    country: O país dos times a serem buscados.

    Retorna:
    Um DataFrame do pandas com os dados dos times
    """
    
    url = "https://api-football-v1.p.rapidapi.com/v3/teams"
    querystring = {"league": str(league), "season": str(season), "country": country}
    headers = {
        "X-RapidAPI-Key": "d7206f3c24msh8dba848e31492f7p13ea6ajsna5aed52364b7",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    
    if response.status_code == 200:
        data = response.json()
        # Supondo que os dados desejados estejam na chave 'response' do JSON
        df = pd.json_normalize(data['response'])
        return df
    else:
        print(f"Erro na requisição: {response.status_code}")
        return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro