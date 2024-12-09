import sqlite3
import pandas as pd
from traceback import print_exc


def parse():
    connection = sqlite3.connect('users_and_bets.s3db')
    log_file_name = 'log1.csv'
    users_file_name = 'users1.csv'

    log_df = pd.read_csv(
        log_file_name, names=['user_id', 'time', 'bet', 'win'], encoding='utf-8', sep=',')

    users_df = pd.read_csv(
        users_file_name, names=['user_id', 'email', 'geo'], encoding='koi8-r', sep='\t')

    log_df.to_sql('LOG', connection, if_exists='append', index=False)
    users_df.to_sql('USERS', connection, if_exists='append', index=False)

    connection.close()


if __name__ == '__main__':
    try:
        parse()
        print("success")
    except:
        print_exc()
