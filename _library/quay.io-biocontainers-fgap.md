---
layout: container
name:  "quay.io/biocontainers/fgap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fgap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fgap/container.yaml"
updated_at: "2024-11-02 03:01:41.623384"
latest: "1.8.1--0"
container_url: "https://biocontainers.pro/tools/fgap"
aliases:
 - "FGAP"
 - "fgap.m"
 - "mkoctfile"
 - "mkoctfile-4.2.1"
 - "octave"
 - "octave-4.2.1"
 - "octave-cli"
 - "octave-cli-4.2.1"
 - "octave-config"
 - "octave-config-4.2.1"
 - "sndfile-regtest"
 - "flac"
 - "metaflac"
 - "sndfile-cmp"
 - "sndfile-concat"
 - "sndfile-convert"
 - "sndfile-deinterleave"
 - "sndfile-info"
 - "sndfile-interleave"
 - "sndfile-metadata-get"
 - "sndfile-metadata-set"
versions:
 - "1.8.1--0"
description: "shpc-registry automated BioContainers addition for fgap"
config: {"url": "https://biocontainers.pro/tools/fgap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fgap", "latest": {"1.8.1--0": "sha256:162fe3d47c71c8684d788c12d8b37532ea433efd4880e8e514e26d36af67eb3d"}, "tags": {"1.8.1--0": "sha256:162fe3d47c71c8684d788c12d8b37532ea433efd4880e8e514e26d36af67eb3d"}, "docker": "quay.io/biocontainers/fgap", "aliases": {"FGAP": "/usr/local/bin/FGAP", "fgap.m": "/usr/local/bin/fgap.m", "mkoctfile": "/usr/local/bin/mkoctfile", "mkoctfile-4.2.1": "/usr/local/bin/mkoctfile-4.2.1", "octave": "/usr/local/bin/octave", "octave-4.2.1": "/usr/local/bin/octave-4.2.1", "octave-cli": "/usr/local/bin/octave-cli", "octave-cli-4.2.1": "/usr/local/bin/octave-cli-4.2.1", "octave-config": "/usr/local/bin/octave-config", "octave-config-4.2.1": "/usr/local/bin/octave-config-4.2.1", "sndfile-regtest": "/usr/local/bin/sndfile-regtest", "flac": "/usr/local/bin/flac", "metaflac": "/usr/local/bin/metaflac", "sndfile-cmp": "/usr/local/bin/sndfile-cmp", "sndfile-concat": "/usr/local/bin/sndfile-concat", "sndfile-convert": "/usr/local/bin/sndfile-convert", "sndfile-deinterleave": "/usr/local/bin/sndfile-deinterleave", "sndfile-info": "/usr/local/bin/sndfile-info", "sndfile-interleave": "/usr/local/bin/sndfile-interleave", "sndfile-metadata-get": "/usr/local/bin/sndfile-metadata-get", "sndfile-metadata-set": "/usr/local/bin/sndfile-metadata-set"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fgap.
shpc-registry automated BioContainers addition for fgap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fgap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fgap:1.8.1--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fgap/1.8.1--0
$ module help quay.io/biocontainers/fgap/1.8.1--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fgap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fgap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fgap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fgap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fgap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fgap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### FGAP

```bash
$ singularity exec <container> /usr/local/bin/FGAP
$ podman run --it --rm --entrypoint /usr/local/bin/FGAP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FGAP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fgap.m

```bash
$ singularity exec <container> /usr/local/bin/fgap.m
$ podman run --it --rm --entrypoint /usr/local/bin/fgap.m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fgap.m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkoctfile

```bash
$ singularity exec <container> /usr/local/bin/mkoctfile
$ podman run --it --rm --entrypoint /usr/local/bin/mkoctfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkoctfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkoctfile-4.2.1

```bash
$ singularity exec <container> /usr/local/bin/mkoctfile-4.2.1
$ podman run --it --rm --entrypoint /usr/local/bin/mkoctfile-4.2.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkoctfile-4.2.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### octave

```bash
$ singularity exec <container> /usr/local/bin/octave
$ podman run --it --rm --entrypoint /usr/local/bin/octave   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/octave   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### octave-4.2.1

```bash
$ singularity exec <container> /usr/local/bin/octave-4.2.1
$ podman run --it --rm --entrypoint /usr/local/bin/octave-4.2.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/octave-4.2.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### octave-cli

```bash
$ singularity exec <container> /usr/local/bin/octave-cli
$ podman run --it --rm --entrypoint /usr/local/bin/octave-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/octave-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### octave-cli-4.2.1

```bash
$ singularity exec <container> /usr/local/bin/octave-cli-4.2.1
$ podman run --it --rm --entrypoint /usr/local/bin/octave-cli-4.2.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/octave-cli-4.2.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### octave-config

```bash
$ singularity exec <container> /usr/local/bin/octave-config
$ podman run --it --rm --entrypoint /usr/local/bin/octave-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/octave-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### octave-config-4.2.1

```bash
$ singularity exec <container> /usr/local/bin/octave-config-4.2.1
$ podman run --it --rm --entrypoint /usr/local/bin/octave-config-4.2.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/octave-config-4.2.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-regtest

```bash
$ singularity exec <container> /usr/local/bin/sndfile-regtest
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-regtest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-regtest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flac

```bash
$ singularity exec <container> /usr/local/bin/flac
$ podman run --it --rm --entrypoint /usr/local/bin/flac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaflac

```bash
$ singularity exec <container> /usr/local/bin/metaflac
$ podman run --it --rm --entrypoint /usr/local/bin/metaflac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaflac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-cmp

```bash
$ singularity exec <container> /usr/local/bin/sndfile-cmp
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-cmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-cmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-concat

```bash
$ singularity exec <container> /usr/local/bin/sndfile-concat
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-concat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-concat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-convert

```bash
$ singularity exec <container> /usr/local/bin/sndfile-convert
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-deinterleave

```bash
$ singularity exec <container> /usr/local/bin/sndfile-deinterleave
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-deinterleave   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-deinterleave   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-info

```bash
$ singularity exec <container> /usr/local/bin/sndfile-info
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-interleave

```bash
$ singularity exec <container> /usr/local/bin/sndfile-interleave
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-interleave   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-interleave   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-metadata-get

```bash
$ singularity exec <container> /usr/local/bin/sndfile-metadata-get
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-metadata-get   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-metadata-get   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sndfile-metadata-set

```bash
$ singularity exec <container> /usr/local/bin/sndfile-metadata-set
$ podman run --it --rm --entrypoint /usr/local/bin/sndfile-metadata-set   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sndfile-metadata-set   -v ${PWD} -w ${PWD} <container> -c " $@"
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