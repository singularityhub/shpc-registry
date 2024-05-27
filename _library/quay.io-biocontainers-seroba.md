---
layout: container
name:  "quay.io/biocontainers/seroba"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seroba/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/seroba/container.yaml"
updated_at: "2024-05-27 02:53:50.777419"
latest: "1.0.2--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/seroba"
aliases:
 - "ariba"
 - "seroba"
 - "kmc"
 - "kmc_dump"
 - "kmc_tools"
 - "fastaq"
 - "FET.pl"
 - "cd-hit-clstr_2_blm8.pl"
 - "cds-mapping-stats"
 - "cds-subgraphs"
 - "clstr_list.pl"
 - "clstr_list_sort.pl"
versions:
 - "1.0.2--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for seroba"
config: {"url": "https://biocontainers.pro/tools/seroba", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for seroba", "latest": {"1.0.2--pyhdfd78af_1": "sha256:36b6ec2c8091d38c0efd4814491e64886e48eaf41b434b5d1baf6ba95ddfef8b"}, "tags": {"1.0.2--pyhdfd78af_1": "sha256:36b6ec2c8091d38c0efd4814491e64886e48eaf41b434b5d1baf6ba95ddfef8b"}, "docker": "quay.io/biocontainers/seroba", "aliases": {"ariba": "/usr/local/bin/ariba", "seroba": "/usr/local/bin/seroba", "kmc": "/usr/local/bin/kmc", "kmc_dump": "/usr/local/bin/kmc_dump", "kmc_tools": "/usr/local/bin/kmc_tools", "fastaq": "/usr/local/bin/fastaq", "FET.pl": "/usr/local/bin/FET.pl", "cd-hit-clstr_2_blm8.pl": "/usr/local/bin/cd-hit-clstr_2_blm8.pl", "cds-mapping-stats": "/usr/local/bin/cds-mapping-stats", "cds-subgraphs": "/usr/local/bin/cds-subgraphs", "clstr_list.pl": "/usr/local/bin/clstr_list.pl", "clstr_list_sort.pl": "/usr/local/bin/clstr_list_sort.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seroba.
shpc-registry automated BioContainers addition for seroba
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seroba
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seroba:1.0.2--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seroba/1.0.2--pyhdfd78af_1
$ module help quay.io/biocontainers/seroba/1.0.2--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seroba-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seroba-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seroba-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seroba-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seroba-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seroba-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ariba

```bash
$ singularity exec <container> /usr/local/bin/ariba
$ podman run --it --rm --entrypoint /usr/local/bin/ariba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ariba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seroba

```bash
$ singularity exec <container> /usr/local/bin/seroba
$ podman run --it --rm --entrypoint /usr/local/bin/seroba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seroba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmc

```bash
$ singularity exec <container> /usr/local/bin/kmc
$ podman run --it --rm --entrypoint /usr/local/bin/kmc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmc_dump

```bash
$ singularity exec <container> /usr/local/bin/kmc_dump
$ podman run --it --rm --entrypoint /usr/local/bin/kmc_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmc_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmc_tools

```bash
$ singularity exec <container> /usr/local/bin/kmc_tools
$ podman run --it --rm --entrypoint /usr/local/bin/kmc_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmc_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaq

```bash
$ singularity exec <container> /usr/local/bin/fastaq
$ podman run --it --rm --entrypoint /usr/local/bin/fastaq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaq   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### cds-mapping-stats

```bash
$ singularity exec <container> /usr/local/bin/cds-mapping-stats
$ podman run --it --rm --entrypoint /usr/local/bin/cds-mapping-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cds-mapping-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cds-subgraphs

```bash
$ singularity exec <container> /usr/local/bin/cds-subgraphs
$ podman run --it --rm --entrypoint /usr/local/bin/cds-subgraphs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cds-subgraphs   -v ${PWD} -w ${PWD} <container> -c " $@"
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