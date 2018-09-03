def table_to_dict(table, transposed=False):
    """
    Convert Step Table to Dictionary
    :param table: Behave feature table data format
    :param transposed: If step data table is transposed.
    :return: dictionary when the table is not transposed and tuple when it is transposed
    """
    test_data = []
    if not transposed:
        for row in table:
            test_data.append([str(row[0]), str(row[1])])
        return dict(test_data)
    else:
        heading = table.headings
        for r in table.rows:
            for i, v in enumerate(r):
                test_data.append((heading[i], v))
        return tuple(test_data)
