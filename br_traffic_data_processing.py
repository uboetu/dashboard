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

cause_to_category = {
    'Driver alcohol consumption': 'Driver is to blame',
    'Late or inefficient driver reaction': 'Driver is to blame',
    'Incompatible speed': 'Driver is to blame',
    'Driving on the wrong side': 'Driver is to blame',
    'Lane change maneuver': 'Lane change maneuver',
    'Water accumulation on the pavement': 'Environmental events',
    'Animals on the road': 'Environmental events',
    'Slippery road': 'Environmental events',
    'Potholed road': 'Environmental events',
    'Accumulation of sand or debris on the pavement': 'Environmental events',
    'Pavement sinking or undulation': 'Environmental events',
    'Oil accumulation on the pavement': 'Environmental events',
    'Lack of shoulder': 'Environmental events',
    'Other natural phenomena': 'Environmental events',
    'Uneven road': 'Environmental events',
    'Steep decline': 'Environmental events',
    'Other roadway failures': 'Environmental events',
    'Uneven shoulder': 'Environmental events',
    'Lane change maneuvers': 'Traffic maneuvers',
    'Improper overtaking': 'Traffic maneuvers',
    'Disregarding intersection priority': 'Traffic maneuvers',
    'Entering the roadway without noticing other vehicles': 'Traffic maneuvers',
    'Forbidden conversion': 'Traffic maneuvers',
    'Entering the roadway without noticing other vehicles': 'Traffic maneuvers',
    'Driving on the wrong side': 'Traffic maneuvers',
    'Exit from carriageway': 'Traffic maneuvers',
    'Riding a motorcycle (or similar) between lanes': 'Traffic maneuvers',
    'Braking sharply': 'Traffic maneuvers',
    'Driving on the shoulder': 'Traffic maneuvers',
    'Forbidden U-turn': 'Traffic maneuvers',
    'Parking or stopping in a prohibited place': 'Traffic maneuvers',
    'Driving on the sidewalk': 'Traffic maneuvers',
    'Other mechanical or electrical failures': 'Improper or failed equipment',
    'Excessive and/or poorly stowed load': 'Improper or failed equipment',
    'Brake issue': 'Improper or failed equipment',
    'Covered signage': 'Improper or failed equipment',
    'Malfunctioning traffic light': 'Improper or failed equipment',
    'Damages and/or excessive tire wear': 'Improper or failed equipment',
    'Poor lighting': 'Improper or failed equipment',
    'Suspension problem': 'Improper or failed equipment',
    'Deficiency in the Lighting/Signaling System': 'Improper or failed equipment',
    'Failure to turn on motorcycle (or similar) headlights': 'Improper or failed equipment',
    'Forbidden modification': 'Improper or failed equipment',
    'Non-compliant speed reducer': 'Improper or failed equipment',
    'Misaligned headlights': 'Improper or failed equipment',
    'Inefficient drainage system': 'Improper or failed equipment',
    'Driving on the wrong side': 'Traffic situations',
    'Unexpected pedestrian entry': 'Traffic situations',
    'Pedestrian walking on the road': 'Traffic situations',
    'Restricted visibility on vertical curves': 'Traffic situations',
    'Restricted visibility on horizontal curves': 'Traffic situations',
    'Irregular access': 'Traffic situations',
    'Pedestrian crossing the road outside the crosswalk': 'Traffic situations',
    'Lack of signaling': 'Traffic situations',
    'Sharp curve': 'Traffic situations',
    'Road obstruction': 'Traffic situations',
    'Roadworks': 'Traffic situations',
    'Temporary detour': 'Traffic situations',
    'Static object on the carriageway': 'Traffic situations',
    'Pedestrian consumption of alcohol and/or psychoactive substances': 'Traffic situations',
    'Pedestrian consumption of alcohol or psychoactive substances': 'Traffic situations',
    'Urban area without an appropriate pedestrian crossing location': 'Traffic situations',
    'Lack of containment element preventing the exit from the carriageway': 'Traffic situations',
    'Poorly positioned signage': 'Traffic situations',
    'Traffic lanes with insufficient width': 'Traffic situations',
    'Fog': 'Weather conditions',
    'Rain': 'Weather conditions',
    'Smoke': 'Weather conditions'
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
