---
layout: container
name:  "quay.io/biocontainers/pgdspider"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pgdspider/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pgdspider/container.yaml"
updated_at: "2022-10-27 01:14:31.427395"
latest: "2.1.1.5--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/pgdspider"
aliases:
 - "PGDSpider2-cli"
 - "PGDSpider2-gui"
versions:
 - "2.1.1.5--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for pgdspider"
config: {"url": "https://biocontainers.pro/tools/pgdspider", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pgdspider", "latest": {"2.1.1.5--hdfd78af_1": "sha256:1380f25c1f9be1e02ca2b54c84f06339b877c10a4bb98dcbb36db944b5874d59"}, "tags": {"2.1.1.5--hdfd78af_1": "sha256:1380f25c1f9be1e02ca2b54c84f06339b877c10a4bb98dcbb36db944b5874d59"}, "docker": "quay.io/biocontainers/pgdspider", "aliases": {"PGDSpider2-cli": "/usr/local/bin/PGDSpider2-cli", "PGDSpider2-gui": "/usr/local/bin/PGDSpider2-gui"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pgdspider.
shpc-registry automated BioContainers addition for pgdspider
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pgdspider
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pgdspider:2.1.1.5--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pgdspider/2.1.1.5--hdfd78af_1
$ module help quay.io/biocontainers/pgdspider/2.1.1.5--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pgdspider-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pgdspider-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pgdspider-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pgdspider-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pgdspider-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pgdspider-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PGDSpider2-cli

```bash
$ singularity exec <container> /usr/local/bin/PGDSpider2-cli
$ podman run --it --rm --entrypoint /usr/local/bin/PGDSpider2-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PGDSpider2-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PGDSpider2-gui

```bash
$ singularity exec <container> /usr/local/bin/PGDSpider2-gui
$ podman run --it --rm --entrypoint /usr/local/bin/PGDSpider2-gui   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PGDSpider2-gui   -v ${PWD} -w ${PWD} <container> -c " $@"
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