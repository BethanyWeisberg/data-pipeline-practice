create table orders (
    orderid int, 
    orderstatus varchar(30), 
    orderdate timestamp, 
    customerid int, 
    ordertotal numeric);
insert into orders (orderid, orderstatus, orderdate, customerid, ordertotal) 
values 
    (1, 'Shipped', '2020-06-09',100,50.05),
    (2, 'Shipped', '2020-07-11',101,57.45),
    (3, 'Shipped', '2020-07-12',102,135.99),
    (4, 'Shipped', '2020-07-12',100,43.00);


create table customers (
    customerid int, 
    customername varchar(20), 
    customercountry VARCHAR(10)
    );
insert into customers (customerid, customername, customercountry)
values 
    (100, 'Jane', 'USA'),
    (101, 'Bob', 'UK'),
    (102, 'Miles', 'UK');


create table if not exists order_summary_daily (
    order_date date,
    order_country varchar(10),
    total_revenue numeric,
    order_count int
);
insert into order_summary_daily (order_date, order_country, total_revenue, order_count)
select
    orders.orderdate as order_date,
    customers.customercountry as order_country,
    sum(orders.ordertotal) as total_revenue,
    count(orders.orderid) as order_count
from orders
inner join customers on customers.customerid = orders.customerid
group by orders.orderdate, customers.customercountry;