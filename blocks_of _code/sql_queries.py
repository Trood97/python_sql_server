
#sql queries

select year,month_name,(south/(south+west+midwest+northeast))*100 as South,(west/(south+west+midwest+northeast)) *100 as west,(midwest/(south+west+midwest+northeast))
*100 as midwest,(northeast/(south+west+midwest+northeast)) * 100 as northeast
 from tutorial.us_housing_units where year > 2000



