PGDMP  -                    |         	   PFCSystem    16.2    16.2     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    33172 	   PFCSystem    DATABASE     �   CREATE DATABASE "PFCSystem" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Philippines.1252';
    DROP DATABASE "PFCSystem";
                postgres    false            �            1259    33179    employee    TABLE     4  CREATE TABLE public.employee (
    emp_id integer NOT NULL,
    emp_name character varying(100) NOT NULL,
    emp_address character varying(100) NOT NULL,
    emp_birthdate date DEFAULT CURRENT_TIMESTAMP,
    emp_contact_num character varying(20) NOT NULL,
    emp_position character varying(30) NOT NULL
);
    DROP TABLE public.employee;
       public         heap    postgres    false            �            1259    33185    members    TABLE       CREATE TABLE public.members (
    mem_id integer NOT NULL,
    mem_name character varying(100) NOT NULL,
    mem_birthdate date DEFAULT CURRENT_TIMESTAMP,
    mem_address character varying(100) NOT NULL,
    mem_telephone character varying(20) NOT NULL,
    mem_physical_act character varying(100) DEFAULT 'N/A'::character varying,
    mem_med_ailment character varying(100) DEFAULT 'N/A'::character varying,
    mem_weight numeric NOT NULL,
    mem_height numeric NOT NULL,
    mem_bp character varying(35) NOT NULL,
    mem_gender character varying(20) NOT NULL,
    mem_status character varying(35) NOT NULL,
    mem_type character varying(35) NOT NULL,
    mem_prev_gym character varying(50) DEFAULT 'N/A'::character varying,
    serv_id integer NOT NULL,
    emp_id integer
);
    DROP TABLE public.members;
       public         heap    postgres    false            �            1259    33222 
   membership    TABLE     ^   CREATE TABLE public.membership (
    mem_id integer NOT NULL,
    serv_id integer NOT NULL
);
    DROP TABLE public.membership;
       public         heap    postgres    false            �            1259    33173    service    TABLE     �   CREATE TABLE public.service (
    serv_id integer NOT NULL,
    serv_type character varying(35) NOT NULL,
    serv_price numeric(9,2) DEFAULT 0.0
);
    DROP TABLE public.service;
       public         heap    postgres    false            �            1259    33206    transaction_history    TABLE     )  CREATE TABLE public.transaction_history (
    tran_id integer NOT NULL,
    mem_id integer NOT NULL,
    tran_date date DEFAULT CURRENT_TIMESTAMP,
    serv_id integer NOT NULL,
    tran_price numeric(9,2) NOT NULL,
    tran_tendered numeric(9,2) NOT NULL,
    tran_change numeric(9,2) NOT NULL
);
 '   DROP TABLE public.transaction_history;
       public         heap    postgres    false            �          0    33179    employee 
   TABLE DATA           o   COPY public.employee (emp_id, emp_name, emp_address, emp_birthdate, emp_contact_num, emp_position) FROM stdin;
    public          postgres    false    216   �"       �          0    33185    members 
   TABLE DATA           �   COPY public.members (mem_id, mem_name, mem_birthdate, mem_address, mem_telephone, mem_physical_act, mem_med_ailment, mem_weight, mem_height, mem_bp, mem_gender, mem_status, mem_type, mem_prev_gym, serv_id, emp_id) FROM stdin;
    public          postgres    false    217   �"       �          0    33222 
   membership 
   TABLE DATA           5   COPY public.membership (mem_id, serv_id) FROM stdin;
    public          postgres    false    219   �"       �          0    33173    service 
   TABLE DATA           A   COPY public.service (serv_id, serv_type, serv_price) FROM stdin;
    public          postgres    false    215   #       �          0    33206    transaction_history 
   TABLE DATA           z   COPY public.transaction_history (tran_id, mem_id, tran_date, serv_id, tran_price, tran_tendered, tran_change) FROM stdin;
    public          postgres    false    218   9#       #           2606    33184    employee employee_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_pkey PRIMARY KEY (emp_id);
 @   ALTER TABLE ONLY public.employee DROP CONSTRAINT employee_pkey;
       public            postgres    false    216            %           2606    33195    members members_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.members
    ADD CONSTRAINT members_pkey PRIMARY KEY (mem_id);
 >   ALTER TABLE ONLY public.members DROP CONSTRAINT members_pkey;
       public            postgres    false    217            )           2606    33226    membership membership_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.membership
    ADD CONSTRAINT membership_pkey PRIMARY KEY (mem_id, serv_id);
 D   ALTER TABLE ONLY public.membership DROP CONSTRAINT membership_pkey;
       public            postgres    false    219    219            !           2606    33178    service service_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.service
    ADD CONSTRAINT service_pkey PRIMARY KEY (serv_id);
 >   ALTER TABLE ONLY public.service DROP CONSTRAINT service_pkey;
       public            postgres    false    215            '           2606    33211 ,   transaction_history transaction_history_pkey 
   CONSTRAINT     o   ALTER TABLE ONLY public.transaction_history
    ADD CONSTRAINT transaction_history_pkey PRIMARY KEY (tran_id);
 V   ALTER TABLE ONLY public.transaction_history DROP CONSTRAINT transaction_history_pkey;
       public            postgres    false    218            *           2606    33201    members members_emp_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.members
    ADD CONSTRAINT members_emp_id_fkey FOREIGN KEY (emp_id) REFERENCES public.employee(emp_id) ON UPDATE CASCADE ON DELETE CASCADE;
 E   ALTER TABLE ONLY public.members DROP CONSTRAINT members_emp_id_fkey;
       public          postgres    false    216    4643    217            +           2606    33196    members members_serv_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.members
    ADD CONSTRAINT members_serv_id_fkey FOREIGN KEY (serv_id) REFERENCES public.service(serv_id) ON UPDATE CASCADE ON DELETE CASCADE;
 F   ALTER TABLE ONLY public.members DROP CONSTRAINT members_serv_id_fkey;
       public          postgres    false    4641    217    215            .           2606    33227 !   membership membership_mem_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.membership
    ADD CONSTRAINT membership_mem_id_fkey FOREIGN KEY (mem_id) REFERENCES public.members(mem_id) ON UPDATE CASCADE ON DELETE CASCADE;
 K   ALTER TABLE ONLY public.membership DROP CONSTRAINT membership_mem_id_fkey;
       public          postgres    false    4645    219    217            /           2606    33232 "   membership membership_serv_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.membership
    ADD CONSTRAINT membership_serv_id_fkey FOREIGN KEY (serv_id) REFERENCES public.service(serv_id) ON UPDATE CASCADE ON DELETE CASCADE;
 L   ALTER TABLE ONLY public.membership DROP CONSTRAINT membership_serv_id_fkey;
       public          postgres    false    4641    215    219            ,           2606    33212 3   transaction_history transaction_history_mem_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.transaction_history
    ADD CONSTRAINT transaction_history_mem_id_fkey FOREIGN KEY (mem_id) REFERENCES public.members(mem_id) ON UPDATE CASCADE ON DELETE CASCADE;
 ]   ALTER TABLE ONLY public.transaction_history DROP CONSTRAINT transaction_history_mem_id_fkey;
       public          postgres    false    217    218    4645            -           2606    33217 4   transaction_history transaction_history_serv_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.transaction_history
    ADD CONSTRAINT transaction_history_serv_id_fkey FOREIGN KEY (serv_id) REFERENCES public.service(serv_id) ON UPDATE CASCADE ON DELETE CASCADE;
 ^   ALTER TABLE ONLY public.transaction_history DROP CONSTRAINT transaction_history_serv_id_fkey;
       public          postgres    false    215    4641    218            �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �     