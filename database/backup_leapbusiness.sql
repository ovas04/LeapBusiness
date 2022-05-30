--
-- PostgreSQL database dump
--

-- Dumped from database version 13.4
-- Dumped by pg_dump version 13.4

-- Started on 2022-05-29 20:29:35

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

--
-- TOC entry 3 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO postgres;

--
-- TOC entry 3193 (class 0 OID 0)
-- Dependencies: 3
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


--
-- TOC entry 244 (class 1255 OID 19934)
-- Name: f_validate_category(numeric, character varying); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.f_validate_category(p_code numeric, p_description character varying) RETURNS numeric
    LANGUAGE plpgsql
    AS $$
DECLARE  
	v_code numeric; 
BEGIN  
	
	if((SELECT count(id_category) FROM public.category 
	WHERE id_category = p_code) = 0) then 
		insert into public.category values(p_code,p_description);
	end if;

	select id_category into v_code
	from public.category 
	WHERE id_category = p_code;

	return v_code;
END;
$$;


ALTER FUNCTION public.f_validate_category(p_code numeric, p_description character varying) OWNER TO postgres;

--
-- TOC entry 229 (class 1255 OID 19935)
-- Name: f_validate_game_language(character varying); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.f_validate_game_language(p_description character varying) RETURNS numeric
    LANGUAGE plpgsql
    AS $$
DECLARE  
	v_code numeric; 
BEGIN  
	
	if((SELECT count(description) FROM public.game_language 
	WHERE p_description = description) = 0) then 
		insert into public.game_language(description) values(p_description);
	end if;


	select id_language into v_code
	from public.game_language 
	WHERE p_description = description;

	return v_code;

end;
$$;


ALTER FUNCTION public.f_validate_game_language(p_description character varying) OWNER TO postgres;

--
-- TOC entry 230 (class 1255 OID 19936)
-- Name: f_validate_genre(numeric, character varying); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.f_validate_genre(p_code numeric, p_description character varying) RETURNS numeric
    LANGUAGE plpgsql
    AS $$
DECLARE  
	v_code numeric; 
BEGIN  
	
	if((SELECT count(id_genre) FROM public.genre g 
	WHERE id_genre = p_code) = 0) then 
		insert into public.genre values(p_code,p_description);
	end if;

	select id_genre into v_code
	from public.genre 
	WHERE id_genre = p_code;

	return v_code;


END;
$$;


ALTER FUNCTION public.f_validate_genre(p_code numeric, p_description character varying) OWNER TO postgres;

--
-- TOC entry 231 (class 1255 OID 19937)
-- Name: f_validate_genre_user(character varying); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.f_validate_genre_user(p_description character varying) RETURNS numeric
    LANGUAGE plpgsql
    AS $$
DECLARE  
	v_code numeric;
BEGIN  
	
	if((SELECT count(description) FROM public.genre_user 
	WHERE p_description = description) = 0) then 
		insert into public.genre_user(description) values(p_description);
	end if;

	select id_genre_user into v_code
	from public.genre_user 
	WHERE p_description = description;

	return v_code;


end;
$$;


ALTER FUNCTION public.f_validate_genre_user(p_description character varying) OWNER TO postgres;

--
-- TOC entry 232 (class 1255 OID 19938)
-- Name: f_validate_platforms(character varying); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.f_validate_platforms(p_description character varying) RETURNS numeric
    LANGUAGE plpgsql
    AS $$
DECLARE  
	v_code numeric;
BEGIN  
	
	if((SELECT count(description) FROM public.platform 
	WHERE p_description = description) = 0) then 
		insert into public.platform(description) values(p_description);
	end if;

	select id_platform into v_code
	from public.platform 
	WHERE p_description = description;

	return v_code;

end;
$$;


ALTER FUNCTION public.f_validate_platforms(p_description character varying) OWNER TO postgres;

--
-- TOC entry 245 (class 1255 OID 19939)
-- Name: f_validate_publisher(character varying); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.f_validate_publisher(p_description character varying) RETURNS numeric
    LANGUAGE plpgsql
    AS $$
DECLARE  
	v_code numeric;
BEGIN  
	
	if((SELECT count(description) FROM public.publisher 
	WHERE p_description = description) = 0) then 
		insert into public.publisher(description) values(p_description);
	end if;

	select id_publisher into v_code
	from public.publisher 
	WHERE p_description = description;

	return v_code;

end;
$$;


ALTER FUNCTION public.f_validate_publisher(p_description character varying) OWNER TO postgres;

--
-- TOC entry 246 (class 1255 OID 19940)
-- Name: f_validate_recommendation(character varying); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.f_validate_recommendation(p_description character varying) RETURNS numeric
    LANGUAGE plpgsql
    AS $$
DECLARE  
	v_code numeric;
BEGIN  
	
	if((SELECT count(description) FROM public.recommendation 
	WHERE p_description = description) = 0) then 
		insert into public.recommendation(description) values(p_description);
	end if;

	select id_recommendation into v_code
	from public.recommendation 
	WHERE p_description = description;

	return v_code;


end;
$$;


ALTER FUNCTION public.f_validate_recommendation(p_description character varying) OWNER TO postgres;

--
-- TOC entry 247 (class 1255 OID 19941)
-- Name: f_validate_tag(numeric, character varying); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.f_validate_tag(p_code numeric, p_description character varying) RETURNS numeric
    LANGUAGE plpgsql
    AS $$
DECLARE  
	v_code numeric;
BEGIN  
	
	if((SELECT count(id_tag) FROM tag
	WHERE id_tag = p_code) = 0) then 
		insert into tag values(p_code,p_description);
	end if;

	select id_tag into v_code
	from public.tag 
	WHERE id_tag = p_code;

	return v_code;

end;
$$;


ALTER FUNCTION public.f_validate_tag(p_code numeric, p_description character varying) OWNER TO postgres;

--
-- TOC entry 249 (class 1255 OID 19944)
-- Name: sp_register_categories(numeric, numeric, character varying); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.sp_register_categories(p_appid numeric, p_id_category numeric, p_description character varying)
    LANGUAGE plpgsql
    AS $$
DECLARE  
	v_id numeric;
BEGIN  
	
	select public.f_validate_category(p_id_category,p_description) into v_id;
	
	insert into tags values (v_id, p_appid);

END
$$;


ALTER PROCEDURE public.sp_register_categories(p_appid numeric, p_id_category numeric, p_description character varying) OWNER TO postgres;

--
-- TOC entry 258 (class 1255 OID 19953)
-- Name: sp_register_current_players(numeric, date, numeric, numeric); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.sp_register_current_players(p_appid numeric, p_date_point date, p_avg_players numeric, p_peak_players numeric)
    LANGUAGE plpgsql
    AS $$
DECLARE  
	v_id numeric;
BEGIN  
	
	if((select count(p_appid) from public.current_players cp 
		where date_point = p_date_point and appid = p_appid ) = 0 ) then 
		insert into current_players values (p_appid, p_date_point, p_avg_players, p_peak_players);
	else 
		update public.current_players
			set avg_players = p_avg_players,
				peak_players = p_peak_players
			where date_point = p_date_point and appid = p_appid;
	end if;

END
$$;


ALTER PROCEDURE public.sp_register_current_players(p_appid numeric, p_date_point date, p_avg_players numeric, p_peak_players numeric) OWNER TO postgres;

--
-- TOC entry 250 (class 1255 OID 19945)
-- Name: sp_register_game_language(numeric, character varying); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.sp_register_game_language(p_appid numeric, p_description character varying)
    LANGUAGE plpgsql
    AS $$
DECLARE  
	v_id numeric;
BEGIN  
	
	select public.f_validate_category(p_description) into v_id;
	
	insert into languages values (v_id, p_appid);

END
$$;


ALTER PROCEDURE public.sp_register_game_language(p_appid numeric, p_description character varying) OWNER TO postgres;

--
-- TOC entry 251 (class 1255 OID 19946)
-- Name: sp_register_genre(numeric, numeric, character varying); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.sp_register_genre(p_appid numeric, p_id_genre numeric, p_description character varying)
    LANGUAGE plpgsql
    AS $$
DECLARE  
	v_id numeric;
BEGIN  
	
	select public.f_validate_genre(p_id_genre,p_description) into v_id;
	
	insert into genres values (v_id, p_appid);

END
$$;


ALTER PROCEDURE public.sp_register_genre(p_appid numeric, p_id_genre numeric, p_description character varying) OWNER TO postgres;

--
-- TOC entry 252 (class 1255 OID 19947)
-- Name: sp_register_genre_user(numeric, character varying); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.sp_register_genre_user(p_appid numeric, p_description character varying)
    LANGUAGE plpgsql
    AS $$
DECLARE  
	v_id numeric;
BEGIN  
	
	select public.f_validate_genre_user(p_description) into v_id;
	
	insert into genres_user values (v_id, p_appid);

END
$$;


ALTER PROCEDURE public.sp_register_genre_user(p_appid numeric, p_description character varying) OWNER TO postgres;

--
-- TOC entry 253 (class 1255 OID 19948)
-- Name: sp_register_platforms(numeric, character varying); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.sp_register_platforms(p_appid numeric, p_description character varying)
    LANGUAGE plpgsql
    AS $$
DECLARE  
	v_id numeric;
BEGIN  
	
	select public.f_validate_platforms(p_description) into v_id;
	
	insert into platforms values (p_appid, v_id);

END
$$;


ALTER PROCEDURE public.sp_register_platforms(p_appid numeric, p_description character varying) OWNER TO postgres;

--
-- TOC entry 257 (class 1255 OID 19952)
-- Name: sp_register_prices(numeric, date, numeric); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.sp_register_prices(p_appid numeric, p_date_point date, p_price numeric)
    LANGUAGE plpgsql
    AS $$
DECLARE  
	v_id numeric;
BEGIN  
	
	if((select count(p_appid) from public.prices p 
		where date_point = p_date_point and appid = p_appid ) = 0 ) then 
		insert into prices values (p_appid, p_date_point, p_price);
	else 
		update public.prices
			set price = p_price
			where date_point = p_date_point and appid = p_appid;
	end if;

END
$$;


ALTER PROCEDURE public.sp_register_prices(p_appid numeric, p_date_point date, p_price numeric) OWNER TO postgres;

--
-- TOC entry 254 (class 1255 OID 19949)
-- Name: sp_register_publishers(numeric, character varying); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.sp_register_publishers(p_appid numeric, p_description character varying)
    LANGUAGE plpgsql
    AS $$
DECLARE  
	v_id numeric;
BEGIN  
	
	select public.f_validate_publisher(p_description) into v_id;
	
	insert into publishers values (v_id, p_appi);

END
$$;


ALTER PROCEDURE public.sp_register_publishers(p_appid numeric, p_description character varying) OWNER TO postgres;

--
-- TOC entry 256 (class 1255 OID 19950)
-- Name: sp_register_recomendations(numeric, character varying, numeric); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.sp_register_recomendations(p_appid numeric, p_description character varying, p_total numeric)
    LANGUAGE plpgsql
    AS $$
DECLARE  
	v_id numeric;
BEGIN  
	
	select public.f_validate_recommendation(p_description) into v_id;
	
	if((select count(id_recommendation) from public.recommendations
		where id_recommendation = v_id and appid = p_appid ) = 0 ) then 
		insert into recommendations values (v_id, p_appi, total);
	else 
		update public.recommendations
			set total = p_total
			where id_recommendation = v_id and appid = p_appid;
	end if;
END
$$;


ALTER PROCEDURE public.sp_register_recomendations(p_appid numeric, p_description character varying, p_total numeric) OWNER TO postgres;

--
-- TOC entry 255 (class 1255 OID 19943)
-- Name: sp_register_tags(numeric, numeric, character varying); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.sp_register_tags(p_appid numeric, p_id_tag numeric, p_description character varying)
    LANGUAGE plpgsql
    AS $$
DECLARE  
	v_id numeric;
BEGIN  
	
	select f_validate_tag(p_id_tag,p_description) into v_id;
	
	insert into tags values (v_id, p_appid);

END
$$;


ALTER PROCEDURE public.sp_register_tags(p_appid numeric, p_id_tag numeric, p_description character varying) OWNER TO postgres;

--
-- TOC entry 248 (class 1255 OID 19942)
-- Name: sp_register_update_videogame(numeric, character varying, numeric, character varying, boolean, numeric, character varying, date, numeric, numeric, numeric, numeric); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.sp_register_update_videogame(p_appid numeric, p_description character varying, p_total_recomendations numeric, p_required_age character varying, p_is_free boolean, p_followers numeric, p_url_metacritic character varying, p_relase_date date, p_minor_price numeric, p_upper_price numeric, p_user_score numeric, p_metascore numeric)
    LANGUAGE plpgsql
    AS $$
DECLARE  
BEGIN  
	
	if((select count(appid) from 
	videogames v where appid = p_appid)=0) then
	insert into videogames (appid,description,total_recommendations,required_age,is_free,followers,url_metacritic, release_date, minor_price,
		upper_price, user_score, metascore, update_date) 
		values (p_appid,
				p_description,
				p_total_recomendations,
				p_required_age,
				p_is_free,
				p_followers,
				p_url_metacritic,
				p_relase_date,
				p_minor_price,
				p_upper_price,
				p_user_score,
				p_metascore,
				now()
				);	
	else
		update videogames 
			set 
			appid = p_appid,
			description = p_description,
			total_recommendations = p_total_recomendations,
			required_age = p_required_age ,
			is_free = p_is_free,
			followers = p_followers,
			url_metacritic = p_url_metacritic, 
			release_date = p_relase_date,
			minor_price = p_minor_price,
			upper_price = p_upper_price,
			user_score = p_user_score,
			metascore = p_metascore,
			update_date = now()
		where appid = p_appid;
	end if;

END
$$;


ALTER PROCEDURE public.sp_register_update_videogame(p_appid numeric, p_description character varying, p_total_recomendations numeric, p_required_age character varying, p_is_free boolean, p_followers numeric, p_url_metacritic character varying, p_relase_date date, p_minor_price numeric, p_upper_price numeric, p_user_score numeric, p_metascore numeric) OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 221 (class 1259 OID 19791)
-- Name: categories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categories (
    id_category numeric(5,0) NOT NULL,
    appid numeric(10,0) NOT NULL
);


ALTER TABLE public.categories OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 19783)
-- Name: category; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.category (
    id_category numeric(5,0) NOT NULL,
    description character varying(500)
);


ALTER TABLE public.category OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 19809)
-- Name: current_players; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.current_players (
    appid numeric(10,0) NOT NULL,
    date_point date NOT NULL,
    avg_players numeric(10,0),
    peak_players numeric(10,0)
);


ALTER TABLE public.current_players OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 19764)
-- Name: game_language; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.game_language (
    id_language integer NOT NULL,
    description character varying(500)
);


ALTER TABLE public.game_language OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 19762)
-- Name: game_language_id_language_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.game_language_id_language_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.game_language_id_language_seq OWNER TO postgres;

--
-- TOC entry 3194 (class 0 OID 0)
-- Dependencies: 216
-- Name: game_language_id_language_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.game_language_id_language_seq OWNED BY public.game_language.id_language;


--
-- TOC entry 219 (class 1259 OID 19775)
-- Name: genre; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.genre (
    id_genre numeric(5,0) NOT NULL,
    description character varying(500)
);


ALTER TABLE public.genre OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 19732)
-- Name: genre_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.genre_user (
    id_genre_user integer NOT NULL,
    description character varying(500)
);


ALTER TABLE public.genre_user OWNER TO postgres;

--
-- TOC entry 208 (class 1259 OID 19730)
-- Name: genre_user_id_genre_user_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.genre_user_id_genre_user_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.genre_user_id_genre_user_seq OWNER TO postgres;

--
-- TOC entry 3195 (class 0 OID 0)
-- Dependencies: 208
-- Name: genre_user_id_genre_user_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.genre_user_id_genre_user_seq OWNED BY public.genre_user.id_genre_user;


--
-- TOC entry 218 (class 1259 OID 19770)
-- Name: genres; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.genres (
    id_genre numeric(5,0) NOT NULL,
    appid numeric(10,0) NOT NULL
);


ALTER TABLE public.genres OWNER TO postgres;

--
-- TOC entry 207 (class 1259 OID 19724)
-- Name: genres_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.genres_user (
    id_genre_user integer NOT NULL,
    appid numeric(10,0) NOT NULL
);


ALTER TABLE public.genres_user OWNER TO postgres;

--
-- TOC entry 206 (class 1259 OID 19722)
-- Name: genres_user_id_genre_user_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.genres_user_id_genre_user_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.genres_user_id_genre_user_seq OWNER TO postgres;

--
-- TOC entry 3196 (class 0 OID 0)
-- Dependencies: 206
-- Name: genres_user_id_genre_user_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.genres_user_id_genre_user_seq OWNED BY public.genres_user.id_genre_user;


--
-- TOC entry 215 (class 1259 OID 19756)
-- Name: languages; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.languages (
    id_language integer NOT NULL,
    appid numeric(10,0) NOT NULL
);


ALTER TABLE public.languages OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 19754)
-- Name: languages_id_language_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.languages_id_language_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.languages_id_language_seq OWNER TO postgres;

--
-- TOC entry 3197 (class 0 OID 0)
-- Dependencies: 214
-- Name: languages_id_language_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.languages_id_language_seq OWNED BY public.languages.id_language;


--
-- TOC entry 213 (class 1259 OID 19748)
-- Name: platform; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.platform (
    id_platform integer NOT NULL,
    description character varying(500)
);


ALTER TABLE public.platform OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 19746)
-- Name: platform_id_platform_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.platform_id_platform_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.platform_id_platform_seq OWNER TO postgres;

--
-- TOC entry 3198 (class 0 OID 0)
-- Dependencies: 212
-- Name: platform_id_platform_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.platform_id_platform_seq OWNED BY public.platform.id_platform;


--
-- TOC entry 211 (class 1259 OID 19740)
-- Name: platforms; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.platforms (
    appid numeric(10,0) NOT NULL,
    id_platform integer NOT NULL
);


ALTER TABLE public.platforms OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 19738)
-- Name: platforms_id_platform_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.platforms_id_platform_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.platforms_id_platform_seq OWNER TO postgres;

--
-- TOC entry 3199 (class 0 OID 0)
-- Dependencies: 210
-- Name: platforms_id_platform_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.platforms_id_platform_seq OWNED BY public.platforms.id_platform;


--
-- TOC entry 201 (class 1259 OID 19701)
-- Name: prices; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.prices (
    appid numeric(10,0) NOT NULL,
    date_point date NOT NULL,
    price numeric(10,2)
);


ALTER TABLE public.prices OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 19824)
-- Name: publisher; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.publisher (
    id_publisher integer NOT NULL,
    description character varying(500)
);


ALTER TABLE public.publisher OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 19822)
-- Name: publisher_id_publisher_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.publisher_id_publisher_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.publisher_id_publisher_seq OWNER TO postgres;

--
-- TOC entry 3200 (class 0 OID 0)
-- Dependencies: 227
-- Name: publisher_id_publisher_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.publisher_id_publisher_seq OWNED BY public.publisher.id_publisher;


--
-- TOC entry 226 (class 1259 OID 19816)
-- Name: publishers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.publishers (
    id_publisher integer NOT NULL,
    appid numeric(10,0) NOT NULL
);


ALTER TABLE public.publishers OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 19814)
-- Name: publishers_id_publisher_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.publishers_id_publisher_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.publishers_id_publisher_seq OWNER TO postgres;

--
-- TOC entry 3201 (class 0 OID 0)
-- Dependencies: 225
-- Name: publishers_id_publisher_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.publishers_id_publisher_seq OWNED BY public.publishers.id_publisher;


--
-- TOC entry 205 (class 1259 OID 19716)
-- Name: recommendation; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.recommendation (
    id_recommendation integer NOT NULL,
    description character varying(500)
);


ALTER TABLE public.recommendation OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 19714)
-- Name: recommendation_id_recommendation_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.recommendation_id_recommendation_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.recommendation_id_recommendation_seq OWNER TO postgres;

--
-- TOC entry 3202 (class 0 OID 0)
-- Dependencies: 204
-- Name: recommendation_id_recommendation_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.recommendation_id_recommendation_seq OWNED BY public.recommendation.id_recommendation;


--
-- TOC entry 203 (class 1259 OID 19708)
-- Name: recommendations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.recommendations (
    id_recommendation integer NOT NULL,
    appid numeric(10,0) NOT NULL,
    total numeric(8,0)
);


ALTER TABLE public.recommendations OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 19706)
-- Name: recommendations_id_recommendation_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.recommendations_id_recommendation_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.recommendations_id_recommendation_seq OWNER TO postgres;

--
-- TOC entry 3203 (class 0 OID 0)
-- Dependencies: 202
-- Name: recommendations_id_recommendation_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.recommendations_id_recommendation_seq OWNED BY public.recommendations.id_recommendation;


--
-- TOC entry 223 (class 1259 OID 19801)
-- Name: tag; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tag (
    id_tag numeric(5,0) NOT NULL,
    descripton character varying(500)
);


ALTER TABLE public.tag OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 19796)
-- Name: tags; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tags (
    id_tag numeric(5,0) NOT NULL,
    appid numeric(10,0) NOT NULL
);


ALTER TABLE public.tags OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 19693)
-- Name: videogames; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.videogames (
    appid numeric(10,0) NOT NULL,
    description character varying(500),
    total_recommendations numeric(8,0),
    required_age character varying(30),
    is_free boolean,
    followers numeric(10,0),
    url_metacritic character varying(300),
    release_date date,
    minor_price numeric(10,2),
    upper_price numeric(10,2),
    user_score numeric(2,1),
    metascore numeric(2,0),
    total_sales numeric(12,2),
    update_date timestamp with time zone
);


ALTER TABLE public.videogames OWNER TO postgres;

--
-- TOC entry 2970 (class 2604 OID 19767)
-- Name: game_language id_language; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_language ALTER COLUMN id_language SET DEFAULT nextval('public.game_language_id_language_seq'::regclass);


--
-- TOC entry 2966 (class 2604 OID 19735)
-- Name: genre_user id_genre_user; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genre_user ALTER COLUMN id_genre_user SET DEFAULT nextval('public.genre_user_id_genre_user_seq'::regclass);


--
-- TOC entry 2965 (class 2604 OID 19727)
-- Name: genres_user id_genre_user; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genres_user ALTER COLUMN id_genre_user SET DEFAULT nextval('public.genres_user_id_genre_user_seq'::regclass);


--
-- TOC entry 2969 (class 2604 OID 19759)
-- Name: languages id_language; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.languages ALTER COLUMN id_language SET DEFAULT nextval('public.languages_id_language_seq'::regclass);


--
-- TOC entry 2968 (class 2604 OID 19751)
-- Name: platform id_platform; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.platform ALTER COLUMN id_platform SET DEFAULT nextval('public.platform_id_platform_seq'::regclass);


--
-- TOC entry 2967 (class 2604 OID 19743)
-- Name: platforms id_platform; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.platforms ALTER COLUMN id_platform SET DEFAULT nextval('public.platforms_id_platform_seq'::regclass);


--
-- TOC entry 2972 (class 2604 OID 19827)
-- Name: publisher id_publisher; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.publisher ALTER COLUMN id_publisher SET DEFAULT nextval('public.publisher_id_publisher_seq'::regclass);


--
-- TOC entry 2971 (class 2604 OID 19819)
-- Name: publishers id_publisher; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.publishers ALTER COLUMN id_publisher SET DEFAULT nextval('public.publishers_id_publisher_seq'::regclass);


--
-- TOC entry 2964 (class 2604 OID 19719)
-- Name: recommendation id_recommendation; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recommendation ALTER COLUMN id_recommendation SET DEFAULT nextval('public.recommendation_id_recommendation_seq'::regclass);


--
-- TOC entry 2963 (class 2604 OID 19711)
-- Name: recommendations id_recommendation; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recommendations ALTER COLUMN id_recommendation SET DEFAULT nextval('public.recommendations_id_recommendation_seq'::regclass);


--
-- TOC entry 3180 (class 0 OID 19791)
-- Dependencies: 221
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3179 (class 0 OID 19783)
-- Dependencies: 220
-- Data for Name: category; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3183 (class 0 OID 19809)
-- Dependencies: 224
-- Data for Name: current_players; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3176 (class 0 OID 19764)
-- Dependencies: 217
-- Data for Name: game_language; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3178 (class 0 OID 19775)
-- Dependencies: 219
-- Data for Name: genre; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3168 (class 0 OID 19732)
-- Dependencies: 209
-- Data for Name: genre_user; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3177 (class 0 OID 19770)
-- Dependencies: 218
-- Data for Name: genres; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3166 (class 0 OID 19724)
-- Dependencies: 207
-- Data for Name: genres_user; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3174 (class 0 OID 19756)
-- Dependencies: 215
-- Data for Name: languages; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3172 (class 0 OID 19748)
-- Dependencies: 213
-- Data for Name: platform; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3170 (class 0 OID 19740)
-- Dependencies: 211
-- Data for Name: platforms; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3160 (class 0 OID 19701)
-- Dependencies: 201
-- Data for Name: prices; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3187 (class 0 OID 19824)
-- Dependencies: 228
-- Data for Name: publisher; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3185 (class 0 OID 19816)
-- Dependencies: 226
-- Data for Name: publishers; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3164 (class 0 OID 19716)
-- Dependencies: 205
-- Data for Name: recommendation; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3162 (class 0 OID 19708)
-- Dependencies: 203
-- Data for Name: recommendations; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3182 (class 0 OID 19801)
-- Dependencies: 223
-- Data for Name: tag; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3181 (class 0 OID 19796)
-- Dependencies: 222
-- Data for Name: tags; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3159 (class 0 OID 19693)
-- Dependencies: 200
-- Data for Name: videogames; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3204 (class 0 OID 0)
-- Dependencies: 216
-- Name: game_language_id_language_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.game_language_id_language_seq', 1, true);


--
-- TOC entry 3205 (class 0 OID 0)
-- Dependencies: 208
-- Name: genre_user_id_genre_user_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.genre_user_id_genre_user_seq', 1, false);


--
-- TOC entry 3206 (class 0 OID 0)
-- Dependencies: 206
-- Name: genres_user_id_genre_user_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.genres_user_id_genre_user_seq', 1, false);


--
-- TOC entry 3207 (class 0 OID 0)
-- Dependencies: 214
-- Name: languages_id_language_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.languages_id_language_seq', 1, false);


--
-- TOC entry 3208 (class 0 OID 0)
-- Dependencies: 212
-- Name: platform_id_platform_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.platform_id_platform_seq', 1, false);


--
-- TOC entry 3209 (class 0 OID 0)
-- Dependencies: 210
-- Name: platforms_id_platform_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.platforms_id_platform_seq', 1, false);


--
-- TOC entry 3210 (class 0 OID 0)
-- Dependencies: 227
-- Name: publisher_id_publisher_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.publisher_id_publisher_seq', 1, false);


--
-- TOC entry 3211 (class 0 OID 0)
-- Dependencies: 225
-- Name: publishers_id_publisher_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.publishers_id_publisher_seq', 1, false);


--
-- TOC entry 3212 (class 0 OID 0)
-- Dependencies: 204
-- Name: recommendation_id_recommendation_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.recommendation_id_recommendation_seq', 1, false);


--
-- TOC entry 3213 (class 0 OID 0)
-- Dependencies: 202
-- Name: recommendations_id_recommendation_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.recommendations_id_recommendation_seq', 1, false);


--
-- TOC entry 3000 (class 2606 OID 19795)
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id_category, appid);


--
-- TOC entry 2998 (class 2606 OID 19790)
-- Name: category category_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category
    ADD CONSTRAINT category_pkey PRIMARY KEY (id_category);


--
-- TOC entry 3006 (class 2606 OID 19813)
-- Name: current_players current_players_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.current_players
    ADD CONSTRAINT current_players_pkey PRIMARY KEY (appid, date_point);


--
-- TOC entry 2992 (class 2606 OID 19769)
-- Name: game_language game_language_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_language
    ADD CONSTRAINT game_language_pkey PRIMARY KEY (id_language);


--
-- TOC entry 2996 (class 2606 OID 19782)
-- Name: genre genre_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genre
    ADD CONSTRAINT genre_pkey PRIMARY KEY (id_genre);


--
-- TOC entry 2984 (class 2606 OID 19737)
-- Name: genre_user genre_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genre_user
    ADD CONSTRAINT genre_user_pkey PRIMARY KEY (id_genre_user);


--
-- TOC entry 2994 (class 2606 OID 19774)
-- Name: genres genres_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genres
    ADD CONSTRAINT genres_pkey PRIMARY KEY (id_genre, appid);


--
-- TOC entry 2982 (class 2606 OID 19729)
-- Name: genres_user genres_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genres_user
    ADD CONSTRAINT genres_user_pkey PRIMARY KEY (id_genre_user, appid);


--
-- TOC entry 2990 (class 2606 OID 19761)
-- Name: languages languages_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.languages
    ADD CONSTRAINT languages_pkey PRIMARY KEY (id_language, appid);


--
-- TOC entry 2988 (class 2606 OID 19753)
-- Name: platform platform_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.platform
    ADD CONSTRAINT platform_pkey PRIMARY KEY (id_platform);


--
-- TOC entry 2986 (class 2606 OID 19745)
-- Name: platforms platforms_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.platforms
    ADD CONSTRAINT platforms_pkey PRIMARY KEY (appid, id_platform);


--
-- TOC entry 2976 (class 2606 OID 19705)
-- Name: prices prices_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prices
    ADD CONSTRAINT prices_pkey PRIMARY KEY (appid, date_point);


--
-- TOC entry 3010 (class 2606 OID 19829)
-- Name: publisher publisher_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.publisher
    ADD CONSTRAINT publisher_pkey PRIMARY KEY (id_publisher);


--
-- TOC entry 3008 (class 2606 OID 19821)
-- Name: publishers publishers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.publishers
    ADD CONSTRAINT publishers_pkey PRIMARY KEY (id_publisher, appid);


--
-- TOC entry 2980 (class 2606 OID 19721)
-- Name: recommendation recommendation_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recommendation
    ADD CONSTRAINT recommendation_pkey PRIMARY KEY (id_recommendation);


--
-- TOC entry 2978 (class 2606 OID 19713)
-- Name: recommendations recommendations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recommendations
    ADD CONSTRAINT recommendations_pkey PRIMARY KEY (id_recommendation, appid);


--
-- TOC entry 3004 (class 2606 OID 19808)
-- Name: tag tag_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tag
    ADD CONSTRAINT tag_pkey PRIMARY KEY (id_tag);


--
-- TOC entry 3002 (class 2606 OID 19800)
-- Name: tags tags_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT tags_pkey PRIMARY KEY (id_tag, appid);


--
-- TOC entry 2974 (class 2606 OID 19700)
-- Name: videogames videogames_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.videogames
    ADD CONSTRAINT videogames_pkey PRIMARY KEY (appid);


--
-- TOC entry 3023 (class 2606 OID 19890)
-- Name: categories fk_categories__appid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT fk_categories__appid FOREIGN KEY (appid) REFERENCES public.videogames(appid);


--
-- TOC entry 3022 (class 2606 OID 19885)
-- Name: categories fk_categories__id_category; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT fk_categories__id_category FOREIGN KEY (id_category) REFERENCES public.category(id_category);


--
-- TOC entry 3026 (class 2606 OID 19905)
-- Name: current_players fk_current_players__appid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.current_players
    ADD CONSTRAINT fk_current_players__appid FOREIGN KEY (appid) REFERENCES public.videogames(appid);


--
-- TOC entry 3021 (class 2606 OID 19880)
-- Name: genres fk_genres__appid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genres
    ADD CONSTRAINT fk_genres__appid FOREIGN KEY (appid) REFERENCES public.videogames(appid);


--
-- TOC entry 3020 (class 2606 OID 19875)
-- Name: genres fk_genres__id_genre; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genres
    ADD CONSTRAINT fk_genres__id_genre FOREIGN KEY (id_genre) REFERENCES public.genre(id_genre);


--
-- TOC entry 3015 (class 2606 OID 19850)
-- Name: genres_user fk_genres_user__appid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genres_user
    ADD CONSTRAINT fk_genres_user__appid FOREIGN KEY (appid) REFERENCES public.videogames(appid);


--
-- TOC entry 3014 (class 2606 OID 19845)
-- Name: genres_user fk_genres_user__id_genre_user; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genres_user
    ADD CONSTRAINT fk_genres_user__id_genre_user FOREIGN KEY (id_genre_user) REFERENCES public.genre_user(id_genre_user);


--
-- TOC entry 3019 (class 2606 OID 19870)
-- Name: languages fk_languages__appid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.languages
    ADD CONSTRAINT fk_languages__appid FOREIGN KEY (appid) REFERENCES public.videogames(appid);


--
-- TOC entry 3018 (class 2606 OID 19865)
-- Name: languages fk_languages__id_language; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.languages
    ADD CONSTRAINT fk_languages__id_language FOREIGN KEY (id_language) REFERENCES public.game_language(id_language);


--
-- TOC entry 3016 (class 2606 OID 19855)
-- Name: platforms fk_platforms__appid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.platforms
    ADD CONSTRAINT fk_platforms__appid FOREIGN KEY (appid) REFERENCES public.videogames(appid);


--
-- TOC entry 3017 (class 2606 OID 19860)
-- Name: platforms fk_platforms__id_platform; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.platforms
    ADD CONSTRAINT fk_platforms__id_platform FOREIGN KEY (id_platform) REFERENCES public.platform(id_platform);


--
-- TOC entry 3011 (class 2606 OID 19830)
-- Name: prices fk_prices__appid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prices
    ADD CONSTRAINT fk_prices__appid FOREIGN KEY (appid) REFERENCES public.videogames(appid);


--
-- TOC entry 3028 (class 2606 OID 19915)
-- Name: publishers fk_publishers__appid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.publishers
    ADD CONSTRAINT fk_publishers__appid FOREIGN KEY (appid) REFERENCES public.videogames(appid);


--
-- TOC entry 3027 (class 2606 OID 19910)
-- Name: publishers fk_publishers__id_publisher; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.publishers
    ADD CONSTRAINT fk_publishers__id_publisher FOREIGN KEY (id_publisher) REFERENCES public.publisher(id_publisher);


--
-- TOC entry 3013 (class 2606 OID 19840)
-- Name: recommendations fk_recommendations__appid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recommendations
    ADD CONSTRAINT fk_recommendations__appid FOREIGN KEY (appid) REFERENCES public.videogames(appid);


--
-- TOC entry 3012 (class 2606 OID 19835)
-- Name: recommendations fk_recommendations__id_recommendation; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recommendations
    ADD CONSTRAINT fk_recommendations__id_recommendation FOREIGN KEY (id_recommendation) REFERENCES public.recommendation(id_recommendation);


--
-- TOC entry 3025 (class 2606 OID 19900)
-- Name: tags fk_tags__appid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT fk_tags__appid FOREIGN KEY (appid) REFERENCES public.videogames(appid);


--
-- TOC entry 3024 (class 2606 OID 19895)
-- Name: tags fk_tags__id_tag; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT fk_tags__id_tag FOREIGN KEY (id_tag) REFERENCES public.tag(id_tag);


-- Completed on 2022-05-29 20:29:35

--
-- PostgreSQL database dump complete
--

