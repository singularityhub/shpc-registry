---
layout: container
name:  "quay.io/biocontainers/pb-dazzler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pb-dazzler/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pb-dazzler/container.yaml"
updated_at: "2024-09-12 03:14:11.418904"
latest: "0.0.1--h031d066_4"
container_url: "https://biocontainers.pro/tools/pb-dazzler"
aliases:
 - "Catrack"
 - "DAM2fasta"
 - "DB2Falcon"
 - "DB2fasta"
 - "DBdump"
 - "DBdust"
 - "DBrm"
 - "DBshow"
 - "DBsplit"
 - "DBstats"
 - "HPC.REPmask"
 - "HPC.TANmask"
 - "HPC.daligner"
 - "LA4Falcon"
 - "LA4Ice"
 - "LAcat"
 - "LAcheck"
 - "LAdump"
 - "LAindex"
 - "LAmerge"
 - "LAshow"
 - "LAsort"
 - "LAsplit"
 - "REPmask"
 - "TANmask"
 - "daligner"
 - "daligner_p"
 - "datander"
 - "dexta"
 - "fasta2DAM"
 - "fasta2DB"
 - "rangen"
 - "simulator"
 - "undexta"
versions:
 - "0.0.1--hec16e2b_2"
 - "0.0.1--h031d066_4"
description: "shpc-registry automated BioContainers addition for pb-dazzler"
config: {"url": "https://biocontainers.pro/tools/pb-dazzler", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pb-dazzler", "latest": {"0.0.1--h031d066_4": "sha256:31f9a71563a9da2a8cf5ad5e79d975526cdb859cafef038f882bfc4764818b90"}, "tags": {"0.0.1--hec16e2b_2": "sha256:ae0bd4afb8926f1b44a96332bc915446a992736c699538efe31b731a0d96c370", "0.0.1--h031d066_4": "sha256:31f9a71563a9da2a8cf5ad5e79d975526cdb859cafef038f882bfc4764818b90"}, "docker": "quay.io/biocontainers/pb-dazzler", "aliases": {"Catrack": "/usr/local/bin/Catrack", "DAM2fasta": "/usr/local/bin/DAM2fasta", "DB2Falcon": "/usr/local/bin/DB2Falcon", "DB2fasta": "/usr/local/bin/DB2fasta", "DBdump": "/usr/local/bin/DBdump", "DBdust": "/usr/local/bin/DBdust", "DBrm": "/usr/local/bin/DBrm", "DBshow": "/usr/local/bin/DBshow", "DBsplit": "/usr/local/bin/DBsplit", "DBstats": "/usr/local/bin/DBstats", "HPC.REPmask": "/usr/local/bin/HPC.REPmask", "HPC.TANmask": "/usr/local/bin/HPC.TANmask", "HPC.daligner": "/usr/local/bin/HPC.daligner", "LA4Falcon": "/usr/local/bin/LA4Falcon", "LA4Ice": "/usr/local/bin/LA4Ice", "LAcat": "/usr/local/bin/LAcat", "LAcheck": "/usr/local/bin/LAcheck", "LAdump": "/usr/local/bin/LAdump", "LAindex": "/usr/local/bin/LAindex", "LAmerge": "/usr/local/bin/LAmerge", "LAshow": "/usr/local/bin/LAshow", "LAsort": "/usr/local/bin/LAsort", "LAsplit": "/usr/local/bin/LAsplit", "REPmask": "/usr/local/bin/REPmask", "TANmask": "/usr/local/bin/TANmask", "daligner": "/usr/local/bin/daligner", "daligner_p": "/usr/local/bin/daligner_p", "datander": "/usr/local/bin/datander", "dexta": "/usr/local/bin/dexta", "fasta2DAM": "/usr/local/bin/fasta2DAM", "fasta2DB": "/usr/local/bin/fasta2DB", "rangen": "/usr/local/bin/rangen", "simulator": "/usr/local/bin/simulator", "undexta": "/usr/local/bin/undexta"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pb-dazzler.
shpc-registry automated BioContainers addition for pb-dazzler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pb-dazzler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pb-dazzler:0.0.1--h031d066_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pb-dazzler/0.0.1--h031d066_4
$ module help quay.io/biocontainers/pb-dazzler/0.0.1--h031d066_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pb-dazzler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pb-dazzler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pb-dazzler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pb-dazzler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pb-dazzler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pb-dazzler-inspect-deffile:

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


#### DB2Falcon

```bash
$ singularity exec <container> /usr/local/bin/DB2Falcon
$ podman run --it --rm --entrypoint /usr/local/bin/DB2Falcon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DB2Falcon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DB2fasta

```bash
$ singularity exec <container> /usr/local/bin/DB2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/DB2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DB2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DBdump

```bash
$ singularity exec <container> /usr/local/bin/DBdump
$ podman run --it --rm --entrypoint /usr/local/bin/DBdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DBdump   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### HPC.REPmask

```bash
$ singularity exec <container> /usr/local/bin/HPC.REPmask
$ podman run --it --rm --entrypoint /usr/local/bin/HPC.REPmask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HPC.REPmask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### HPC.TANmask

```bash
$ singularity exec <container> /usr/local/bin/HPC.TANmask
$ podman run --it --rm --entrypoint /usr/local/bin/HPC.TANmask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HPC.TANmask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### HPC.daligner

```bash
$ singularity exec <container> /usr/local/bin/HPC.daligner
$ podman run --it --rm --entrypoint /usr/local/bin/HPC.daligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HPC.daligner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LA4Falcon

```bash
$ singularity exec <container> /usr/local/bin/LA4Falcon
$ podman run --it --rm --entrypoint /usr/local/bin/LA4Falcon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LA4Falcon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LA4Ice

```bash
$ singularity exec <container> /usr/local/bin/LA4Ice
$ podman run --it --rm --entrypoint /usr/local/bin/LA4Ice   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LA4Ice   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### LAdump

```bash
$ singularity exec <container> /usr/local/bin/LAdump
$ podman run --it --rm --entrypoint /usr/local/bin/LAdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LAdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LAindex

```bash
$ singularity exec <container> /usr/local/bin/LAindex
$ podman run --it --rm --entrypoint /usr/local/bin/LAindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LAindex   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### REPmask

```bash
$ singularity exec <container> /usr/local/bin/REPmask
$ podman run --it --rm --entrypoint /usr/local/bin/REPmask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/REPmask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TANmask

```bash
$ singularity exec <container> /usr/local/bin/TANmask
$ podman run --it --rm --entrypoint /usr/local/bin/TANmask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TANmask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### daligner

```bash
$ singularity exec <container> /usr/local/bin/daligner
$ podman run --it --rm --entrypoint /usr/local/bin/daligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/daligner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### daligner_p

```bash
$ singularity exec <container> /usr/local/bin/daligner_p
$ podman run --it --rm --entrypoint /usr/local/bin/daligner_p   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/daligner_p   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### datander

```bash
$ singularity exec <container> /usr/local/bin/datander
$ podman run --it --rm --entrypoint /usr/local/bin/datander   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/datander   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dexta

```bash
$ singularity exec <container> /usr/local/bin/dexta
$ podman run --it --rm --entrypoint /usr/local/bin/dexta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dexta   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### rangen

```bash
$ singularity exec <container> /usr/local/bin/rangen
$ podman run --it --rm --entrypoint /usr/local/bin/rangen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rangen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simulator

```bash
$ singularity exec <container> /usr/local/bin/simulator
$ podman run --it --rm --entrypoint /usr/local/bin/simulator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simulator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### undexta

```bash
$ singularity exec <container> /usr/local/bin/undexta
$ podman run --it --rm --entrypoint /usr/local/bin/undexta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/undexta   -v ${PWD} -w ${PWD} <container> -c " $@"
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