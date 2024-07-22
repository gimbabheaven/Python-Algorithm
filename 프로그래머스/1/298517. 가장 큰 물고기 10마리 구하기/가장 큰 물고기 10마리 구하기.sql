-- 코드를 작성해주세요
select * from (
select id, ifnull(length, null) as length
from fish_info
order by length desc) z limit 10