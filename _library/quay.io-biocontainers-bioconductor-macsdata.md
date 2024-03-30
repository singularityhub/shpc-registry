---
layout: container
name:  "quay.io/biocontainers/bioconductor-macsdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-macsdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-macsdata/container.yaml"
updated_at: "2024-03-30 02:51:00.265744"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-macsdata"

versions:
 - "1.2.0--r41hdfd78af_1"
 - "1.5.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-macsdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-macsdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-macsdata", "latest": {"1.10.0--r43hdfd78af_0": "sha256:008c69e7294053d5605aba16557195362ae255df5b9fe75dfb3759eef478b8bb"}, "tags": {"1.2.0--r41hdfd78af_1": "sha256:8d246380d29382da93d960731c03f2fb8148a5fd09f683161c962a9560faad60", "1.5.0--r42hdfd78af_0": "sha256:7f9f8801626932b7033ce39cb66aab0a1a05ce32f42216c36d5ea05f5d8ec960", "1.8.0--r43hdfd78af_0": "sha256:5cf3db7a684956b1f70e2b30afade34770304a2e8c5494fc86671afa61256fd5", "1.10.0--r43hdfd78af_0": "sha256:008c69e7294053d5605aba16557195362ae255df5b9fe75dfb3759eef478b8bb"}, "docker": "quay.io/biocontainers/bioconductor-macsdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-macsdata.
shpc-registry automated BioContainers addition for bioconductor-macsdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-macsdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-macsdata:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-macsdata/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-macsdata/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-macsdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-macsdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-macsdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-macsdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-macsdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-macsdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-macsdata

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