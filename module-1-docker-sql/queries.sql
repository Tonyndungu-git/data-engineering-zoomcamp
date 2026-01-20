-- Question 3: Counting short trips
SELECT COUNT(*) AS short_trips
FROM green_tripdata
WHERE lpep_pickup_datetime >= '2025-11-01'
  AND lpep_pickup_datetime < '2025-12-01'
  AND trip_distance <= 1;

-- Question 4: Longest trip for each day
SELECT DATE(lpep_pickup_datetime) AS pickup_date,
       MAX(trip_distance) AS max_distance
FROM green_tripdata
WHERE trip_distance < 100
  AND lpep_pickup_datetime >= '2025-11-01'
  AND lpep_pickup_datetime < '2025-12-01'
GROUP BY pickup_date
ORDER BY max_distance DESC
LIMIT 1;

-- Question 5: Biggest pickup zone (total_amount) Nov 18
SELECT z."Zone",
       SUM(g.total_amount) AS total_amount_sum
FROM green_tripdata g
JOIN taxi_zone_lookup z
  ON g.pulocationid = z."LocationID"
WHERE DATE(g.lpep_pickup_datetime) = '2025-11-18'
GROUP BY z."Zone"
ORDER BY total_amount_sum DESC
LIMIT 1;

-- Question 6: Largest tip from East Harlem North pickups
SELECT dz."Zone",
       MAX(g.tip_amount) AS max_tip
FROM green_tripdata g
JOIN taxi_zone_lookup pz
  ON g.pulocationid = pz."LocationID"
JOIN taxi_zone_lookup dz
  ON g.dolocationid = dz."LocationID"
WHERE pz."Zone" = 'East Harlem North'
  AND g.lpep_pickup_datetime >= '2025-11-01'
  AND g.lpep_pickup_datetime < '2025-12-01'
GROUP BY dz."Zone"
ORDER BY max_tip DESC
LIMIT 1;
