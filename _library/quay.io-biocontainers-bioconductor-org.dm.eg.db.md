---
layout: container
name:  "quay.io/biocontainers/bioconductor-org.dm.eg.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-org.dm.eg.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-org.dm.eg.db/container.yaml"
updated_at: "2025-01-02 02:55:18.969889"
latest: "3.20.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-org.dm.eg.db"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.8.2--r36_1"
 - "3.16.0--r42hdfd78af_0"
 - "3.14.0--r41hdfd78af_1"
 - "3.13.0--r41hdfd78af_0"
 - "3.12.0--r40hdfd78af_1"
 - "3.11.1--r40_0"
 - "3.17.0--r43hdfd78af_0"
 - "3.18.0--r43hdfd78af_0"
 - "3.20.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-org.dm.eg.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-org.dm.eg.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-org.dm.eg.db", "latest": {"3.20.0--r44hdfd78af_0": "sha256:83acfc4da2f64573ccfcbd9d22c5d1d49f7ef21ce924b239efbe7e3828856bd9"}, "tags": {"3.8.2--r36_1": "sha256:0377c243accc4afdde5cbd6400b19b9b7f853b37021f63bdb6a6453f7f5a9028", "3.16.0--r42hdfd78af_0": "sha256:e8f8beed7c8df3bbfdbc36fb756ce0f9b9e6e03fdd4faf8314cc3b738c4f76c3", "3.14.0--r41hdfd78af_1": "sha256:78745e35ccf043f9ca933eec775cba4e018eab9c36209dc7fdc5f557fb599b5e", "3.13.0--r41hdfd78af_0": "sha256:0dfb024c0bb60289a1310a20e8138d8ef8889a16b7e94cd1939db61d26abb86d", "3.12.0--r40hdfd78af_1": "sha256:d66881d9345bfedbb0674fa52256e8e66c261e2b7eebaeddfad3dc70bc08ed0d", "3.11.1--r40_0": "sha256:a925138946b154c6e75abeb0d1f11f25601c1a9d85723ff74d1d475b058a4176", "3.17.0--r43hdfd78af_0": "sha256:94219e6ac6f9e557e782c6294d1acb033ea63589a782ec921e50b7130298e51b", "3.18.0--r43hdfd78af_0": "sha256:9df0ce38ead4f30e152897733208e3eff48011159a3d0e09f02c3edd986c3239", "3.20.0--r44hdfd78af_0": "sha256:83acfc4da2f64573ccfcbd9d22c5d1d49f7ef21ce924b239efbe7e3828856bd9"}, "docker": "quay.io/biocontainers/bioconductor-org.dm.eg.db", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-org.dm.eg.db.
shpc-registry automated BioContainers addition for bioconductor-org.dm.eg.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-org.dm.eg.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-org.dm.eg.db:3.20.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-org.dm.eg.db/3.20.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-org.dm.eg.db/3.20.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-org.dm.eg.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.dm.eg.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.dm.eg.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-org.dm.eg.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-org.dm.eg.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-org.dm.eg.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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