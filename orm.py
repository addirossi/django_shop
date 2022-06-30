#SELECT

# SELECT * FROM product;
# Product.objects.all()

# SELECT name, price FROM product;
# Product.objects.only('name', 'price')

# SELECT * FROM product WHERE условие;
# Product.objects.filter(условие)

#сравнения
# ==
# SELECT * FROM product WHERE category_id = 'tv';
# Product.objects.filter(category_id='tv')

# !=
# SELECT * FROM product WHERE NOT category_id = 'tv';
# Product.objects.filter(~Q(category_id='tv'))
# Product.objects.exclude(category_id='tv')

# >
# SELECT * FROM product WHERE price > 30000;
# Product.objects.filter(price__gt=30000)

# <
# SELECT * FROM product WHERE price < 30000;
# Product.objects.filter(price__lt=30000)

# >=
# SELECT * FROM product WHERE price >= 30000;
# Product.objects.filter(price__gte=30000)

# <=
# SELECT * FROM product WHERE price <= 30000;
# Product.objects.filter(price__lte=30000)

#IN
# SELECT * FROM product WHERE category_id IN ('tv', 'smartphones');
# Product.objects.filter(category_id__in=['tv', 'smartphones'])

#BETWEEN
# SELECT * FROM product WHERE price BETWEEN 40000 AND 50000;
# Product.objects.filter(price__range=[40000, 50000])

#LIKE
#ILIKE

'str'
# SELECT * FROM product WHERE name LIKE 'Apple Iphone 13';
# Product.objects.filter(name__exact='Apple Iphone 13')

# SELECT * FROM product WHERE name ILIKE 'Apple Iphone 13';
# Product.objects.filter(name__iexact='Apple Iphone 13')

'str%'
# SELECT * FROM product WHERE name LIKE 'Apple%';
# Product.objects.filter(name__startswith='Apple')

# SELECT * FROM product WHERE name ILIKE 'Apple%';
# Product.objects.filter(name__istartswith='Apple')

'%str'
# SELECT * FROM product WHERE name LIKE '%13';
# Product.objects.filter(name__endswith='13')

# SELECT * FROM product WHERE name ILIKE '%13';
# Product.objects.filter(name__iendswith='13')

'%str%'
# SELECT * FROM product WHERE name LIKE '%Apple%';
# Product.objects.filter(name__contains='Apple')

# SELECT * FROM product WHERE name ILIKE '%Apple%';
# Product.objects.filter(name__icontains='Apple')

#ORDER BY

# SELECT * FROM product ORDER BY price ASC;
# Product.objects.order_by('price')

# SELECT * FROM product ORDER BY price DESC;
# Product.objects.order_by('-price')

# SELECT * FROM product LIMIT 10;
# Product.objects.all()[:10]

# SELECT * FROM product LIMIT 10 OFFSET 5;
# Product.objects.all()[5:15]

#INSERT
#UPDATE
#DELETE