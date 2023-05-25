---
layout: container
name:  "quay.io/biocontainers/commet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/commet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/commet/container.yaml"
updated_at: "2023-05-25 03:23:48.610219"
latest: "24.7.14--r42hfada1a9_8"
container_url: "https://biocontainers.pro/tools/commet"
aliases:
 - "Commet.py"
 - "bvop"
 - "compare_reads"
 - "dendro.R"
 - "extract_reads"
 - "filter_reads"
 - "heatmap.r"
 - "index_and_search"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "24.7.14--r41hfada1a9_7"
 - "24.7.14--r42hfada1a9_8"
description: "shpc-registry automated BioContainers addition for commet"
config: {"url": "https://biocontainers.pro/tools/commet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for commet", "latest": {"24.7.14--r42hfada1a9_8": "sha256:fb6b30e2129a1593956647efa9585607b13ec0847bfed2d0a1937e44c3f90cb7"}, "tags": {"24.7.14--r41hfada1a9_7": "sha256:c1942271fbd8abdb58bc26d68310c1cf07e2f295678a00ef9f75b12c60052e38", "24.7.14--r42hfada1a9_8": "sha256:fb6b30e2129a1593956647efa9585607b13ec0847bfed2d0a1937e44c3f90cb7"}, "docker": "quay.io/biocontainers/commet", "aliases": {"Commet.py": "/usr/local/bin/Commet.py", "bvop": "/usr/local/bin/bvop", "compare_reads": "/usr/local/bin/compare_reads", "dendro.R": "/usr/local/bin/dendro.R", "extract_reads": "/usr/local/bin/extract_reads", "filter_reads": "/usr/local/bin/filter_reads", "heatmap.r": "/usr/local/bin/heatmap.r", "index_and_search": "/usr/local/bin/index_and_search", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/commet.
shpc-registry automated BioContainers addition for commet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/commet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/commet:24.7.14--r42hfada1a9_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/commet/24.7.14--r42hfada1a9_8
$ module help quay.io/biocontainers/commet/24.7.14--r42hfada1a9_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### commet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### commet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### commet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### commet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### commet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### commet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Commet.py

```bash
$ singularity exec <container> /usr/local/bin/Commet.py
$ podman run --it --rm --entrypoint /usr/local/bin/Commet.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Commet.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bvop

```bash
$ singularity exec <container> /usr/local/bin/bvop
$ podman run --it --rm --entrypoint /usr/local/bin/bvop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bvop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compare_reads

```bash
$ singularity exec <container> /usr/local/bin/compare_reads
$ podman run --it --rm --entrypoint /usr/local/bin/compare_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dendro.R

```bash
$ singularity exec <container> /usr/local/bin/dendro.R
$ podman run --it --rm --entrypoint /usr/local/bin/dendro.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dendro.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_reads

```bash
$ singularity exec <container> /usr/local/bin/extract_reads
$ podman run --it --rm --entrypoint /usr/local/bin/extract_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_reads

```bash
$ singularity exec <container> /usr/local/bin/filter_reads
$ podman run --it --rm --entrypoint /usr/local/bin/filter_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### heatmap.r

```bash
$ singularity exec <container> /usr/local/bin/heatmap.r
$ podman run --it --rm --entrypoint /usr/local/bin/heatmap.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/heatmap.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index_and_search

```bash
$ singularity exec <container> /usr/local/bin/index_and_search
$ podman run --it --rm --entrypoint /usr/local/bin/index_and_search   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index_and_search   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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