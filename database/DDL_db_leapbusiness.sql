
-- Database: db_leap_business
-- Author: OscarL
CREATE DATABASE db_leap_business
    WITH OWNER = postgres
        ENCODING = 'UTF8'
        TABLESPACE = pg_default
        CONNECTION LIMIT = -1;

CREATE TABLE public.videogames (
    appid numeric(10,0) NOT NULL,
    description varchar(500),
    total_recommendations numeric(8,0),
    required_age varchar(30),
    is_free boolean,
    followers numeric(10,0),
    url_metacritic varchar(300),
    release_date date,
    minor_price numeric(10,2),
    upper_price numeric(10,2),
    user_score numeric(2,1),
    metascore numeric(2,0),
    total_sales numeric(12,2),
    update_date timestamp with time zone,
    PRIMARY KEY (appid)
);


CREATE TABLE public.prices (
    appid numeric(10,0) NOT NULL,
    date_point date NOT NULL,
    price numeric(10,2),
    PRIMARY KEY (appid, date_point)
);


CREATE TABLE public.recommendations (
    id_recommendation numeric(5,0) NOT NULL,
    appid numeric(10,0) NOT NULL,
    total numeric(8,0),
    PRIMARY KEY (id_recommendation, appid)
);


CREATE TABLE public.recommendation (
    id_recommendation numeric(5,0) NOT NULL,
    description varchar(500),
    PRIMARY KEY (id_recommendation)
);


CREATE TABLE public.generes_user (
    id_genere_user numeric(5,0) NOT NULL,
    appid numeric(10,0) NOT NULL,
    PRIMARY KEY (id_genere_user, appid)
);


CREATE TABLE public.genere_user (
    id_genere_user numeric(5,0) NOT NULL,
    description varchar(500),
    PRIMARY KEY (id_genere_user)
);


CREATE TABLE public.platforms (
    appid numeric(10,0) NOT NULL,
    id_platform numeric(5,0) NOT NULL,
    PRIMARY KEY (appid, id_platform)
);


CREATE TABLE public.platform (
    id_platform numeric(5,0) NOT NULL,
    description varchar(500),
    PRIMARY KEY (id_platform)
);


CREATE TABLE public.languages (
    id_language numeric(5,0) NOT NULL,
    appid numeric(10,0) NOT NULL,
    PRIMARY KEY (id_language, appid)
);


CREATE TABLE public.game_language (
    id_language numeric(5,0) NOT NULL,
    description varchar(500),
    PRIMARY KEY (id_language)
);


CREATE TABLE public.generes (
    id_genere numeric(5,0) NOT NULL,
    appid numeric(10,0) NOT NULL,
    PRIMARY KEY (id_genere, appid)
);


CREATE TABLE public.genere (
    id_genere numeric(5,0) NOT NULL,
    description varchar(500),
    PRIMARY KEY (id_genere)
);


CREATE TABLE public.category (
    id_category numeric(5,0) NOT NULL,
    description varchar(500),
    PRIMARY KEY (id_category)
);


CREATE TABLE public.categories (
    id_category numeric(5,0) NOT NULL,
    appid numeric(10,0) NOT NULL,
    PRIMARY KEY (id_category, appid)
);


CREATE TABLE public.tags (
    id_tag numeric(5,0) NOT NULL,
    appid numeric(10,0) NOT NULL,
    PRIMARY KEY (id_tag, appid)
);


CREATE TABLE public.tag (
    id_tag numeric(5,0) NOT NULL,
    descripton varchar(500),
    PRIMARY KEY (id_tag)
);


CREATE TABLE public.current_players (
    appid numeric(10,0) NOT NULL,
    date_point date NOT NULL,
    avg_players numeric(10,0),
    peak_players numeric(10,0),
    PRIMARY KEY (appid, date_point)
);


CREATE TABLE public.publishers (
    id_publisher numeric(5,0) NOT NULL,
    appid numeric(10,0) NOT NULL,
    PRIMARY KEY (id_publisher, appid)
);


CREATE TABLE public.publisher (
    id_publisher numeric(5,0) NOT NULL,
    description varchar(500),
    PRIMARY KEY (id_publisher)
);


ALTER TABLE public.prices ADD CONSTRAINT FK_prices__appid FOREIGN KEY (appid) REFERENCES public.videogames(appid);
ALTER TABLE public.recommendations ADD CONSTRAINT FK_recommendations__id_recommendation FOREIGN KEY (id_recommendation) REFERENCES public.recommendation(id_recommendation);
ALTER TABLE public.recommendations ADD CONSTRAINT FK_recommendations__appid FOREIGN KEY (appid) REFERENCES public.videogames(appid);
ALTER TABLE public.generes_user ADD CONSTRAINT FK_generes_user__id_genere_user FOREIGN KEY (id_genere_user) REFERENCES public.genere_user(id_genere_user);
ALTER TABLE public.generes_user ADD CONSTRAINT FK_generes_user__appid FOREIGN KEY (appid) REFERENCES public.videogames(appid);
ALTER TABLE public.platforms ADD CONSTRAINT FK_platforms__appid FOREIGN KEY (appid) REFERENCES public.videogames(appid);
ALTER TABLE public.platforms ADD CONSTRAINT FK_platforms__id_platform FOREIGN KEY (id_platform) REFERENCES public.platform(id_platform);
ALTER TABLE public.languages ADD CONSTRAINT FK_languages__id_language FOREIGN KEY (id_language) REFERENCES public.game_language(id_language);
ALTER TABLE public.languages ADD CONSTRAINT FK_languages__appid FOREIGN KEY (appid) REFERENCES public.videogames(appid);
ALTER TABLE public.generes ADD CONSTRAINT FK_generes__id_genere FOREIGN KEY (id_genere) REFERENCES public.genere(id_genere);
ALTER TABLE public.generes ADD CONSTRAINT FK_generes__appid FOREIGN KEY (appid) REFERENCES public.videogames(appid);
ALTER TABLE public.categories ADD CONSTRAINT FK_categories__id_category FOREIGN KEY (id_category) REFERENCES public.category(id_category);
ALTER TABLE public.categories ADD CONSTRAINT FK_categories__appid FOREIGN KEY (appid) REFERENCES public.videogames(appid);
ALTER TABLE public.tags ADD CONSTRAINT FK_tags__id_tag FOREIGN KEY (id_tag) REFERENCES public.tag(id_tag);
ALTER TABLE public.tags ADD CONSTRAINT FK_tags__appid FOREIGN KEY (appid) REFERENCES public.videogames(appid);
ALTER TABLE public.current_players ADD CONSTRAINT FK_current_players__appid FOREIGN KEY (appid) REFERENCES public.videogames(appid);
ALTER TABLE public.publishers ADD CONSTRAINT FK_publishers__id_publisher FOREIGN KEY (id_publisher) REFERENCES public.publisher(id_publisher);
ALTER TABLE public.publishers ADD CONSTRAINT FK_publishers__appid FOREIGN KEY (appid) REFERENCES public.videogames(appid);