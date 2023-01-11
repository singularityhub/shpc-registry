---
layout: container
name:  "quay.io/biocontainers/panx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/panx/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/panx/container.yaml"
updated_at: "2023-01-11 20:31:07.907926"
latest: "1.6.0--py27_0"
container_url: "https://biocontainers.pro/tools/panx"
aliases:
 - "FastTree.c"
 - "ancestral_reconstruction.py"
 - "ete"
 - "panX.py"
 - "temporal_signal.py"
 - "timetree_inference.py"
 - "createfontdatachunk.py"
 - "clm"
 - "clmformat"
 - "clxdo"
 - "mcl"
 - "mclblastline"
 - "mclcm"
 - "mclpipeline"
 - "mcx"
 - "mcxarray"
versions:
 - "1.6.0--py27_0"
description: "shpc-registry automated BioContainers addition for panx"
config: {"url": "https://biocontainers.pro/tools/panx", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for panx", "latest": {"1.6.0--py27_0": "sha256:07c58714d624590440defb27a33e0472ae3fda841f7afb4af0510c281b594ee4"}, "tags": {"1.6.0--py27_0": "sha256:07c58714d624590440defb27a33e0472ae3fda841f7afb4af0510c281b594ee4"}, "docker": "quay.io/biocontainers/panx", "aliases": {"FastTree.c": "/usr/local/bin/FastTree.c", "ancestral_reconstruction.py": "/usr/local/bin/ancestral_reconstruction.py", "ete": "/usr/local/bin/ete", "panX.py": "/usr/local/bin/panX.py", "temporal_signal.py": "/usr/local/bin/temporal_signal.py", "timetree_inference.py": "/usr/local/bin/timetree_inference.py", "createfontdatachunk.py": "/usr/local/bin/createfontdatachunk.py", "clm": "/usr/local/bin/clm", "clmformat": "/usr/local/bin/clmformat", "clxdo": "/usr/local/bin/clxdo", "mcl": "/usr/local/bin/mcl", "mclblastline": "/usr/local/bin/mclblastline", "mclcm": "/usr/local/bin/mclcm", "mclpipeline": "/usr/local/bin/mclpipeline", "mcx": "/usr/local/bin/mcx", "mcxarray": "/usr/local/bin/mcxarray"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/panx.
shpc-registry automated BioContainers addition for panx
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/panx
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/panx:1.6.0--py27_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/panx/1.6.0--py27_0
$ module help quay.io/biocontainers/panx/1.6.0--py27_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### panx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### panx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### panx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### panx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### panx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### panx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### FastTree.c

```bash
$ singularity exec <container> /usr/local/bin/FastTree.c
$ podman run --it --rm --entrypoint /usr/local/bin/FastTree.c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTree.c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ancestral_reconstruction.py

```bash
$ singularity exec <container> /usr/local/bin/ancestral_reconstruction.py
$ podman run --it --rm --entrypoint /usr/local/bin/ancestral_reconstruction.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ancestral_reconstruction.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ete

```bash
$ singularity exec <container> /usr/local/bin/ete
$ podman run --it --rm --entrypoint /usr/local/bin/ete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### panX.py

```bash
$ singularity exec <container> /usr/local/bin/panX.py
$ podman run --it --rm --entrypoint /usr/local/bin/panX.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/panX.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### temporal_signal.py

```bash
$ singularity exec <container> /usr/local/bin/temporal_signal.py
$ podman run --it --rm --entrypoint /usr/local/bin/temporal_signal.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/temporal_signal.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### timetree_inference.py

```bash
$ singularity exec <container> /usr/local/bin/timetree_inference.py
$ podman run --it --rm --entrypoint /usr/local/bin/timetree_inference.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/timetree_inference.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### createfontdatachunk.py

```bash
$ singularity exec <container> /usr/local/bin/createfontdatachunk.py
$ podman run --it --rm --entrypoint /usr/local/bin/createfontdatachunk.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/createfontdatachunk.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clm

```bash
$ singularity exec <container> /usr/local/bin/clm
$ podman run --it --rm --entrypoint /usr/local/bin/clm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clmformat

```bash
$ singularity exec <container> /usr/local/bin/clmformat
$ podman run --it --rm --entrypoint /usr/local/bin/clmformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clmformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clxdo

```bash
$ singularity exec <container> /usr/local/bin/clxdo
$ podman run --it --rm --entrypoint /usr/local/bin/clxdo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clxdo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcl

```bash
$ singularity exec <container> /usr/local/bin/mcl
$ podman run --it --rm --entrypoint /usr/local/bin/mcl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclblastline

```bash
$ singularity exec <container> /usr/local/bin/mclblastline
$ podman run --it --rm --entrypoint /usr/local/bin/mclblastline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclblastline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclcm

```bash
$ singularity exec <container> /usr/local/bin/mclcm
$ podman run --it --rm --entrypoint /usr/local/bin/mclcm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclcm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclpipeline

```bash
$ singularity exec <container> /usr/local/bin/mclpipeline
$ podman run --it --rm --entrypoint /usr/local/bin/mclpipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclpipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcx

```bash
$ singularity exec <container> /usr/local/bin/mcx
$ podman run --it --rm --entrypoint /usr/local/bin/mcx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxarray

```bash
$ singularity exec <container> /usr/local/bin/mcxarray
$ podman run --it --rm --entrypoint /usr/local/bin/mcxarray   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxarray   -v ${PWD} -w ${PWD} <container> -c " $@"
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