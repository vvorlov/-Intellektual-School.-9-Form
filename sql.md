Базу можно скачать по адресу: https://goo.gl/lbUQjW.

Вывести треки композитора AC/DC длительностью более 300000 миллисекунд:
```sql
SELECT * 
FROM Track
WHERE Composer='AC/DC' and Milliseconds>300000;
```

Добавить новый альбом с названием "aaa" c id 348 и id исполнителя 2:
```sql
INSERT INTO Album
VALUES (348, 'aaa', 2);
```

Изменить название альбом с id 348 на название "bbb":
```sql
UPDATE Album
SET Title='bbb'
WHERE AlbumId=348;
```

Вывести треки, отсортированные по длительности:
```sql
SELECT Name, Milliseconds 
FROM Track
ORDER BY Milliseconds;
```

Вывести 3 любых трека с композитором "AC/DC":
```sql
SELECT * 
FROM Track
WHERE Composer='AC/DC'
LIMIT 3;
```

Вывести исполнителя/исполнителей для альбома "Big Ones":
```sql
SELECT Name, Artist.ArtistId, Title 
FROM Artist, (
   SELECT Album.ArtistId as id, Title 
   From Album
   WHERE Title='Big Ones')
WHERE Artist.ArtistId = id;
```

Вывести список альбомов и их исполнителей:
```sql
SELECT Album.Title, Artist.Name
FROM Artist
INNER JOIN Album
ON Album.ArtistId=Artist.ArtistId;
```

Вывести исполнителя/исполнителей для альбома "Big Ones" с использованием join:
```sql
SELECT Album.Title, Artist.Name
FROM Artist
INNER JOIN Album
ON Album.ArtistId=Artist.ArtistId
WHERE Album.Title='Big Ones';
```

Вывести количество альбомов у каждого исполнителя:
```sql
SELECT Count(Album.Title) as albumCount, Artist.Name
FROM Artist
INNER JOIN Album
ON Album.ArtistId=Artist.ArtistId
GROUP BY Name
```

Получить список всех альбомов Audioslave (текстом):
```sql
SELECT Album.Title, Artist.Name
FROM Artist
INNER JOIN Album
ON Album.ArtistId=Artist.ArtistId
WHERE Artist.Name='Audioslave’;
```

Вывести количество покупок по странам (count + без повторений):
```sql
SELECT BillingCountry, Count(BillingCountry) 
FROM Invoice
GROUP BY BillingCountry;
```

Показать топ 3 покупаемых трека:
```sql
SELECT Track.Name, Count(InvoiceLine.TrackId) as invoiceCount
FROM InvoiceLine
INNER JOIN Track
ON Track.TrackId=InvoiceLine.TrackId
GROUP BY Track.Name
ORDER BY invoiceCount DESC
Limit 3;
```

Создание таблицы:

```sql
CREATE TABLE Person (
PersonID INT PRIMARY KEY UNIQUE NOT NULL, 
Name VARCHAR NOT NULL, 
Age INT NOT NULL, 
City VARCHAR NOT NULL)
```