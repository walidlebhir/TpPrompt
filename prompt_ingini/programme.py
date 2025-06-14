def format_product_code(product_id):
   
    if not isinstance(product_id, str) or len(product_id) != 10 or not product_id.isalnum():
        raise ValueError("Le product_id doit être une chaîne alphanumérique de 10 caractères.")
    return f"{product_id[:3]}-{product_id[3:7]}-{product_id[7:]}"


format_product_code("736387IUEA") 