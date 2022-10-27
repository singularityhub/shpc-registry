---
layout: container
name:  "quay.io/biocontainers/repenrich"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/repenrich/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/repenrich/container.yaml"
updated_at: "2022-10-27 00:51:00.254134"
latest: "1.2--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/repenrich"
aliases:
 - "RepEnrich.py"
 - "RepEnrich_setup.py"
versions:
 - "1.2--hdfd78af_3"
description: "shpc-registry automated BioContainers addition for repenrich"
config: {"url": "https://biocontainers.pro/tools/repenrich", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for repenrich", "latest": {"1.2--hdfd78af_3": "sha256:31e724e00affc4320d30a2e1edb91095ef2b5275ac319033bfc5e8c55b4f045d"}, "tags": {"1.2--hdfd78af_3": "sha256:31e724e00affc4320d30a2e1edb91095ef2b5275ac319033bfc5e8c55b4f045d"}, "docker": "quay.io/biocontainers/repenrich", "aliases": {"RepEnrich.py": "/usr/local/bin/RepEnrich.py", "RepEnrich_setup.py": "/usr/local/bin/RepEnrich_setup.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/repenrich.
shpc-registry automated BioContainers addition for repenrich
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/repenrich
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/repenrich:1.2--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/repenrich/1.2--hdfd78af_3
$ module help quay.io/biocontainers/repenrich/1.2--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### repenrich-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### repenrich-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### repenrich-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### repenrich-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### repenrich-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### repenrich-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RepEnrich.py

```bash
$ singularity exec <container> /usr/local/bin/RepEnrich.py
$ podman run --it --rm --entrypoint /usr/local/bin/RepEnrich.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RepEnrich.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RepEnrich_setup.py

```bash
$ singularity exec <container> /usr/local/bin/RepEnrich_setup.py
$ podman run --it --rm --entrypoint /usr/local/bin/RepEnrich_setup.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RepEnrich_setup.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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