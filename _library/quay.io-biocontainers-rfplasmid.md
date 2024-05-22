---
layout: container
name:  "quay.io/biocontainers/rfplasmid"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rfplasmid/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rfplasmid/container.yaml"
updated_at: "2024-05-22 02:37:24.323904"
latest: "0.0.18--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/rfplasmid"
aliases:
 - "checkm"
 - "rfplasmid"
 - "rppr"
 - "guppy"
 - "pplacer"
 - "dendropy-format"
 - "jellyfish"
 - "sumlabels.py"
 - "sumtrees.py"
 - "diamond"
 - "prodigal"
 - "hmmpgmd_shard"
versions:
 - "0.0.18--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for rfplasmid"
config: {"url": "https://biocontainers.pro/tools/rfplasmid", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rfplasmid", "latest": {"0.0.18--pyhdfd78af_0": "sha256:037bef18bcae57e403e40856d6434c08441a17ff24f1e62b8b9a7139843de870"}, "tags": {"0.0.18--pyhdfd78af_0": "sha256:037bef18bcae57e403e40856d6434c08441a17ff24f1e62b8b9a7139843de870"}, "docker": "quay.io/biocontainers/rfplasmid", "aliases": {"checkm": "/usr/local/bin/checkm", "rfplasmid": "/usr/local/bin/rfplasmid", "rppr": "/usr/local/bin/rppr", "guppy": "/usr/local/bin/guppy", "pplacer": "/usr/local/bin/pplacer", "dendropy-format": "/usr/local/bin/dendropy-format", "jellyfish": "/usr/local/bin/jellyfish", "sumlabels.py": "/usr/local/bin/sumlabels.py", "sumtrees.py": "/usr/local/bin/sumtrees.py", "diamond": "/usr/local/bin/diamond", "prodigal": "/usr/local/bin/prodigal", "hmmpgmd_shard": "/usr/local/bin/hmmpgmd_shard"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rfplasmid.
shpc-registry automated BioContainers addition for rfplasmid
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rfplasmid
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rfplasmid:0.0.18--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rfplasmid/0.0.18--pyhdfd78af_0
$ module help quay.io/biocontainers/rfplasmid/0.0.18--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rfplasmid-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rfplasmid-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rfplasmid-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rfplasmid-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rfplasmid-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rfplasmid-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### checkm

```bash
$ singularity exec <container> /usr/local/bin/checkm
$ podman run --it --rm --entrypoint /usr/local/bin/checkm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rfplasmid

```bash
$ singularity exec <container> /usr/local/bin/rfplasmid
$ podman run --it --rm --entrypoint /usr/local/bin/rfplasmid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rfplasmid   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### dendropy-format

```bash
$ singularity exec <container> /usr/local/bin/dendropy-format
$ podman run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dendropy-format   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jellyfish

```bash
$ singularity exec <container> /usr/local/bin/jellyfish
$ podman run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumlabels.py

```bash
$ singularity exec <container> /usr/local/bin/sumlabels.py
$ podman run --it --rm --entrypoint /usr/local/bin/sumlabels.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumlabels.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sumtrees.py

```bash
$ singularity exec <container> /usr/local/bin/sumtrees.py
$ podman run --it --rm --entrypoint /usr/local/bin/sumtrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sumtrees.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diamond

```bash
$ singularity exec <container> /usr/local/bin/diamond
$ podman run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prodigal

```bash
$ singularity exec <container> /usr/local/bin/prodigal
$ podman run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmpgmd_shard

```bash
$ singularity exec <container> /usr/local/bin/hmmpgmd_shard
$ podman run --it --rm --entrypoint /usr/local/bin/hmmpgmd_shard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmpgmd_shard   -v ${PWD} -w ${PWD} <container> -c " $@"
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