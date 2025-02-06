---
layout: container
name:  "quay.io/biocontainers/bioconductor-cnvrd2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cnvrd2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cnvrd2/container.yaml"
updated_at: "2025-02-06 03:10:57.174855"
latest: "1.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cnvrd2"
aliases:
 - "jags"
versions:
 - "1.32.0--r41hdfd78af_0"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cnvrd2"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cnvrd2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cnvrd2", "latest": {"1.44.0--r44hdfd78af_0": "sha256:b856c3403645cacaa087ba68be189c6fa64bcef0775e5e6fba4a123d840fc565"}, "tags": {"1.32.0--r41hdfd78af_0": "sha256:3d938bcc74b3631f4cb53021f5a12fefaa0470d4cbd162e49c76da5e888e63b5", "1.36.0--r42hdfd78af_0": "sha256:d9f4956ebdfbbdd841de35f193bf828324493e5003970031f474041181e4a189", "1.38.0--r43hdfd78af_0": "sha256:fa0aa64320d5cb054e074776c73fcfe3329e7e6eb63251db35ced654d9123c5a", "1.40.0--r43hdfd78af_0": "sha256:c0d698a7624d6ecdd54a4933b63d9a44d2ca88f796c488ff632fa23457f593b5", "1.44.0--r44hdfd78af_0": "sha256:b856c3403645cacaa087ba68be189c6fa64bcef0775e5e6fba4a123d840fc565"}, "docker": "quay.io/biocontainers/bioconductor-cnvrd2", "aliases": {"jags": "/usr/local/bin/jags"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cnvrd2.
shpc-registry automated BioContainers addition for bioconductor-cnvrd2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cnvrd2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cnvrd2:1.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cnvrd2/1.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cnvrd2/1.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cnvrd2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cnvrd2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cnvrd2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cnvrd2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cnvrd2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cnvrd2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jags

```bash
$ singularity exec <container> /usr/local/bin/jags
$ podman run --it --rm --entrypoint /usr/local/bin/jags   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jags   -v ${PWD} -w ${PWD} <container> -c " $@"
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