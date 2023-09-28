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
    "accident_cause":   {
    'Falta de Atenção à Condução': 'Lack of Attention to Driving',
    'Não guardar distância de segurança': 'Not Keeping Safe Distance',
    'Ingestão de Álcool': 'Alcohol Ingestion',
    'Ultrapassagem Indevida': 'Improper Overtaking',
    'Defeito Mecânico no Veículo': 'Vehicle Mechanical Failure',
    'Avarias e/ou desgaste excessivo no pneu': 'Damage and/or Excessive Tire Wear',
    'Condutor Dormindo': 'Driver Sleeping',
    'Velocidade Incompatível': 'Incompatible Speed',
    'Fenômenos da Natureza': 'Natural Phenomena',
    'Carga excessiva e/ou mal acondicionada': 'Excessive and/or Poorly Stowed Load',
    'Animais na Pista': 'Animals on the Road',
    'Falta de Atenção do Pedestre': 'Lack of Pedestrian Attention',
    'Defeito na Via': 'Road Defect',
    'Pista Escorregadia': 'Slippery Road',
    'Desobediência às normas de trânsito pelo condutor': 'Disobedience to Traffic Rules by Driver',
    'Sinalização da via insuficiente ou inadequada': 'Insufficient or Inadequate Road Signaling',
    'Restrição de Visibilidade': 'Visibility Restriction',
    'Objeto estático sobre o leito carroçável': 'Static Object on Carriageway',
    'Mal Súbito': 'Sudden Illness',
    'Deficiência ou não Acionamento do Sistema de Iluminação/Sinalização do Veículo': 'Deficiency or Non-Activation of Vehicle Lighting/Signaling System',
    'Ingestão de Substâncias Psicoativas': 'Ingestion of Psychoactive Substances',
    'Agressão Externa': 'External Aggression',
    'Desobediência às normas de trânsito pelo pedestre': 'Disobedience to Traffic Rules by Pedestrian',
    'Ingestão de álcool e/ou substâncias psicoativas pelo pedestre': 'Alcohol and/or Psychoactive Substance Consumption by Pedestrian',
    'Acumulo de areia ou detritos sobre o pavimento': 'Accumulation of Sand or Debris on Pavement',
    'Ingestão de álcool pelo condutor': 'Alcohol Consumption by Driver',
    'Curva acentuada': 'Sharp Curve',
    'Reação tardia ou ineficiente do condutor': 'Late or Inefficient Driver Reaction',
    'Desrespeitar a preferência no cruzamento': 'Disrespecting Intersection Preference',
    'Pedestre andava na pista': 'Pedestrian Walking on the Road'
},
    "accident_type" :{
    'Colisão frontal': 'Frontal Collision',
    'Colisão traseira': 'Rear Collision',
    'Colisão lateral': 'Lateral Collision',
    'Saída de leito carroçável': 'Exit from Carriageway',
    'Tombamento': 'Tipping Over',
    'Colisão transversal': 'Transverse Collision',
    'Incêndio': 'Fire',
    'Colisão com objeto estático': 'Collision with Static Object',
    'Derramamento de carga': 'Cargo Spill',
    'Atropelamento de Animal': 'Animal Run-Over',
    'Atropelamento de Pedestre': 'Pedestrian Hit',
    'Engavetamento': 'Pile-Up',
    'Capotamento': 'Rollover',
    'Queda de ocupante de veículo': 'Fall of Vehicle Occupant',
    'Colisão com objeto em movimento': 'Collision with Moving Object',
    'Danos eventuais': 'Occasional Damages',
    'Colisão lateral mesmo sentido': 'Side Collision, Same Direction'
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
        'Sim': 'Urban',
        'Não': 'Rural'
    }
}

cause_to_category = {
    'Lack of Attention to Driving': 'Driver is to blame',
    'Not Keeping Safe Distance': 'Driver is to blame',
    'Alcohol Ingestion': 'Driver is to blame',
    'Improper Overtaking': 'Traffic maneuvers',
    'Vehicle Mechanical Failure': 'Improper or failed equipment',
    'Damage and/or Excessive Tire Wear': 'Improper or failed equipment',
    'Driver Sleeping': 'Driver is to blame',
    'Incompatible Speed': 'Driver is to blame',
    'Natural Phenomena': 'Environmental events',
    'Excessive and/or Poorly Stowed Load': 'Improper or failed equipment',
    'Animals on the Road': 'Environmental events',
    'Lack of Pedestrian Attention': 'Traffic situations',
    'Road Defect': 'Environmental events',
    'Slippery Road': 'Environmental events',
    'Disobedience to Traffic Rules by Driver': 'Traffic maneuvers',
    'Insufficient or Inadequate Road Signaling': 'Traffic situations',
    'Visibility Restriction': 'Traffic situations',
    'Static Object on Carriageway': 'Traffic situations',
    'Sudden Illness': 'Driver is to blame',
    'Deficiency or Non-Activation of Vehicle Lighting/Signaling System': 'Improper or failed equipment',
    'Ingestion of Psychoactive Substances': 'Driver is to blame',
    'External Aggression': 'Traffic situations',
    'Disobedience to Traffic Rules by Pedestrian': 'Traffic situations',
    'Alcohol and/or Psychoactive Substance Consumption by Pedestrian': 'Traffic situations',
    'Accumulation of Sand or Debris on Pavement': 'Environmental events',
    'Alcohol Consumption by Driver': 'Driver is to blame',
    'Sharp Curve': 'Traffic situations',
    'Late or Inefficient Driver Reaction': 'Driver is to blame',
    'Disrespecting Intersection Preference': 'Traffic maneuvers',
    'Pedestrian Walking on the Road': 'Traffic situations'
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
        df_year = pd.read_csv(file_path, encoding='latin-1', delimiter=';')
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
