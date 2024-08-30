-- 코드를 입력하세요
SELECT book_id, date_format(published_date, '%Y-%m-%d') as published_date
FROM BOOK
WHERE date_format(published_date, '%Y') ='2021'
and category = '인문'
order by published_date;