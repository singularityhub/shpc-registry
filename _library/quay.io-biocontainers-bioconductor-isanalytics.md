---
layout: container
name:  "quay.io/biocontainers/bioconductor-isanalytics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-isanalytics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-isanalytics/container.yaml"
updated_at: "2023-08-03 04:04:31.702348"
latest: "1.10.1--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-isanalytics"

versions:
 - "1.4.1--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.1--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-isanalytics"
config: {"url": "https://biocontainers.pro/tools/bioconductor-isanalytics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-isanalytics", "latest": {"1.10.1--r43hdfd78af_0": "sha256:5bd376a83fa7912e57838ed2336dd2041363e10070b923a942cc92ad9563081e"}, "tags": {"1.4.1--r41hdfd78af_0": "sha256:8a57b1287c5f118ffbbc69e851a2b2bd69c74b33f53c28deea433660914367b5", "1.8.0--r42hdfd78af_0": "sha256:7924276bf42f704deebe01ac534e08c057a0fcf2ec7c1fcf0403cb7ca23db0e8", "1.10.1--r43hdfd78af_0": "sha256:5bd376a83fa7912e57838ed2336dd2041363e10070b923a942cc92ad9563081e"}, "docker": "quay.io/biocontainers/bioconductor-isanalytics"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-isanalytics.
shpc-registry automated BioContainers addition for bioconductor-isanalytics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-isanalytics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-isanalytics:1.10.1--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-isanalytics/1.10.1--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-isanalytics/1.10.1--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-isanalytics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-isanalytics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-isanalytics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-isanalytics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-isanalytics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-isanalytics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-isanalytics

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