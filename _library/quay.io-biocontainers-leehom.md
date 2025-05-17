---
layout: container
name:  "quay.io/biocontainers/leehom"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/leehom/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/leehom/container.yaml"
updated_at: "2025-05-17 03:32:27.518241"
latest: "1.2.15--hdc46a4b_6"
container_url: "https://biocontainers.pro/tools/leehom"
aliases:
 - "leeHom"
 - "bamtools"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.2.15--he40e34d_4"
 - "1.2.15--ha267990_5"
 - "1.2.15--hdc46a4b_6"
description: "shpc-registry automated BioContainers addition for leehom"
config: {"url": "https://biocontainers.pro/tools/leehom", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for leehom", "latest": {"1.2.15--hdc46a4b_6": "sha256:42323bcc1d6a017f17515bfbaeed248ea89ed03fb0ac0cec2b7aa131ff286106"}, "tags": {"1.2.15--he40e34d_4": "sha256:e2ceba1a6cf41bf0bbfe5fa413970c3bdb9a33de5d1643744bdff48321f8f9c7", "1.2.15--ha267990_5": "sha256:ff751239241b445f699abaf7f824080520f36cdb1ce2dac5eab7c1b8cfda6f9e", "1.2.15--hdc46a4b_6": "sha256:42323bcc1d6a017f17515bfbaeed248ea89ed03fb0ac0cec2b7aa131ff286106"}, "docker": "quay.io/biocontainers/leehom", "aliases": {"leeHom": "/usr/local/bin/leeHom", "bamtools": "/usr/local/bin/bamtools", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/leehom.
shpc-registry automated BioContainers addition for leehom
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/leehom
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/leehom:1.2.15--hdc46a4b_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/leehom/1.2.15--hdc46a4b_6
$ module help quay.io/biocontainers/leehom/1.2.15--hdc46a4b_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### leehom-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### leehom-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### leehom-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### leehom-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### leehom-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### leehom-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### leeHom

```bash
$ singularity exec <container> /usr/local/bin/leeHom
$ podman run --it --rm --entrypoint /usr/local/bin/leeHom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/leeHom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtools

```bash
$ singularity exec <container> /usr/local/bin/bamtools
$ podman run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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