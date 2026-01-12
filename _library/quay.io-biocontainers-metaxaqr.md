---
layout: container
name:  "quay.io/biocontainers/metaxaqr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metaxaqr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metaxaqr/container.yaml"
updated_at: "2026-01-12 04:20:07.176286"
latest: "3.0rc2--py314pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/metaxaqr"
aliases:
 - "get_fasta"
 - "metaxaQR"
 - "metaxaQR_c"
 - "metaxaQR_dbb"
 - "metaxaQR_dc"
 - "metaxaQR_install_database"
 - "metaxaQR_rf"
 - "metaxaQR_si"
 - "metaxaQR_ttt"
 - "metaxaQR_uc"
 - "metaxaQR_x"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "gawk-5.3.1"
 - "vsearch"
 - "gawkbug"
 - "shmemrun"
 - "oshCC"
 - "oshc++"
 - "oshcxx"
 - "shmemCC"
 - "shmemc++"
 - "shmemcxx"
 - "oshcc"
 - "oshfort"
 - "oshmem_info"
 - "oshrun"
 - "shmemcc"
 - "shmemfort"
 - "aggregate_profile.pl"
 - "profile2mat.pl"
 - "ompi-clean"
 - "ompi-server"
 - "orte-clean"
versions:
 - "3.0rc1.1--py314pl5321hdfd78af_0"
 - "3.0rc2--py314pl5321hdfd78af_0"
description: "singularity registry hpc automated addition for metaxaqr"
config: {"url": "https://biocontainers.pro/tools/metaxaqr", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for metaxaqr", "latest": {"3.0rc2--py314pl5321hdfd78af_0": "sha256:b85a9c48b2140f67ceb08d8dc8167a482d6f202520ff1b63121aa80b6f412cd6"}, "tags": {"3.0rc1.1--py314pl5321hdfd78af_0": "sha256:31d8fc942b714d93594806d6bd6b58801783c5341748d14bc87a19d8a7c16812", "3.0rc2--py314pl5321hdfd78af_0": "sha256:b85a9c48b2140f67ceb08d8dc8167a482d6f202520ff1b63121aa80b6f412cd6"}, "docker": "quay.io/biocontainers/metaxaqr", "aliases": {"get_fasta": "/usr/local/bin/get_fasta", "metaxaQR": "/usr/local/bin/metaxaQR", "metaxaQR_c": "/usr/local/bin/metaxaQR_c", "metaxaQR_dbb": "/usr/local/bin/metaxaQR_dbb", "metaxaQR_dc": "/usr/local/bin/metaxaQR_dc", "metaxaQR_install_database": "/usr/local/bin/metaxaQR_install_database", "metaxaQR_rf": "/usr/local/bin/metaxaQR_rf", "metaxaQR_si": "/usr/local/bin/metaxaQR_si", "metaxaQR_ttt": "/usr/local/bin/metaxaQR_ttt", "metaxaQR_uc": "/usr/local/bin/metaxaQR_uc", "metaxaQR_x": "/usr/local/bin/metaxaQR_x", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "gawk-5.3.1": "/usr/local/bin/gawk-5.3.1", "vsearch": "/usr/local/bin/vsearch", "gawkbug": "/usr/local/bin/gawkbug", "shmemrun": "/usr/local/bin/shmemrun", "oshCC": "/usr/local/bin/oshCC", "oshc++": "/usr/local/bin/oshc++", "oshcxx": "/usr/local/bin/oshcxx", "shmemCC": "/usr/local/bin/shmemCC", "shmemc++": "/usr/local/bin/shmemc++", "shmemcxx": "/usr/local/bin/shmemcxx", "oshcc": "/usr/local/bin/oshcc", "oshfort": "/usr/local/bin/oshfort", "oshmem_info": "/usr/local/bin/oshmem_info", "oshrun": "/usr/local/bin/oshrun", "shmemcc": "/usr/local/bin/shmemcc", "shmemfort": "/usr/local/bin/shmemfort", "aggregate_profile.pl": "/usr/local/bin/aggregate_profile.pl", "profile2mat.pl": "/usr/local/bin/profile2mat.pl", "ompi-clean": "/usr/local/bin/ompi-clean", "ompi-server": "/usr/local/bin/ompi-server", "orte-clean": "/usr/local/bin/orte-clean"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metaxaqr.
singularity registry hpc automated addition for metaxaqr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metaxaqr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metaxaqr:3.0rc2--py314pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metaxaqr/3.0rc2--py314pl5321hdfd78af_0
$ module help quay.io/biocontainers/metaxaqr/3.0rc2--py314pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metaxaqr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metaxaqr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metaxaqr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metaxaqr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metaxaqr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metaxaqr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### get_fasta

```bash
$ singularity exec <container> /usr/local/bin/get_fasta
$ podman run --it --rm --entrypoint /usr/local/bin/get_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxaQR

```bash
$ singularity exec <container> /usr/local/bin/metaxaQR
$ podman run --it --rm --entrypoint /usr/local/bin/metaxaQR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxaQR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxaQR_c

```bash
$ singularity exec <container> /usr/local/bin/metaxaQR_c
$ podman run --it --rm --entrypoint /usr/local/bin/metaxaQR_c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxaQR_c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxaQR_dbb

```bash
$ singularity exec <container> /usr/local/bin/metaxaQR_dbb
$ podman run --it --rm --entrypoint /usr/local/bin/metaxaQR_dbb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxaQR_dbb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxaQR_dc

```bash
$ singularity exec <container> /usr/local/bin/metaxaQR_dc
$ podman run --it --rm --entrypoint /usr/local/bin/metaxaQR_dc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxaQR_dc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxaQR_install_database

```bash
$ singularity exec <container> /usr/local/bin/metaxaQR_install_database
$ podman run --it --rm --entrypoint /usr/local/bin/metaxaQR_install_database   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxaQR_install_database   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxaQR_rf

```bash
$ singularity exec <container> /usr/local/bin/metaxaQR_rf
$ podman run --it --rm --entrypoint /usr/local/bin/metaxaQR_rf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxaQR_rf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxaQR_si

```bash
$ singularity exec <container> /usr/local/bin/metaxaQR_si
$ podman run --it --rm --entrypoint /usr/local/bin/metaxaQR_si   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxaQR_si   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxaQR_ttt

```bash
$ singularity exec <container> /usr/local/bin/metaxaQR_ttt
$ podman run --it --rm --entrypoint /usr/local/bin/metaxaQR_ttt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxaQR_ttt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxaQR_uc

```bash
$ singularity exec <container> /usr/local/bin/metaxaQR_uc
$ podman run --it --rm --entrypoint /usr/local/bin/metaxaQR_uc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxaQR_uc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaxaQR_x

```bash
$ singularity exec <container> /usr/local/bin/metaxaQR_x
$ podman run --it --rm --entrypoint /usr/local/bin/metaxaQR_x   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaxaQR_x   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.3.1

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.3.1
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsearch

```bash
$ singularity exec <container> /usr/local/bin/vsearch
$ podman run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawkbug

```bash
$ singularity exec <container> /usr/local/bin/gawkbug
$ podman run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemrun

```bash
$ singularity exec <container> /usr/local/bin/shmemrun
$ podman run --it --rm --entrypoint /usr/local/bin/shmemrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshCC

```bash
$ singularity exec <container> /usr/local/bin/oshCC
$ podman run --it --rm --entrypoint /usr/local/bin/oshCC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshCC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshc++

```bash
$ singularity exec <container> /usr/local/bin/oshc++
$ podman run --it --rm --entrypoint /usr/local/bin/oshc++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshc++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshcxx

```bash
$ singularity exec <container> /usr/local/bin/oshcxx
$ podman run --it --rm --entrypoint /usr/local/bin/oshcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemCC

```bash
$ singularity exec <container> /usr/local/bin/shmemCC
$ podman run --it --rm --entrypoint /usr/local/bin/shmemCC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemCC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemc++

```bash
$ singularity exec <container> /usr/local/bin/shmemc++
$ podman run --it --rm --entrypoint /usr/local/bin/shmemc++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemc++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemcxx

```bash
$ singularity exec <container> /usr/local/bin/shmemcxx
$ podman run --it --rm --entrypoint /usr/local/bin/shmemcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshcc

```bash
$ singularity exec <container> /usr/local/bin/oshcc
$ podman run --it --rm --entrypoint /usr/local/bin/oshcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshfort

```bash
$ singularity exec <container> /usr/local/bin/oshfort
$ podman run --it --rm --entrypoint /usr/local/bin/oshfort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshfort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshmem_info

```bash
$ singularity exec <container> /usr/local/bin/oshmem_info
$ podman run --it --rm --entrypoint /usr/local/bin/oshmem_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshmem_info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshrun

```bash
$ singularity exec <container> /usr/local/bin/oshrun
$ podman run --it --rm --entrypoint /usr/local/bin/oshrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemcc

```bash
$ singularity exec <container> /usr/local/bin/shmemcc
$ podman run --it --rm --entrypoint /usr/local/bin/shmemcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemfort

```bash
$ singularity exec <container> /usr/local/bin/shmemfort
$ podman run --it --rm --entrypoint /usr/local/bin/shmemfort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemfort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aggregate_profile.pl

```bash
$ singularity exec <container> /usr/local/bin/aggregate_profile.pl
$ podman run --it --rm --entrypoint /usr/local/bin/aggregate_profile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregate_profile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### profile2mat.pl

```bash
$ singularity exec <container> /usr/local/bin/profile2mat.pl
$ podman run --it --rm --entrypoint /usr/local/bin/profile2mat.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/profile2mat.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ompi-clean

```bash
$ singularity exec <container> /usr/local/bin/ompi-clean
$ podman run --it --rm --entrypoint /usr/local/bin/ompi-clean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ompi-clean   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ompi-server

```bash
$ singularity exec <container> /usr/local/bin/ompi-server
$ podman run --it --rm --entrypoint /usr/local/bin/ompi-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ompi-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orte-clean

```bash
$ singularity exec <container> /usr/local/bin/orte-clean
$ podman run --it --rm --entrypoint /usr/local/bin/orte-clean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orte-clean   -v ${PWD} -w ${PWD} <container> -c " $@"
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