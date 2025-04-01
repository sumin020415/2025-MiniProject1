INSERT INTO ORDER_TABLE (ORDER_ID, ORDER_PRICE, ORDER_DATE)
VALUES (100, 21600, TO_DATE('2025-03-22', 'YYYY-MM-DD'));

INSERT INTO ORDER_TABLE (ORDER_ID, ORDER_PRICE, ORDER_DATE)
VALUES (200, 15600, TO_DATE('2025-03-23', 'YYYY-MM-DD'));

INSERT INTO ORDER_TABLE (ORDER_ID, ORDER_PRICE, ORDER_DATE)
VALUES (300, 10800, TO_DATE('2025-03-24', 'YYYY-MM-DD'));

INSERT INTO ORDER_TABLE (ORDER_ID, ORDER_PRICE, ORDER_DATE)
VALUES (400, 5000, TO_DATE('2025-03-27', 'YYYY-MM-DD'));





INSERT INTO ORDERINFO (ORDERINFO_ID, ORDER_ID, MENU_ID, PRICE, COUNT)
VALUES (101, 100, 31, 4100, 1);

INSERT INTO ORDERINFO (ORDERINFO_ID, ORDER_ID, MENU_ID, PRICE, COUNT)
VALUES (102, 100, 123, 5900, 2);

INSERT INTO ORDERINFO (ORDERINFO_ID, ORDER_ID, MENU_ID, PRICE, COUNT)
VALUES (103, 100, 121, 5700, 1);



INSERT INTO ORDERINFO (ORDERINFO_ID, ORDER_ID, MENU_ID, PRICE, COUNT)
VALUES (104, 200, 83, 4200, 1);

INSERT INTO ORDERINFO (ORDERINFO_ID, ORDER_ID, MENU_ID, PRICE, COUNT)
VALUES (105, 200, 121, 5700, 2);



INSERT INTO ORDERINFO (ORDERINFO_ID, ORDER_ID, MENU_ID, PRICE, COUNT)
VALUES (106, 300, 121, 5700, 1);

INSERT INTO ORDERINFO (ORDERINFO_ID, ORDER_ID, MENU_ID, PRICE, COUNT)
VALUES (107, 300, 122, 5100, 1);



INSERT INTO ORDERINFO (ORDERINFO_ID, ORDER_ID, MENU_ID, PRICE, COUNT)
VALUES (108, 400, 200, 5000, 1);


