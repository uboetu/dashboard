import pandas as pd

file_path_template = 'Dados_PRF_{}.csv'
dfs = []

for year in range(2017, 2024):
    file_path = file_path_template.format(year)
    try:
        df_year = pd.read_csv(file_path, encoding='ISO-8859-1', delimiter=';')
        df_year = df_year.drop_duplicates()
        dfs.append(df_year)
    except FileNotFoundError:
        print(f"File for year {year} not found. Skipping...")



translation_dict = {
    'id': 'ID',
    'data_inversa': 'date',
    'dia_semana': 'weekday',
    'horario': 'time',
    'uf': 'state',
    'br': 'highway',
    'km': 'kilometer',
    'municipio': 'city',
    'causa_acidente': 'accident_cause',
    'tipo_acidente': 'accident_type',
    'classificacao_acidente': 'accident_classification',
    'fase_dia': 'time_of_day',
    'sentido_via': 'direction',
    'condicao_metereologica': 'weather_condition',
    'tipo_pista': 'type_of_road',
    'tracado_via': 'road_layout',
    'uso_solo': 'urban_rural',
    'ano': 'year',
    'pessoas': 'people',
    'mortos': 'deceased',
    'feridos_leves': 'lightly_injured',
    'feridos_graves': 'severely_injured',
    'ilesos': 'unharmed',
    'ignorados': 'unknown',
    'feridos': 'injured',
    'veiculos': 'vehicles',
    'latitude': 'latitude',
    'longitude': 'longitude',
    'regional': 'regional',
    'delegacia': 'police_station',
    'uop': 'operational_unit'
}


def translate_dataframe(df, translation_dict):
    """Load the CSV file from the given path, translate its columns, and return the translated dataframe."""
    df_translated = df.rename(columns=translation_dict)
    return df_translated


data22 = translate_dataframe(data22, translation_dict)

translations = {
    "weekday": {
        'sábado': 'Saturday',
        'domingo': 'Sunday',
        'segunda-feira': 'Monday',
        'terça-feira': 'Tuesday',
        'quarta-feira': 'Wednesday',
        'quinta-feira': 'Thursday',
        'sexta-feira': 'Friday'
    },
    "accident_cause": {
        'Ingestão de álcool pelo condutor': 'Driver alcohol consumption',
        'Condutor deixou de manter distância do veículo da frente': 'Driver failed to maintain distance from the vehicle in front',
        'Reação tardia ou ineficiente do condutor': 'Late or inefficient driver reaction',
        'Acumulo de água sobre o pavimento': 'Water accumulation on the pavement',
        'Mal súbito do condutor': 'Driver sudden illness',
        'Chuva': 'Rain',
        'Ausência de reação do condutor': 'Lack of driver reaction',
        'Manobra de mudança de faixa': 'Lane change maneuver',
        'Pista Escorregadia': 'Slippery road',
        'Ausência de sinalização': 'Lack of signaling',
        'Condutor Dormindo': 'Driver sleeping',
        'Velocidade Incompatível': 'Incompatible speed',
        'Acessar a via sem observar a presença dos outros veículos': 'Entering the roadway without noticing other vehicles',
        'Conversão proibida': 'Forbidden conversion',
        'Transitar na contramão': 'Driving on the wrong side',
        'Ultrapassagem Indevida': 'Improper overtaking',
        'Desrespeitar a preferência no cruzamento': 'Disregarding intersection priority',
        'Acostamento em desnível': 'Uneven shoulder',
        'Demais falhas mecânicas ou elétricas': 'Other mechanical or electrical failures',
        'Carga excessiva e/ou mal acondicionada': 'Excessive and/or poorly stowed load',
        'Problema com o freio': 'Brake issue',
        'Ingestão de álcool e/ou substâncias psicoativas pelo pedestre': 'Pedestrian consumption of alcohol and/or psychoactive substances',
        'Curva acentuada': 'Sharp curve',
        'Estacionar ou parar em local proibido': 'Parking or stopping in a prohibited place',
        'Avarias e/ou desgaste excessivo no pneu': 'Damages and/or excessive tire wear',
        'Pedestre cruzava a pista fora da faixa': 'Pedestrian crossing the road outside the crosswalk',
        'Obstrução na via': 'Road obstruction',
        'Acesso irregular': 'Irregular access',
        'Pista esburacada': 'Potholed road',
        'Animais na Pista': 'Animals on the road',
        'Falta de acostamento': 'Lack of shoulder',
        'Entrada inopinada do pedestre': 'Unexpected pedestrian entry',
        'Acumulo de areia ou detritos sobre o pavimento': 'Accumulation of sand or debris on the pavement',
        'Pedestre andava na pista': 'Pedestrian walking on the road',
        'Desvio temporário': 'Temporary detour',
        'Transitar no acostamento': 'Driving on the shoulder',
        'Problema na suspensão': 'Suspension problem',
        'Objeto estático sobre o leito carroçável': 'Static object on the carriageway',
        'Deficiência do Sistema de Iluminação/Sinalização': 'Deficiency in the Lighting/Signaling System',
        'Trafegar com motocicleta (ou similar) entre as faixas': 'Riding a motorcycle (or similar) between lanes',
        'Condutor usando celular': 'Driver using cellphone',
        'Restrição de visibilidade em curvas horizontais': 'Restricted visibility on horizontal curves',
        'Ingestão de álcool ou de substâncias psicoativas pelo pedestre': 'Pedestrian consumption of alcohol or psychoactive substances',
        'Declive acentuado': 'Steep decline',
        'Frear bruscamente': 'Braking sharply',
        'Iluminação deficiente': 'Poor lighting',
        'Área urbana sem a presença de local apropriado para a travessia de pedestres': 'Urban area without an appropriate pedestrian crossing location',
        'Demais Fenômenos da natureza': 'Other natural phenomena',
        'Demais falhas na via': 'Other roadway failures',
        'Faixas de trânsito com largura insuficiente': 'Traffic lanes with insufficient width',
        'Obras na pista': 'Roadworks',
        'Retorno proibido': 'Forbidden U-turn',
        'Afundamento ou ondulação no pavimento': 'Pavement sinking or undulation',
        'Falta de elemento de contenção que evite a saída do leito carroçável': 'Lack of containment element preventing the exit from the carriageway',
        'Ingestão de substâncias psicoativas pelo condutor': 'Driver consumption of psychoactive substances',
        'Neblina': 'Fog',
        'Condutor desrespeitou a iluminação vermelha do semáforo': 'Driver disrespected the red traffic light',
        'Sistema de drenagem ineficiente': 'Inefficient drainage system',
        'Acumulo de óleo sobre o pavimento': 'Oil accumulation on the pavement',
        'Sinalização mal posicionada': 'Poorly positioned signage',
        'Pista em desnível': 'Uneven road',
        'Transitar na calçada': 'Driving on the sidewalk',
        'Fumaça': 'Smoke',
        'Redutor de velocidade em desacordo': 'Non-compliant speed reducer',
        'Deixar de acionar o farol da motocicleta (ou similar)': 'Failure to turn on motorcycle (or similar) headlights',
        'Restrição de visibilidade em curvas verticais': 'Restricted visibility on vertical curves',
        'Semáforo com defeito': 'Malfunctioning traffic light',
        'Faróis desregulados': 'Misaligned headlights',
        'Modificação proibida': 'Forbidden modification',
        'Participar de racha': 'Engaging in street racing',
        'Sinalização encoberta': 'Covered signage'
    },
    "accident_type": {
        'Colisão traseira': 'Rear-end collision',
        'Tombamento': 'Tipping over',
        'Colisão frontal': 'Head-on collision',
        'Saída de leito carroçável': 'Exit from carriageway',
        'Colisão com objeto': 'Collision with object',
        'Colisão lateral mesmo sentido': 'Side collision, same direction',
        'Engavetamento': 'Pile-up',
        'Atropelamento de pessoa': 'Pedestrian run-over',
        'Colisão com objeto em movimento': 'Collision with moving object',
        'Colisão lateral sentido oposto': 'Side collision, opposite direction',
        'Incêndio': 'Fire',
        'Queda de motocicleta / bicicleta / veículo': 'Fall from motorcycle/bicycle/vehicle',
        'Derramamento de carga': 'Cargo spill',
        'Atropelamento de Animal': 'Animal run-over',
        'Colisão transversal': 'Transverse collision',
        'Capotamento': 'Rollover',
        'Queda de ocupante de veículo': 'Fall of vehicle occupant',
        'Atropelamento de Pedestre': 'Pedestrian Hit',
        'Eventos atípicos': 'Atypical events'
    },
    "accident_classification": {
        'Com Vítimas Feridas': 'With Injured Victims',
        'Com Vítimas Fatais': 'With Fatalities',
        'Sem Vítimas': 'No Victims'
    },
    "time_of_day": {
        'Plena Noite': 'Deep Night',
        'Pleno dia': 'Broad Daylight',
        'Amanhecer': 'Dawn',
        'Anoitecer': 'Dusk'
    },
    "direction": {
        'Decrescente': 'Decreasing',
        'Crescente': 'Increasing',
        'Não Informado': 'Not Informed'
    },
    "weather_condition": {
        'Nublado': 'Cloudy',
        'Céu Claro': 'Clear Sky',
        'Chuva': 'Rain',
        'Sol': 'Sun',
        'Vento': 'Wind',
        'Granizo': 'Hail',
        'Nevoeiro/neblina': 'Fog/Mist',
        'Neve': 'Snow',
        'Garoa/Chuvisco': 'Drizzle',
        'Ignorado': 'Unknown',
        'Nevoeiro/Neblina': 'Fog/Mist'
    },
    "type_of_road": {
        'Simples': 'Single',
        'Dupla': 'Double',
        'Múltipla': 'Multiple'
    },
    "road_layout": {
        'Reta': 'Straight',
        'Curva': 'Curve',
        'Desvio temporário': 'Temporary detour',
        'Rotatória': 'Roundabout',
        'Ponte': 'Bridge',
        'Interseção de vias': 'Road intersection',
        'Retorno regulamentado': 'Regulated return',
        'Viaduto': 'Overpass',
        'Túnel': 'Tunnel',
        'Não Informado': 'Not Informed',
        'Desvio Temporário': 'Temporary Detour',
        'Retorno Regulamentado': 'Regulated Return'
    },
    "urban_rural": {
        'Sim': 'Yes',
        'Não': 'No'
    }
}




for column, mapping in translations.items():
    if column in data22:
        data22[column] = data22[column].map(mapping)


print(data22.isnull().sum())



# 1. List the rows where a specific column has a missing value:
print(data22[data22['weekday'].isnull()])



# 2. List rows with any missing value:
print(data22[data22.isnull().any(axis=1)])



# 3. Percentage of missing data:
missing_percentage = (data22.isnull().sum() / len(data22)) * 100
print(missing_percentage)



# 4. Visualize missing data:
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))
sns.heatmap(data22.isnull(), cbar=False, cmap='viridis', yticklabels=False)
plt.show()


data22.to_csv("Dados_PRF_2022_translated.csv", index=False, encoding='utf-8', sep=';')
df['longitude'] = df['longitude'].str.replace(',', '.').astype(float)
df['latitude'] = df['latitude'].str.replace(',', '.').astype(float)
