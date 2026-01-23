FEW_SHOT_EXAMPLES = [
    {
        "question": "Show me all listings in Colombo under 50,000 LKR",
        "sql": "SELECT * FROM listing WHERE location='Colombo' AND price < 50000;"
    },
    {
        "question": "Get all listings by seller John Doe",
        "sql": """
        SELECT l.title, l.location, l.price, l.bedrooms, l.bathrooms, 
               s.owner_fname, s.owner_lname, s.email
        FROM listing l
        JOIN seller s ON l.seller_id = s.seller_id
        WHERE s.owner_fname='John' AND s.owner_lname='Doe';
        """
    },
    {
        "question": "List all flats with 3 bedrooms",
        "sql": "SELECT * FROM listing WHERE property_type='flat' AND bedrooms = 3;"
    },
    {
        "question": "Show all listings in Malabe with images",
        "sql": """
        SELECT l.title, l.location, l.price, li.url AS image_url
        FROM listing l
        LEFT JOIN listing_image li ON l.listing_id = li.listing_id
        WHERE l.location='Malabe';
        """
    }
]