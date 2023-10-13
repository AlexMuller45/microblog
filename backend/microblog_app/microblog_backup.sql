--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0 (Debian 16.0-1.pgdg120+1)
-- Dumped by pg_dump version 16.0 (Debian 16.0-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: developer
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO developer;

--
-- Name: follows_tab; Type: TABLE; Schema: public; Owner: developer
--

CREATE TABLE public.follows_tab (
    user_id integer NOT NULL,
    follow_user_id integer NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.follows_tab OWNER TO developer;

--
-- Name: follows_tab_id_seq; Type: SEQUENCE; Schema: public; Owner: developer
--

CREATE SEQUENCE public.follows_tab_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.follows_tab_id_seq OWNER TO developer;

--
-- Name: follows_tab_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: developer
--

ALTER SEQUENCE public.follows_tab_id_seq OWNED BY public.follows_tab.id;


--
-- Name: likes_tab; Type: TABLE; Schema: public; Owner: developer
--

CREATE TABLE public.likes_tab (
    name character varying NOT NULL,
    user_id integer NOT NULL,
    tweet_id integer NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.likes_tab OWNER TO developer;

--
-- Name: likes_tab_id_seq; Type: SEQUENCE; Schema: public; Owner: developer
--

CREATE SEQUENCE public.likes_tab_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.likes_tab_id_seq OWNER TO developer;

--
-- Name: likes_tab_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: developer
--

ALTER SEQUENCE public.likes_tab_id_seq OWNED BY public.likes_tab.id;


--
-- Name: medias_tab; Type: TABLE; Schema: public; Owner: developer
--

CREATE TABLE public.medias_tab (
    filename character varying NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.medias_tab OWNER TO developer;

--
-- Name: medias_tab_id_seq; Type: SEQUENCE; Schema: public; Owner: developer
--

CREATE SEQUENCE public.medias_tab_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.medias_tab_id_seq OWNER TO developer;

--
-- Name: medias_tab_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: developer
--

ALTER SEQUENCE public.medias_tab_id_seq OWNED BY public.medias_tab.id;


--
-- Name: tweets_tab; Type: TABLE; Schema: public; Owner: developer
--

CREATE TABLE public.tweets_tab (
    content character varying NOT NULL,
    author_id integer NOT NULL,
    attachments character varying[],
    views integer NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.tweets_tab OWNER TO developer;

--
-- Name: tweets_tab_id_seq; Type: SEQUENCE; Schema: public; Owner: developer
--

CREATE SEQUENCE public.tweets_tab_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.tweets_tab_id_seq OWNER TO developer;

--
-- Name: tweets_tab_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: developer
--

ALTER SEQUENCE public.tweets_tab_id_seq OWNED BY public.tweets_tab.id;


--
-- Name: users_tab; Type: TABLE; Schema: public; Owner: developer
--

CREATE TABLE public.users_tab (
    name character varying NOT NULL,
    api_key character varying NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.users_tab OWNER TO developer;

--
-- Name: users_tab_id_seq; Type: SEQUENCE; Schema: public; Owner: developer
--

CREATE SEQUENCE public.users_tab_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_tab_id_seq OWNER TO developer;

--
-- Name: users_tab_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: developer
--

ALTER SEQUENCE public.users_tab_id_seq OWNED BY public.users_tab.id;


--
-- Name: follows_tab id; Type: DEFAULT; Schema: public; Owner: developer
--

ALTER TABLE ONLY public.follows_tab ALTER COLUMN id SET DEFAULT nextval('public.follows_tab_id_seq'::regclass);


--
-- Name: likes_tab id; Type: DEFAULT; Schema: public; Owner: developer
--

ALTER TABLE ONLY public.likes_tab ALTER COLUMN id SET DEFAULT nextval('public.likes_tab_id_seq'::regclass);


--
-- Name: medias_tab id; Type: DEFAULT; Schema: public; Owner: developer
--

ALTER TABLE ONLY public.medias_tab ALTER COLUMN id SET DEFAULT nextval('public.medias_tab_id_seq'::regclass);


--
-- Name: tweets_tab id; Type: DEFAULT; Schema: public; Owner: developer
--

ALTER TABLE ONLY public.tweets_tab ALTER COLUMN id SET DEFAULT nextval('public.tweets_tab_id_seq'::regclass);


--
-- Name: users_tab id; Type: DEFAULT; Schema: public; Owner: developer
--

ALTER TABLE ONLY public.users_tab ALTER COLUMN id SET DEFAULT nextval('public.users_tab_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: developer
--

COPY public.alembic_version (version_num) FROM stdin;
e613593a1487
\.


--
-- Data for Name: follows_tab; Type: TABLE DATA; Schema: public; Owner: developer
--

COPY public.follows_tab (user_id, follow_user_id, id) FROM stdin;
1	2	1
2	1	2
1	6	3
1	4	10
1	5	11
1	8	12
1	1	14
\.


--
-- Data for Name: likes_tab; Type: TABLE DATA; Schema: public; Owner: developer
--

COPY public.likes_tab (name, user_id, tweet_id, id) FROM stdin;
test1	1	11	1
test1	1	12	3
test1	1	13	4
test1	1	10	5
\.


--
-- Data for Name: medias_tab; Type: TABLE DATA; Schema: public; Owner: developer
--

COPY public.medias_tab (filename, id) FROM stdin;
2023-07-01 00.57.19.jpg	4
2023-07-01 00.57.19.jpg	5
2023-07-01 00.57.19.jpg	6
GitLab_issue.png	7
nginx-1142x650-1.png	8
fb0194a52f41abe20e0ff0af29sj--kukly-i-igrushki-vyazanaya-pchelka.jpg	9
4__2023-07-01 00.57.19.jpg	10
fb0194a52f41abe20e0ff0af29sj--kukly-i-igrushki-vyazanaya-pchelka.jpg	11
enhance_the_glow_of_elements_on_clothes_add_glowing_neon_elements_to_clothes_208592592.jpg	12
\.


--
-- Data for Name: tweets_tab; Type: TABLE DATA; Schema: public; Owner: developer
--

COPY public.tweets_tab (content, author_id, attachments, views, id) FROM stdin;
"🚀 GoLang: Where simplicity meets performance! 🐹✨ #GoLang #Programming #PerformanceMatters" #GoLang	1	\N	90	21
23	1	\N	51	23
fb	1	\N	12	24
sdfsdf	1	{"/api/medias/10__4__2023-07-01 00.57.19.jpg"}	5	25
"Привет! Я YouBot - твой личный помощник в написании. Я всегда готов вдохнуть жизнь в твои идеи и помочь тебе достичь творческих высот. Давай вместе создадим нечто удивительное! #YouBot #помощник #творчество"	1	{/api/medias/12__enhance_the_glow_of_elements_on_clothes_add_glowing_neon_elements_to_clothes_208592592.jpg}	2	27
werg b etertgrb gbdfgbtrbr rtbrn rgn gnrn fgbnrtnb fg rtb gf rtnfg gndfgn	1	{"/api/medias/5__2023-07-01 00.57.19.jpg"}	95	4
Привет, фитнес-любители! ️‍️️‍️ Сегодня я бы хотел поговорить о том, как искусственный интеллект и информационные технологии преобразуют нашу тренировку и помогают достичь желаемых результатов 	2	{"/api/medias/4__2023-07-01 00.57.19.jpg"}	92	10
sdgafgheh	1	{"/api/medias/5__2023-07-01 00.57.19.jpg","/api/medias/6__2023-07-01 00.57.19.jpg",/api/medias/7__GitLab_issue.png}	95	20
fgnfgj	1	{/api/medias/11__fb0194a52f41abe20e0ff0af29sj--kukly-i-igrushki-vyazanaya-pchelka.jpg}	4	26
Самое замечательное в современной эпохе  это то, что ИИ и ИТ предлагают нам невероятные возможности для фитнеса. Возможности, которые ранее казались недостижимыми. Теперь мы можем использовать специальные сенсоры и умные трекеры, чтобы отслеживать нашу активность и прогресс. Это помогает нам быть более осознанными в тренировках и контролировать свое здоровье. ️	5	\N	92	11
"🚀 NGINX: The web server that powers the internet's speed and reliability! 🌐💨 #NGINX #WebHosting #Performance"	1	{/api/medias/7__GitLab_issue.png}	85	22
Когда-то нам приходилось полагаться только на наши ощущения и субъективные представления о тренировке. Но теперь у нас есть ИИ-ассистенты, которые помогают нам оптимизировать тренировочные программы. Они анализируют нашу активность, питание и даже сон, чтобы предложить нам наиболее эффективный подход. 	6	\N	92	12
Get ready to dive into the world of Python!	1	\N	95	13
\.


--
-- Data for Name: users_tab; Type: TABLE DATA; Schema: public; Owner: developer
--

COPY public.users_tab (name, api_key, id) FROM stdin;
test1	test	1
test2	test2	2
rodrick.kuvalis	aHqySekG7A	3
chester.conroy	FsCTM68vxl	4
fidel.carter	UFq4LkJyi9	5
claude.rice	B0SAKJzi1j	6
leilani.kemmer	BAoCdh7E64	7
joan.leannon	IoQU4AZC0p	8
richie.walker	x46nEG5R2e	9
jong.gusikowski	9TSVYJZjFG	10
stanley.maggio	Ja2tVZby5i	11
stan.upton	RcSF85B94O	12
\.


--
-- Name: follows_tab_id_seq; Type: SEQUENCE SET; Schema: public; Owner: developer
--

SELECT pg_catalog.setval('public.follows_tab_id_seq', 14, true);


--
-- Name: likes_tab_id_seq; Type: SEQUENCE SET; Schema: public; Owner: developer
--

SELECT pg_catalog.setval('public.likes_tab_id_seq', 5, true);


--
-- Name: medias_tab_id_seq; Type: SEQUENCE SET; Schema: public; Owner: developer
--

SELECT pg_catalog.setval('public.medias_tab_id_seq', 12, true);


--
-- Name: tweets_tab_id_seq; Type: SEQUENCE SET; Schema: public; Owner: developer
--

SELECT pg_catalog.setval('public.tweets_tab_id_seq', 27, true);


--
-- Name: users_tab_id_seq; Type: SEQUENCE SET; Schema: public; Owner: developer
--

SELECT pg_catalog.setval('public.users_tab_id_seq', 12, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: developer
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: follows_tab follows_tab_pkey; Type: CONSTRAINT; Schema: public; Owner: developer
--

ALTER TABLE ONLY public.follows_tab
    ADD CONSTRAINT follows_tab_pkey PRIMARY KEY (id);


--
-- Name: follows_tab follows_tab_user_id_follow_user_id_key; Type: CONSTRAINT; Schema: public; Owner: developer
--

ALTER TABLE ONLY public.follows_tab
    ADD CONSTRAINT follows_tab_user_id_follow_user_id_key UNIQUE (user_id, follow_user_id);


--
-- Name: likes_tab likes_tab_pkey; Type: CONSTRAINT; Schema: public; Owner: developer
--

ALTER TABLE ONLY public.likes_tab
    ADD CONSTRAINT likes_tab_pkey PRIMARY KEY (id);


--
-- Name: medias_tab medias_tab_pkey; Type: CONSTRAINT; Schema: public; Owner: developer
--

ALTER TABLE ONLY public.medias_tab
    ADD CONSTRAINT medias_tab_pkey PRIMARY KEY (id);


--
-- Name: tweets_tab tweets_tab_pkey; Type: CONSTRAINT; Schema: public; Owner: developer
--

ALTER TABLE ONLY public.tweets_tab
    ADD CONSTRAINT tweets_tab_pkey PRIMARY KEY (id);


--
-- Name: users_tab users_tab_api_key_key; Type: CONSTRAINT; Schema: public; Owner: developer
--

ALTER TABLE ONLY public.users_tab
    ADD CONSTRAINT users_tab_api_key_key UNIQUE (api_key);


--
-- Name: users_tab users_tab_pkey; Type: CONSTRAINT; Schema: public; Owner: developer
--

ALTER TABLE ONLY public.users_tab
    ADD CONSTRAINT users_tab_pkey PRIMARY KEY (id);


--
-- Name: follows_tab follows_tab_follow_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: developer
--

ALTER TABLE ONLY public.follows_tab
    ADD CONSTRAINT follows_tab_follow_user_id_fkey FOREIGN KEY (follow_user_id) REFERENCES public.users_tab(id);


--
-- Name: follows_tab follows_tab_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: developer
--

ALTER TABLE ONLY public.follows_tab
    ADD CONSTRAINT follows_tab_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users_tab(id);


--
-- Name: likes_tab likes_tab_tweet_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: developer
--

ALTER TABLE ONLY public.likes_tab
    ADD CONSTRAINT likes_tab_tweet_id_fkey FOREIGN KEY (tweet_id) REFERENCES public.tweets_tab(id);


--
-- Name: likes_tab likes_tab_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: developer
--

ALTER TABLE ONLY public.likes_tab
    ADD CONSTRAINT likes_tab_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users_tab(id);


--
-- Name: tweets_tab tweets_tab_author_fkey; Type: FK CONSTRAINT; Schema: public; Owner: developer
--

ALTER TABLE ONLY public.tweets_tab
    ADD CONSTRAINT tweets_tab_author_fkey FOREIGN KEY (author_id) REFERENCES public.users_tab(id);


--
-- PostgreSQL database dump complete
--

