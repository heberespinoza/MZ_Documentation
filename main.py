from src.util.connections.snowflake import snowpark_custom_session
from src.util.functions.xml_functions import dictionary_dataframe_to_xml

session = snowpark_custom_session()
query = """SELECT * FROM MZDWDEV.CONFIG.DATA_DICTIONARY_GENERATOR
WHERE TABLE_SCHEMA = 'MODEL'
;"""
df = session.qry_to_pd(query)
dictionary_dataframe_to_xml(df, "model_schema.xml")

session.close()