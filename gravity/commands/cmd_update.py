import click

from gravity import process_manager


@click.command("update")
@click.pass_context
def cli(ctx):
    """Update process manager from config changes."""
    with process_manager.process_manager(state_dir=ctx.parent.state_dir) as pm:
        pm.update()
