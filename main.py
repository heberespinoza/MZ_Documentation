from src.util.connections.snowflake import snowpark_custom_session
from src.util.functions.markdown import generate_markdown

session = snowpark_custom_session()
query = """SELECT * FROM MZDWDEV.CONFIG.DATA_DICTIONARY_GENERATOR
WHERE TABLE_SCHEMA = 'MODEL'
;"""
df = session.qry_to_pd(query)
generate_markdown(df, "model_schema.md")

session.close()