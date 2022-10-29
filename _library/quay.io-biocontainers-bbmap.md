---
layout: container
name:  "quay.io/biocontainers/bbmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bbmap/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bbmap/container.yaml"
updated_at: "2022-10-29 05:43:26.381465"
latest: "38.79--h516909a_0"
container_url: "https://biocontainers.pro/tools/bbmap"
aliases:
 - "demuxbyname2.sh"
 - "a_sample_mt.sh"
 - "addadapters.sh"
 - "addssu.sh"
 - "adjusthomopolymers.sh"
 - "alltoall.sh"
 - "analyzeaccession.sh"
 - "analyzegenes.sh"
 - "analyzesketchresults.sh"
 - "applyvariants.sh"
 - "aserver"
versions:
 - "38.89--h1296035_0"
 - "38.90--he522d1c_3"
 - "38.91--he522d1c_1"
 - "38.92--he522d1c_0"
 - "38.93--he522d1c_0"
 - "38.96--h5c4e2a8_0"
 - "38.79--h516909a_0"
description: "shpc-registry automated BioContainers addition for bbmap"
config: {"docker": "quay.io/biocontainers/bbmap", "url": "https://biocontainers.pro/tools/bbmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bbmap", "latest": {"38.79--h516909a_0": "sha256:f12df79cf92bbc50effabab6cda944c128954295340070e5a3bdc2c991a65b87"}, "tags": {"38.89--h1296035_0": "sha256:acc26b0e54b1323c2db287fabb8bffecda94e766b6759dfdddc7472687b52f33", "38.90--he522d1c_3": "sha256:e85733071f68bc84959aa97155f9d13b87fdfd17f41703fe861c057a56dec2b0", "38.91--he522d1c_1": "sha256:5679f2c146844662be023769146fa787ea101f3dd833ade36aaa0bb533c9939a", "38.92--he522d1c_0": "sha256:103f3a1ec4144933c583da1f8f9bfc7447468e0150c9591d4cc1aff8f98830b9", "38.93--he522d1c_0": "sha256:c171d975ea9b1d4232af2e3608927b5ec83807608263d4e12428964b2f99e4dc", "38.96--h5c4e2a8_0": "sha256:1bc2b5f07fd506ee2cce882a1f8b7b40abffe4e860a89bd87e6599e09dee827c", "38.79--h516909a_0": "sha256:f12df79cf92bbc50effabab6cda944c128954295340070e5a3bdc2c991a65b87"}, "aliases": {"demuxbyname2.sh": "/usr/local/bin/demuxbyname2.sh", "a_sample_mt.sh": "/usr/local/bin/a_sample_mt.sh", "addadapters.sh": "/usr/local/bin/addadapters.sh", "addssu.sh": "/usr/local/bin/addssu.sh", "adjusthomopolymers.sh": "/usr/local/bin/adjusthomopolymers.sh", "alltoall.sh": "/usr/local/bin/alltoall.sh", "analyzeaccession.sh": "/usr/local/bin/analyzeaccession.sh", "analyzegenes.sh": "/usr/local/bin/analyzegenes.sh", "analyzesketchresults.sh": "/usr/local/bin/analyzesketchresults.sh", "applyvariants.sh": "/usr/local/bin/applyvariants.sh", "aserver": "/usr/local/bin/aserver"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bbmap.
shpc-registry automated BioContainers addition for bbmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bbmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bbmap:38.89--h1296035_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bbmap/38.89--h1296035_0
$ module help quay.io/biocontainers/bbmap/38.89--h1296035_0
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


#### demuxbyname2.sh

```bash
$ singularity exec <container> /usr/local/bin/demuxbyname2.sh
$ podman run --it --rm --entrypoint /usr/local/bin/demuxbyname2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/demuxbyname2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### a_sample_mt.sh

```bash
$ singularity exec <container> /usr/local/bin/a_sample_mt.sh
$ podman run --it --rm --entrypoint /usr/local/bin/a_sample_mt.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/a_sample_mt.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### addadapters.sh

```bash
$ singularity exec <container> /usr/local/bin/addadapters.sh
$ podman run --it --rm --entrypoint /usr/local/bin/addadapters.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addadapters.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### alltoall.sh

```bash
$ singularity exec <container> /usr/local/bin/alltoall.sh
$ podman run --it --rm --entrypoint /usr/local/bin/alltoall.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alltoall.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### analyzesketchresults.sh

```bash
$ singularity exec <container> /usr/local/bin/analyzesketchresults.sh
$ podman run --it --rm --entrypoint /usr/local/bin/analyzesketchresults.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyzesketchresults.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### applyvariants.sh

```bash
$ singularity exec <container> /usr/local/bin/applyvariants.sh
$ podman run --it --rm --entrypoint /usr/local/bin/applyvariants.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/applyvariants.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
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