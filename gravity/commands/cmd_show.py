import json

import click

from gravity import config_manager
from gravity import options


@click.command("show")
@options.required_config_arg()
@click.pass_context
def cli(ctx, config):
    """Show details of registered config.

    aliases: get
    """
    with config_manager.config_manager(state_dir=ctx.parent.state_dir) as cm:
        config_data = cm.get_registered_config(config)
        if config is None:
            click.echo(f"{config} not found")
        else:
            click.echo(json.dumps(config_data, sort_keys=True, indent=4, separators=(",", ": ")))
