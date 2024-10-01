---
layout: container
name:  "quay.io/biocontainers/seqcluster"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seqcluster/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/seqcluster/container.yaml"
updated_at: "2024-10-01 03:14:53.450342"
latest: "1.2.9--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/seqcluster"
aliases:
 - "RNAmultifold"
 - "mirtop"
 - "seqcluster"
 - "seqcluster_install"
 - "RNAdos"
 - "AnalyseDists"
 - "AnalyseSeqs"
 - "RNAlocmin"
 - "RNApvmin"
 - "b2ct"
 - "ct2db"
 - "kinwalker"
 - "popt"
 - "RNA2Dfold"
versions:
 - "1.2.9--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for seqcluster"
config: {"url": "https://biocontainers.pro/tools/seqcluster", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for seqcluster", "latest": {"1.2.9--pyh5e36f6f_0": "sha256:61eeb06073d386649651d5fca1030671294e737808436079ef306fb7e983d97c"}, "tags": {"1.2.9--pyh5e36f6f_0": "sha256:61eeb06073d386649651d5fca1030671294e737808436079ef306fb7e983d97c"}, "docker": "quay.io/biocontainers/seqcluster", "aliases": {"RNAmultifold": "/usr/local/bin/RNAmultifold", "mirtop": "/usr/local/bin/mirtop", "seqcluster": "/usr/local/bin/seqcluster", "seqcluster_install": "/usr/local/bin/seqcluster_install", "RNAdos": "/usr/local/bin/RNAdos", "AnalyseDists": "/usr/local/bin/AnalyseDists", "AnalyseSeqs": "/usr/local/bin/AnalyseSeqs", "RNAlocmin": "/usr/local/bin/RNAlocmin", "RNApvmin": "/usr/local/bin/RNApvmin", "b2ct": "/usr/local/bin/b2ct", "ct2db": "/usr/local/bin/ct2db", "kinwalker": "/usr/local/bin/kinwalker", "popt": "/usr/local/bin/popt", "RNA2Dfold": "/usr/local/bin/RNA2Dfold"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seqcluster.
shpc-registry automated BioContainers addition for seqcluster
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seqcluster
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seqcluster:1.2.9--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seqcluster/1.2.9--pyh5e36f6f_0
$ module help quay.io/biocontainers/seqcluster/1.2.9--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seqcluster-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seqcluster-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seqcluster-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seqcluster-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seqcluster-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seqcluster-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RNAmultifold

```bash
$ singularity exec <container> /usr/local/bin/RNAmultifold
$ podman run --it --rm --entrypoint /usr/local/bin/RNAmultifold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAmultifold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirtop

```bash
$ singularity exec <container> /usr/local/bin/mirtop
$ podman run --it --rm --entrypoint /usr/local/bin/mirtop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirtop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqcluster

```bash
$ singularity exec <container> /usr/local/bin/seqcluster
$ podman run --it --rm --entrypoint /usr/local/bin/seqcluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqcluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqcluster_install

```bash
$ singularity exec <container> /usr/local/bin/seqcluster_install
$ podman run --it --rm --entrypoint /usr/local/bin/seqcluster_install   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqcluster_install   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAdos

```bash
$ singularity exec <container> /usr/local/bin/RNAdos
$ podman run --it --rm --entrypoint /usr/local/bin/RNAdos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAdos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AnalyseDists

```bash
$ singularity exec <container> /usr/local/bin/AnalyseDists
$ podman run --it --rm --entrypoint /usr/local/bin/AnalyseDists   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AnalyseDists   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AnalyseSeqs

```bash
$ singularity exec <container> /usr/local/bin/AnalyseSeqs
$ podman run --it --rm --entrypoint /usr/local/bin/AnalyseSeqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AnalyseSeqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAlocmin

```bash
$ singularity exec <container> /usr/local/bin/RNAlocmin
$ podman run --it --rm --entrypoint /usr/local/bin/RNAlocmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAlocmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNApvmin

```bash
$ singularity exec <container> /usr/local/bin/RNApvmin
$ podman run --it --rm --entrypoint /usr/local/bin/RNApvmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNApvmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### b2ct

```bash
$ singularity exec <container> /usr/local/bin/b2ct
$ podman run --it --rm --entrypoint /usr/local/bin/b2ct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/b2ct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ct2db

```bash
$ singularity exec <container> /usr/local/bin/ct2db
$ podman run --it --rm --entrypoint /usr/local/bin/ct2db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ct2db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kinwalker

```bash
$ singularity exec <container> /usr/local/bin/kinwalker
$ podman run --it --rm --entrypoint /usr/local/bin/kinwalker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kinwalker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### popt

```bash
$ singularity exec <container> /usr/local/bin/popt
$ podman run --it --rm --entrypoint /usr/local/bin/popt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/popt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNA2Dfold

```bash
$ singularity exec <container> /usr/local/bin/RNA2Dfold
$ podman run --it --rm --entrypoint /usr/local/bin/RNA2Dfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNA2Dfold   -v ${PWD} -w ${PWD} <container> -c " $@"
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