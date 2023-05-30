---
layout: container
name:  "quay.io/biocontainers/pbbam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbbam/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pbbam/container.yaml"
updated_at: "2023-05-30 17:23:07.433992"
latest: "2.1.0--h65681a6_4"
container_url: "https://biocontainers.pro/tools/pbbam"
aliases:
 - "ccs-kinetics-bystrandify"
 - "extracthifi"
 - "pbindex"
 - "pbindexdump"
 - "pbmerge"
 - "zmwfilter"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "2.1.0--h218f6fc_3"
 - "2.1.0--h65681a6_4"
description: "shpc-registry automated BioContainers addition for pbbam"
config: {"url": "https://biocontainers.pro/tools/pbbam", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pbbam", "latest": {"2.1.0--h65681a6_4": "sha256:8974351da859d63aa425823067d5bdd8f498c0033725bc716f04c3da80a8088a"}, "tags": {"2.1.0--h218f6fc_3": "sha256:41f6225765f09151bafb660cfdfed0ab9bc268a80a5b6df392568a5dae73cba8", "2.1.0--h65681a6_4": "sha256:8974351da859d63aa425823067d5bdd8f498c0033725bc716f04c3da80a8088a"}, "docker": "quay.io/biocontainers/pbbam", "aliases": {"ccs-kinetics-bystrandify": "/usr/local/bin/ccs-kinetics-bystrandify", "extracthifi": "/usr/local/bin/extracthifi", "pbindex": "/usr/local/bin/pbindex", "pbindexdump": "/usr/local/bin/pbindexdump", "pbmerge": "/usr/local/bin/pbmerge", "zmwfilter": "/usr/local/bin/zmwfilter", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pbbam.
shpc-registry automated BioContainers addition for pbbam
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pbbam
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pbbam:2.1.0--h65681a6_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pbbam/2.1.0--h65681a6_4
$ module help quay.io/biocontainers/pbbam/2.1.0--h65681a6_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pbbam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pbbam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pbbam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pbbam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pbbam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pbbam-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ccs-kinetics-bystrandify

```bash
$ singularity exec <container> /usr/local/bin/ccs-kinetics-bystrandify
$ podman run --it --rm --entrypoint /usr/local/bin/ccs-kinetics-bystrandify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccs-kinetics-bystrandify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extracthifi

```bash
$ singularity exec <container> /usr/local/bin/extracthifi
$ podman run --it --rm --entrypoint /usr/local/bin/extracthifi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extracthifi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbindex

```bash
$ singularity exec <container> /usr/local/bin/pbindex
$ podman run --it --rm --entrypoint /usr/local/bin/pbindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbindexdump

```bash
$ singularity exec <container> /usr/local/bin/pbindexdump
$ podman run --it --rm --entrypoint /usr/local/bin/pbindexdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbindexdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbmerge

```bash
$ singularity exec <container> /usr/local/bin/pbmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pbmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zmwfilter

```bash
$ singularity exec <container> /usr/local/bin/zmwfilter
$ podman run --it --rm --entrypoint /usr/local/bin/zmwfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zmwfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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