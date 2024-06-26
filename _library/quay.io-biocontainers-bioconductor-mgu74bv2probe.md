---
layout: container
name:  "quay.io/biocontainers/bioconductor-mgu74bv2probe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mgu74bv2probe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mgu74bv2probe/container.yaml"
updated_at: "2024-06-26 02:36:27.137361"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-mgu74bv2probe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-mgu74bv2probe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mgu74bv2probe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mgu74bv2probe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:370908567d10801f5407f8193fa1779c0e63c004630562c2300ec97acbc24b44"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:c8d04aaa7da63e79d13ae57e8e0a4ca925e9b7dfa37a177c5a687e89b7a8f5fe", "2.18.0--r42hdfd78af_10": "sha256:18f4484ee38565e5cc8600e41fdd713505e9cdf137dc7152026bfaffee18ae09", "2.18.0--r43hdfd78af_11": "sha256:d4b68fad1f08919e385e176812cbb9a95fb367b18b033c22338fb6cca131f891", "2.18.0--r43hdfd78af_12": "sha256:370908567d10801f5407f8193fa1779c0e63c004630562c2300ec97acbc24b44"}, "docker": "quay.io/biocontainers/bioconductor-mgu74bv2probe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mgu74bv2probe.
shpc-registry automated BioContainers addition for bioconductor-mgu74bv2probe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74bv2probe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74bv2probe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mgu74bv2probe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-mgu74bv2probe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mgu74bv2probe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74bv2probe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74bv2probe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mgu74bv2probe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mgu74bv2probe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mgu74bv2probe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mgu74bv2probe

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