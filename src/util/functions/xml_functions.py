import pandas as pd
import os
import xml.etree.ElementTree as Et
from definitions import XML_FILE_PATH


def create_table_element(table, table_description):
    # Create table element
    table_elem = Et.Element("table")
    table_elem.text = f"{table}: {table_description}"
    return table_elem


def create_column_element(column, column_description, datatype, notes):
    # Create column element
    column_elem = Et.Element("column")
    # column_elem.text = f"{column}: {column_description}"

    datatype_elem = Et.SubElement(column_elem, "column")
    datatype_elem.text = column

    datatype_elem = Et.SubElement(column_elem, "column_description")
    datatype_elem.text = column_description

    # Create datatype element
    datatype_elem = Et.SubElement(column_elem, "datatype")
    datatype_elem.text = datatype

    # Create notes element
    notes_elem = Et.SubElement(column_elem, "notes")
    notes_elem.text = notes

    return column_elem


def dictionary_dataframe_to_xml(df, file_name):
    # Create the root element of the XML tree
    root = Et.Element("tables")
    output_path = os.path.join(XML_FILE_PATH, file_name)

    # Iterate over each row in the dataframe
    for index, row in df.iterrows():
        # Create table element
        table_elem = create_table_element(row['TABLE_NAME'], row['TABLE_DESCRIPTION'])

        # Create columns element
        columns_elem = Et.SubElement(table_elem, "columns")

        # Create column elements
        column_elem = create_column_element(row['COLUMN_NAME'], row['COLUMN_DESCRIPTION'], row['DATA_TYPE'], row['NOTES'])
        columns_elem.append(column_elem)

        # Append table element to root
        root.append(table_elem)

        # Writes XML to path
        tree = Et.ElementTree(root)
        if os.path.exists(output_path):
            os.remove(output_path)

        tree.write(output_path, encoding="utf-8", xml_declaration=True)
        result = f"Saved file: {file_name} in {XML_FILE_PATH}"
        return print(result)


