---
layout: container
name:  "quay.io/biocontainers/pbdagcon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbdagcon/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pbdagcon/container.yaml"
updated_at: "2023-08-07 02:50:02.863515"
latest: "0.1--boost1.64_0"
container_url: "https://biocontainers.pro/tools/pbdagcon"
aliases:
 - "Catrack"
 - "DAM2fasta"
 - "DB2fasta"
 - "DB2quiva"
 - "DBdust"
 - "DBrm"
 - "DBshow"
 - "DBsplit"
 - "DBstats"
 - "HPCdaligner"
 - "HPCmapper"
 - "LAcat"
 - "LAcheck"
 - "LAmerge"
 - "LAshow"
 - "LAsort"
 - "LAsplit"
 - "daligner"
 - "dazcon"
 - "fasta2DAM"
 - "fasta2DB"
 - "pbdagcon"
 - "quiva2DB"
 - "simulator"
 - "easy_install-3.6"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
 - "python3.6m-config"
 - "pyvenv-3.6"
 - "h5clear"
versions:
 - "0.1--boost1.64_0"
description: "shpc-registry automated BioContainers addition for pbdagcon"
config: {"url": "https://biocontainers.pro/tools/pbdagcon", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pbdagcon", "latest": {"0.1--boost1.64_0": "sha256:fbd203850410140f2512deeed50a6626ceac3dd182d6c251e3e0ad0474df62bb"}, "tags": {"0.1--boost1.64_0": "sha256:fbd203850410140f2512deeed50a6626ceac3dd182d6c251e3e0ad0474df62bb"}, "docker": "quay.io/biocontainers/pbdagcon", "aliases": {"Catrack": "/usr/local/bin/Catrack", "DAM2fasta": "/usr/local/bin/DAM2fasta", "DB2fasta": "/usr/local/bin/DB2fasta", "DB2quiva": "/usr/local/bin/DB2quiva", "DBdust": "/usr/local/bin/DBdust", "DBrm": "/usr/local/bin/DBrm", "DBshow": "/usr/local/bin/DBshow", "DBsplit": "/usr/local/bin/DBsplit", "DBstats": "/usr/local/bin/DBstats", "HPCdaligner": "/usr/local/bin/HPCdaligner", "HPCmapper": "/usr/local/bin/HPCmapper", "LAcat": "/usr/local/bin/LAcat", "LAcheck": "/usr/local/bin/LAcheck", "LAmerge": "/usr/local/bin/LAmerge", "LAshow": "/usr/local/bin/LAshow", "LAsort": "/usr/local/bin/LAsort", "LAsplit": "/usr/local/bin/LAsplit", "daligner": "/usr/local/bin/daligner", "dazcon": "/usr/local/bin/dazcon", "fasta2DAM": "/usr/local/bin/fasta2DAM", "fasta2DB": "/usr/local/bin/fasta2DB", "pbdagcon": "/usr/local/bin/pbdagcon", "quiva2DB": "/usr/local/bin/quiva2DB", "simulator": "/usr/local/bin/simulator", "easy_install-3.6": "/usr/local/bin/easy_install-3.6", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config", "pyvenv-3.6": "/usr/local/bin/pyvenv-3.6", "h5clear": "/usr/local/bin/h5clear"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pbdagcon.
shpc-registry automated BioContainers addition for pbdagcon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pbdagcon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pbdagcon:0.1--boost1.64_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pbdagcon/0.1--boost1.64_0
$ module help quay.io/biocontainers/pbdagcon/0.1--boost1.64_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pbdagcon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pbdagcon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pbdagcon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pbdagcon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pbdagcon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pbdagcon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Catrack

```bash
$ singularity exec <container> /usr/local/bin/Catrack
$ podman run --it --rm --entrypoint /usr/local/bin/Catrack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Catrack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DAM2fasta

```bash
$ singularity exec <container> /usr/local/bin/DAM2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/DAM2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DAM2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DB2fasta

```bash
$ singularity exec <container> /usr/local/bin/DB2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/DB2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DB2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DB2quiva

```bash
$ singularity exec <container> /usr/local/bin/DB2quiva
$ podman run --it --rm --entrypoint /usr/local/bin/DB2quiva   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DB2quiva   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DBdust

```bash
$ singularity exec <container> /usr/local/bin/DBdust
$ podman run --it --rm --entrypoint /usr/local/bin/DBdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DBdust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DBrm

```bash
$ singularity exec <container> /usr/local/bin/DBrm
$ podman run --it --rm --entrypoint /usr/local/bin/DBrm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DBrm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DBshow

```bash
$ singularity exec <container> /usr/local/bin/DBshow
$ podman run --it --rm --entrypoint /usr/local/bin/DBshow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DBshow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DBsplit

```bash
$ singularity exec <container> /usr/local/bin/DBsplit
$ podman run --it --rm --entrypoint /usr/local/bin/DBsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DBsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DBstats

```bash
$ singularity exec <container> /usr/local/bin/DBstats
$ podman run --it --rm --entrypoint /usr/local/bin/DBstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DBstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### HPCdaligner

```bash
$ singularity exec <container> /usr/local/bin/HPCdaligner
$ podman run --it --rm --entrypoint /usr/local/bin/HPCdaligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HPCdaligner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### HPCmapper

```bash
$ singularity exec <container> /usr/local/bin/HPCmapper
$ podman run --it --rm --entrypoint /usr/local/bin/HPCmapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HPCmapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LAcat

```bash
$ singularity exec <container> /usr/local/bin/LAcat
$ podman run --it --rm --entrypoint /usr/local/bin/LAcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LAcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LAcheck

```bash
$ singularity exec <container> /usr/local/bin/LAcheck
$ podman run --it --rm --entrypoint /usr/local/bin/LAcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LAcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LAmerge

```bash
$ singularity exec <container> /usr/local/bin/LAmerge
$ podman run --it --rm --entrypoint /usr/local/bin/LAmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LAmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LAshow

```bash
$ singularity exec <container> /usr/local/bin/LAshow
$ podman run --it --rm --entrypoint /usr/local/bin/LAshow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LAshow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LAsort

```bash
$ singularity exec <container> /usr/local/bin/LAsort
$ podman run --it --rm --entrypoint /usr/local/bin/LAsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LAsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LAsplit

```bash
$ singularity exec <container> /usr/local/bin/LAsplit
$ podman run --it --rm --entrypoint /usr/local/bin/LAsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LAsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### daligner

```bash
$ singularity exec <container> /usr/local/bin/daligner
$ podman run --it --rm --entrypoint /usr/local/bin/daligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/daligner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dazcon

```bash
$ singularity exec <container> /usr/local/bin/dazcon
$ podman run --it --rm --entrypoint /usr/local/bin/dazcon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dazcon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta2DAM

```bash
$ singularity exec <container> /usr/local/bin/fasta2DAM
$ podman run --it --rm --entrypoint /usr/local/bin/fasta2DAM   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta2DAM   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta2DB

```bash
$ singularity exec <container> /usr/local/bin/fasta2DB
$ podman run --it --rm --entrypoint /usr/local/bin/fasta2DB   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta2DB   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbdagcon

```bash
$ singularity exec <container> /usr/local/bin/pbdagcon
$ podman run --it --rm --entrypoint /usr/local/bin/pbdagcon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbdagcon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quiva2DB

```bash
$ singularity exec <container> /usr/local/bin/quiva2DB
$ podman run --it --rm --entrypoint /usr/local/bin/quiva2DB   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quiva2DB   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simulator

```bash
$ singularity exec <container> /usr/local/bin/simulator
$ podman run --it --rm --entrypoint /usr/local/bin/simulator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simulator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy_install-3.6

```bash
$ singularity exec <container> /usr/local/bin/easy_install-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.6

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6

```bash
$ singularity exec <container> /usr/local/bin/python3.6
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m

```bash
$ singularity exec <container> /usr/local/bin/python3.6m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.6

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5clear

```bash
$ singularity exec <container> /usr/local/bin/h5clear
$ podman run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
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