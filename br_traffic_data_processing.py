def convert_coords(df):
    """
    Converts the longitude and latitude columns from string to float,
    replacing commas with dots.
    """
    if 'longitude' in df.columns and df['longitude'].dtype == 'object':
        df['longitude'] = df['longitude'].str.replace(',', '.').astype(float)
    if 'latitude' in df.columns and df['latitude'].dtype == 'object':
        df['latitude'] = df['latitude'].str.replace(',', '.').astype(float)
    return df




import pandas as pd

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_template = os.path.join(script_dir, 'Dados_PRF_{}.csv')
dfs = []

# Dictionary for column name translations
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


# Dictionary for specific value translations
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
    'Ingestão de álcool pelo condutor': 'Alcohol ingestion by the driver',
    'Condutor deixou de manter distância do veículo da frente': 'Driver failed to maintain distance from the front vehicle',
    'Reação tardia ou ineficiente do condutor': 'Late or inefficient driver reaction',
    'Acumulo de água sobre o pavimento': 'Water accumulation on the pavement',
    'Mal súbito do condutor': 'Driver\'s sudden illness',
    'Chuva': 'Rain',
    'Ausência de reação do condutor': 'Lack of driver reaction',
    'Manobra de mudança de faixa': 'Lane changing maneuver',
    'Pista Escorregadia': 'Slippery road',
    'Ausência de sinalização': 'Lack of signage',
    'Condutor Dormindo': 'Driver sleeping',
    'Velocidade Incompatível': 'Incompatible speed',
    'Acessar a via sem observar a presença dos outros veículos': 'Accessing the road without noticing other vehicles',
    'Conversão proibida': 'Forbidden turn',
    'Transitar na contramão': 'Driving on the wrong side of the road',
    'Ultrapassagem Indevida': 'Improper overtaking',
    'Desrespeitar a preferência no cruzamento': 'Disregarding the right of way at an intersection',
    'Acostamento em desnível': 'Shoulder at uneven level',
    'Demais falhas mecânicas ou elétricas': 'Other mechanical or electrical failures',
    'Carga excessiva e/ou mal acondicionada': 'Excessive and/or poorly stowed cargo',
    'Problema com o freio': 'Braking problem',
    'Ingestão de álcool e/ou substâncias psicoativas pelo pedestre': 'Pedestrian under the influence of alcohol or psychoactive substances',
    'Curva acentuada': 'Sharp curve',
    'Estacionar ou parar em local proibido': 'Parking or stopping in a prohibited area',
    'Avarias e/ou desgaste excessivo no pneu': 'Tire damage and/or excessive wear',
    'Pedestre cruzava a pista fora da faixa': 'Pedestrian crossed the road outside the crosswalk',
    'Obstrução na via': 'Obstruction on the road',
    'Acesso irregular': 'Irregular access',
    'Pista esburacada': 'Potholed road',
    'Animais na Pista': 'Animals on the road',
    'Falta de acostamento': 'Lack of shoulder',
    'Entrada inopinada do pedestre': 'Unexpected pedestrian entry',
    'Acumulo de areia ou detritos sobre o pavimento': 'Sand or debris accumulation on the pavement',
    'Pedestre andava na pista': 'Pedestrian walking on the road',
    'Desvio temporário': 'Temporary detour',
    'Transitar no acostamento': 'Driving on the shoulder',
    'Problema na suspensão': 'Suspension problem',
    'Objeto estático sobre o leito carroçável': 'Static object on the carriageway',
    'Deficiência do Sistema de Iluminação/Sinalização': 'Deficient lighting/signaling system',
    'Trafegar com motocicleta (ou similar) entre as faixas': 'Riding a motorcycle (or similar) between lanes',
    'Condutor usando celular': 'Driver using cellphone',
    'Restrição de visibilidade em curvas horizontais': 'Restricted visibility on horizontal curves',
    'Ingestão de álcool ou de substâncias psicoativas pelo pedestre': 'Pedestrian ingesting alcohol or psychoactive substances',
    'Declive acentuado': 'Steep slope',
    'Frear bruscamente': 'Braking sharply',
    'Iluminação deficiente': 'Poor lighting',
    'Área urbana sem a presença de local apropriado para a travessia de pedestres': 'Urban area without a proper pedestrian crossing',
    'Demais Fenômenos da natureza': 'Other natural phenomena',
    'Demais falhas na via': 'Other road failures',
    'Faixas de trânsito com largura insuficiente': 'Traffic lanes with insufficient width',
    'Obras na pista': 'Roadworks',
    'Retorno proibido': 'Forbidden return',
    'Afundamento ou ondulação no pavimento': 'Road depression or wavy surface',
    'Falta de elemento de contenção que evite a saída do leito carroçável': 'Lack of containment element preventing exit from the carriageway',
    'Ingestão de substâncias psicoativas pelo condutor': 'Driver ingesting psychoactive substances',
    'Neblina': 'Fog',
    'Condutor desrespeitou a iluminação vermelha do semáforo': 'Driver disregarded the red traffic light',
    'Sistema de drenagem ineficiente': 'Inefficient drainage system',
    'Acumulo de óleo sobre o pavimento': 'Oil accumulation on the pavement',
    'Sinalização mal posicionada': 'Poorly positioned signage',
    'Pista em desnível': 'Uneven road',
    'Transitar na calçada': 'Driving on the sidewalk',
    'Fumaça': 'Smoke',
    'Redutor de velocidade em desacordo': 'Speed bump not in accordance',
    'Deixar de acionar o farol da motocicleta (ou similar)': 'Failure to turn on motorcycle (or similar) headlights',
    'Restrição de visibilidade em curvas verticais': 'Restricted visibility on vertical curves',
    'Semáforo com defeito': 'Faulty traffic light',
    'Faróis desregulados': 'Misaligned headlights',
    'Modificação proibida': 'Forbidden modification',
    'Participar de racha': 'Participate in drag racing',
    'Sinalização encoberta': 'Covered signaling',
    'Desobediência às normas de trânsito pelo pedestre': 'Disobedience to traffic rules by the pedestrian',
    'Fenômenos da Natureza': 'Natural phenomena',
    'Sinalização da via insuficiente ou inadequada': 'Insufficient or inadequate road signage',
    'Falta de Atenção do Pedestre': 'Lack of pedestrian attention',
    'Falta de Atenção à Condução': 'Lack of attention to driving',
    'Ingestão de Álcool': 'Alcohol ingestion',
    'Mal Súbito': 'Sudden illness',
    'Defeito Mecânico no Veículo': 'Mechanical defect in the vehicle',
    'Não guardar distância de segurança': 'Not keeping a safe distance',
    'Deficiência ou não Acionamento do Sistema de Iluminação/Sinalização do Veículo': 'Deficiency or non-activation of the Vehicle Lighting/Signaling System',
    'Desobediência às normas de trânsito pelo condutor': 'Disobedience to traffic rules by the driver',
    'Agressão Externa': 'External aggression',
    'Ingestão de Substâncias Psicoativas': 'Ingestion of psychoactive substances',
    'Restrição de Visibilidade': 'Visibility restriction',
    'Defeito na Via': 'Defect in the road'

},
    "accident_type" : {
    'Colisão traseira': 'Rear collision',
    'Tombamento': 'Overturning',
    'Colisão frontal': 'Frontal collision',
    'Saída de leito carroçável': 'Exit from the carriageway',
    'Colisão com objeto': 'Collision with object',
    'Colisão lateral mesmo sentido': 'Side collision in the same direction',
    'Engavetamento': 'Pile-up',
    'Colisão lateral sentido oposto': 'Side collision in the opposite direction',
    'Colisão transversal': 'Transversal collision',
    'Capotamento': 'Rollover',
    'Queda de ocupante de veículo': 'Fall from vehicle',
    'Incêndio': 'Fire',
    'Derramamento de carga': 'Cargo spill',
    'Atropelamento de Pedestre': 'Pedestrian run over',
    'Eventos atípicos': 'Atypical events',
    'Atropelamento de Animal': 'Animal run over',
    'nan': 'Not applicable or unknown',
    'Colisão com objeto estático': 'Collision with static object',
    'Danos eventuais': 'Occasional damages',
    'Colisão lateral': 'Side collision',
    'Colisão com objeto em movimento': 'Collision with moving object'
}
,
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
        'Sim': 'Urban',
        'Não': 'Rural'
    }
}

categorized_terms = {
    "Alcohol or Substance Abuse": [
        'Alcohol ingestion by the driver',
        'Driver ingesting psychoactive substances',
        'Pedestrian under the influence of alcohol or psychoactive substances',
        'Pedestrian ingesting alcohol or psychoactive substances',
        'Ingestion of psychoactive substances',
        'Ingestion of Substances Psychoactive',
        'Ingestion of Álcohol'
    ],
    "Driver Error": [
        'Driver failed to maintain distance from the front vehicle',
        'Late or inefficient driver reaction',
        'Lack of driver reaction',
        'Driver sleeping',
        'Driver using cellphone',
        'Disobedience to traffic rules by the driver',
        'Lack of attention to driving',
        'Not keeping a safe distance'
    ],
    "Road Conditions": [
        'Water accumulation on the pavement',
        'Slippery road',
        'Potholed road',
        'Oil accumulation on the pavement',
        'Uneven road',
        'Road depression or wavy surface',
        'Sand or debris accumulation on the pavement',
    ],
    "Vehicle Issues": [
        'Other mechanical or electrical failures',
        'Braking problem',
        'Tire damage and/or excessive wear',
        'Mechanical defect in the vehicle',
        'Suspension problem',
        'Failure to turn on motorcycle (or similar) headlights',
        'Misaligned headlights'
    ],
    "Weather Conditions": [
        'Rain',
        'Fog',
        'Smoke',
        'Natural phenomena',
        'Other natural phenomena'
    ],
    "Pedestrian-Related": [
        'Pedestrian crossed the road outside the crosswalk',
        'Unexpected pedestrian entry',
        'Pedestrian walking on the road',
        'Disobedience to traffic rules by the pedestrian',
        'Lack of pedestrian attention'
    ],
    "Traffic Rule Violation": [
        'Lane changing maneuver',
        'Forbidden turn',
        'Driving on the wrong side of the road',
        'Improper overtaking',
        'Disregarding the right of way at an intersection',
        'Driving on the shoulder',
        'Driver disregarded the red traffic light',
        'Riding a motorcycle (or similar) between lanes',
        'Participate in drag racing'
    ],
    "Infrastructure Issues": [
        'Lack of signage',
        'Shoulder at uneven level',
        'Lack of shoulder',
        'Deficient lighting/signaling system',
        'Poor lighting',
        'Insufficient or inadequate road signage',
        'Faulty traffic light',
        'Covered signaling'
    ],
    "Other Issues": [
        "Driver's sudden illness",
        'Sudden illness',
        'Obstruction on the road',
        'Animals on the road',
        'External aggression',
        'Visibility restriction',
        'Defect in the road'
    ],
    "Unlawful Acts": [
        'Accessing the road without noticing other vehicles',
        'Parking or stopping in a prohibited area',
        'Irregular access',
        'Forbidden return',
        'Transit on the sidewalk',
        'Forbidden modification'
    ]
}

def translate_dataframe(df, translation_dict):
    """Load the CSV file from the given path, translate its columns, and return the translated dataframe."""
    df_translated = df.rename(columns=translation_dict)
    return df_translated

def translate_values(df, translations):
    for column, mapping in translations.items():
        if column in df:
            df[column] = df[column].map(mapping)
    return df

def convert_datetime(df):
    """
    Converts the date and time columns to datetime objects.
    """
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    if 'time' in df.columns:
        # Concatenating date and time for better datetime representation
        df['datetime'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['time'], errors='coerce')
        df = df.drop(columns=['time'])  # dropping the 'time' column after creating 'datetime'
    return df

cause_to_category = {}
for category, causes in categorized_terms.items():
    for cause in causes:
        cause_to_category[cause] = category

additional_causes_mapping = {
    'Incompatible speed': 'Traffic Rule Violation',
    'Excessive and/or poorly stowed cargo': 'Vehicle Issues',
    'Sharp curve': 'Road Conditions',
    'Braking sharply': 'Driver Error',
    'Other road failures': 'Other Issues',
    'Restricted visibility on horizontal curves': 'Visibility restriction',
    'Lack of containment element preventing exit from the carriageway': 'Infrastructure Issues',
    'Roadworks': 'Infrastructure Issues',
    'Temporary detour': 'Infrastructure Issues',
    'Speed bump not in accordance': 'Infrastructure Issues',
    'Driving on the sidewalk': 'Unlawful Acts',
    'Poorly positioned signage': 'Infrastructure Issues',
    'Static object on the carriageway': 'Infrastructure Issues',
    'Steep slope': 'Road Conditions',
    'Traffic lanes with insufficient width': 'Infrastructure Issues',
    'Urban area without a proper pedestrian crossing': 'Infrastructure Issues',
    'Restricted visibility on vertical curves': 'Visibility restriction'
}

cause_to_category.update(additional_causes_mapping)

for year in range(2017, 2024):
    file_path = file_path_template.format(year)
    try:
        df_year = pd.read_csv(file_path, encoding='iso-8859-1', delimiter=';')
        df_year = df_year.drop_duplicates()
        
        # Translate column names
        df_translated = translate_dataframe(df_year, translation_dict)
        
        # Convert coordinates
        df_translated = convert_coords(df_translated)

        # Convert date and time to datetime objects
        df_translated = convert_datetime(df_translated)
        
        # Translate specific values
        df_translated = translate_values(df_translated, translations)
        
        df_translated['accident_cause_category'] = df_translated['accident_cause'].map(cause_to_category)
        # Save translated CSV
        output_file_name = os.path.join(script_dir, "Dados_PRF_" + str(year) + "_translated.csv")
        df_translated.to_csv(output_file_name, index=False, encoding='utf-8', sep=';')
        
    except FileNotFoundError:
        print("File for year " + str(year) + " not found. Skipping...")
# Map the accident causes to categories
df_translated['accident_cause_category'] = df_translated['accident_cause'].map(cause_to_category)

# Debugging: Print out values that didn't get mapped
unmapped_causes = df_translated[df_translated['accident_cause_category'].isna()]['accident_cause'].unique()
print("Unmapped Causes for Year", year, ":", unmapped_causes)