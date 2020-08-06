## Update Project to Use Latest Version of Python

When Python releases a new version, you may need to update your project so that it uses that version.

This process looks at how to update the version of Python that your
project uses when you use `pipenv` as the package/dependency manager
and virtual environment solution. It uses `pyenv` as the utility for
managing the global Python installations on your machine, which enables
you to keep a relatively clutter free Python environment.

Firstly, install `pyenv`. Outside of the virtual environment:

```sh
brew install pyenv
```

Check the versions of Python available on your local machine

```sh
pyenv versions
```

Check if the most recent version is available within `pyenv`

```sh
pyenv install --list  # Is your chosen version in the list?
```

If your chosen version is **NOT** in list (perhaps you already has
`pyenv` installed), `pyenv` must be updated

```sh
brew upgrade pyenv
```

Recheck to see if the most recent version is now available within
`pyenv`

```sh
pyenv install --list  # Is your chosen version now in the list?
```

Install your desired version of Python

```sh
pyenv install {full_version_num}
```

Check it has installed

```sh
pyenv versions
```

You will note that the newly installed version is not the global one. If
you'd like to make it the global version:

```sh
pyenv global {full_version_num}
```

Remove the existing virtual environment

```sh
docker-compose down  # Run this if building inside of a Docker container
pipenv --rm
```

Crucially, your `Pipfile` and `Pipfile.lock` will still be there for you
in the directory. We'll come back to this in a few steps.

Update your `pipenv` project.

Before doing the next step, open a completely new terminal window as
`pipenv` could give you a warning that you're already in a virtual
environment...

The following command will activate a new virtual environment using the
global version of Python that you specified in a previous step.

```sh
pipenv shell
```

The existing project packages will no longer be available within the
`.venv` folder. We will sort this in the next command. This might cause
the language server or linting tool to report hundreds of missing
imports, etc.

The version number is specified in the `pyvenv.cfg` file in the `.venv`
directory. Check this to validate it's the new version of Python that
you've just updated to.

To rebuild the project again with all of the project's packages and
dependencies, run the following command inside the virtual environment:

```sh
pipenv install --ignore-pipfile --deploy --dev
```

If you're using Docker, rebuild the project and bring up the dev server
again.

Make sure the base image of Python that you're pulling from Docker Hub,
perhaps specified in the `FROM` directive of your Dockerfile, is pulling
the matching Python image.

**NOTE:** When Python releases a new version, it sometimes takes 24-48
hours before an image for that same version becomes available on Docker
Hub.

```sh
docker-compose build
docker-compose up
```

If you're sure none of your other projects depend upon the old version
of Python, you can remove it from your system to keep it clean.

Outside of your virtual environment:

```sh
pyenv uninstall {full_version_num}
```
