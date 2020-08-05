from IPython.core.magic import needs_local_scope, register_cell_magic
from IPython.display import HTML, display

# embed the script
display(
    HTML('<script src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/8.6.4/mermaid.min.js"></script>')
)


COUNTER = 0


TEMPLATE = """
<div id="mermaid_{id}">
{content}
</div>

<script>mermaid.initialize({init_args})</script>
<script>mermaid.init({init_args}, "#mermaid_{id}");</script>
"""


@register_cell_magic
@needs_local_scope
def mermaid(line, cell, local_ns):
    if not line:
        line = {}
    global COUNTER
    content = cell.format(**local_ns)
    COUNTER += 1

    return HTML(
        TEMPLATE
        .format(
            content=content,
            id=COUNTER,
            init_args=line
        )
    )
