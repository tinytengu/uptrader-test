from django import template

from tree_menu.models import MenuItem

register = template.Library()


def _build_tree(items: list[MenuItem]):
    """Simple elements tree. 100% needs to be refactored, but couldn't care less."""
    tree = {}

    for item in items:
        parent = item.parent
        if not parent:
            tree[item] = {}
            continue

        if parent not in tree:
            tree[parent] = {}
        tree[parent][item] = {}

    return tree


@register.inclusion_tag("tree_menu/menu.html", takes_context=True)
def draw_menu(context: template.RequestContext, slug: str):
    items = (
        MenuItem.objects.filter(category__slug=slug)
        .select_related("category")
        .order_by("pk")
    )

    active_item = None

    for item in items:
        if item.is_url_match(context.request.path):
            active_item = item
            break

    items_tree = _build_tree(items)

    return {
        "category_name": items[0].category.name,
        "items": items_tree,
        "active_item": active_item,
    }
