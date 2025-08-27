---
layout: container
name:  "quay.io/biocontainers/sambamba"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sambamba/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sambamba/container.yaml"
updated_at: "2025-08-27 03:24:10.497076"
latest: "1.0.1--he614052_4"
container_url: "https://biocontainers.pro/tools/sambamba"
aliases:
 - "ldc-build-runtime"
 - "ldc-profdata"
 - "ldc-prune-cache"
 - "ldc2"
 - "ldmd2"
 - "sambamba"
versions:
 - "0.6.9--h89e63da_0"
 - "0.7.1--h984e79f_3"
 - "0.8.2--h98b6b92_2"
 - "1.0--h98b6b92_0"
 - "1.0.1--h6f6fda4_0"
 - "1.0.1--h6f6fda4_2"
 - "1.0.1--he614052_3"
 - "1.0.1--he614052_4"
description: "shpc-registry automated BioContainers addition for sambamba"
config: {"url": "https://biocontainers.pro/tools/sambamba", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sambamba", "latest": {"1.0.1--he614052_4": "sha256:c10cc00a218b682cf8d5a255fd53a5e73ef6f5f720a12e20b354b040a6a33fe9"}, "tags": {"0.6.9--h89e63da_0": "sha256:9b92e2f14ae15436430922783e08d695067eb248f10eb6dc83f6a8496b030635", "0.7.1--h984e79f_3": "sha256:9ec72d3d0991c4209830e4ff17937986808c64c430780071559e7072e8317ab3", "0.8.2--h98b6b92_2": "sha256:7eef9b8c037f526a3ecb71cc05604c77eda72d90a50ca29c0af42a6e94580073", "1.0--h98b6b92_0": "sha256:bfceddf000b9ca1a2d5250098f6d8fdeb7ca4481626da140e42f379ca71d75f9", "1.0.1--h6f6fda4_0": "sha256:97fa815aa116595c31e6656447424e5be53eaca8d8174b0c110c64ad2c5adffc", "1.0.1--h6f6fda4_2": "sha256:1961ef9548ed3a76e5000bc11387fc54d4606750409ee3433b5045e3ddb8e677", "1.0.1--he614052_3": "sha256:812c41eb9f80ab7be8c1077b9d9ac5aa491ac0fd5b1367bdbb4c5cc996d86ef8", "1.0.1--he614052_4": "sha256:c10cc00a218b682cf8d5a255fd53a5e73ef6f5f720a12e20b354b040a6a33fe9"}, "docker": "quay.io/biocontainers/sambamba", "aliases": {"ldc-build-runtime": "/usr/local/bin/ldc-build-runtime", "ldc-profdata": "/usr/local/bin/ldc-profdata", "ldc-prune-cache": "/usr/local/bin/ldc-prune-cache", "ldc2": "/usr/local/bin/ldc2", "ldmd2": "/usr/local/bin/ldmd2", "sambamba": "/usr/local/bin/sambamba"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sambamba.
shpc-registry automated BioContainers addition for sambamba
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sambamba
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sambamba:1.0.1--he614052_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sambamba/1.0.1--he614052_4
$ module help quay.io/biocontainers/sambamba/1.0.1--he614052_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sambamba-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sambamba-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sambamba-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sambamba-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sambamba-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sambamba-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ldc-build-runtime

```bash
$ singularity exec <container> /usr/local/bin/ldc-build-runtime
$ podman run --it --rm --entrypoint /usr/local/bin/ldc-build-runtime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldc-build-runtime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldc-profdata

```bash
$ singularity exec <container> /usr/local/bin/ldc-profdata
$ podman run --it --rm --entrypoint /usr/local/bin/ldc-profdata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldc-profdata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldc-prune-cache

```bash
$ singularity exec <container> /usr/local/bin/ldc-prune-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ldc-prune-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldc-prune-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldc2

```bash
$ singularity exec <container> /usr/local/bin/ldc2
$ podman run --it --rm --entrypoint /usr/local/bin/ldc2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldc2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldmd2

```bash
$ singularity exec <container> /usr/local/bin/ldmd2
$ podman run --it --rm --entrypoint /usr/local/bin/ldmd2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldmd2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sambamba

```bash
$ singularity exec <container> /usr/local/bin/sambamba
$ podman run --it --rm --entrypoint /usr/local/bin/sambamba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sambamba   -v ${PWD} -w ${PWD} <container> -c " $@"
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