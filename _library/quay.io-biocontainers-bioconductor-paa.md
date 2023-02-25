---
layout: container
name:  "quay.io/biocontainers/bioconductor-paa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-paa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-paa/container.yaml"
updated_at: "2023-02-25 03:06:02.401615"
latest: "1.32.0--r42hc247a5b_0"
container_url: "https://biocontainers.pro/tools/bioconductor-paa"
aliases:
 - "glpsol"
versions:
 - "1.28.0--r41hc247a5b_2"
 - "1.32.0--r42hc247a5b_0"
description: "shpc-registry automated BioContainers addition for bioconductor-paa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-paa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-paa", "latest": {"1.32.0--r42hc247a5b_0": "sha256:051d93e3ae92673dbc14bbc9c04705ee47217a16a68cabcffe50885cce1516de"}, "tags": {"1.28.0--r41hc247a5b_2": "sha256:29a2e4487e4a186a36100af63c530bd23c19f4bf3501fe1558b96c3608475e39", "1.32.0--r42hc247a5b_0": "sha256:051d93e3ae92673dbc14bbc9c04705ee47217a16a68cabcffe50885cce1516de"}, "docker": "quay.io/biocontainers/bioconductor-paa", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-paa.
shpc-registry automated BioContainers addition for bioconductor-paa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-paa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-paa:1.32.0--r42hc247a5b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-paa/1.32.0--r42hc247a5b_0
$ module help quay.io/biocontainers/bioconductor-paa/1.32.0--r42hc247a5b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-paa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-paa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-paa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-paa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-paa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-paa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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