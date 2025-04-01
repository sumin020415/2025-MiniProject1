CREATE TABLE CMEMBERLIST (
	user_name varchar(20) PRIMARY KEY NOT NULL 
	,user_title varchar(20) NOT NULL 
	,user_id varchar(20) NOT NULL 
	,user_pw NUMBER(6) CHECK (LENGTH(user_pw) = 6) NOT NULL
);

INSERT ALL 
INTO CMEMBERLIST VALUES ('박수민','manager','sumin0759@gmail.com',123456)
INTO CMEMBERLIST VALUES ('이동호','staff','dongho7736@gmail.com',123456)
INTO CMEMBERLIST VALUES ('박세찬','deliver','guppy135@naver.com',123456)
INTO CMEMBERLIST VALUES ('이경주','deliver','rudwnzlxl6@naver.com',123456)
SELECT * FROM dual; 

COMMIT ; 
SELECT * FROM CMEMBERLIST; 











CREATE TABLE cmember(
   user_title varchar(20) PRIMARY KEY NOT NULL,
   user_name varchar(20) NOT NULL,
   user_level NUMBER(5,0) NOT NULL
); 

--level 1에 가까울 수록 보스
INSERT ALL
INTO cmember VALUES ('manager','매니저',1) 
INTO cmember VALUES ('staff','스태프',2 )
INTO cmember VALUES ('deliver','배달기사',3 )
SELECT * FROM dual;


CREATE USER deliver IDENTIFIED BY 12345;
GRANT SELECT ANY TABLE TO deliver;

--스태프한테 teamprod 테이블에 select,update,insert on teamprod to staff; 
-- 다시 스태프한테 delivery 권한은 select만 준 코드입니다 
-- 스태프는 상품 수정 빼곤 다 되지만 발주에서는 조회만 가능

CREATE USER staff IDENTIFIED BY 12345;
GRANT SELECT ON delivery TO staff;


SELECT * FROM cmember;

COMMIT;

grant connect, resource to sampleuser;

GRANT CREATE TABLE TO deliver;
GRANT CREATE ANY TABLE TO [사용자 이름];


UPDATE CMEMBER
SET user_level = 1
WHERE user_name = '스태프'; 

UPDATE CMEMBER
SET user_level = 2
WHERE user_name = '배달기사'; 

SELECT * FROM USER_SYS_PRIVS;