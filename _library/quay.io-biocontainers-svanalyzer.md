---
layout: container
name:  "quay.io/biocontainers/svanalyzer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/svanalyzer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/svanalyzer/container.yaml"
updated_at: "2024-11-19 03:16:01.114214"
latest: "0.36--pl5321hdfd78af_2"
container_url: "https://biocontainers.pro/tools/svanalyzer"
aliases:
 - "SVbenchmark"
 - "SVcomp"
 - "SVmerge"
 - "SVrefine"
 - "SVwiden"
 - "svanalyzer"
 - "l4p-tmpl"
 - "mapview"
 - "mgaps"
 - "run-mummer1"
 - "run-mummer3"
 - "combineMUMs"
 - "delta-filter"
 - "dnadiff"
 - "exact-tandems"
 - "mummer"
versions:
 - "0.36--pl5321hdfd78af_2"
description: "shpc-registry automated BioContainers addition for svanalyzer"
config: {"url": "https://biocontainers.pro/tools/svanalyzer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for svanalyzer", "latest": {"0.36--pl5321hdfd78af_2": "sha256:d5ddfe600cb2c6b0db9f16cfd6e4e8cffe7d708e7aa51012cb3e4fd24801af2b"}, "tags": {"0.36--pl5321hdfd78af_2": "sha256:d5ddfe600cb2c6b0db9f16cfd6e4e8cffe7d708e7aa51012cb3e4fd24801af2b"}, "docker": "quay.io/biocontainers/svanalyzer", "aliases": {"SVbenchmark": "/usr/local/bin/SVbenchmark", "SVcomp": "/usr/local/bin/SVcomp", "SVmerge": "/usr/local/bin/SVmerge", "SVrefine": "/usr/local/bin/SVrefine", "SVwiden": "/usr/local/bin/SVwiden", "svanalyzer": "/usr/local/bin/svanalyzer", "l4p-tmpl": "/usr/local/bin/l4p-tmpl", "mapview": "/usr/local/bin/mapview", "mgaps": "/usr/local/bin/mgaps", "run-mummer1": "/usr/local/bin/run-mummer1", "run-mummer3": "/usr/local/bin/run-mummer3", "combineMUMs": "/usr/local/bin/combineMUMs", "delta-filter": "/usr/local/bin/delta-filter", "dnadiff": "/usr/local/bin/dnadiff", "exact-tandems": "/usr/local/bin/exact-tandems", "mummer": "/usr/local/bin/mummer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/svanalyzer.
shpc-registry automated BioContainers addition for svanalyzer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/svanalyzer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/svanalyzer:0.36--pl5321hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/svanalyzer/0.36--pl5321hdfd78af_2
$ module help quay.io/biocontainers/svanalyzer/0.36--pl5321hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### svanalyzer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### svanalyzer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### svanalyzer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### svanalyzer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### svanalyzer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### svanalyzer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SVbenchmark

```bash
$ singularity exec <container> /usr/local/bin/SVbenchmark
$ podman run --it --rm --entrypoint /usr/local/bin/SVbenchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SVbenchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SVcomp

```bash
$ singularity exec <container> /usr/local/bin/SVcomp
$ podman run --it --rm --entrypoint /usr/local/bin/SVcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SVcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SVmerge

```bash
$ singularity exec <container> /usr/local/bin/SVmerge
$ podman run --it --rm --entrypoint /usr/local/bin/SVmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SVmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SVrefine

```bash
$ singularity exec <container> /usr/local/bin/SVrefine
$ podman run --it --rm --entrypoint /usr/local/bin/SVrefine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SVrefine   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SVwiden

```bash
$ singularity exec <container> /usr/local/bin/SVwiden
$ podman run --it --rm --entrypoint /usr/local/bin/SVwiden   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SVwiden   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svanalyzer

```bash
$ singularity exec <container> /usr/local/bin/svanalyzer
$ podman run --it --rm --entrypoint /usr/local/bin/svanalyzer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svanalyzer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### l4p-tmpl

```bash
$ singularity exec <container> /usr/local/bin/l4p-tmpl
$ podman run --it --rm --entrypoint /usr/local/bin/l4p-tmpl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/l4p-tmpl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapview

```bash
$ singularity exec <container> /usr/local/bin/mapview
$ podman run --it --rm --entrypoint /usr/local/bin/mapview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mgaps

```bash
$ singularity exec <container> /usr/local/bin/mgaps
$ podman run --it --rm --entrypoint /usr/local/bin/mgaps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mgaps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-mummer1

```bash
$ singularity exec <container> /usr/local/bin/run-mummer1
$ podman run --it --rm --entrypoint /usr/local/bin/run-mummer1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-mummer1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-mummer3

```bash
$ singularity exec <container> /usr/local/bin/run-mummer3
$ podman run --it --rm --entrypoint /usr/local/bin/run-mummer3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-mummer3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combineMUMs

```bash
$ singularity exec <container> /usr/local/bin/combineMUMs
$ podman run --it --rm --entrypoint /usr/local/bin/combineMUMs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combineMUMs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delta-filter

```bash
$ singularity exec <container> /usr/local/bin/delta-filter
$ podman run --it --rm --entrypoint /usr/local/bin/delta-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delta-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnadiff

```bash
$ singularity exec <container> /usr/local/bin/dnadiff
$ podman run --it --rm --entrypoint /usr/local/bin/dnadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exact-tandems

```bash
$ singularity exec <container> /usr/local/bin/exact-tandems
$ podman run --it --rm --entrypoint /usr/local/bin/exact-tandems   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exact-tandems   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mummer

```bash
$ singularity exec <container> /usr/local/bin/mummer
$ podman run --it --rm --entrypoint /usr/local/bin/mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
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