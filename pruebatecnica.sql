PGDMP         (            	    z            prueba_tecnica    15.0    15.0 
    ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                        0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    32769    prueba_tecnica    DATABASE     ?   CREATE DATABASE prueba_tecnica WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Colombia.1252';
    DROP DATABASE prueba_tecnica;
                postgres    false            ?            1259    32776    comentarios    TABLE     e   CREATE TABLE public.comentarios (
    "ID" character(36),
    "Comentario" character varying(300)
);
    DROP TABLE public.comentarios;
       public         heap    postgres    false            ?            1259    32779    noticias    TABLE     ?   CREATE TABLE public.noticias (
    "ID" character(36),
    "Título" character varying(100),
    "Descripción" character varying(200)
);
    DROP TABLE public.noticias;
       public         heap    postgres    false            ?            1259    32770    usuarios    TABLE     ?   CREATE TABLE public.usuarios (
    "Nombre Completo" character varying(100),
    "Correo" character varying(100),
    "Contraseña" character varying(20),
    "Dirección" character varying(100),
    "Teléfono" bigint,
    "Fecha de nacimiento" date
);
    DROP TABLE public.usuarios;
       public         heap    postgres    false            ?          0    32776    comentarios 
   TABLE DATA           9   COPY public.comentarios ("ID", "Comentario") FROM stdin;
    public          postgres    false    215   ?	       ?          0    32779    noticias 
   TABLE DATA           C   COPY public.noticias ("ID", "Título", "Descripción") FROM stdin;
    public          postgres    false    216   ?
       ?          0    32770    usuarios 
   TABLE DATA           ?   COPY public.usuarios ("Nombre Completo", "Correo", "Contraseña", "Dirección", "Teléfono", "Fecha de nacimiento") FROM stdin;
    public          postgres    false    214   g       ?   ?   x??A? @?u9???ҖNY?w???0$$??&=?G?b??O?7?p?NK???SV?ЏIۮ3?s????൱?~`?vX(???\=?,g],?W?#Zb?$p?'?$???%i|@???B?i6???mb?	r?g???b????׳x???'X5H      ?   ?   x?=?1n?0Eg???
;??? Y?ݲPU?P???
???:??Xe?D???}^?????5?zg?#Pj?`?? w?4\?'X?S?95??Q????>%?n?҆?QjT????;??:&7m??~??????#3?J<S????E??U??'I.4??(?Z??!?l??D>Gd?z?4#x^?e?n+u?Q7n?????VxcL???I?O?^?      ?   ?   x?M?M?0???)? ??Jw&Dn?????Cqõ<?d?f??|?????1???@\&،?{?+qj=?.?G?PH%P[??*?
?UB?AC1???u?y?LKsȳ?
ͤ?&?D^???THq?????????谻????f???L*m???֘?D?D~K9?_bn?     