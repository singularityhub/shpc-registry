---
layout: container
name:  "quay.io/biocontainers/bioconductor-hspeccdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hspeccdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hspeccdf/container.yaml"
updated_at: "2025-09-04 03:02:35.035406"
latest: "0.99.1--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-hspeccdf"

versions:
 - "0.99.1--r41hdfd78af_9"
 - "0.99.1--r42hdfd78af_10"
 - "0.99.1--r43hdfd78af_11"
 - "0.99.1--r43hdfd78af_12"
 - "0.99.1--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-hspeccdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hspeccdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hspeccdf", "latest": {"0.99.1--r44hdfd78af_13": "sha256:856a69c455a0baf84b5c1bcd372f74feec4e0f27bbc7d5f4e8a3f4b352ab1853"}, "tags": {"0.99.1--r41hdfd78af_9": "sha256:8e39aa578bc0e06bb61a2869e53e8ab023c6ba89ac018f7e9372e6659d0955d2", "0.99.1--r42hdfd78af_10": "sha256:589805a6645368b5a2ce2e32d584ae026265cc276c04ec54014f4e8b4e4a7a20", "0.99.1--r43hdfd78af_11": "sha256:26b48413a10f1cd468fb58294fe8ccd4ffbc653148aa9a3639ca0167a4453737", "0.99.1--r43hdfd78af_12": "sha256:341b893b85791704142c55e0d902c514e0db05387cc8756931859136aca1b375", "0.99.1--r44hdfd78af_13": "sha256:856a69c455a0baf84b5c1bcd372f74feec4e0f27bbc7d5f4e8a3f4b352ab1853"}, "docker": "quay.io/biocontainers/bioconductor-hspeccdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hspeccdf.
shpc-registry automated BioContainers addition for bioconductor-hspeccdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hspeccdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hspeccdf:0.99.1--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hspeccdf/0.99.1--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-hspeccdf/0.99.1--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hspeccdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hspeccdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hspeccdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hspeccdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hspeccdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hspeccdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hspeccdf

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