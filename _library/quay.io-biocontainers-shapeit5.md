---
layout: container
name:  "quay.io/biocontainers/shapeit5"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/shapeit5/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/shapeit5/container.yaml"
updated_at: "2024-02-01 03:24:44.725523"
latest: "5.1.1--hb60d31d_0"
container_url: "https://biocontainers.pro/tools/shapeit5"
aliases:
 - "SHAPEIT5_ligate"
 - "SHAPEIT5_phase_common"
 - "SHAPEIT5_phase_rare"
 - "SHAPEIT5_switch"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.0.0--h0c8ee15_0"
 - "5.1.1--hb60d31d_0"
description: "singularity registry hpc automated addition for shapeit5"
config: {"url": "https://biocontainers.pro/tools/shapeit5", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for shapeit5", "latest": {"5.1.1--hb60d31d_0": "sha256:f91aff59fab017df5c017efbfba1f7abb8dca0beea86e2417d63f97df6aa800d"}, "tags": {"1.0.0--h0c8ee15_0": "sha256:000bdf6df6b10d5a6d284ab45ceb1eb9bd409781d5a4f62a401f7ceee82c5194", "5.1.1--hb60d31d_0": "sha256:f91aff59fab017df5c017efbfba1f7abb8dca0beea86e2417d63f97df6aa800d"}, "docker": "quay.io/biocontainers/shapeit5", "aliases": {"SHAPEIT5_ligate": "/usr/local/bin/SHAPEIT5_ligate", "SHAPEIT5_phase_common": "/usr/local/bin/SHAPEIT5_phase_common", "SHAPEIT5_phase_rare": "/usr/local/bin/SHAPEIT5_phase_rare", "SHAPEIT5_switch": "/usr/local/bin/SHAPEIT5_switch", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/shapeit5.
singularity registry hpc automated addition for shapeit5
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/shapeit5
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/shapeit5:5.1.1--hb60d31d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/shapeit5/5.1.1--hb60d31d_0
$ module help quay.io/biocontainers/shapeit5/5.1.1--hb60d31d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### shapeit5-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### shapeit5-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### shapeit5-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### shapeit5-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### shapeit5-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### shapeit5-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SHAPEIT5_ligate

```bash
$ singularity exec <container> /usr/local/bin/SHAPEIT5_ligate
$ podman run --it --rm --entrypoint /usr/local/bin/SHAPEIT5_ligate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SHAPEIT5_ligate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SHAPEIT5_phase_common

```bash
$ singularity exec <container> /usr/local/bin/SHAPEIT5_phase_common
$ podman run --it --rm --entrypoint /usr/local/bin/SHAPEIT5_phase_common   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SHAPEIT5_phase_common   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SHAPEIT5_phase_rare

```bash
$ singularity exec <container> /usr/local/bin/SHAPEIT5_phase_rare
$ podman run --it --rm --entrypoint /usr/local/bin/SHAPEIT5_phase_rare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SHAPEIT5_phase_rare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SHAPEIT5_switch

```bash
$ singularity exec <container> /usr/local/bin/SHAPEIT5_switch
$ podman run --it --rm --entrypoint /usr/local/bin/SHAPEIT5_switch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SHAPEIT5_switch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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