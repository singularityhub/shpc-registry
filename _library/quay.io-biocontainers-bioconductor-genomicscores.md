---
layout: container
name:  "quay.io/biocontainers/bioconductor-genomicscores"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genomicscores/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genomicscores/container.yaml"
updated_at: "2023-07-22 03:20:50.906673"
latest: "2.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genomicscores"

versions:
 - "2.6.0--r41hdfd78af_0"
 - "2.10.0--r42hdfd78af_0"
 - "2.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genomicscores"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genomicscores", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genomicscores", "latest": {"2.12.0--r43hdfd78af_0": "sha256:25bafdc8745459e94dda06ac7725f5689dcd2713e0dd54625245fd63f249533f"}, "tags": {"2.6.0--r41hdfd78af_0": "sha256:85e37c88267e15433747d682dd3bf636e7c6ecdc6399c88d1b3f3e06d01c2def", "2.10.0--r42hdfd78af_0": "sha256:a51847a99cfd5f616c478c72095695f6e00f066cba9bc4bb323b58d44e4ecf6a", "2.12.0--r43hdfd78af_0": "sha256:25bafdc8745459e94dda06ac7725f5689dcd2713e0dd54625245fd63f249533f"}, "docker": "quay.io/biocontainers/bioconductor-genomicscores"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genomicscores.
shpc-registry automated BioContainers addition for bioconductor-genomicscores
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genomicscores
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genomicscores:2.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genomicscores/2.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-genomicscores/2.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genomicscores-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomicscores-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomicscores-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genomicscores-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genomicscores-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genomicscores-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-genomicscores

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