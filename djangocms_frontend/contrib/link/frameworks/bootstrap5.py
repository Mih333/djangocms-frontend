class LinkRenderMixin:
    def render(self, context, instance, placeholder):
        link_classes = []
        if instance.link_context:
            if instance.link_type == "link":
                link_classes.append("text-{}".format(instance.link_context))
            else:
                link_classes.append("btn")
                if not instance.link_outline:
                    link_classes.append("btn-{}".format(instance.link_context))
                else:
                    link_classes.append("btn-outline-{}".format(instance.link_context))
        if instance.link_size:
            link_classes.append(instance.link_size)
        if instance.link_block:
            link_classes.append("btn-block")
        parent = context.get("parent", None)
        if parent and parent.ui_item == "ListGroup":
            link_classes.append("list-group-item")
            link_classes.append("list-group-item-action")

        context["link"] = instance.get_link()
        context["link_classes"] = " ".join(link_classes)
        return super().render(context, instance, placeholder)
