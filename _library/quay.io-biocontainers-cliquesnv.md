---
layout: container
name:  "quay.io/biocontainers/cliquesnv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cliquesnv/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/cliquesnv/container.yaml"
updated_at: "2022-10-27 01:09:03.800225"
latest: "2.0.3--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/cliquesnv"
aliases:
 - "cliquesnv"
versions:
 - "2.0.3--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for cliquesnv"
config: {"url": "https://biocontainers.pro/tools/cliquesnv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cliquesnv", "latest": {"2.0.3--hdfd78af_0": "sha256:6e270a94e75832e7f75a763df51327b8eff1fd7753fbf67d7d10cee2bba27ab0"}, "tags": {"2.0.3--hdfd78af_0": "sha256:6e270a94e75832e7f75a763df51327b8eff1fd7753fbf67d7d10cee2bba27ab0"}, "docker": "quay.io/biocontainers/cliquesnv", "aliases": {"cliquesnv": "/usr/local/bin/cliquesnv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cliquesnv.
shpc-registry automated BioContainers addition for cliquesnv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cliquesnv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cliquesnv:2.0.3--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cliquesnv/2.0.3--hdfd78af_0
$ module help quay.io/biocontainers/cliquesnv/2.0.3--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cliquesnv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cliquesnv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cliquesnv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cliquesnv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cliquesnv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cliquesnv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cliquesnv

```bash
$ singularity exec <container> /usr/local/bin/cliquesnv
$ podman run --it --rm --entrypoint /usr/local/bin/cliquesnv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cliquesnv   -v ${PWD} -w ${PWD} <container> -c " $@"
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