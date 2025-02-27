---
layout: container
name:  "quay.io/biocontainers/bioconductor-chimphumanbraindata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chimphumanbraindata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chimphumanbraindata/container.yaml"
updated_at: "2025-02-27 02:59:42.161043"
latest: "1.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chimphumanbraindata"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chimphumanbraindata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chimphumanbraindata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chimphumanbraindata", "latest": {"1.44.0--r44hdfd78af_0": "sha256:31dab5c8fff8ce58839165a82f939569b5d6a5226e25165ca7e6214d291237b0"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:dc94d743d7dc00051d265e8a854e96b49ca494af216c3213408017ecce1e283e", "1.36.0--r42hdfd78af_0": "sha256:a9b7e8a0b19f5da04d987c5fb198d501567381c236c266b586f5b28752804da3", "1.38.0--r43hdfd78af_0": "sha256:648289a146a624450c0b12237a25102632f8a1d2de49aee6c26a3cdae18813b8", "1.44.0--r44hdfd78af_0": "sha256:31dab5c8fff8ce58839165a82f939569b5d6a5226e25165ca7e6214d291237b0"}, "docker": "quay.io/biocontainers/bioconductor-chimphumanbraindata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chimphumanbraindata.
shpc-registry automated BioContainers addition for bioconductor-chimphumanbraindata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chimphumanbraindata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chimphumanbraindata:1.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chimphumanbraindata/1.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-chimphumanbraindata/1.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chimphumanbraindata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chimphumanbraindata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chimphumanbraindata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chimphumanbraindata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chimphumanbraindata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chimphumanbraindata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-chimphumanbraindata

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