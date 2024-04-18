import pandas as pd
from config import settings
import pyodbc


class BaseDAO:
    table = 'data'
    @classmethod
    def execute_sql_query(cls,query, conn):
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    @classmethod
    def get_smth(cls, kn, t):
        conn = pyodbc.connect(settings.get_database_url)
        # Выполняем SQL запрос с использованием кадастрового номера из Streamlit input
        query = f'''SELECT TOP 1 data.{t}
        FROM {cls.table}
        WHERE data.kn = '{kn}'
        and(data.comment IS NULL OR data.comment = 'статья 378.2 НК РФ')
        AND data.status = 'Published'
        AND CAST(data.datestart AS DATE) <= GETDATE()
        ORDER BY data.datefound DESC, data.datetime DESC;'''
        query_result = cls.execute_sql_query(query, conn)# результат запроса
        conn.close()
        result = None
        for row in query_result:
            result = str(row[0])
        return result


    @classmethod
    def get_actual_kc(cls, kn):
        conn = pyodbc.connect(settings.get_database_url)
        # Выполняем SQL запрос с использованием кадастрового номера из Streamlit input
        query = f'''SELECT TOP 1 data.kc
        FROM {cls.table}
        WHERE data.kn = '{kn}'
        and(data.comment IS NULL OR data.comment = 'статья 378.2 НК РФ')
        AND data.status = 'Published'
        AND CAST(data.datestart AS DATE) <= GETDATE()
        ORDER BY data.datefound DESC, data.datetime DESC;'''
        query_result = cls.execute_sql_query(query, conn)# результат запроса
        conn.close()
        result = None
        for row in query_result:
            result = str(row[0])
        return result
    
    @classmethod
    def get_all_kc(cls, kn):
        conn = pyodbc.connect(settings.get_database_url)
        # Выполняем SQL запрос с использованием кадастрового номера из Streamlit input
        query = f'''SELECT data.kc, data.docname
        FROM {cls.table}
        WHERE data.kn = '{kn}'
        and(data.comment IS NULL OR data.comment = 'статья 378.2 НК РФ')
        AND data.status = 'Published'
        AND CAST(data.datestart AS DATE) <= GETDATE()
        ORDER BY data.datefound DESC, data.datetime DESC;'''
        query_result = cls.execute_sql_query(query, conn)# результат запроса
        conn.close()
        # print(query_result)
        # Получаем результаты запроса
        
        # Преобразуем результаты в датафрейм
        # query_result_cleaned = [(kc, docname) for kc, docname in query_result]

        # # Создание DataFrame
        # df = pd.DataFrame(query_result_cleaned, columns=['Кадастровая стоимость', 'Название документа'])
        # # Выводим датафрейм на экран
        # return df
        return query_result