def flatten_menu(node):
    # Base case: if node is None or not a dict, return empty list
    if node is None or not isinstance(node, dict):
        return []

    node_type = node.get("type")

    # If it's an item, return its name (if available)
    if node_type == "item":
        name = node.get("name")
        return [name] if name else []

    # If it's a category, flatten all its children
    if node_type == "category":
        children = node.get("children", [])
        result = []
        for child in children:
            result.extend(flatten_menu(child))
        return result

    # Unknown or missing type → ignore
    return []
