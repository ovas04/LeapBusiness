
/*****************************************************************************************/
CREATE OR REPLACE PROCEDURE public.sp_register_categories(
p_appid numeric,
p_id_category numeric,
p_description varchar(500)
)
LANGUAGE plpgsql
AS $procedure$
DECLARE  
	v_id numeric;
BEGIN  
	
	select public.f_validate_category(p_id_category,p_description) into v_id;
	
	insert into tags values (v_id, p_appid);

END
$procedure$
;


/*****************************************************************************************/
CREATE OR REPLACE PROCEDURE public.sp_register_game_language(
p_appid numeric,
p_description varchar(500)
)
LANGUAGE plpgsql
AS $procedure$
DECLARE  
	v_id numeric;
BEGIN  
	
	select p	ublic.f_validate_category(p_description) into v_id;
	
	insert into languages values (v_id, p_appid);

END
$procedure$
;


/*****************************************************************************************/
CREATE OR REPLACE PROCEDURE public.sp_register_genre(
p_appid numeric,
p_id_genre numeric,
p_description varchar(500)
)
LANGUAGE plpgsql
AS $procedure$
DECLARE  
	v_id numeric;
BEGIN  
	
	select public.f_validate_genre(p_id_genre,p_description) into v_id;
	
	insert into genres values (v_id, p_appid);

END
$procedure$
;


/*****************************************************************************************/
CREATE OR REPLACE PROCEDURE public.sp_register_genre_user(
p_appid numeric,
p_description varchar(500)
)
LANGUAGE plpgsql
AS $procedure$
DECLARE  
	v_id numeric;
BEGIN  
	
	select public.f_validate_genre_user(p_description) into v_id;
	
	insert into genres_user values (v_id, p_appid);

END
$procedure$
;



/*****************************************************************************************/
CREATE OR REPLACE PROCEDURE public.sp_register_platforms(
p_appid numeric,
p_description varchar(500)
)
LANGUAGE plpgsql
AS $procedure$
DECLARE  
	v_id numeric;
BEGIN  
	
	select public.f_validate_platforms(p_description) into v_id;
	
	insert into platforms values (p_appid, v_id);

END
$procedure$
;

/*****************************************************************************************/
CREATE OR REPLACE PROCEDURE public.sp_register_publishers(
p_appid numeric,
p_description varchar(500)
)
LANGUAGE plpgsql
AS $procedure$
DECLARE  
	v_id numeric;
BEGIN  
	
	select public.f_validate_publisher(p_description) into v_id;
	
	insert into publishers values (v_id, p_appi);

END
$procedure$
;


/*****************************************************************************************/
CREATE OR REPLACE PROCEDURE public.sp_register_recomendations(
p_appid numeric,
p_description varchar(500),
p_total numeric (8)
)
LANGUAGE plpgsql
AS $procedure$
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
$procedure$
;

/*****************************************************************************************/
CREATE OR REPLACE PROCEDURE public.sp_register_tags(
p_appid numeric,
p_id_tag numeric,
p_description varchar(500)
)
LANGUAGE plpgsql
AS $procedure$
DECLARE  
	v_id numeric;
BEGIN  
	
	select f_validate_tag(p_id_tag,p_description) into v_id;
	
	insert into tags values (v_id, p_appid);

END
$procedure$
;


/*****************************************************************************************/
CREATE OR REPLACE PROCEDURE public.sp_register_prices(
p_appid numeric,
p_date_point date,
p_price numeric(10,2)
)
LANGUAGE plpgsql
AS $procedure$
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
$procedure$
;

/*****************************************************************************************/
CREATE OR REPLACE PROCEDURE public.sp_register_current_players(
p_appid numeric,
p_date_point date,
p_avg_players numeric(10),
p_peak_players numeric (10)
)
LANGUAGE plpgsql
AS $procedure$
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
$procedure$
;


/*****************************************************************************************/

CREATE OR REPLACE PROCEDURE public.sp_register_update_videogame(p_appid numeric, p_description character varying, p_total_recomendations numeric, p_required_age character varying, p_is_free boolean, p_followers numeric, p_url_metacritic character varying, p_relase_date date, p_minor_price numeric, p_upper_price numeric, p_user_score numeric, p_metascore numeric)
 LANGUAGE plpgsql
AS $procedure$
DECLARE  
BEGIN  
	
	if((select count(appid) from 
	videogames v where appid = p_appid)=0) then
	insert into videogames (appid,description,total_recommendations,required_age,
		is_free,followers,url_metacritic, release_date, minor_price,
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
$procedure$
;
















