"""Object typing relationships used when rendering entity attributes."""


def has_predefined_type_on_assigned_type(occurrence, concepts, supertypes, attributes):
    """Does a type paired with this occurrence supply a PredefinedType attribute?"""
    def lineage(entity):
        while entity:
            yield entity
            entity = supertypes.get(entity)

    occurrence_classes = set(lineage(occurrence))
    for pair in concepts.get("GeneralUsage", {}).get("ObjectTyping", []):
        if pair["ApplicableEntity"] in occurrence_classes:
            if any(f"{cls}.PredefinedType" in attributes for cls in lineage(pair["RelatingType"])):
                return True
    return False
