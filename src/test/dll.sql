--
-- PostgreSQL database dump
--

-- Dumped from database version: 13.4
-- Dumped by pg_dump version: 13.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: example_table; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.example_table (
    id integer NOT NULL,
    name character varying(100),
    age integer
);

ALTER TABLE public.example_table OWNER TO postgres;

--
-- Data for Name: example_table; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.example_table (id, name, age) FROM stdin;
1   John    30
2   Alice   25
3   Bob     35
\.

--
-- Name: example_sequence; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.example_sequence
    INCREMENT 1
    MINVALUE 1
    MAXVALUE 1000
    START 1
    CACHE 1;

ALTER TABLE public.example_sequence OWNER TO postgres;

--
-- Name: example_table_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.example_sequence OWNED BY public.example_table.id;

--
-- PostgreSQL database dump complete
--
