---
layout: container
name:  "quay.io/biocontainers/metilene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metilene/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/metilene/container.yaml"
updated_at: "2022-10-27 01:11:47.383081"
latest: "0.2.8--hec16e2b_2"
container_url: "https://biocontainers.pro/tools/metilene"
aliases:
 - "metilene"
 - "metilene_input.pl"
 - "metilene_output.R"
 - "metilene_output.pl"
versions:
 - "0.2.8--hec16e2b_2"
description: "shpc-registry automated BioContainers addition for metilene"
config: {"url": "https://biocontainers.pro/tools/metilene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metilene", "latest": {"0.2.8--hec16e2b_2": "sha256:a32860d56312ec89f0e1c0b522563b14462adca62c4eb080c7e688cd2266f90c"}, "tags": {"0.2.8--hec16e2b_2": "sha256:a32860d56312ec89f0e1c0b522563b14462adca62c4eb080c7e688cd2266f90c"}, "docker": "quay.io/biocontainers/metilene", "aliases": {"metilene": "/usr/local/bin/metilene", "metilene_input.pl": "/usr/local/bin/metilene_input.pl", "metilene_output.R": "/usr/local/bin/metilene_output.R", "metilene_output.pl": "/usr/local/bin/metilene_output.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metilene.
shpc-registry automated BioContainers addition for metilene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metilene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metilene:0.2.8--hec16e2b_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metilene/0.2.8--hec16e2b_2
$ module help quay.io/biocontainers/metilene/0.2.8--hec16e2b_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metilene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metilene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metilene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metilene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metilene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metilene-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### metilene

```bash
$ singularity exec <container> /usr/local/bin/metilene
$ podman run --it --rm --entrypoint /usr/local/bin/metilene   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metilene   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metilene_input.pl

```bash
$ singularity exec <container> /usr/local/bin/metilene_input.pl
$ podman run --it --rm --entrypoint /usr/local/bin/metilene_input.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metilene_input.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metilene_output.R

```bash
$ singularity exec <container> /usr/local/bin/metilene_output.R
$ podman run --it --rm --entrypoint /usr/local/bin/metilene_output.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metilene_output.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metilene_output.pl

```bash
$ singularity exec <container> /usr/local/bin/metilene_output.pl
$ podman run --it --rm --entrypoint /usr/local/bin/metilene_output.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metilene_output.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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