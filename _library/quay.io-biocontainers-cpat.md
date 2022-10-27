---
layout: container
name:  "quay.io/biocontainers/cpat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cpat/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/cpat/container.yaml"
updated_at: "2022-10-27 01:07:58.168724"
latest: "3.0.4--py36h40b2fa4_1"
container_url: "https://biocontainers.pro/tools/cpat"
aliases:
 - "cpat.py"
 - "make_hexamer_tab.py"
 - "make_logitModel.py"
versions:
 - "3.0.4--py36h40b2fa4_1"
description: "shpc-registry automated BioContainers addition for cpat"
config: {"url": "https://biocontainers.pro/tools/cpat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cpat", "latest": {"3.0.4--py36h40b2fa4_1": "sha256:0113650a0fc7cfaee126d3ae94201979fbf84716a89706e82848371eda7f6228"}, "tags": {"3.0.4--py36h40b2fa4_1": "sha256:0113650a0fc7cfaee126d3ae94201979fbf84716a89706e82848371eda7f6228"}, "docker": "quay.io/biocontainers/cpat", "aliases": {"cpat.py": "/usr/local/bin/cpat.py", "make_hexamer_tab.py": "/usr/local/bin/make_hexamer_tab.py", "make_logitModel.py": "/usr/local/bin/make_logitModel.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cpat.
shpc-registry automated BioContainers addition for cpat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cpat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cpat:3.0.4--py36h40b2fa4_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cpat/3.0.4--py36h40b2fa4_1
$ module help quay.io/biocontainers/cpat/3.0.4--py36h40b2fa4_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cpat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cpat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cpat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cpat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cpat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cpat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cpat.py

```bash
$ singularity exec <container> /usr/local/bin/cpat.py
$ podman run --it --rm --entrypoint /usr/local/bin/cpat.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpat.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_hexamer_tab.py

```bash
$ singularity exec <container> /usr/local/bin/make_hexamer_tab.py
$ podman run --it --rm --entrypoint /usr/local/bin/make_hexamer_tab.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_hexamer_tab.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_logitModel.py

```bash
$ singularity exec <container> /usr/local/bin/make_logitModel.py
$ podman run --it --rm --entrypoint /usr/local/bin/make_logitModel.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_logitModel.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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