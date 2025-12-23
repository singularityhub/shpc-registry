---
layout: container
name:  "quay.io/biocontainers/unifire"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/unifire/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/unifire/container.yaml"
updated_at: "2025-12-23 03:58:57.723010"
latest: "1.0.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/unifire"
aliases:
 - "bottle"
 - "bottle.py"
 - "ete4"
 - "fasta-header-validator"
 - "pirsr"
 - "unifire"
 - "updateIPRScanWithTaxonomicLineage"
 - "egrep"
 - "fgrep"
 - "grep"
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
 - "orte-info"
 - "orte-server"
 - "ortecc"
 - "orted"
versions:
 - "1.0.1--hdfd78af_0"
description: "singularity registry hpc automated addition for unifire"
config: {"url": "https://biocontainers.pro/tools/unifire", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for unifire", "latest": {"1.0.1--hdfd78af_0": "sha256:f6079d473c3be643bfc5bc0ebaab7d7a020079e6b86c6979e92f4128efd20d0f"}, "tags": {"1.0.1--hdfd78af_0": "sha256:f6079d473c3be643bfc5bc0ebaab7d7a020079e6b86c6979e92f4128efd20d0f"}, "docker": "quay.io/biocontainers/unifire", "aliases": {"bottle": "/usr/local/bin/bottle", "bottle.py": "/usr/local/bin/bottle.py", "ete4": "/usr/local/bin/ete4", "fasta-header-validator": "/usr/local/bin/fasta-header-validator", "pirsr": "/usr/local/bin/pirsr", "unifire": "/usr/local/bin/unifire", "updateIPRScanWithTaxonomicLineage": "/usr/local/bin/updateIPRScanWithTaxonomicLineage", "egrep": "/usr/local/bin/egrep", "fgrep": "/usr/local/bin/fgrep", "grep": "/usr/local/bin/grep", "shmemrun": "/usr/local/bin/shmemrun", "oshCC": "/usr/local/bin/oshCC", "oshc++": "/usr/local/bin/oshc++", "oshcxx": "/usr/local/bin/oshcxx", "shmemCC": "/usr/local/bin/shmemCC", "shmemc++": "/usr/local/bin/shmemc++", "shmemcxx": "/usr/local/bin/shmemcxx", "oshcc": "/usr/local/bin/oshcc", "oshfort": "/usr/local/bin/oshfort", "oshmem_info": "/usr/local/bin/oshmem_info", "oshrun": "/usr/local/bin/oshrun", "shmemcc": "/usr/local/bin/shmemcc", "shmemfort": "/usr/local/bin/shmemfort", "aggregate_profile.pl": "/usr/local/bin/aggregate_profile.pl", "profile2mat.pl": "/usr/local/bin/profile2mat.pl", "ompi-clean": "/usr/local/bin/ompi-clean", "ompi-server": "/usr/local/bin/ompi-server", "orte-clean": "/usr/local/bin/orte-clean", "orte-info": "/usr/local/bin/orte-info", "orte-server": "/usr/local/bin/orte-server", "ortecc": "/usr/local/bin/ortecc", "orted": "/usr/local/bin/orted"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/unifire.
singularity registry hpc automated addition for unifire
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/unifire
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/unifire:1.0.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/unifire/1.0.1--hdfd78af_0
$ module help quay.io/biocontainers/unifire/1.0.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### unifire-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### unifire-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### unifire-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### unifire-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### unifire-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### unifire-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bottle

```bash
$ singularity exec <container> /usr/local/bin/bottle
$ podman run --it --rm --entrypoint /usr/local/bin/bottle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bottle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bottle.py

```bash
$ singularity exec <container> /usr/local/bin/bottle.py
$ podman run --it --rm --entrypoint /usr/local/bin/bottle.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bottle.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ete4

```bash
$ singularity exec <container> /usr/local/bin/ete4
$ podman run --it --rm --entrypoint /usr/local/bin/ete4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ete4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-header-validator

```bash
$ singularity exec <container> /usr/local/bin/fasta-header-validator
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-header-validator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-header-validator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pirsr

```bash
$ singularity exec <container> /usr/local/bin/pirsr
$ podman run --it --rm --entrypoint /usr/local/bin/pirsr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pirsr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unifire

```bash
$ singularity exec <container> /usr/local/bin/unifire
$ podman run --it --rm --entrypoint /usr/local/bin/unifire   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unifire   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### updateIPRScanWithTaxonomicLineage

```bash
$ singularity exec <container> /usr/local/bin/updateIPRScanWithTaxonomicLineage
$ podman run --it --rm --entrypoint /usr/local/bin/updateIPRScanWithTaxonomicLineage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/updateIPRScanWithTaxonomicLineage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### egrep

```bash
$ singularity exec <container> /usr/local/bin/egrep
$ podman run --it --rm --entrypoint /usr/local/bin/egrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/egrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fgrep

```bash
$ singularity exec <container> /usr/local/bin/fgrep
$ podman run --it --rm --entrypoint /usr/local/bin/fgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grep

```bash
$ singularity exec <container> /usr/local/bin/grep
$ podman run --it --rm --entrypoint /usr/local/bin/grep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grep   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### orte-info

```bash
$ singularity exec <container> /usr/local/bin/orte-info
$ podman run --it --rm --entrypoint /usr/local/bin/orte-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orte-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orte-server

```bash
$ singularity exec <container> /usr/local/bin/orte-server
$ podman run --it --rm --entrypoint /usr/local/bin/orte-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orte-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ortecc

```bash
$ singularity exec <container> /usr/local/bin/ortecc
$ podman run --it --rm --entrypoint /usr/local/bin/ortecc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ortecc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orted

```bash
$ singularity exec <container> /usr/local/bin/orted
$ podman run --it --rm --entrypoint /usr/local/bin/orted   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orted   -v ${PWD} -w ${PWD} <container> -c " $@"
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