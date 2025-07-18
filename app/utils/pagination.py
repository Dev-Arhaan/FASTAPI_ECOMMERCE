def paginate(data: list, offset: int, limit: int) -> dict:
    return {
        "data": data,
        "page": {
            "next": str(offset + limit),
            "limit": limit,
            "previous": str(offset - limit)
        }
    }
