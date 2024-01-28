---
layout: container
name:  "quay.io/biocontainers/bioconductor-ensembldb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ensembldb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ensembldb/container.yaml"
updated_at: "2024-01-28 03:45:55.346111"
latest: "2.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ensembldb"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "2.8.0--r36_1"
 - "2.22.0--r42hdfd78af_0"
 - "2.18.1--r41hdfd78af_0"
 - "2.16.0--r41hdfd78af_0"
 - "2.14.0--r40hdfd78af_1"
 - "2.12.1--r40_0"
 - "2.24.0--r43hdfd78af_0"
 - "2.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ensembldb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ensembldb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ensembldb", "latest": {"2.26.0--r43hdfd78af_0": "sha256:f015bc65051c1ca65329f7a1f18eba87ac44bfb9e40bdda5216dd9d22d114671"}, "tags": {"2.8.0--r36_1": "sha256:9bf51457e181aef932b10635ce230708740f9f94bfa62e457705d0f9559760cf", "2.22.0--r42hdfd78af_0": "sha256:7fcdc821d13fad1f054b462969b81e31553e1f15a6faaebfca61b890a6aeb87c", "2.18.1--r41hdfd78af_0": "sha256:3771fdacc832fddc15e62c42bafc997589b96fb0f87600bd169b6986d099d4a6", "2.16.0--r41hdfd78af_0": "sha256:0e75f67c4bf89b21a3e9673d5a36cc888466d96c9e21a7a29fc4fa111f2113b4", "2.14.0--r40hdfd78af_1": "sha256:86d10a4348345e8dcb298d30edb7de333507270b84cad7b6436dd4715cd55e87", "2.12.1--r40_0": "sha256:f98c50b4ae528b2906334aff5436952cdd74b0f1684fba8290924cc76701d9db", "2.24.0--r43hdfd78af_0": "sha256:fb9ac5cd22eb2174278ed7988504d733147cd39a59919376fa9a1d12f44b0c98", "2.26.0--r43hdfd78af_0": "sha256:f015bc65051c1ca65329f7a1f18eba87ac44bfb9e40bdda5216dd9d22d114671"}, "docker": "quay.io/biocontainers/bioconductor-ensembldb", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ensembldb.
shpc-registry automated BioContainers addition for bioconductor-ensembldb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ensembldb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ensembldb:2.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ensembldb/2.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ensembldb/2.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ensembldb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ensembldb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ensembldb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ensembldb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ensembldb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ensembldb-inspect-deffile:

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