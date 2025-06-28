---
layout: container
name:  "quay.io/biocontainers/daligner"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/daligner/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/daligner/container.yaml"
updated_at: "2025-06-28 03:39:10.508054"
latest: "1.0.20230620--h7b50bb2_1"
container_url: "https://biocontainers.pro/tools/daligner"
aliases:
 - "HPC.daligner"
 - "LAcat"
 - "LAcheck"
 - "LAdump"
 - "LAindex"
 - "LAmerge"
 - "LAshow"
 - "LAsort"
 - "LAsplit"
 - "daligner"
versions:
 - "1.0p2--h470a237_1"
 - "1.0.20200322--hec16e2b_2"
 - "1.0.20200322--hec16e2b_3"
 - "1.0.20200322--h031d066_4"
 - "1.0.20230620--h031d066_0"
 - "1.0.20230620--h7b50bb2_1"
description: "shpc-registry automated BioContainers addition for daligner"
config: {"url": "https://biocontainers.pro/tools/daligner", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for daligner", "latest": {"1.0.20230620--h7b50bb2_1": "sha256:26f6987ec43861cf1af563add41c0428f010c47f4a408c54c11c5afafa2847c3"}, "tags": {"1.0p2--h470a237_1": "sha256:31555c02cbd76d66b687b916be23403eacb50ef7d6a92931e6b480a2a23a9980", "1.0.20200322--hec16e2b_2": "sha256:328449639c1e5b3d1d97ab2edea4b9e51ab3d523b53ec249a153c579ef877186", "1.0.20200322--hec16e2b_3": "sha256:48d65260d900316fe5c0be86a38fa60bb6adac0853c6fca5c1787ae1ea9594c4", "1.0.20200322--h031d066_4": "sha256:0133b75e96165e69ffc58a80587605666aac9ef8eb7c09727d2f9d1d728a577f", "1.0.20230620--h031d066_0": "sha256:7f3ea0156a4baff089acca0ccd86b9aa35be8ad0564f9d0e82db7a3c9a3ea959", "1.0.20230620--h7b50bb2_1": "sha256:26f6987ec43861cf1af563add41c0428f010c47f4a408c54c11c5afafa2847c3"}, "docker": "quay.io/biocontainers/daligner", "aliases": {"HPC.daligner": "/usr/local/bin/HPC.daligner", "LAcat": "/usr/local/bin/LAcat", "LAcheck": "/usr/local/bin/LAcheck", "LAdump": "/usr/local/bin/LAdump", "LAindex": "/usr/local/bin/LAindex", "LAmerge": "/usr/local/bin/LAmerge", "LAshow": "/usr/local/bin/LAshow", "LAsort": "/usr/local/bin/LAsort", "LAsplit": "/usr/local/bin/LAsplit", "daligner": "/usr/local/bin/daligner"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/daligner.
shpc-registry automated BioContainers addition for daligner
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/daligner
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/daligner:1.0.20230620--h7b50bb2_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/daligner/1.0.20230620--h7b50bb2_1
$ module help quay.io/biocontainers/daligner/1.0.20230620--h7b50bb2_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### daligner-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### daligner-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### daligner-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### daligner-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### daligner-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### daligner-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### HPC.daligner

```bash
$ singularity exec <container> /usr/local/bin/HPC.daligner
$ podman run --it --rm --entrypoint /usr/local/bin/HPC.daligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HPC.daligner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LAcat

```bash
$ singularity exec <container> /usr/local/bin/LAcat
$ podman run --it --rm --entrypoint /usr/local/bin/LAcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LAcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LAcheck

```bash
$ singularity exec <container> /usr/local/bin/LAcheck
$ podman run --it --rm --entrypoint /usr/local/bin/LAcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LAcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LAdump

```bash
$ singularity exec <container> /usr/local/bin/LAdump
$ podman run --it --rm --entrypoint /usr/local/bin/LAdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LAdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LAindex

```bash
$ singularity exec <container> /usr/local/bin/LAindex
$ podman run --it --rm --entrypoint /usr/local/bin/LAindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LAindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LAmerge

```bash
$ singularity exec <container> /usr/local/bin/LAmerge
$ podman run --it --rm --entrypoint /usr/local/bin/LAmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LAmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LAshow

```bash
$ singularity exec <container> /usr/local/bin/LAshow
$ podman run --it --rm --entrypoint /usr/local/bin/LAshow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LAshow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LAsort

```bash
$ singularity exec <container> /usr/local/bin/LAsort
$ podman run --it --rm --entrypoint /usr/local/bin/LAsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LAsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LAsplit

```bash
$ singularity exec <container> /usr/local/bin/LAsplit
$ podman run --it --rm --entrypoint /usr/local/bin/LAsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LAsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### daligner

```bash
$ singularity exec <container> /usr/local/bin/daligner
$ podman run --it --rm --entrypoint /usr/local/bin/daligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/daligner   -v ${PWD} -w ${PWD} <container> -c " $@"
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