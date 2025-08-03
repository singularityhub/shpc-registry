---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu95dprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu95dprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu95dprobe/container.yaml"
updated_at: "2025-08-03 04:16:15.632038"
latest: "2.18.0--r44hdfd78af_14"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu95dprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r41hdfd78af_10"
 - "2.18.0--r42hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r43hdfd78af_13"
 - "2.18.0--r44hdfd78af_14"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu95dprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu95dprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu95dprobe", "latest": {"2.18.0--r44hdfd78af_14": "sha256:e73d1577bd4b295488453763bc438082499d22a5f75bfee3f4a2399923255365"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:7e8762028c0a8ee1945a16c59db526b50dce534d65e99b4bf80709224e2ee4a9", "2.18.0--r41hdfd78af_10": "sha256:0703fd11cc57c7ca5ed4b1724d67bd16591073c0f3de820f79df0b6693a2aa65", "2.18.0--r42hdfd78af_11": "sha256:dc05a993d26b30e9240a8787dab033303a3f799f62c22c2f0d36e08d93650f83", "2.18.0--r43hdfd78af_12": "sha256:73a4a6ce1972c65e76639626d84c487ef13dc9f5dec6aaf46d38d1497e149bc3", "2.18.0--r43hdfd78af_13": "sha256:c31f5f30ea4ab97137876b694cd5e97e8227addc94c8f893e59f267f8a0985b8", "2.18.0--r44hdfd78af_14": "sha256:e73d1577bd4b295488453763bc438082499d22a5f75bfee3f4a2399923255365"}, "docker": "quay.io/biocontainers/bioconductor-hgu95dprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu95dprobe.
shpc-registry automated BioContainers addition for bioconductor-hgu95dprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu95dprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu95dprobe:2.18.0--r44hdfd78af_14
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu95dprobe/2.18.0--r44hdfd78af_14
$ module help quay.io/biocontainers/bioconductor-hgu95dprobe/2.18.0--r44hdfd78af_14
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu95dprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu95dprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu95dprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu95dprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu95dprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu95dprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgu95dprobe

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