---
layout: container
name:  "quay.io/biocontainers/baredsc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/baredsc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/baredsc/container.yaml"
updated_at: "2025-01-09 03:15:49.150843"
latest: "1.1.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/baredsc"
aliases:
 - "baredSC_1d"
 - "baredSC_2d"
 - "combineMultipleModels_1d"
 - "combineMultipleModels_2d"
 - "nc3tonc4"
 - "nc4tonc3"
 - "ncinfo"
 - "zipcmp"
 - "zipmerge"
 - "ziptool"
 - "natsort"
 - "gif2hdf"
 - "h4_ncdump"
 - "h4_ncgen"
 - "h4cc"
 - "h4redeploy"
 - "hdf24to8"
versions:
 - "1.1.1--pyhdfd78af_0"
 - "1.1.2--pyhdfd78af_0"
 - "1.1.3--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for baredsc"
config: {"url": "https://biocontainers.pro/tools/baredsc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for baredsc", "latest": {"1.1.3--pyhdfd78af_0": "sha256:47eb4534c9b41abf8ba7089167c3c55af0ded5f28183db4f8b846e2e485562be"}, "tags": {"1.1.1--pyhdfd78af_0": "sha256:7c68e8bc91e75aab98e1d869807c9940fac36eabede9240b1b33fb5d11345967", "1.1.2--pyhdfd78af_0": "sha256:a03c2697b335154c3327fa9cea97acbf17913151e296adbe6cd886695cc23a2f", "1.1.3--pyhdfd78af_0": "sha256:47eb4534c9b41abf8ba7089167c3c55af0ded5f28183db4f8b846e2e485562be"}, "docker": "quay.io/biocontainers/baredsc", "aliases": {"baredSC_1d": "/usr/local/bin/baredSC_1d", "baredSC_2d": "/usr/local/bin/baredSC_2d", "combineMultipleModels_1d": "/usr/local/bin/combineMultipleModels_1d", "combineMultipleModels_2d": "/usr/local/bin/combineMultipleModels_2d", "nc3tonc4": "/usr/local/bin/nc3tonc4", "nc4tonc3": "/usr/local/bin/nc4tonc3", "ncinfo": "/usr/local/bin/ncinfo", "zipcmp": "/usr/local/bin/zipcmp", "zipmerge": "/usr/local/bin/zipmerge", "ziptool": "/usr/local/bin/ziptool", "natsort": "/usr/local/bin/natsort", "gif2hdf": "/usr/local/bin/gif2hdf", "h4_ncdump": "/usr/local/bin/h4_ncdump", "h4_ncgen": "/usr/local/bin/h4_ncgen", "h4cc": "/usr/local/bin/h4cc", "h4redeploy": "/usr/local/bin/h4redeploy", "hdf24to8": "/usr/local/bin/hdf24to8"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/baredsc.
shpc-registry automated BioContainers addition for baredsc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/baredsc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/baredsc:1.1.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/baredsc/1.1.3--pyhdfd78af_0
$ module help quay.io/biocontainers/baredsc/1.1.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### baredsc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### baredsc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### baredsc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### baredsc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### baredsc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### baredsc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### baredSC_1d

```bash
$ singularity exec <container> /usr/local/bin/baredSC_1d
$ podman run --it --rm --entrypoint /usr/local/bin/baredSC_1d   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/baredSC_1d   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### baredSC_2d

```bash
$ singularity exec <container> /usr/local/bin/baredSC_2d
$ podman run --it --rm --entrypoint /usr/local/bin/baredSC_2d   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/baredSC_2d   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combineMultipleModels_1d

```bash
$ singularity exec <container> /usr/local/bin/combineMultipleModels_1d
$ podman run --it --rm --entrypoint /usr/local/bin/combineMultipleModels_1d   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineMultipleModels_1d   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combineMultipleModels_2d

```bash
$ singularity exec <container> /usr/local/bin/combineMultipleModels_2d
$ podman run --it --rm --entrypoint /usr/local/bin/combineMultipleModels_2d   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineMultipleModels_2d   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nc3tonc4

```bash
$ singularity exec <container> /usr/local/bin/nc3tonc4
$ podman run --it --rm --entrypoint /usr/local/bin/nc3tonc4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nc3tonc4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nc4tonc3

```bash
$ singularity exec <container> /usr/local/bin/nc4tonc3
$ podman run --it --rm --entrypoint /usr/local/bin/nc4tonc3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nc4tonc3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncinfo

```bash
$ singularity exec <container> /usr/local/bin/ncinfo
$ podman run --it --rm --entrypoint /usr/local/bin/ncinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipcmp

```bash
$ singularity exec <container> /usr/local/bin/zipcmp
$ podman run --it --rm --entrypoint /usr/local/bin/zipcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipmerge

```bash
$ singularity exec <container> /usr/local/bin/zipmerge
$ podman run --it --rm --entrypoint /usr/local/bin/zipmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ziptool

```bash
$ singularity exec <container> /usr/local/bin/ziptool
$ podman run --it --rm --entrypoint /usr/local/bin/ziptool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ziptool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### natsort

```bash
$ singularity exec <container> /usr/local/bin/natsort
$ podman run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2hdf

```bash
$ singularity exec <container> /usr/local/bin/gif2hdf
$ podman run --it --rm --entrypoint /usr/local/bin/gif2hdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2hdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h4_ncdump

```bash
$ singularity exec <container> /usr/local/bin/h4_ncdump
$ podman run --it --rm --entrypoint /usr/local/bin/h4_ncdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h4_ncdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h4_ncgen

```bash
$ singularity exec <container> /usr/local/bin/h4_ncgen
$ podman run --it --rm --entrypoint /usr/local/bin/h4_ncgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h4_ncgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h4cc

```bash
$ singularity exec <container> /usr/local/bin/h4cc
$ podman run --it --rm --entrypoint /usr/local/bin/h4cc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h4cc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h4redeploy

```bash
$ singularity exec <container> /usr/local/bin/h4redeploy
$ podman run --it --rm --entrypoint /usr/local/bin/h4redeploy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h4redeploy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdf24to8

```bash
$ singularity exec <container> /usr/local/bin/hdf24to8
$ podman run --it --rm --entrypoint /usr/local/bin/hdf24to8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdf24to8   -v ${PWD} -w ${PWD} <container> -c " $@"
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