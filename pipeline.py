from nbpipeline.rules import discover_notebooks


groups = discover_notebooks(
    ignored_dirs={'backlog', 'archive'},
    ignore={'notebook_setup.ipynb'},
    only_tracked_in_git=True
)['groups']
