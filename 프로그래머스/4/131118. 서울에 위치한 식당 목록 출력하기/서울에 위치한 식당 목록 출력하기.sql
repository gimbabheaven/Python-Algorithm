-- 코드를 입력하세요
SELECT R.REST_ID
    , I.REST_NAME
    , I.FOOD_TYPE
    , I.FAVORITES
    , I.ADDRESS
    , ROUND(AVG(REVIEW_SCORE), 2) AS AVG_REVIEW_SCORE
FROM REST_REVIEW R, REST_INFO I
WHERE R.REST_ID = I.REST_ID
AND I.ADDRESS LIKE '서울%'
GROUP BY R.REST_ID, I.REST_NAME, I.FOOD_TYPE, I.FAVORITES, I.ADDRESS
ORDER BY AVG_REVIEW_SCORE DESC, FAVORITES DESC