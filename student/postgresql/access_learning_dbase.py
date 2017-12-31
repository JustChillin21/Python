import psycopg2
connection = psycopg2.connect(database="learning", user="y2venom", password="jun34u2I", host="10.6.21.25")
# cursor.execute('CREATE TABLE public.movies ('
#                'id SERIAL PRIMARY KEY NOT NULL,'
#                'name character varying(100),'
#                'genre character varying(65),'
#                'watched boolean);')
with connection.cursor() as cursor:
#cursor.execute('DROP TABLE public.movies;')
    cursor.execute("INSERT INTO movies(name,genre,watched) VALUES('The Matrix','Sci-Fi',true)")
    cursor.execute("INSERT INTO movies(name,genre,watched) VALUES('Okja','Drama',false)")
    #cursor.execute("INSERT INTO public.movies(name,genre,watched) VALUES('Okja','Drama',FALSE );")
    cursor.execute("INSERT INTO movies(name,genre,watched) VALUES('Sleepy Hollow','Fantasy',false)")
    #cursor.execute("SELECT * FROM public.movies;")
connection.commit()
connection.close()

i=0
data=[]
for row in cursor:
    data.append(row)
    print(data[i])
#
#    # for value in data[i]:
#    #     print(value)
    i += 1