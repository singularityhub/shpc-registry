---
layout: container
name:  "quay.io/biocontainers/bioconductor-mouse4302frmavecs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mouse4302frmavecs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mouse4302frmavecs/container.yaml"
updated_at: "2025-12-09 03:45:06.557813"
latest: "1.5.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-mouse4302frmavecs"

versions:
 - "1.5.0--r41hdfd78af_9"
 - "1.5.0--r42hdfd78af_10"
 - "1.5.0--r43hdfd78af_11"
 - "1.5.0--r43hdfd78af_12"
 - "1.5.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-mouse4302frmavecs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mouse4302frmavecs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mouse4302frmavecs", "latest": {"1.5.0--r44hdfd78af_13": "sha256:1f13528d4916689094cc392441cf2069809dfc076e819501b87d32e74f196b6a"}, "tags": {"1.5.0--r41hdfd78af_9": "sha256:0b4988d6a0a806ef17218f3b7aa5c739173c7d141ee2c697366586aedb6bf3ab", "1.5.0--r42hdfd78af_10": "sha256:d623170a133e79a744c9bcd9a9d05e72ea25a8852709cd2cd81dfa7791d43eb7", "1.5.0--r43hdfd78af_11": "sha256:c065c2507148ce2229b3242c99a8844d0c04b01850ad8215b783265ffe5d79d3", "1.5.0--r43hdfd78af_12": "sha256:728add9094cad1cb8f29dfab1b99988e2f45378d07f5d8c259d1d69c8f6c587d", "1.5.0--r44hdfd78af_13": "sha256:1f13528d4916689094cc392441cf2069809dfc076e819501b87d32e74f196b6a"}, "docker": "quay.io/biocontainers/bioconductor-mouse4302frmavecs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mouse4302frmavecs.
shpc-registry automated BioContainers addition for bioconductor-mouse4302frmavecs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mouse4302frmavecs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mouse4302frmavecs:1.5.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mouse4302frmavecs/1.5.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-mouse4302frmavecs/1.5.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mouse4302frmavecs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mouse4302frmavecs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mouse4302frmavecs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mouse4302frmavecs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mouse4302frmavecs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mouse4302frmavecs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mouse4302frmavecs

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