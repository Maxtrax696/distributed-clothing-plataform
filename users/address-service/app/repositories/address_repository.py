from app.core.db import get_connection
from app.models.address_schema import AddressCreate, AddressUpdate

def create_address(data: AddressCreate):
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO addresses (user_id, street, city, state, postal_code, country, address_type)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING id
            """, (data.user_id, data.street, data.city, data.state, data.postal_code, data.country, data.address_type))
            new_id = cur.fetchone()[0]
    conn.close()
    return {"id": new_id, **data.dict()}

def get_addresses_by_user(user_id: int):
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, user_id, street, city, state, postal_code, country, address_type FROM addresses WHERE user_id = %s", (user_id,))
            result = cur.fetchall()
    conn.close()
    return [dict(zip(
        ["id", "user_id", "street", "city", "state", "postal_code", "country", "address_type"], row
    )) for row in result]

def update_address(address_id: int, data: AddressUpdate):
    updates = []
    values = []
    for key, value in data.dict(exclude_unset=True).items():
        updates.append(f"{key} = %s")
        values.append(value)
    if not updates:
        return None
    values.append(address_id)

    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"""
                UPDATE addresses SET {', '.join(updates)} WHERE id = %s RETURNING *
            """, values)
            updated = cur.fetchone()
    conn.close()
    return updated

def delete_address(address_id: int):
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM addresses WHERE id = %s RETURNING id", (address_id,))
            deleted = cur.fetchone()
    conn.close()
    return bool(deleted)
