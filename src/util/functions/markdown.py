import pandas as pd
import os
from definitions import MD_FILE_PATH


def generate_markdown(df, file_name):
    # Group dataframe by TABLE
    grouped = df.groupby(['TABLE_NAME', 'TABLE_DESCRIPTION'])

    markdown_code = ""
    for name, group in grouped:
        table_name, table_description = name
        markdown_code += f"## {table_name}: {table_description}\n\n"

        # Create Markdown table
        markdown_code += "| COLUMN | COLUMN_DESCRIPTION | DATA_TYPE | NOTES |\n"
        markdown_code += "| ------ | ------------------ | -------- | ------ |\n"
        for index, row in group.iterrows():
            markdown_code += f"| {row['COLUMN_NAME']} | {row['COLUMN_DESCRIPTION']} | {row['DATA_TYPE']} | {row['NOTES']} |\n"
        markdown_code += "\n\n"

    output_path = os.path.join(MD_FILE_PATH, file_name)
    with open(output_path, "w") as markdown_file:
        markdown_file.write(markdown_code)
    result = f"Saved file: {output_path}"
    return print(result)

