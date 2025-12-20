def team_to_dict(team):
    if not team:
        return None
    return {
        "id": team.id,
        "name": team.name,
        "description": team.description,
        "lead_id": team.lead_id,
        "created_at": team.created_at.isoformat() if team.created_at is not None else None,
        "members": [
            {"id": m.id, "name": m.name, "email": m.email} for m in getattr(team, "members", [])
        ],
        "projects": [
            {"id": p.id, "title": p.title} for p in getattr(team, "projects", [])
        ],
    }
