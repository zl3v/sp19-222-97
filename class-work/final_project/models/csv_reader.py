import csv
import numpy as np

with open('./data/MOCK_DATA.csv') as csv_file:
    entries = []
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row)
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\tName: {row[0]} Score: {row[1]} Level: {row[2]} Playtime: {row[3]}')
            new_entry = row
            entries.append(new_entry)
            line_count += 1

    #sort_nam(entries)

    #entries_np_arr = np.asarray(entries)
    #np.matrix.sort(entries_np_arr)
    print(entries)

    print(f'Processed {line_count} lines.')
