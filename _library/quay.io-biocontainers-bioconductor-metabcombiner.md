---
layout: container
name:  "quay.io/biocontainers/bioconductor-metabcombiner"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-metabcombiner/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-metabcombiner/container.yaml"
updated_at: "2023-05-19 02:41:05.620236"
latest: "1.8.0--r42hc0cfd56_0"
container_url: "https://biocontainers.pro/tools/bioconductor-metabcombiner"

versions:
 - "1.4.0--r41hc0cfd56_2"
 - "1.8.0--r42hc0cfd56_0"
description: "shpc-registry automated BioContainers addition for bioconductor-metabcombiner"
config: {"url": "https://biocontainers.pro/tools/bioconductor-metabcombiner", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-metabcombiner", "latest": {"1.8.0--r42hc0cfd56_0": "sha256:8d0578f0ff0f815fe38ea1e3963facb0ecbed5844db43fc279a6863319b4f426"}, "tags": {"1.4.0--r41hc0cfd56_2": "sha256:db6a0072945908e682b77e2e8116ecb4830335158adffcd5063bdc5e5af5297f", "1.8.0--r42hc0cfd56_0": "sha256:8d0578f0ff0f815fe38ea1e3963facb0ecbed5844db43fc279a6863319b4f426"}, "docker": "quay.io/biocontainers/bioconductor-metabcombiner"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-metabcombiner.
shpc-registry automated BioContainers addition for bioconductor-metabcombiner
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-metabcombiner
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-metabcombiner:1.8.0--r42hc0cfd56_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-metabcombiner/1.8.0--r42hc0cfd56_0
$ module help quay.io/biocontainers/bioconductor-metabcombiner/1.8.0--r42hc0cfd56_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-metabcombiner-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metabcombiner-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metabcombiner-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-metabcombiner-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-metabcombiner-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-metabcombiner-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-metabcombiner

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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