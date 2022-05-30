CREATE OR REPLACE function public.f_validate_category(p_code numeric, p_description character varying)
 returns numeric 
 LANGUAGE plpgsql
as
$$
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

/********************************************************************************************/

CREATE OR REPLACE function public.f_validate_game_language(p_description character varying)
 returns numeric 
 LANGUAGE plpgsql
as
$$
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
$$
;

/********************************************************************************************/

CREATE OR REPLACE function public.f_validate_genre(p_code numeric, p_description character varying)
returns numeric 
 LANGUAGE plpgsql
as
$$
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
$$
;

/********************************************************************************************/
CREATE OR REPLACE function public.f_validate_genre_user(p_description character varying)
 returns numeric 
 LANGUAGE plpgsql
as
$$
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
$$
;
/********************************************************************************************/

CREATE OR REPLACE function public.f_validate_platforms(p_description character varying)
 returns numeric 
 LANGUAGE plpgsql
as
$$
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
$$
;

/********************************************************************************************/
CREATE OR REPLACE function public.f_validate_publisher(p_description character varying)
 returns numeric 
 LANGUAGE plpgsql
as
$$
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
$$
;

/********************************************************************************************/
CREATE OR REPLACE function public.f_validate_recommendation(p_description character varying)
 returns numeric 
 LANGUAGE plpgsql
as
$$
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
$$
;

/********************************************************************************************/
CREATE OR REPLACE function public.f_validate_tag(p_code numeric, p_description character varying)
 returns numeric 
 LANGUAGE plpgsql
as
$$
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
$$
;

