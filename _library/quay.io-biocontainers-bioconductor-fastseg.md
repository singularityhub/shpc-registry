---
layout: container
name:  "quay.io/biocontainers/bioconductor-fastseg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-fastseg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-fastseg/container.yaml"
updated_at: "2024-04-06 02:58:50.160343"
latest: "1.48.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-fastseg"

versions:
 - "1.40.0--r41hc247a5b_2"
 - "1.44.0--r42hc247a5b_0"
 - "1.44.0--r42hf17093f_1"
 - "1.46.0--r43hf17093f_0"
 - "1.48.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-fastseg"
config: {"url": "https://biocontainers.pro/tools/bioconductor-fastseg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-fastseg", "latest": {"1.48.0--r43hf17093f_0": "sha256:603e125cdcaad0e2bd2c735966013086c6e0850c8c1b79febb283c12b8be9aa7"}, "tags": {"1.40.0--r41hc247a5b_2": "sha256:9c87eef8aa54836cccd6086645028ea6feb4ff2fe216133ae068472e95e65381", "1.44.0--r42hc247a5b_0": "sha256:6bb7aabd3e04fac6c642ab382a3ab7fd4d2b0c409e6a9c1ed7c9dc55d3560ff4", "1.44.0--r42hf17093f_1": "sha256:c6ea0ba447507071fbb02432a458f3f981b8a7fc82effea0059813454c9a29da", "1.46.0--r43hf17093f_0": "sha256:32d38f350987ddeea12e2af12223d78044b872d323157ed2c8c7c09a70905034", "1.48.0--r43hf17093f_0": "sha256:603e125cdcaad0e2bd2c735966013086c6e0850c8c1b79febb283c12b8be9aa7"}, "docker": "quay.io/biocontainers/bioconductor-fastseg"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-fastseg.
shpc-registry automated BioContainers addition for bioconductor-fastseg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-fastseg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-fastseg:1.48.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-fastseg/1.48.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-fastseg/1.48.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-fastseg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fastseg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fastseg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-fastseg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-fastseg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-fastseg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-fastseg

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