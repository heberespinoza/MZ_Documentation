import pandas as pd
import re
import time
from datetime import datetime, timedelta, date
from src.util.connections.snowflake import snowpark_custom_session
from src.util.functions.transformation import format_sp_list


def get_date_lvl(row, range_type):
    range_value = row.get(f'{range_type}_RANGE')
    column_name = f'{range_value}_{range_type}'
    return row.get(column_name)


def concatenate_non_null(row):
    return '_'.join(str(val) for val in row if pd.notnull(val))


def extract_parameters(row):
    sp_parameters_map = {
        'DBASE': 'TARGET_DB',
        'START_DATE': 'SP_START_DATE',
        'END_DATE': 'SP_END_DATE',
        'DAYS_STORED': 'SP_DAYS_STORED',
        'ORG_ID': 'ORG_ID'
    }
    param_string = row['PARAMS']
    param_names = re.findall(r'(\w+)', param_string)
    values = []
    for param_name in param_names:
        if param_name in sp_parameters_map and sp_parameters_map[param_name] in row.index:
            values.append(row[sp_parameters_map[param_name]])
    return values


def sp_config_data(session, config_query):
    # config_query = """SELECT * FROM MZCOREDEV.CONFIG.JOB_CONFIG2"""
    # Receives data from CONFIG.JOB_CONFIG
    date_config_df = session.get_query(config_query).toPandas()
    date_config_df['L0_END_DATE'] = date.today() + timedelta(days=3)
    date_config_df['L0_START_DATE'] = pd.to_datetime(date_config_df['L0_END_DATE']) - pd.to_timedelta(date_config_df['DAYS_PROCESSED'], unit='D') - timedelta(days=3)
    date_config_df['L0_DAYS_STORED'] = date_config_df['DAYS_STORED']

    date_config_df['L1_END_DATE'] = pd.to_datetime(date_config_df['L0_END_DATE']) + timedelta(days=2)
    date_config_df['L1_START_DATE'] = pd.to_datetime(date_config_df['L0_START_DATE']) + timedelta(days=-2)
    date_config_df['L1_DAYS_STORED'] = date_config_df['L0_DAYS_STORED'] + 3

    date_config_df['L2_END_DATE'] = pd.to_datetime(date_config_df['L0_END_DATE']) + timedelta(days=3)
    date_config_df['L2_START_DATE'] = pd.to_datetime(date_config_df['L0_START_DATE']) + timedelta(days=-5)
    date_config_df['L2_DAYS_STORED'] = date_config_df['L0_DAYS_STORED'] + 5

    date_config_df['L3_END_DATE'] = pd.to_datetime(date_config_df['L0_END_DATE']) + timedelta(days=3)
    date_config_df['L3_START_DATE'] = pd.to_datetime(date_config_df['L0_START_DATE']) + timedelta(days=-30)
    date_config_df['L3_DAYS_STORED'] = date_config_df['L0_DAYS_STORED'] + 30

    date_columns = ['L0_END_DATE', 'L0_START_DATE', 'L1_END_DATE', 'L1_START_DATE',
                    'L2_END_DATE', 'L2_START_DATE', 'L3_END_DATE', 'L3_START_DATE']
    date_config_df[date_columns] = date_config_df[date_columns].apply(lambda x: pd.to_datetime(x).dt.date)

    # Creates the configured dates for the run.
    session.insert_pd(date_config_df, table_name="DATE_CONFIG", database="MZDWDEV", schema="CONFIG",  table_type='transient', overwrite=True)

    # Query to generate the procedures to be executed and their parameters, uses CONFIG.SP_SETTINGS table.
    procedures_query = """
    SELECT DISTINCT  S.*,  C.ORG_ID, C.TARGET_DB, C.START_DATE, C.DAYS_PROCESSED, C.DAYS_STORED, C.L0_END_DATE, C.L0_START_DATE, C.L0_DAYS_STORED, C.L1_END_DATE, 
    C.L1_START_DATE, C.L1_DAYS_STORED, C.L2_END_DATE, C.L2_START_DATE,C. L2_DAYS_STORED, C.L3_END_DATE, C.L3_START_DATE, C.L3_DAYS_STORED
    FROM MZDWDEV.CONFIG.SP_SETTINGS S
    INNER JOIN MZDWDEV.CONFIG.DATE_CONFIG C
    ON S.ORG_GROUP = C.GROUP_NAME  
    and S.ORG_NAME = C.org_name
    WHERE S.TESTING
    UNION
    SELECT DISTINCT S.*, C.ORG_ID, C.TARGET_DB, C.START_DATE, C.DAYS_PROCESSED, C.DAYS_STORED,  C.L0_END_DATE, C.L0_START_DATE, C.L0_DAYS_STORED, C.L1_END_DATE, 
    C.L1_START_DATE, C.L1_DAYS_STORED, C.L2_END_DATE, C.L2_START_DATE,C. L2_DAYS_STORED, C.L3_END_DATE, C.L3_START_DATE, C.L3_DAYS_STORED
    FROM MZDWDEV.CONFIG.SP_SETTINGS S
    INNER JOIN MZDWDEV.CONFIG.DATE_CONFIG C
    ON S.ACTIVE = C.ACTIVE
    WHERE 
    C.GROUP_NAME not in ('DEFAULT') and S.ORG_NAME = 'EVERYONE' and S.TESTING
    ;"""

    procedures_df = session.get_query(procedures_query).toPandas()
    default_range = 'L0'
    range_columns = ['START_DATE_RANGE', 'END_DATE_RANGE', 'DAYS_STORED_RANGE']
    procedures_df[range_columns] = procedures_df[range_columns].fillna(default_range)

    # Apply the function for START_DATE, END_DATE, and DAYS and create new columns
    procedures_df['SP_START_DATE'] = procedures_df.apply(lambda row: get_date_lvl(row, 'START_DATE'), axis=1)
    procedures_df['SP_END_DATE'] = procedures_df.apply(lambda row: get_date_lvl(row, 'END_DATE'), axis=1)
    procedures_df['SP_DAYS_STORED'] = procedures_df.apply(lambda row: get_date_lvl(row, 'DAYS_STORED'), axis=1)
    procedures_df['QUERY_TAG_KEY'] = procedures_df['PROCEDURE_NAME'] + '_' + procedures_df['ORG_ID'] + '_' + procedures_df['SP_START_DATE'].astype(str)
    procedures_df['BUILD_NUMBER'] = session.get_build_number()


    # Replace NULL/NaN values in 'range_type_COLUMN' with the default value


    # Apply function to map parameter names
    procedures_df['PARAMS_LIST'] = procedures_df.apply(lambda row: extract_parameters(row), axis=1)
    procedures_df['SP_PARAMS'] = procedures_df['PARAMS_LIST'].apply(format_sp_list)
    procedures_df = procedures_df.drop(columns=['PARAMS_LIST'])
    procedures_df['SP_PARAMS'] = procedures_df['SP_PARAMS'].apply(lambda x: str(x))
    procedures_df['CALL_STATEMENT'] = procedures_df.apply(lambda row: f'CALL {row["FULL_NAME"]}{row["SP_PARAMS"]}',
                                                          axis=1)
    # procedures_df.to_csv('C:/Users/admin/Desktop/procedures.csv', index=False)
    session.insert_pd(df=procedures_df, auto_create_table=True, table_name='LAST_RUN_SP', database='MZDWDEV',
                      schema='CONFIG',  overwrite=True, table_type='transient')
    return procedures_df;


