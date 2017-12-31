import psycopg2 as pq
cn = pq.connect('dbname=mydb user=me')
cr = cn.cursor()
cr.execute('SELECT * FROM test1;')
tmp = cr.fetchall()

# Extract the column names
col_names = []
for elt in cr.description:
    col_names.append(elt[0])

# Create the dataframe, passing in the list of col_names extracted from the description
df = pq.DataFrame(tmp, columns=col_names)