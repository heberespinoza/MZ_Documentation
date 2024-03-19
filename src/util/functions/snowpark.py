import itertools
from snowflake.snowpark import Session
from typing import Union, Optional, Sequence, Any


class CustomSession(Session):

    def __init__(self, session):
        self.session = session

    def __dir__(self):
        return sorted(set(dir(self.session) + dir(type(self)) + dir(super())))

    def __getattribute__(self, attr):
        try:
            return super().__getattribute__(attr)
        except AttributeError:
            return getattr(self.session, attr)

    def __getattr__(self, attr):
        return getattr(self.session, attr)

    def __call__(self, *args, **kwargs):
        return self.session(*args, **kwargs)

    insert_pd = Session.write_pandas
    pd_to_sp = Session.create_dataframe
    get_table = Session.table
    get_query = Session.sql

    log_query = """INSERT INTO MZCOREDEV.CUSTOMLOGS.BUILD_INFORMATION_TBL_TEST
    SELECT {} BUILD_NUMBER, LG.*, '{}' BUILD_STATUS FROM {}.CONFIG.LOG_GENERATOR LG;"""

    async_log_query = """INSERT INTO MZCOREDEV.CUSTOMLOGS.BUILD_INFORMATION_TBL_TEST
       SELECT {} BUILD_NUMBER, LG.*, '{}' BUILD_STATUS FROM {}.CONFIG.ASYNC_LOG_GENERATOR LG
       WHERE QUERY_ID = '{}';"""

    def exec(self, query: str, params: Optional[Sequence[Any]] = None):
        return self.sql(query, params).collect()

    def exec_batch(self, queries, params: Optional[Sequence[Any]] = None):
        results = [self.exec(query, params) for query in queries]
        return results

    def async_exec(self, query: str, params: Optional[Sequence[Any]] = None):
        return self.sql(query, params).collect_nowait()

    def async_exec_batch(self, queries, params: Optional[Sequence[Any]] = None):
        async_jobs = [self.async_exec(query, params) for query in queries]
        results = [async_job.result() for async_job in async_jobs]
        return async_jobs

    def assign_log(self, build_number, build_status):
        database = self.get_current_database()
        log = self.log_query.format(build_number, build_status, database)
        return log

    def assign_async_log(self, build_number, build_status, query_id):
        database = self.get_current_database()
        log = self.async_log_query.format(build_number, build_status, database, query_id)
        return log

    def exec_log(self, query, build_number, build_status):
        self.exec(query)
        log = self.assign_log(build_number, build_status)
        return self.exec(log)

    def exec_log_batch(self, queries, build_number, build_status):
        results = [self.exec_log(query, build_number, build_status) for query in queries]
        return results

    def async_exec_log(self, query, build_number, build_status):
        # Executes queries and creates log in custom table
        self.async_exec(query)
        log = self.assign_log(build_number, build_status)
        return self.async_exec(log)

    def async_exec_log_batch(self, queries, build_number, build_status):
        async_jobs = self.async_exec_batch(queries)
        query_ids = [async_job.query_id for async_job in async_jobs]
        logs = [self.assign_async_log(build_number, build_status, query_id) for query_id in query_ids]
        return self.async_exec_batch(logs)

    def qry_to_dicts(self, query):
        query_result = self.exec(query)
        query_dict = [row.asDict() for row in query_result]
        return query_dict

    def qry_to_url(self, endpoint, query):
        """
           :param endpoint: endpoint string in triple quote and expected position for keys using {}
           :param query: snowflake query, values must be in the same order as expected in the endpoint string
           :return: list of formatted urls with keys from query
           """
        url = []
        query_dict = self.qry_to_dicts(query)
        for item in query_dict:
            parameters = list(item.values())
            url.append(endpoint.format(*parameters))
        return url

    def qry_to_pd(self, query):
        return self.get_query(query).toPandas()

    def values_to_list(self, query):
        query_list = []
        query_dict = self.qry_to_dicts(query)
        for item in query_dict:
            query_list.append(list(item.values()))
        return query_list

    def single_list(self, query):
        query_list = []
        query_dict = self.qry_to_dicts(query)
        for item in query_dict:
            query_list.extend(list(item.values()))
        return query_list

    def get_build_number(self):
        bn_query = """
        SELECT COALESCE(
        (select TOP 1
        (BUILD_NUMBER + 1) BUILD_NUMBER
        from 
        MZCOREDEV.CUSTOMLOGS.BUILD_INFORMATION_TBL_TEST) 
        ,0) as BUILD_NUMBER
        ORDER BY BUILD_NUMBER DESC; """
        return self.exec(bn_query)[0]['BUILD_NUMBER']

    def get_table_columns(self, table_name):
        column_query = """
        SELECT TOP 1
        TABLE_CATALOG, 
        TABLE_SCHEMA, 
        TABLE_NAME, 
        array_to_string(arrayagg(column_name) within group ( order by ordinal_position), ', ' ) COLUMN_LIST,
        array_to_string(arrayagg('"' || column_name || '"') within group ( order by ordinal_position), ', ' ) QUOTED_COLUMN_LIST
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA not in ('INFORMATION_SCHEMA', 'CONFIG')
        and TABLE_NAME = '{}'
        GROUP BY TABLE_CATALOG,TABLE_SCHEMA, TABLE_NAME;""".format(table_name)
        return self.exec(column_query)[0]['QUOTED_COLUMN_LIST']



    # async_jobs = [df.collect_nowait() for df in dfs]
    # res = [async_job.result() for async_job in async_jobs]
