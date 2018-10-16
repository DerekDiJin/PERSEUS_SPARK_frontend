import sys, os
import multiprocessing as mp

from app.services.utils import create_data_sql, create_edges_sql

def main():
    # create and import sqls
    demo_data_file = os.path.join(os.path.dirname(__file__), 'app/data/demo/db.csv')
    demo_data_sql_path = os.path.join(os.path.dirname(__file__), 'app/data/demo/data.sql')
    create_data_sql(demo_data_file, demo_data_sql_path, 1)
    os.system('sqlite3 db.sqlite3 < %s' % demo_data_sql_path)
        
    demo_edge_file = os.path.join(os.path.dirname(__file__), 'app/data/demo/edges.tsv')
    demo_edge_sql_path = os.path.join(os.path.dirname(__file__), 'app/data/demo/edges.sql')
    create_edges_sql(demo_edge_file, demo_edge_sql_path, 1)
    os.system('sqlite3 db.sqlite3 < %s' % demo_edge_sql_path)
        
    # associate with the dataset object
    os.system(""" sqlite3 db.sqlite3 'UPDATE app_dataset SET analyzed_fulldata_file = "%s", analyzed_graph_file = "%s" WHERE id = 1' """ %
                ('data/demo/db.csv', 'data/demo/display.csv'))

if __name__ == '__main__':
    main()
