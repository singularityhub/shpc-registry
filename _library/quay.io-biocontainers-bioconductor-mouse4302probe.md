---
layout: container
name:  "quay.io/biocontainers/bioconductor-mouse4302probe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mouse4302probe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mouse4302probe/container.yaml"
updated_at: "2025-05-12 03:53:13.245470"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-mouse4302probe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-mouse4302probe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mouse4302probe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mouse4302probe", "latest": {"2.18.0--r44hdfd78af_13": "sha256:0dd74af0d430d1a8fd558e00720c1845ec51f6211a97cba519f8cc7d5b7ba17c"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:492bdd459bb0e4624389c13c7e4917c184c3538e0b5247f80a0af2f81a4f1976", "2.18.0--r42hdfd78af_10": "sha256:b2a766a42d6f95894775d38782398d0e4dcda116e5812fd1167ae880e82323b2", "2.18.0--r43hdfd78af_11": "sha256:efd0c9775b25f61e34430354c9ad713ff20835fe7e11823a56a0ca32ae122d5a", "2.18.0--r43hdfd78af_12": "sha256:b45e58792f5c10f75b6528e9bcd0d65d59fb8411b2400d07e98649220a6a36d0", "2.18.0--r44hdfd78af_13": "sha256:0dd74af0d430d1a8fd558e00720c1845ec51f6211a97cba519f8cc7d5b7ba17c"}, "docker": "quay.io/biocontainers/bioconductor-mouse4302probe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mouse4302probe.
shpc-registry automated BioContainers addition for bioconductor-mouse4302probe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mouse4302probe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mouse4302probe:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mouse4302probe/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-mouse4302probe/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mouse4302probe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mouse4302probe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mouse4302probe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mouse4302probe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mouse4302probe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mouse4302probe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mouse4302probe

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