create table market_food_prices
(
	country_id                              number,
	country_name                            varchar2(255),
	locality_id                             number,
	locality_name                           varchar2(255),
	market_id                               number,
	market_name                             varchar2(255),
	commodity_purchase_id                   number,
	commodity_purchased                     varchar2(255),
	currency_id                             number,
	name_of_currency                        varchar2(255),
	market_type_id                          number,
	market_type                             varchar2(255),
	measurement_id                          number,
	unit_of_goods_measurement               varchar2(255),
	month_recorded                          varchar2(255),
	year_recorded                           varchar2(255),
	price_paid                              float,
	source_of_information                   varchar2(255)
);

-- country_id, country_name, locality_id, locality_name, market_id, market_name, commodity_purchase_id, commodity_purchased, currency_id, name_of_currency, market_type_id, market_type, measurement_id, unit_of_goods_measurement, month_recorded, year_recorded, price_paid, source_of_information

select unique(country_name) from market_food_prices order by country_name;

-- Raw
SELECT COUNTRY_NAME, COMMODITY_PURCHASED, MEASUREMENT_ID, UNIT_OF_GOODS_MEASUREMENT, MONTH_RECORDED, YEAR_RECORDER, PRICE_PAID from market_food_prices where country_name like 'Colombia';

-- Ideal
SELECT LOCALITY_NAME, COMMODITY_PURCHASED, MONTH_RECORDED, YEAR_RECORDER, PRICE_PAID from market_food_prices where country_name like 'Colombia' and UNIT_OF_GOODS_MEASUREMENT like 'KG';

SELECT UNIQUE(UNIT_OF_GOODS_MEASUREMENT) FROM MARKET_FOOD_PRICES WHERE COUNTRY_NAME LIKE 'Colombia';
SELECT UNIQUE(UNIT_OF_GOODS_MEASUREMENT) FROM MARKET_FOOD_PRICES;

-- GoodData generated
select "DEMO_PIMS"."MARKET_FOOD_PRICES"."LOCALITY_NAME","DEMO_PIMS"."MARKET_FOOD_PRICES"."COMMODITY_PURCHASED","DEMO_PIMS"."MARKET_FOOD_PRICES"."MONTH_RECORDED","DEMO_PIMS"."MARKET_FOOD_PRICES"."YEAR_RECORDER","DEMO_PIMS"."MARKET_FOOD_PRICES"."PRICE_PAID"
from "DEMO_PIMS"."MARKET_FOOD_PRICES"



-- ---------- Processing data ---------- --

-- Wich country has the most registers
select country_name, count(*) quantity from market_food_prices group by country_name order by quantity desc;

-- Colombia


-- Colombia specific table with KG only
create table market_food_prices_colombia as
(
    SELECT LOCALITY_NAME, COMMODITY_PURCHASED, MONTH_RECORDED, YEAR_RECORDER, PRICE_PAID from market_food_prices where country_name like 'Colombia' and UNIT_OF_GOODS_MEASUREMENT like 'KG'
);

-- Adding Date field
alter table market_food_prices_colombia
add date_recorded date;

-- Joining fields to add a Date type
update market_food_prices_colombia mfpc
set date_recorded = (select to_date(mfpc.YEAR_RECORDER || '-' || mfpc.MONTH_RECORDED, 'YYYY-MM') from dual);

-- Removing year and month columns
alter table market_food_prices_colombia
drop (month_recorded, year_recorder);



-- India

-- India specific table with KG only
create table market_food_prices_india as
(
    SELECT LOCALITY_NAME, COMMODITY_PURCHASED, MONTH_RECORDED, YEAR_RECORDER, PRICE_PAID from market_food_prices where country_name like 'India' and UNIT_OF_GOODS_MEASUREMENT like 'KG'
);

-- Adding Date field
alter table market_food_prices_india
add date_recorded date;

-- Joining fields to add a Date type
update market_food_prices_india mfpc
set date_recorded = (select to_date(mfpc.YEAR_RECORDER || '-' || mfpc.MONTH_RECORDED, 'YYYY-MM') from dual);

-- Removing year and month columns
alter table market_food_prices_india
drop (month_recorded, year_recorder);




-- Generating a general dataset with cleaned fields (less id fields)

create table FOOD_PRICES as
(
    SELECT COUNTRY_NAME, LOCALITY_NAME, MARKET_NAME, COMMODITY_PURCHASED, UNIT_OF_GOODS_MEASUREMENT, NAME_OF_CURRENCY, MONTH_RECORDED, YEAR_RECORDER, PRICE_PAID from MARKET_FOOD_PRICES
);

-- Adding Date field
alter table FOOD_PRICES
add date_recorded date;

-- Joining fields to add a Date type
update FOOD_PRICES mfpc
set date_recorded = (select to_date(mfpc.YEAR_RECORDER || '-' || mfpc.MONTH_RECORDED, 'YYYY-MM') from dual);

-- Removing year and month columns
alter table FOOD_PRICES
drop (month_recorded, year_recorder);