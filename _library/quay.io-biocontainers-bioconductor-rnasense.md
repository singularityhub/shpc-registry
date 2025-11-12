---
layout: container
name:  "quay.io/biocontainers/bioconductor-rnasense"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rnasense/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rnasense/container.yaml"
updated_at: "2025-11-12 03:38:51.517844"
latest: "1.20.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rnasense"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.20.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rnasense"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rnasense", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rnasense", "latest": {"1.20.0--r44hdfd78af_0": "sha256:ff141949363ba7ba84925f6b9aa60e65e1e9317390e95f6b9ece3a16e74f049a"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:e181de18b69039c9695172122c42115d77e006c910e6fcff505bfacdb0ce72b9", "1.12.0--r42hdfd78af_0": "sha256:525ff195dea324493f42583b9db10e75f57c9af653d4ed2574b02f999dc9085b", "1.14.0--r43hdfd78af_0": "sha256:bb4cd5654aafb1356a3c1b4605962260f727dab06c0368b22c65779974f77ef6", "1.16.0--r43hdfd78af_0": "sha256:952e19854e98061766d40cc8f427fbbcb5f308e04d3c5b457dc8469323351a37", "1.20.0--r44hdfd78af_0": "sha256:ff141949363ba7ba84925f6b9aa60e65e1e9317390e95f6b9ece3a16e74f049a"}, "docker": "quay.io/biocontainers/bioconductor-rnasense"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rnasense.
shpc-registry automated BioContainers addition for bioconductor-rnasense
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rnasense
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rnasense:1.20.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rnasense/1.20.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rnasense/1.20.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rnasense-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnasense-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnasense-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rnasense-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rnasense-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rnasense-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rnasense

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