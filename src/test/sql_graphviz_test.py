from src.connections.snowflake import snowpark_session

from src.functions import graphviz

session = snowpark_session()


# current_directory = os.getcwd()
#
# # Specify the output file name
# output_file = 'export.sql'
#
# # Construct the output file path
# output_file_path = os.path.join(current_directory, output_file)
#
# # Generate the EXPORT INTO FILE command
# export_command = f"EXPORT INTO FILE://{output_file_path} FROM TABLES (<database>.<schema>.*);"
#
# # Execute the EXPORT INTO FILE command
# cursor = conn.cursor()
# cursor.execute(export_command)
#
# # Fetch the result if needed
# result = cursor.fetchall()
#
# # Process the result as per your requirements
#
# # Close the cursor and connection
# cursor.close()
# conn.close()


with open("/src/test/dll.sql", "rb") as data:
    x = graphviz(data)

session.close()