---
layout: container
name:  "quay.io/biocontainers/genericrepeatfinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genericrepeatfinder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genericrepeatfinder/container.yaml"
updated_at: "2024-01-27 02:37:25.660733"
latest: "1.0--h4ac6f70_3"
container_url: "https://biocontainers.pro/tools/genericrepeatfinder"
aliases:
 - "grf-alignment"
 - "grf-alignment2"
 - "grf-dbn"
 - "grf-filter"
 - "grf-intersperse"
 - "grf-main"
 - "grf-mite-cluster"
 - "grf-nest"
 - "FET.pl"
 - "cd-hit-clstr_2_blm8.pl"
 - "clstr_list.pl"
 - "clstr_list_sort.pl"
 - "cd-hit"
 - "cd-hit-2d"
 - "cd-hit-2d-para.pl"
 - "cd-hit-454"
 - "cd-hit-div"
 - "cd-hit-div.pl"
versions:
 - "1.0--h9f5acd7_2"
 - "1.0--h4ac6f70_3"
description: "shpc-registry automated BioContainers addition for genericrepeatfinder"
config: {"url": "https://biocontainers.pro/tools/genericrepeatfinder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genericrepeatfinder", "latest": {"1.0--h4ac6f70_3": "sha256:eb503bfbeddc6caefcf260acfd2f46926d562f171a6cb63af4853fb20fa4c8f5"}, "tags": {"1.0--h9f5acd7_2": "sha256:d71ebb1867d9f6d3a7b6e80f39888a3276066e76ee816bf6ef9ef2a74b888226", "1.0--h4ac6f70_3": "sha256:eb503bfbeddc6caefcf260acfd2f46926d562f171a6cb63af4853fb20fa4c8f5"}, "docker": "quay.io/biocontainers/genericrepeatfinder", "aliases": {"grf-alignment": "/usr/local/bin/grf-alignment", "grf-alignment2": "/usr/local/bin/grf-alignment2", "grf-dbn": "/usr/local/bin/grf-dbn", "grf-filter": "/usr/local/bin/grf-filter", "grf-intersperse": "/usr/local/bin/grf-intersperse", "grf-main": "/usr/local/bin/grf-main", "grf-mite-cluster": "/usr/local/bin/grf-mite-cluster", "grf-nest": "/usr/local/bin/grf-nest", "FET.pl": "/usr/local/bin/FET.pl", "cd-hit-clstr_2_blm8.pl": "/usr/local/bin/cd-hit-clstr_2_blm8.pl", "clstr_list.pl": "/usr/local/bin/clstr_list.pl", "clstr_list_sort.pl": "/usr/local/bin/clstr_list_sort.pl", "cd-hit": "/usr/local/bin/cd-hit", "cd-hit-2d": "/usr/local/bin/cd-hit-2d", "cd-hit-2d-para.pl": "/usr/local/bin/cd-hit-2d-para.pl", "cd-hit-454": "/usr/local/bin/cd-hit-454", "cd-hit-div": "/usr/local/bin/cd-hit-div", "cd-hit-div.pl": "/usr/local/bin/cd-hit-div.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genericrepeatfinder.
shpc-registry automated BioContainers addition for genericrepeatfinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genericrepeatfinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genericrepeatfinder:1.0--h4ac6f70_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genericrepeatfinder/1.0--h4ac6f70_3
$ module help quay.io/biocontainers/genericrepeatfinder/1.0--h4ac6f70_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genericrepeatfinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genericrepeatfinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genericrepeatfinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genericrepeatfinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genericrepeatfinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genericrepeatfinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### grf-alignment

```bash
$ singularity exec <container> /usr/local/bin/grf-alignment
$ podman run --it --rm --entrypoint /usr/local/bin/grf-alignment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grf-alignment   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grf-alignment2

```bash
$ singularity exec <container> /usr/local/bin/grf-alignment2
$ podman run --it --rm --entrypoint /usr/local/bin/grf-alignment2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grf-alignment2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grf-dbn

```bash
$ singularity exec <container> /usr/local/bin/grf-dbn
$ podman run --it --rm --entrypoint /usr/local/bin/grf-dbn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grf-dbn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grf-filter

```bash
$ singularity exec <container> /usr/local/bin/grf-filter
$ podman run --it --rm --entrypoint /usr/local/bin/grf-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grf-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grf-intersperse

```bash
$ singularity exec <container> /usr/local/bin/grf-intersperse
$ podman run --it --rm --entrypoint /usr/local/bin/grf-intersperse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grf-intersperse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grf-main

```bash
$ singularity exec <container> /usr/local/bin/grf-main
$ podman run --it --rm --entrypoint /usr/local/bin/grf-main   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grf-main   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grf-mite-cluster

```bash
$ singularity exec <container> /usr/local/bin/grf-mite-cluster
$ podman run --it --rm --entrypoint /usr/local/bin/grf-mite-cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grf-mite-cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grf-nest

```bash
$ singularity exec <container> /usr/local/bin/grf-nest
$ podman run --it --rm --entrypoint /usr/local/bin/grf-nest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grf-nest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FET.pl

```bash
$ singularity exec <container> /usr/local/bin/FET.pl
$ podman run --it --rm --entrypoint /usr/local/bin/FET.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FET.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-clstr_2_blm8.pl

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-clstr_2_blm8.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-clstr_2_blm8.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-clstr_2_blm8.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr_list.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr_list.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr_list.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr_list.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clstr_list_sort.pl

```bash
$ singularity exec <container> /usr/local/bin/clstr_list_sort.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clstr_list_sort.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clstr_list_sort.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit

```bash
$ singularity exec <container> /usr/local/bin/cd-hit
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-2d

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-2d
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-2d   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-2d   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-2d-para.pl

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-2d-para.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-2d-para.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-2d-para.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-454

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-454
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-454   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-454   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-div

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-div
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-div   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-div   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-div.pl

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-div.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-div.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-div.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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