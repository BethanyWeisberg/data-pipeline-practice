create table all_orders as 
select
    orderid,
    orderstatus,
    lastupdated,
    row_number() over(partition by orderid, orderstatus 
        order by lastupdated desc) as duplicate_count
from orders;

truncate table orders;

-- insert deduplicated records
insert into orders (orderid, orderstatus, lastupdated)
select
    orderid,
    orderstatus,
    lastupdated
from all_orders
where duplicate_count = 1;

drop table all_orders;