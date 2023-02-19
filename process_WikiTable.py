import pandas as pd
import requests


if __name__ == '__main__':
    data = requests.get('https://raw.githubusercontent.com/ppasupat/WikiTableQuestions/master/misc/table-metadata.tsv')
    res_dict = {
        "title": [],
        "table_link": [],
        "statement": [],
        "isUnderReview": [],
        "area": [],
        "contact": []
    }
    with open('./tablefact.csv', 'w') as f:
        table_meta = data.text
        tables = table_meta.split('\n')[1: -1]
        for table in tables:
            t = table.split('\t')
            title, path = t[4], 'https://raw.githubusercontent.com/ppasupat/WikiTableQuestions/master/' + t[0]
            res_dict["title"].append(title)
            res_dict["table_link"].append(path)
            res_dict["statement"].append('')
            res_dict["isUnderReview"].append('false')
            res_dict["area"].append('')
            res_dict["contact"].append('')

        df = pd.DataFrame(res_dict)
        df.to_csv(f, index=False)