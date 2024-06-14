---
layout: container
name:  "quay.io/biocontainers/opfi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/opfi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/opfi/container.yaml"
updated_at: "2024-06-14 02:53:33.674363"
latest: "0.1.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/opfi"
aliases:
 - "grf-alignment"
 - "grf-alignment2"
 - "grf-dbn"
 - "grf-filter"
 - "grf-intersperse"
 - "grf-main"
 - "grf-mite-cluster"
 - "grf-nest"
 - "hypothesis"
 - "pilercr"
 - "filter-table"
 - "spdi2prod"
 - "mmseqs"
 - "FET.pl"
 - "cd-hit-clstr_2_blm8.pl"
 - "clstr_list.pl"
 - "clstr_list_sort.pl"
 - "cd-hit"
 - "cd-hit-2d"
 - "cd-hit-2d-para.pl"
versions:
 - "0.1.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for opfi"
config: {"url": "https://biocontainers.pro/tools/opfi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for opfi", "latest": {"0.1.2--pyhdfd78af_0": "sha256:6e4c04a579feca5379d397e640de49cd9319c74c04e49eaa8d7f8b88e1eb3b5e"}, "tags": {"0.1.2--pyhdfd78af_0": "sha256:6e4c04a579feca5379d397e640de49cd9319c74c04e49eaa8d7f8b88e1eb3b5e"}, "docker": "quay.io/biocontainers/opfi", "aliases": {"grf-alignment": "/usr/local/bin/grf-alignment", "grf-alignment2": "/usr/local/bin/grf-alignment2", "grf-dbn": "/usr/local/bin/grf-dbn", "grf-filter": "/usr/local/bin/grf-filter", "grf-intersperse": "/usr/local/bin/grf-intersperse", "grf-main": "/usr/local/bin/grf-main", "grf-mite-cluster": "/usr/local/bin/grf-mite-cluster", "grf-nest": "/usr/local/bin/grf-nest", "hypothesis": "/usr/local/bin/hypothesis", "pilercr": "/usr/local/bin/pilercr", "filter-table": "/usr/local/bin/filter-table", "spdi2prod": "/usr/local/bin/spdi2prod", "mmseqs": "/usr/local/bin/mmseqs", "FET.pl": "/usr/local/bin/FET.pl", "cd-hit-clstr_2_blm8.pl": "/usr/local/bin/cd-hit-clstr_2_blm8.pl", "clstr_list.pl": "/usr/local/bin/clstr_list.pl", "clstr_list_sort.pl": "/usr/local/bin/clstr_list_sort.pl", "cd-hit": "/usr/local/bin/cd-hit", "cd-hit-2d": "/usr/local/bin/cd-hit-2d", "cd-hit-2d-para.pl": "/usr/local/bin/cd-hit-2d-para.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/opfi.
shpc-registry automated BioContainers addition for opfi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/opfi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/opfi:0.1.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/opfi/0.1.2--pyhdfd78af_0
$ module help quay.io/biocontainers/opfi/0.1.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### opfi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### opfi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### opfi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### opfi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### opfi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### opfi-inspect-deffile:

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


#### hypothesis

```bash
$ singularity exec <container> /usr/local/bin/hypothesis
$ podman run --it --rm --entrypoint /usr/local/bin/hypothesis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hypothesis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pilercr

```bash
$ singularity exec <container> /usr/local/bin/pilercr
$ podman run --it --rm --entrypoint /usr/local/bin/pilercr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pilercr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-table

```bash
$ singularity exec <container> /usr/local/bin/filter-table
$ podman run --it --rm --entrypoint /usr/local/bin/filter-table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spdi2prod

```bash
$ singularity exec <container> /usr/local/bin/spdi2prod
$ podman run --it --rm --entrypoint /usr/local/bin/spdi2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spdi2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mmseqs

```bash
$ singularity exec <container> /usr/local/bin/mmseqs
$ podman run --it --rm --entrypoint /usr/local/bin/mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
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