from aqt.browser import Browser
from aqt.qt import QIcon
from anki.hooks import wrap


# Separator used between hierarchies
SEPARATOR = '::'


def _userTagTree(self, root, _old):
    tags = sorted(self.col.tags.all())
    tags_tree = {}

    for t in tags:
        if t.lower() == "marked" or t.lower() == "leech":
            continue

        components = t.split(SEPARATOR)
        for idx, c in enumerate(components):
            partial_tag = SEPARATOR.join(components[0:idx + 1])
            if not tags_tree.get(partial_tag):
                if idx == 0:
                    parent = root
                else:
                    parent_tag = SEPARATOR.join(components[0:idx])
                    parent = tags_tree[parent_tag]

                item = self.CallbackItem(
                    parent, c,
                    lambda partial_tag=partial_tag: self.setFilter("tag", partial_tag + '*'))
                item.setIcon(0, QIcon(":/icons/anki-tag.png"))

                tags_tree[partial_tag] = item


Browser._userTagTree = wrap(Browser._userTagTree, _userTagTree, 'around')
