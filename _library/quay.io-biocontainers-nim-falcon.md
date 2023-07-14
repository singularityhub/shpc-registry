---
layout: container
name:  "quay.io/biocontainers/nim-falcon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nim-falcon/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nim-falcon/container.yaml"
updated_at: "2023-07-14 03:14:12.964612"
latest: "3.0.2--h18d090a_1"
container_url: "https://biocontainers.pro/tools/nim-falcon"
aliases:
 - "falconc"
 - "fc_consensus.exe"
 - "fc_rr_hctg_track.exe"
 - "fc_rr_hctg_track2.exe"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "3.0.2--h18d090a_1"
description: "shpc-registry automated BioContainers addition for nim-falcon"
config: {"url": "https://biocontainers.pro/tools/nim-falcon", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nim-falcon", "latest": {"3.0.2--h18d090a_1": "sha256:c31482c31b6c24d54e67875be8da35f328897ccea22542cc5335ed4376cfe348"}, "tags": {"3.0.2--h18d090a_1": "sha256:c31482c31b6c24d54e67875be8da35f328897ccea22542cc5335ed4376cfe348"}, "docker": "quay.io/biocontainers/nim-falcon", "aliases": {"falconc": "/usr/local/bin/falconc", "fc_consensus.exe": "/usr/local/bin/fc_consensus.exe", "fc_rr_hctg_track.exe": "/usr/local/bin/fc_rr_hctg_track.exe", "fc_rr_hctg_track2.exe": "/usr/local/bin/fc_rr_hctg_track2.exe", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nim-falcon.
shpc-registry automated BioContainers addition for nim-falcon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nim-falcon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nim-falcon:3.0.2--h18d090a_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nim-falcon/3.0.2--h18d090a_1
$ module help quay.io/biocontainers/nim-falcon/3.0.2--h18d090a_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nim-falcon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nim-falcon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nim-falcon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nim-falcon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nim-falcon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nim-falcon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### falconc

```bash
$ singularity exec <container> /usr/local/bin/falconc
$ podman run --it --rm --entrypoint /usr/local/bin/falconc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/falconc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc_consensus.exe

```bash
$ singularity exec <container> /usr/local/bin/fc_consensus.exe
$ podman run --it --rm --entrypoint /usr/local/bin/fc_consensus.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc_consensus.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc_rr_hctg_track.exe

```bash
$ singularity exec <container> /usr/local/bin/fc_rr_hctg_track.exe
$ podman run --it --rm --entrypoint /usr/local/bin/fc_rr_hctg_track.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc_rr_hctg_track.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc_rr_hctg_track2.exe

```bash
$ singularity exec <container> /usr/local/bin/fc_rr_hctg_track2.exe
$ podman run --it --rm --entrypoint /usr/local/bin/fc_rr_hctg_track2.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc_rr_hctg_track2.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
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