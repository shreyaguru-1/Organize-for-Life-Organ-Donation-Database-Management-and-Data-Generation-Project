--Select statement
select * from user_info;

--Select with Where clause
select u.user_id, u.user_name
from user_info as u, donor as d, organ as o
where u.user_id=d.user_id and o.user_id=d.user_id and o.availibility='Yes';

--Group By Clause
select blood_type, count(user_id) as donors_count
from donor 
group by blood_type;

--Avg() Operator
SELECT AVG(weight) as wei_avg
FROM donor
WHERE gender = 'Male';

--Join Tables
select d.user_id, o.organ_type
from donor as d natural join organ as o 
where o.organ_type='Kidney';

--Subquery
SELECT user_id, blood_type
FROM (
  SELECT user_id, blood_type FROM donor
) AS user_organ;

--Insertion
INSERT INTO user_info (user_id, user_name, user_email, phone_number, address, user_type) VALUES ('7001', 'Jason', 'Jason_Hancock4184@urn0m.mobi', '1173575390', '"Bury  Way, 6204"', 'R');

--Updation
UPDATE user_info
SET phone_number = '5555555555'
WHERE user_id = '123';

--Deletion
DELETE FROM organ WHERE organ_id = '123';

--Indexing for user_info table
CREATE INDEX user_info_phone_idx ON user_info (user_email);

--Indexing for donor table
CREATE INDEX donor_blood_type_idx ON donor (blood_type);

--Indexing for recipient table
CREATE INDEX recipient_blood_type_idx ON recipient (blood_type);

--Indexing for organ table
CREATE INDEX organ_user_idx ON organ (user_id);

--Indexing for health_history table
CREATE INDEX health_history_habits_idx ON health_history (smoker, drinker, drug_abuse, surgical_history);

--Problemetic Queries
SELECT * FROM recipient WHERE dob > '2000-01-01' AND gender = 'Male' AND organ_needed = 'Kidney';

SELECT * FROM organ WHERE organ_type = 'Kidney' AND availibility = 'Yes';

SELECT * FROM recipient WHERE blood_type = 'AB-' AND organ_needed = 'Liver';