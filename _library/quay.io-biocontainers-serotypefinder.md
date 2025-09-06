---
layout: container
name:  "quay.io/biocontainers/serotypefinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/serotypefinder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/serotypefinder/container.yaml"
updated_at: "2025-09-06 03:31:28.368633"
latest: "2.0.2--py312hdfd78af_1"
container_url: "https://biocontainers.pro/tools/serotypefinder"
aliases:
 - "kma"
 - "kma_index"
 - "kma_shm"
 - "kma_update"
 - "serotypefinder"
 - "update-serotypefinder-db"
 - "CA.pm"
 - "cacert.pem"
 - "index-themes"
 - "tabulate"
 - "fetch-extras"
 - "go.mod"
 - "go.sum"
 - "hlp-xtract.txt"
 - "index-extras"
 - "pm-collect"
versions:
 - "2.0.1--py39hdfd78af_0"
 - "2.0.2--py312hdfd78af_1"
description: "shpc-registry automated BioContainers addition for serotypefinder"
config: {"url": "https://biocontainers.pro/tools/serotypefinder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for serotypefinder", "latest": {"2.0.2--py312hdfd78af_1": "sha256:3a4953edfbcb7e22226aefc1c785310145e448eb0f3f89297e3d845f14794b05"}, "tags": {"2.0.1--py39hdfd78af_0": "sha256:04d3dd31d77ca3f0d2d35dfb090c2beccad959f07fb9fe87a0c6db2d0650f99a", "2.0.2--py312hdfd78af_1": "sha256:3a4953edfbcb7e22226aefc1c785310145e448eb0f3f89297e3d845f14794b05"}, "docker": "quay.io/biocontainers/serotypefinder", "aliases": {"kma": "/usr/local/bin/kma", "kma_index": "/usr/local/bin/kma_index", "kma_shm": "/usr/local/bin/kma_shm", "kma_update": "/usr/local/bin/kma_update", "serotypefinder": "/usr/local/bin/serotypefinder", "update-serotypefinder-db": "/usr/local/bin/update-serotypefinder-db", "CA.pm": "/usr/local/bin/CA.pm", "cacert.pem": "/usr/local/bin/cacert.pem", "index-themes": "/usr/local/bin/index-themes", "tabulate": "/usr/local/bin/tabulate", "fetch-extras": "/usr/local/bin/fetch-extras", "go.mod": "/usr/local/bin/go.mod", "go.sum": "/usr/local/bin/go.sum", "hlp-xtract.txt": "/usr/local/bin/hlp-xtract.txt", "index-extras": "/usr/local/bin/index-extras", "pm-collect": "/usr/local/bin/pm-collect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/serotypefinder.
shpc-registry automated BioContainers addition for serotypefinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/serotypefinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/serotypefinder:2.0.2--py312hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/serotypefinder/2.0.2--py312hdfd78af_1
$ module help quay.io/biocontainers/serotypefinder/2.0.2--py312hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### serotypefinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### serotypefinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### serotypefinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### serotypefinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### serotypefinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### serotypefinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kma

```bash
$ singularity exec <container> /usr/local/bin/kma
$ podman run --it --rm --entrypoint /usr/local/bin/kma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_index

```bash
$ singularity exec <container> /usr/local/bin/kma_index
$ podman run --it --rm --entrypoint /usr/local/bin/kma_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_shm

```bash
$ singularity exec <container> /usr/local/bin/kma_shm
$ podman run --it --rm --entrypoint /usr/local/bin/kma_shm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_shm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kma_update

```bash
$ singularity exec <container> /usr/local/bin/kma_update
$ podman run --it --rm --entrypoint /usr/local/bin/kma_update   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kma_update   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### serotypefinder

```bash
$ singularity exec <container> /usr/local/bin/serotypefinder
$ podman run --it --rm --entrypoint /usr/local/bin/serotypefinder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/serotypefinder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### update-serotypefinder-db

```bash
$ singularity exec <container> /usr/local/bin/update-serotypefinder-db
$ podman run --it --rm --entrypoint /usr/local/bin/update-serotypefinder-db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/update-serotypefinder-db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CA.pm

```bash
$ singularity exec <container> /usr/local/bin/CA.pm
$ podman run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cacert.pem

```bash
$ singularity exec <container> /usr/local/bin/cacert.pem
$ podman run --it --rm --entrypoint /usr/local/bin/cacert.pem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cacert.pem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index-themes

```bash
$ singularity exec <container> /usr/local/bin/index-themes
$ podman run --it --rm --entrypoint /usr/local/bin/index-themes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index-themes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabulate

```bash
$ singularity exec <container> /usr/local/bin/tabulate
$ podman run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch-extras

```bash
$ singularity exec <container> /usr/local/bin/fetch-extras
$ podman run --it --rm --entrypoint /usr/local/bin/fetch-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go.mod

```bash
$ singularity exec <container> /usr/local/bin/go.mod
$ podman run --it --rm --entrypoint /usr/local/bin/go.mod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go.mod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go.sum

```bash
$ singularity exec <container> /usr/local/bin/go.sum
$ podman run --it --rm --entrypoint /usr/local/bin/go.sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go.sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hlp-xtract.txt

```bash
$ singularity exec <container> /usr/local/bin/hlp-xtract.txt
$ podman run --it --rm --entrypoint /usr/local/bin/hlp-xtract.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hlp-xtract.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index-extras

```bash
$ singularity exec <container> /usr/local/bin/index-extras
$ podman run --it --rm --entrypoint /usr/local/bin/index-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pm-collect

```bash
$ singularity exec <container> /usr/local/bin/pm-collect
$ podman run --it --rm --entrypoint /usr/local/bin/pm-collect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pm-collect   -v ${PWD} -w ${PWD} <container> -c " $@"
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