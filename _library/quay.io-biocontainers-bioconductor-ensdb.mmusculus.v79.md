---
layout: container
name:  "quay.io/biocontainers/bioconductor-ensdb.mmusculus.v79"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ensdb.mmusculus.v79/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ensdb.mmusculus.v79/container.yaml"
updated_at: "2023-08-12 02:55:25.994126"
latest: "2.99.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-ensdb.mmusculus.v79"

versions:
 - "2.99.0--r41hdfd78af_9"
 - "2.99.0--r42hdfd78af_10"
 - "2.99.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-ensdb.mmusculus.v79"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ensdb.mmusculus.v79", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ensdb.mmusculus.v79", "latest": {"2.99.0--r43hdfd78af_11": "sha256:7c1ca8052c2b88ee3e6c7229dfd1d43f4a5bf74d6665403de8f367504a8431e7"}, "tags": {"2.99.0--r41hdfd78af_9": "sha256:5006b011fc92b873c6d3be411b7404fe11e2a2a45d3a7bd52e19116284957c32", "2.99.0--r42hdfd78af_10": "sha256:81949a0ab1b09243a445324e9d3143f394668d9e50368ed7fbe9bfc9d8c4a306", "2.99.0--r43hdfd78af_11": "sha256:7c1ca8052c2b88ee3e6c7229dfd1d43f4a5bf74d6665403de8f367504a8431e7"}, "docker": "quay.io/biocontainers/bioconductor-ensdb.mmusculus.v79"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ensdb.mmusculus.v79.
shpc-registry automated BioContainers addition for bioconductor-ensdb.mmusculus.v79
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ensdb.mmusculus.v79
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ensdb.mmusculus.v79:2.99.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ensdb.mmusculus.v79/2.99.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-ensdb.mmusculus.v79/2.99.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ensdb.mmusculus.v79-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ensdb.mmusculus.v79-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ensdb.mmusculus.v79-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ensdb.mmusculus.v79-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ensdb.mmusculus.v79-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ensdb.mmusculus.v79-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ensdb.mmusculus.v79

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