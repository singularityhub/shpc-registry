---
layout: container
name:  "quay.io/biocontainers/bioconductor-tuberculosis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tuberculosis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tuberculosis/container.yaml"
updated_at: "2025-06-23 04:16:38.370069"
latest: "1.12.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tuberculosis"

versions:
 - "1.0.0--r41hdfd78af_1"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.12.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tuberculosis"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tuberculosis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tuberculosis", "latest": {"1.12.0--r44hdfd78af_0": "sha256:e4e3bf34646f191d51a120e12c62c128a6f30711ada648375d91d143aba2586f"}, "tags": {"1.0.0--r41hdfd78af_1": "sha256:c9685b78ece366d205a1ad6122ecf4f1343b9b53cae07ea1240dae5db7727a4a", "1.4.0--r42hdfd78af_0": "sha256:18d74e37fae6288b98be907769121bb031e1c914e7404e720c7dff83344f318f", "1.6.0--r43hdfd78af_0": "sha256:cabf4223623a0248bc8dab76315993e06c0db13cbdc28ac9abe97e1cbc8ca278", "1.8.0--r43hdfd78af_0": "sha256:c7aed8a0d98ade3250c04e5f88e56e1c813e8f3e8bf3af69cc5425beb4df7185", "1.12.0--r44hdfd78af_0": "sha256:e4e3bf34646f191d51a120e12c62c128a6f30711ada648375d91d143aba2586f"}, "docker": "quay.io/biocontainers/bioconductor-tuberculosis"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tuberculosis.
shpc-registry automated BioContainers addition for bioconductor-tuberculosis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tuberculosis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tuberculosis:1.12.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tuberculosis/1.12.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tuberculosis/1.12.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tuberculosis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tuberculosis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tuberculosis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tuberculosis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tuberculosis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tuberculosis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tuberculosis

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