#!/usr/bin/env python3
import click

APP_FOLDER = 'exercises'


@click.group()
def cli():  # NOQA
    pass


@cli.command()
@click.option('--coverage', 'with_coverage', is_flag=True)
@click.option('--no-html', is_flag=True)
@click.option('--no-report', is_flag=True)
@click.option('--verbose', '-v', is_flag=True)
def test(with_coverage, no_html, no_report, verbose):
    """Run the tests."""
    if with_coverage:
        # Initialize coverage.py.
        import coverage
        COV = coverage.coverage(branch=True,
                                source=[APP_FOLDER])
        COV.start()

    # Run all unit tests found in tests folder.
    import pytest
    if verbose:
        exit_code = pytest.main(['tests', '-v'])
    else:
        exit_code = pytest.main(['tests'])

    if with_coverage:
        # Sum up the results of the code coverage analysis.
        COV.stop()
        COV.save()

        if not no_html:
            # Generate HTML report and move to tmp directory.
            import os
            basedir = os.path.abspath(os.path.dirname(__file__))
            covdir = os.path.join(basedir, 'tmp/coverage')
            COV.html_report(directory=covdir)

        if not no_report:
            # Show the report and clean up.
            click.echo('\nCoverage Summary\n{}'.format('=' * 70))
            COV.report()
            COV.erase()

    raise SystemExit(exit_code)


@cli.command()
@click.option('--all', is_flag=True)
@click.option('--stats', is_flag=True)
def lint(all, stats):
    """Run the linter."""
    from flake8 import main as flake8
    import sys

    if all:
        click.echo('Running linter (including skeleton code).')
        sys.argv = ['flake8', '.']
    else:
        click.echo('Running Linter...')
        sys.argv = ['flake8', APP_FOLDER]

    if stats:
        sys.argv.extend(['--statistics', '-qq'])

    flake8.main()


if __name__ == "__main__":
    cli()
