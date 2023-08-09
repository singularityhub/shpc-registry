---
layout: container
name:  "quay.io/biocontainers/cgat-report"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cgat-report/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cgat-report/container.yaml"
updated_at: "2023-08-09 03:12:09.971950"
latest: "0.9.1--py_0"
container_url: "https://biocontainers.pro/tools/cgat-report"
aliases:
 - "cgatreport-build"
 - "cgatreport-clean"
 - "cgatreport-get"
 - "cgatreport-profile"
 - "cgatreport-quickstart"
 - "cgatreport-serve"
 - "cgatreport-test"
 - "sphinx-apidoc"
 - "sphinx-autogen"
 - "sphinx-build"
 - "sphinx-quickstart"
 - "nosetests"
 - "pybabel"
 - "bokeh"
 - "rst2html4.py"
 - "rst2html5.py"
 - "rst2html.py"
versions:
 - "0.9.1--py_0"
description: "shpc-registry automated BioContainers addition for cgat-report"
config: {"url": "https://biocontainers.pro/tools/cgat-report", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cgat-report", "latest": {"0.9.1--py_0": "sha256:29e015051c290043fc2b95277b8127857cd3a416635c6b72b7eaa9fbfe101e94"}, "tags": {"0.9.1--py_0": "sha256:29e015051c290043fc2b95277b8127857cd3a416635c6b72b7eaa9fbfe101e94"}, "docker": "quay.io/biocontainers/cgat-report", "aliases": {"cgatreport-build": "/usr/local/bin/cgatreport-build", "cgatreport-clean": "/usr/local/bin/cgatreport-clean", "cgatreport-get": "/usr/local/bin/cgatreport-get", "cgatreport-profile": "/usr/local/bin/cgatreport-profile", "cgatreport-quickstart": "/usr/local/bin/cgatreport-quickstart", "cgatreport-serve": "/usr/local/bin/cgatreport-serve", "cgatreport-test": "/usr/local/bin/cgatreport-test", "sphinx-apidoc": "/usr/local/bin/sphinx-apidoc", "sphinx-autogen": "/usr/local/bin/sphinx-autogen", "sphinx-build": "/usr/local/bin/sphinx-build", "sphinx-quickstart": "/usr/local/bin/sphinx-quickstart", "nosetests": "/usr/local/bin/nosetests", "pybabel": "/usr/local/bin/pybabel", "bokeh": "/usr/local/bin/bokeh", "rst2html4.py": "/usr/local/bin/rst2html4.py", "rst2html5.py": "/usr/local/bin/rst2html5.py", "rst2html.py": "/usr/local/bin/rst2html.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cgat-report.
shpc-registry automated BioContainers addition for cgat-report
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cgat-report
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cgat-report:0.9.1--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cgat-report/0.9.1--py_0
$ module help quay.io/biocontainers/cgat-report/0.9.1--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cgat-report-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cgat-report-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cgat-report-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cgat-report-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cgat-report-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cgat-report-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cgatreport-build

```bash
$ singularity exec <container> /usr/local/bin/cgatreport-build
$ podman run --it --rm --entrypoint /usr/local/bin/cgatreport-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cgatreport-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cgatreport-clean

```bash
$ singularity exec <container> /usr/local/bin/cgatreport-clean
$ podman run --it --rm --entrypoint /usr/local/bin/cgatreport-clean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cgatreport-clean   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cgatreport-get

```bash
$ singularity exec <container> /usr/local/bin/cgatreport-get
$ podman run --it --rm --entrypoint /usr/local/bin/cgatreport-get   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cgatreport-get   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cgatreport-profile

```bash
$ singularity exec <container> /usr/local/bin/cgatreport-profile
$ podman run --it --rm --entrypoint /usr/local/bin/cgatreport-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cgatreport-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cgatreport-quickstart

```bash
$ singularity exec <container> /usr/local/bin/cgatreport-quickstart
$ podman run --it --rm --entrypoint /usr/local/bin/cgatreport-quickstart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cgatreport-quickstart   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cgatreport-serve

```bash
$ singularity exec <container> /usr/local/bin/cgatreport-serve
$ podman run --it --rm --entrypoint /usr/local/bin/cgatreport-serve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cgatreport-serve   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cgatreport-test

```bash
$ singularity exec <container> /usr/local/bin/cgatreport-test
$ podman run --it --rm --entrypoint /usr/local/bin/cgatreport-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cgatreport-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-apidoc

```bash
$ singularity exec <container> /usr/local/bin/sphinx-apidoc
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-apidoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-apidoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-autogen

```bash
$ singularity exec <container> /usr/local/bin/sphinx-autogen
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-autogen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-autogen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-build

```bash
$ singularity exec <container> /usr/local/bin/sphinx-build
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-quickstart

```bash
$ singularity exec <container> /usr/local/bin/sphinx-quickstart
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-quickstart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-quickstart   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nosetests

```bash
$ singularity exec <container> /usr/local/bin/nosetests
$ podman run --it --rm --entrypoint /usr/local/bin/nosetests   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nosetests   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybabel

```bash
$ singularity exec <container> /usr/local/bin/pybabel
$ podman run --it --rm --entrypoint /usr/local/bin/pybabel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybabel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bokeh

```bash
$ singularity exec <container> /usr/local/bin/bokeh
$ podman run --it --rm --entrypoint /usr/local/bin/bokeh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bokeh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html4.py

```bash
$ singularity exec <container> /usr/local/bin/rst2html4.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html5.py

```bash
$ singularity exec <container> /usr/local/bin/rst2html5.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html5.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html5.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html.py

```bash
$ singularity exec <container> /usr/local/bin/rst2html.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)