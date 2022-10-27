---
layout: container
name:  "quay.io/biocontainers/nerpa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nerpa/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/nerpa/container.yaml"
updated_at: "2022-10-27 00:52:04.411875"
latest: "1.0.0--py37h96cfd12_3"
container_url: "https://biocontainers.pro/tools/nerpa"
aliases:
 - "NRPsMatcher"
 - "nerpa.py"
 - "nerpa_init.py"
versions:
 - "1.0.0--py37h96cfd12_3"
description: "shpc-registry automated BioContainers addition for nerpa"
config: {"url": "https://biocontainers.pro/tools/nerpa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nerpa", "latest": {"1.0.0--py37h96cfd12_3": "sha256:69ec060b9b2a85c55eec39740432cff442ca9bcec83cf741dd0e823c13ae5119"}, "tags": {"1.0.0--py37h96cfd12_3": "sha256:69ec060b9b2a85c55eec39740432cff442ca9bcec83cf741dd0e823c13ae5119"}, "docker": "quay.io/biocontainers/nerpa", "aliases": {"NRPsMatcher": "/usr/local/bin/NRPsMatcher", "nerpa.py": "/usr/local/bin/nerpa.py", "nerpa_init.py": "/usr/local/bin/nerpa_init.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nerpa.
shpc-registry automated BioContainers addition for nerpa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nerpa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nerpa:1.0.0--py37h96cfd12_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nerpa/1.0.0--py37h96cfd12_3
$ module help quay.io/biocontainers/nerpa/1.0.0--py37h96cfd12_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nerpa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nerpa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nerpa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nerpa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nerpa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nerpa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### NRPsMatcher

```bash
$ singularity exec <container> /usr/local/bin/NRPsMatcher
$ podman run --it --rm --entrypoint /usr/local/bin/NRPsMatcher   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NRPsMatcher   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nerpa.py

```bash
$ singularity exec <container> /usr/local/bin/nerpa.py
$ podman run --it --rm --entrypoint /usr/local/bin/nerpa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nerpa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nerpa_init.py

```bash
$ singularity exec <container> /usr/local/bin/nerpa_init.py
$ podman run --it --rm --entrypoint /usr/local/bin/nerpa_init.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nerpa_init.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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