---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowcut"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowcut/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowcut/container.yaml"
updated_at: "2025-12-13 03:53:11.231974"
latest: "1.16.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowcut"
aliases:
 - "geosop"
 - "geos-config"
versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.16.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowcut"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowcut", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowcut", "latest": {"1.16.0--r44hdfd78af_0": "sha256:156574dc13f9959dbf76d77d5f07fa04071fdcf143dabb9e5ac1f693bddb7799"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:06982b6e2d8666f508fd4d321fdbab9806ff09c46d85a52a019790bceb136419", "1.8.0--r42hdfd78af_0": "sha256:0cbcae48854fba8405b2121a8d985696aa6394154fb1971c46da0a2c1379a2fc", "1.10.0--r43hdfd78af_0": "sha256:8bf972e049b89149878d860a38794dc73d1a7d2ffdd59660c94130313ed462d5", "1.12.0--r43hdfd78af_0": "sha256:c8f36b481890a855b746676ea5f5b86ffd1ee5433af813624300c5f114f792bf", "1.16.0--r44hdfd78af_0": "sha256:156574dc13f9959dbf76d77d5f07fa04071fdcf143dabb9e5ac1f693bddb7799"}, "docker": "quay.io/biocontainers/bioconductor-flowcut", "aliases": {"geosop": "/usr/local/bin/geosop", "geos-config": "/usr/local/bin/geos-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowcut.
shpc-registry automated BioContainers addition for bioconductor-flowcut
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowcut
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowcut:1.16.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowcut/1.16.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-flowcut/1.16.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowcut-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowcut-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowcut-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowcut-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowcut-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowcut-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### geosop

```bash
$ singularity exec <container> /usr/local/bin/geosop
$ podman run --it --rm --entrypoint /usr/local/bin/geosop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geosop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geos-config

```bash
$ singularity exec <container> /usr/local/bin/geos-config
$ podman run --it --rm --entrypoint /usr/local/bin/geos-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geos-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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