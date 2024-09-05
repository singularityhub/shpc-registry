---
layout: container
name:  "quay.io/biocontainers/bioconductor-fcbf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-fcbf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-fcbf/container.yaml"
updated_at: "2024-09-05 02:43:58.809216"
latest: "2.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-fcbf"

versions:
 - "2.2.0--r41hdfd78af_0"
 - "2.6.0--r42hdfd78af_0"
 - "2.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-fcbf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-fcbf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-fcbf", "latest": {"2.8.0--r43hdfd78af_0": "sha256:db6d33ec4bb853c22c5c91b260d0d37aac65ea273b59324c32839bdc394ae54f"}, "tags": {"2.2.0--r41hdfd78af_0": "sha256:c78f3b7c2a48549932d326ff284a9b427d6ae0112e5e564338df083dd1bd9b4b", "2.6.0--r42hdfd78af_0": "sha256:b557b2282ce376fff6df7ec60a31d751a70876171710a77d2c7a7979836d69e4", "2.8.0--r43hdfd78af_0": "sha256:db6d33ec4bb853c22c5c91b260d0d37aac65ea273b59324c32839bdc394ae54f"}, "docker": "quay.io/biocontainers/bioconductor-fcbf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-fcbf.
shpc-registry automated BioContainers addition for bioconductor-fcbf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-fcbf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-fcbf:2.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-fcbf/2.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-fcbf/2.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-fcbf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fcbf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fcbf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-fcbf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-fcbf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-fcbf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-fcbf

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