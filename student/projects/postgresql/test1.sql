PGDMP                          u           learning    9.6.5    9.6.5 +    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false            �           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    3            _           1247    16543    mood    TYPE     s   CREATE TYPE mood AS ENUM (
    'extremely unhappy',
    'unhappy',
    'ok',
    'happy',
    'extremely happy'
);
    DROP TYPE public.mood;
       public       postgres    false    3            e           1247    16577    union_status    TYPE     Y   CREATE TYPE union_status AS ENUM (
    'NU',
    'BEM',
    'APP',
    'FM',
    'LM'
);
    DROP TYPE public.union_status;
       public       postgres    false    3            �            1259    16474    total_revenue_per_customer    TABLE     �   CREATE TABLE total_revenue_per_customer (
    "ID" integer,
    "First Name" character varying(100),
    "Last Name" character varying(255),
    "Total Price" numeric
);

ALTER TABLE ONLY total_revenue_per_customer REPLICA IDENTITY NOTHING;
 .   DROP TABLE public.total_revenue_per_customer;
       public         postgres    false    3            �            1259    16478    awesome_customers    VIEW     8  CREATE VIEW awesome_customers AS
 SELECT total_revenue_per_customer."ID",
    total_revenue_per_customer."First Name",
    total_revenue_per_customer."Last Name",
    total_revenue_per_customer."Total Price"
   FROM total_revenue_per_customer
  WHERE (total_revenue_per_customer."Total Price" > (150)::numeric);
 $   DROP VIEW public.awesome_customers;
       public       postgres    false    189    189    189    189    3            �            1259    16395 	   customers    TABLE     �   CREATE TABLE customers (
    first_name character varying(100),
    id integer NOT NULL,
    last_name character varying(255)
);
    DROP TABLE public.customers;
       public         postgres    false    3            �            1259    16523    customers_id_seq    SEQUENCE     r   CREATE SEQUENCE customers_id_seq
    START WITH 6
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.customers_id_seq;
       public       postgres    false    3    186            �           0    0    customers_id_seq    SEQUENCE OWNED BY     7   ALTER SEQUENCE customers_id_seq OWNED BY customers.id;
            public       postgres    false    196            �            1259    16400    items    TABLE     s   CREATE TABLE items (
    name character varying(255) NOT NULL,
    id integer NOT NULL,
    price numeric(10,2)
);
    DROP TABLE public.items;
       public         postgres    false    3            �            1259    16507    expensive_items    VIEW     �   CREATE VIEW expensive_items AS
 SELECT items.name,
    items.id,
    items.price
   FROM items
  WHERE (items.price >= (100)::numeric)
  WITH LOCAL CHECK OPTION;
 "   DROP VIEW public.expensive_items;
       public       postgres    false    187    187    187    3            �            1259    16553    expensive_items_diff    VIEW     *  CREATE VIEW expensive_items_diff AS
 SELECT items.name,
    items.id,
    items.price,
    (items.price - ( SELECT avg(items_1.price) AS avg
           FROM items items_1
          WHERE (items_1.price > (100)::numeric))) AS "Price Difference"
   FROM items
  WHERE (items.price > (100)::numeric);
 '   DROP VIEW public.expensive_items_diff;
       public       postgres    false    187    187    187    3            �            1259    16694    get_work_hours    VIEW       CREATE VIEW get_work_hours AS
 SELECT (((date_part('hours'::text, COALESCE((((age(timesheet.wrap_time, timesheet.start_time) + age(timesheet.start_time, COALESCE(timesheet.travel_start, COALESCE(timesheet.start_time, timesheet.ndb_time)))) + age(COALESCE(timesheet.travel_wrap, timesheet.wrap_time), timesheet.wrap_time)) - age(timesheet.meal1_end, timesheet.meal1_start)), ((age(timesheet.wrap_time, timesheet.start_time) + age(timesheet.start_time, COALESCE(timesheet.travel_start, COALESCE(timesheet.start_time, timesheet.ndb_time)))) + age(COALESCE(timesheet.travel_wrap, timesheet.wrap_time), timesheet.wrap_time)))) * (60)::double precision) + date_part('minutes'::text, COALESCE((((age(timesheet.wrap_time, timesheet.start_time) + age(timesheet.start_time, COALESCE(timesheet.travel_start, COALESCE(timesheet.start_time, timesheet.ndb_time)))) + age(COALESCE(timesheet.travel_wrap, timesheet.wrap_time), timesheet.wrap_time)) - age(timesheet.meal1_end, timesheet.meal1_start)), ((age(timesheet.wrap_time, timesheet.start_time) + age(timesheet.start_time, COALESCE(timesheet.travel_start, COALESCE(timesheet.start_time, timesheet.ndb_time)))) + age(COALESCE(timesheet.travel_wrap, timesheet.wrap_time), timesheet.wrap_time))))) / (60)::double precision) AS work_hours
   FROM bbase.timesheet;
 !   DROP VIEW public.get_work_hours;
       public       postgres    false    3            �            1259    16519    items_id_seq    SEQUENCE     o   CREATE SEQUENCE items_id_seq
    START WITH 10
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.items_id_seq;
       public       postgres    false    187    3            �           0    0    items_id_seq    SEQUENCE OWNED BY     /   ALTER SEQUENCE items_id_seq OWNED BY items.id;
            public       postgres    false    195            �            1259    16517    movie_id_seq    SEQUENCE     n   CREATE SEQUENCE movie_id_seq
    START WITH 3
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.movie_id_seq;
       public       postgres    false    3            �            1259    16511    non_luxury_items    VIEW     �   CREATE VIEW non_luxury_items AS
 SELECT expensive_items.name,
    expensive_items.id,
    expensive_items.price
   FROM expensive_items
  WHERE (expensive_items.price < (10000)::numeric)
  WITH CASCADED CHECK OPTION;
 #   DROP VIEW public.non_luxury_items;
       public       postgres    false    191    191    191    3            �            1259    16405 	   purchases    TABLE     b   CREATE TABLE purchases (
    id integer NOT NULL,
    item_id integer,
    customer_id integer
);
    DROP TABLE public.purchases;
       public         postgres    false    3            �            1259    16528    purchases_id_seq    SEQUENCE     s   CREATE SEQUENCE purchases_id_seq
    START WITH 12
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.purchases_id_seq;
       public       postgres    false    3    188            �           0    0    purchases_id_seq    SEQUENCE OWNED BY     7   ALTER SEQUENCE purchases_id_seq OWNED BY purchases.id;
            public       postgres    false    197            �            1259    16539    students    TABLE     R   CREATE TABLE students (
    name character varying(255),
    current_mood mood
);
    DROP TABLE public.students;
       public         postgres    false    607    3            �            1259    16657    temp    TABLE     %   CREATE TABLE temp (
    a integer
);
    DROP TABLE public.temp;
       public         postgres    false    3            �            1259    16515    users_id_seq    SEQUENCE     n   CREATE SEQUENCE users_id_seq
    START WITH 3
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.users_id_seq;
       public       postgres    false    3                       2604    16525    customers id    DEFAULT     ^   ALTER TABLE ONLY customers ALTER COLUMN id SET DEFAULT nextval('customers_id_seq'::regclass);
 ;   ALTER TABLE public.customers ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    196    186                       2604    16526    items id    DEFAULT     V   ALTER TABLE ONLY items ALTER COLUMN id SET DEFAULT nextval('items_id_seq'::regclass);
 7   ALTER TABLE public.items ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    195    187            �          0    16395 	   customers 
   TABLE DATA               7   COPY customers (first_name, id, last_name) FROM stdin;
    public       postgres    false    186   �2       �           0    0    customers_id_seq    SEQUENCE SET     8   SELECT pg_catalog.setval('customers_id_seq', 6, false);
            public       postgres    false    196            �          0    16400    items 
   TABLE DATA               )   COPY items (name, id, price) FROM stdin;
    public       postgres    false    187   3       �           0    0    items_id_seq    SEQUENCE SET     5   SELECT pg_catalog.setval('items_id_seq', 10, false);
            public       postgres    false    195            �           0    0    movie_id_seq    SEQUENCE SET     4   SELECT pg_catalog.setval('movie_id_seq', 3, false);
            public       postgres    false    194            �          0    16405 	   purchases 
   TABLE DATA               6   COPY purchases (id, item_id, customer_id) FROM stdin;
    public       postgres    false    188   �3       �           0    0    purchases_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('purchases_id_seq', 12, false);
            public       postgres    false    197            �          0    16539    students 
   TABLE DATA               /   COPY students (name, current_mood) FROM stdin;
    public       postgres    false    198   �3       �          0    16657    temp 
   TABLE DATA                  COPY temp (a) FROM stdin;
    public       postgres    false    203   >4       �           0    0    users_id_seq    SEQUENCE SET     4   SELECT pg_catalog.setval('users_id_seq', 3, false);
            public       postgres    false    193                       2606    16399    customers customers_pkey 
   CONSTRAINT     O   ALTER TABLE ONLY customers
    ADD CONSTRAINT customers_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.customers DROP CONSTRAINT customers_pkey;
       public         postgres    false    186    186                       2606    16404    items items_pkey 
   CONSTRAINT     G   ALTER TABLE ONLY items
    ADD CONSTRAINT items_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.items DROP CONSTRAINT items_pkey;
       public         postgres    false    187    187                       2606    16409    purchases purchases_pkey 
   CONSTRAINT     O   ALTER TABLE ONLY purchases
    ADD CONSTRAINT purchases_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.purchases DROP CONSTRAINT purchases_pkey;
       public         postgres    false    188    188            �           2618    16477 "   total_revenue_per_customer _RETURN    RULE     �  CREATE RULE "_RETURN" AS
    ON SELECT TO total_revenue_per_customer DO INSTEAD  SELECT customers.id AS "ID",
    customers.first_name AS "First Name",
    customers.last_name AS "Last Name",
    sum(items.price) AS "Total Price"
   FROM ((customers
     JOIN purchases ON ((customers.id = purchases.customer_id)))
     JOIN items ON ((purchases.item_id = items.id)))
  GROUP BY customers.id;
 :   DROP RULE "_RETURN" ON public.total_revenue_per_customer;
       public       postgres    false    188    186    186    186    187    187    2075    188    189                        2606    16410    purchases fk_customer_purchase    FK CONSTRAINT     w   ALTER TABLE ONLY purchases
    ADD CONSTRAINT fk_customer_purchase FOREIGN KEY (customer_id) REFERENCES customers(id);
 H   ALTER TABLE ONLY public.purchases DROP CONSTRAINT fk_customer_purchase;
       public       postgres    false    2075    186    188            !           2606    16415    purchases fk_purchase_item    FK CONSTRAINT     k   ALTER TABLE ONLY purchases
    ADD CONSTRAINT fk_purchase_item FOREIGN KEY (item_id) REFERENCES items(id);
 D   ALTER TABLE ONLY public.purchases DROP CONSTRAINT fk_purchase_item;
       public       postgres    false    188    187    2077            �   U   x��;
�0���av��)ll����| .�ߙ��=|V���W0�s��TZcr�Flo-�4�|�f�i�,	3�řΎ�~���      �   {   x�%�1�0�W��sC�&B �@����p"+�~l��ݙ=/ߴ���-$4��[�ѯ۲�C��"4�9��;���O3��8�U��-\���v��4���B�Pt"u,���a��`"�SX �      �   8   x����@����/�	z��:��3+Y^�Ҏ-�����ؼY�9��w?���      �   I   x�s���Q��,���H,(��
J���S+J�RsSs* 2^�yR�yPm�i��P��l.���J(�"F��� ��&�      �      x�3�2�2����� �]     