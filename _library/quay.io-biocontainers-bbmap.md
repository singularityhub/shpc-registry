---
layout: container
name:  "quay.io/biocontainers/bbmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bbmap/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bbmap/container.yaml"
updated_at: "2022-10-29 07:45:37.678885"
latest: "38.79--h516909a_0"
container_url: "https://biocontainers.pro/tools/bbmap"
aliases:
 - "bbmap.sh"
 - "bbmapskimmer.sh"
 - "demuxbyname2.sh"
 - "alltoall.sh"
 - "analyzesketchresults.sh"
 - "comparessu.sh"
 - "filtersilva.sh"
 - "sketchblacklist2.sh"
 - "splitribo.sh"
 - "addssu.sh"
 - "adjusthomopolymers.sh"
 - "analyzeaccession.sh"
 - "analyzegenes.sh"
versions:
 - "38.79--h516909a_0"
description: "shpc-registry automated BioContainers addition for bbmap"
config: {"url": "https://biocontainers.pro/tools/bbmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bbmap", "latest": {"38.79--h516909a_0": "sha256:f12df79cf92bbc50effabab6cda944c128954295340070e5a3bdc2c991a65b87"}, "tags": {"38.79--h516909a_0": "sha256:f12df79cf92bbc50effabab6cda944c128954295340070e5a3bdc2c991a65b87"}, "docker": "quay.io/biocontainers/bbmap", "aliases": {"bbmap.sh": "/usr/local/bin/bbmap.sh", "bbmapskimmer.sh": "/usr/local/bin/bbmapskimmer.sh", "demuxbyname2.sh": "/usr/local/bin/demuxbyname2.sh", "alltoall.sh": "/usr/local/bin/alltoall.sh", "analyzesketchresults.sh": "/usr/local/bin/analyzesketchresults.sh", "comparessu.sh": "/usr/local/bin/comparessu.sh", "filtersilva.sh": "/usr/local/bin/filtersilva.sh", "sketchblacklist2.sh": "/usr/local/bin/sketchblacklist2.sh", "splitribo.sh": "/usr/local/bin/splitribo.sh", "addssu.sh": "/usr/local/bin/addssu.sh", "adjusthomopolymers.sh": "/usr/local/bin/adjusthomopolymers.sh", "analyzeaccession.sh": "/usr/local/bin/analyzeaccession.sh", "analyzegenes.sh": "/usr/local/bin/analyzegenes.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bbmap.
shpc-registry automated BioContainers addition for bbmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bbmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bbmap:38.79--h516909a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bbmap/38.79--h516909a_0
$ module help quay.io/biocontainers/bbmap/38.79--h516909a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bbmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bbmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bbmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bbmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bbmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bbmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bbmap.sh

```bash
$ singularity exec <container> /usr/local/bin/bbmap.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bbmap.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bbmap.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bbmapskimmer.sh

```bash
$ singularity exec <container> /usr/local/bin/bbmapskimmer.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bbmapskimmer.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bbmapskimmer.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### demuxbyname2.sh

```bash
$ singularity exec <container> /usr/local/bin/demuxbyname2.sh
$ podman run --it --rm --entrypoint /usr/local/bin/demuxbyname2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/demuxbyname2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alltoall.sh

```bash
$ singularity exec <container> /usr/local/bin/alltoall.sh
$ podman run --it --rm --entrypoint /usr/local/bin/alltoall.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alltoall.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyzesketchresults.sh

```bash
$ singularity exec <container> /usr/local/bin/analyzesketchresults.sh
$ podman run --it --rm --entrypoint /usr/local/bin/analyzesketchresults.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyzesketchresults.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### comparessu.sh

```bash
$ singularity exec <container> /usr/local/bin/comparessu.sh
$ podman run --it --rm --entrypoint /usr/local/bin/comparessu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/comparessu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filtersilva.sh

```bash
$ singularity exec <container> /usr/local/bin/filtersilva.sh
$ podman run --it --rm --entrypoint /usr/local/bin/filtersilva.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filtersilva.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sketchblacklist2.sh

```bash
$ singularity exec <container> /usr/local/bin/sketchblacklist2.sh
$ podman run --it --rm --entrypoint /usr/local/bin/sketchblacklist2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sketchblacklist2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splitribo.sh

```bash
$ singularity exec <container> /usr/local/bin/splitribo.sh
$ podman run --it --rm --entrypoint /usr/local/bin/splitribo.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitribo.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### addssu.sh

```bash
$ singularity exec <container> /usr/local/bin/addssu.sh
$ podman run --it --rm --entrypoint /usr/local/bin/addssu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addssu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adjusthomopolymers.sh

```bash
$ singularity exec <container> /usr/local/bin/adjusthomopolymers.sh
$ podman run --it --rm --entrypoint /usr/local/bin/adjusthomopolymers.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adjusthomopolymers.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyzeaccession.sh

```bash
$ singularity exec <container> /usr/local/bin/analyzeaccession.sh
$ podman run --it --rm --entrypoint /usr/local/bin/analyzeaccession.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyzeaccession.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### analyzegenes.sh

```bash
$ singularity exec <container> /usr/local/bin/analyzegenes.sh
$ podman run --it --rm --entrypoint /usr/local/bin/analyzegenes.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyzegenes.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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