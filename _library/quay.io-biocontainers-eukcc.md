---
layout: container
name:  "quay.io/biocontainers/eukcc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/eukcc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/eukcc/container.yaml"
updated_at: "2023-10-20 03:27:45.191550"
latest: "2.1.0--pypyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/eukcc"
aliases:
 - "binlinks.py"
 - "epa-ng"
 - "eukcc"
 - "filter_euk_bins.py"
 - "metaeuk"
 - "shared_markers"
 - "rppr"
 - "guppy"
 - "pplacer"
 - "ete3"
 - "gawk-5.1.0"
 - "xkbcli"
 - "awk"
 - "gawk"
 - "pg_config"
 - "qdistancefieldgenerator"
versions:
 - "2.1.0--pypyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for eukcc"
config: {"url": "https://biocontainers.pro/tools/eukcc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for eukcc", "latest": {"2.1.0--pypyhdfd78af_0": "sha256:5d12324186ac9d29b62326338aba059c97e51094fc51e87447f61d0b46cb96d4"}, "tags": {"2.1.0--pypyhdfd78af_0": "sha256:5d12324186ac9d29b62326338aba059c97e51094fc51e87447f61d0b46cb96d4"}, "docker": "quay.io/biocontainers/eukcc", "aliases": {"binlinks.py": "/usr/local/bin/binlinks.py", "epa-ng": "/usr/local/bin/epa-ng", "eukcc": "/usr/local/bin/eukcc", "filter_euk_bins.py": "/usr/local/bin/filter_euk_bins.py", "metaeuk": "/usr/local/bin/metaeuk", "shared_markers": "/usr/local/bin/shared_markers", "rppr": "/usr/local/bin/rppr", "guppy": "/usr/local/bin/guppy", "pplacer": "/usr/local/bin/pplacer", "ete3": "/usr/local/bin/ete3", "gawk-5.1.0": "/usr/local/bin/gawk-5.1.0", "xkbcli": "/usr/local/bin/xkbcli", "awk": "/usr/local/bin/awk", "gawk": "/usr/local/bin/gawk", "pg_config": "/usr/local/bin/pg_config", "qdistancefieldgenerator": "/usr/local/bin/qdistancefieldgenerator"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/eukcc.
shpc-registry automated BioContainers addition for eukcc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/eukcc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/eukcc:2.1.0--pypyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/eukcc/2.1.0--pypyhdfd78af_0
$ module help quay.io/biocontainers/eukcc/2.1.0--pypyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### eukcc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### eukcc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### eukcc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### eukcc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### eukcc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### eukcc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### binlinks.py

```bash
$ singularity exec <container> /usr/local/bin/binlinks.py
$ podman run --it --rm --entrypoint /usr/local/bin/binlinks.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/binlinks.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### epa-ng

```bash
$ singularity exec <container> /usr/local/bin/epa-ng
$ podman run --it --rm --entrypoint /usr/local/bin/epa-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/epa-ng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eukcc

```bash
$ singularity exec <container> /usr/local/bin/eukcc
$ podman run --it --rm --entrypoint /usr/local/bin/eukcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eukcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_euk_bins.py

```bash
$ singularity exec <container> /usr/local/bin/filter_euk_bins.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter_euk_bins.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_euk_bins.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaeuk

```bash
$ singularity exec <container> /usr/local/bin/metaeuk
$ podman run --it --rm --entrypoint /usr/local/bin/metaeuk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaeuk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shared_markers

```bash
$ singularity exec <container> /usr/local/bin/shared_markers
$ podman run --it --rm --entrypoint /usr/local/bin/shared_markers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shared_markers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rppr

```bash
$ singularity exec <container> /usr/local/bin/rppr
$ podman run --it --rm --entrypoint /usr/local/bin/rppr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rppr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guppy

```bash
$ singularity exec <container> /usr/local/bin/guppy
$ podman run --it --rm --entrypoint /usr/local/bin/guppy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guppy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pplacer

```bash
$ singularity exec <container> /usr/local/bin/pplacer
$ podman run --it --rm --entrypoint /usr/local/bin/pplacer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pplacer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ete3

```bash
$ singularity exec <container> /usr/local/bin/ete3
$ podman run --it --rm --entrypoint /usr/local/bin/ete3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ete3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.1.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xkbcli

```bash
$ singularity exec <container> /usr/local/bin/xkbcli
$ podman run --it --rm --entrypoint /usr/local/bin/xkbcli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xkbcli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### awk

```bash
$ singularity exec <container> /usr/local/bin/awk
$ podman run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk

```bash
$ singularity exec <container> /usr/local/bin/gawk
$ podman run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_config

```bash
$ singularity exec <container> /usr/local/bin/pg_config
$ podman run --it --rm --entrypoint /usr/local/bin/pg_config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdistancefieldgenerator

```bash
$ singularity exec <container> /usr/local/bin/qdistancefieldgenerator
$ podman run --it --rm --entrypoint /usr/local/bin/qdistancefieldgenerator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdistancefieldgenerator   -v ${PWD} -w ${PWD} <container> -c " $@"
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