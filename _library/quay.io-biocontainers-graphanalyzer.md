---
layout: container
name:  "quay.io/biocontainers/graphanalyzer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/graphanalyzer/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/graphanalyzer/container.yaml"
updated_at: "2022-10-27 01:01:38.741145"
latest: "1.5.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/graphanalyzer"
aliases:
 - "colorcet"
 - "graphanalyzer.py"
 - "holoviews"
 - "panel"
versions:
 - "1.5.1--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for graphanalyzer"
config: {"url": "https://biocontainers.pro/tools/graphanalyzer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for graphanalyzer", "latest": {"1.5.1--hdfd78af_0": "sha256:afc55571e6efb598671119a911fd45459b9def0af688c5e1b045464e2a8c2e4b"}, "tags": {"1.5.1--hdfd78af_0": "sha256:afc55571e6efb598671119a911fd45459b9def0af688c5e1b045464e2a8c2e4b"}, "docker": "quay.io/biocontainers/graphanalyzer", "aliases": {"colorcet": "/usr/local/bin/colorcet", "graphanalyzer.py": "/usr/local/bin/graphanalyzer.py", "holoviews": "/usr/local/bin/holoviews", "panel": "/usr/local/bin/panel"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/graphanalyzer.
shpc-registry automated BioContainers addition for graphanalyzer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/graphanalyzer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/graphanalyzer:1.5.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/graphanalyzer/1.5.1--hdfd78af_0
$ module help quay.io/biocontainers/graphanalyzer/1.5.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### graphanalyzer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### graphanalyzer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### graphanalyzer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### graphanalyzer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### graphanalyzer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### graphanalyzer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### colorcet

```bash
$ singularity exec <container> /usr/local/bin/colorcet
$ podman run --it --rm --entrypoint /usr/local/bin/colorcet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/colorcet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### graphanalyzer.py

```bash
$ singularity exec <container> /usr/local/bin/graphanalyzer.py
$ podman run --it --rm --entrypoint /usr/local/bin/graphanalyzer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graphanalyzer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### holoviews

```bash
$ singularity exec <container> /usr/local/bin/holoviews
$ podman run --it --rm --entrypoint /usr/local/bin/holoviews   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/holoviews   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### panel

```bash
$ singularity exec <container> /usr/local/bin/panel
$ podman run --it --rm --entrypoint /usr/local/bin/panel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/panel   -v ${PWD} -w ${PWD} <container> -c " $@"
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