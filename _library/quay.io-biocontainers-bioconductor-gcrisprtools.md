---
layout: container
name:  "quay.io/biocontainers/bioconductor-gcrisprtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gcrisprtools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gcrisprtools/container.yaml"
updated_at: "2024-05-30 04:48:17.389115"
latest: "2.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gcrisprtools"
aliases:
 - "pandoc"
versions:
 - "2.0.0--r41hdfd78af_0"
 - "2.4.0--r42hdfd78af_0"
 - "2.6.0--r43hdfd78af_0"
 - "2.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gcrisprtools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gcrisprtools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gcrisprtools", "latest": {"2.8.0--r43hdfd78af_0": "sha256:238c987ec7cbb0c4043de375c766c1124074613771622ae915cf68e39c84fc99"}, "tags": {"2.0.0--r41hdfd78af_0": "sha256:47da2386925bdfd79c8d9758d74c43f8a29dd5f7f54e862bb894150dd3d8fc0b", "2.4.0--r42hdfd78af_0": "sha256:843a8160e754dff0798ed698eb68e32720b8dd8cb631ac1735ffab35e231eb09", "2.6.0--r43hdfd78af_0": "sha256:f095cfa26038651d93ee82a242c860d81ac953bafcb7baabe823e4a5fa98f324", "2.8.0--r43hdfd78af_0": "sha256:238c987ec7cbb0c4043de375c766c1124074613771622ae915cf68e39c84fc99"}, "docker": "quay.io/biocontainers/bioconductor-gcrisprtools", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gcrisprtools.
shpc-registry automated BioContainers addition for bioconductor-gcrisprtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gcrisprtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gcrisprtools:2.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gcrisprtools/2.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gcrisprtools/2.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gcrisprtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gcrisprtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gcrisprtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gcrisprtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gcrisprtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gcrisprtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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