---
layout: container
name:  "quay.io/biocontainers/crispresso2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/crispresso2/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/crispresso2/container.yaml"
updated_at: "2022-10-27 01:03:09.629301"
latest: "2.2.8--py38h6eac312_0"
container_url: "https://biocontainers.pro/tools/crispresso2"
aliases:
 - "CRISPResso"
 - "CRISPRessoAggregate"
 - "CRISPRessoBatch"
 - "CRISPRessoCompare"
 - "CRISPRessoPooled"
 - "CRISPRessoPooledWGSCompare"
 - "CRISPRessoWGS"
versions:
 - "2.2.8--py38h6eac312_0"
description: "shpc-registry automated BioContainers addition for crispresso2"
config: {"url": "https://biocontainers.pro/tools/crispresso2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for crispresso2", "latest": {"2.2.8--py38h6eac312_0": "sha256:77f2952faf107bd2412e2373d37e50d7ecbf1da81d75d008233f24cf42fc1d5e"}, "tags": {"2.2.8--py38h6eac312_0": "sha256:77f2952faf107bd2412e2373d37e50d7ecbf1da81d75d008233f24cf42fc1d5e"}, "docker": "quay.io/biocontainers/crispresso2", "aliases": {"CRISPResso": "/usr/local/bin/CRISPResso", "CRISPRessoAggregate": "/usr/local/bin/CRISPRessoAggregate", "CRISPRessoBatch": "/usr/local/bin/CRISPRessoBatch", "CRISPRessoCompare": "/usr/local/bin/CRISPRessoCompare", "CRISPRessoPooled": "/usr/local/bin/CRISPRessoPooled", "CRISPRessoPooledWGSCompare": "/usr/local/bin/CRISPRessoPooledWGSCompare", "CRISPRessoWGS": "/usr/local/bin/CRISPRessoWGS"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/crispresso2.
shpc-registry automated BioContainers addition for crispresso2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/crispresso2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/crispresso2:2.2.8--py38h6eac312_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/crispresso2/2.2.8--py38h6eac312_0
$ module help quay.io/biocontainers/crispresso2/2.2.8--py38h6eac312_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### crispresso2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### crispresso2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### crispresso2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### crispresso2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### crispresso2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### crispresso2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CRISPResso

```bash
$ singularity exec <container> /usr/local/bin/CRISPResso
$ podman run --it --rm --entrypoint /usr/local/bin/CRISPResso   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CRISPResso   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CRISPRessoAggregate

```bash
$ singularity exec <container> /usr/local/bin/CRISPRessoAggregate
$ podman run --it --rm --entrypoint /usr/local/bin/CRISPRessoAggregate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CRISPRessoAggregate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CRISPRessoBatch

```bash
$ singularity exec <container> /usr/local/bin/CRISPRessoBatch
$ podman run --it --rm --entrypoint /usr/local/bin/CRISPRessoBatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CRISPRessoBatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CRISPRessoCompare

```bash
$ singularity exec <container> /usr/local/bin/CRISPRessoCompare
$ podman run --it --rm --entrypoint /usr/local/bin/CRISPRessoCompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CRISPRessoCompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CRISPRessoPooled

```bash
$ singularity exec <container> /usr/local/bin/CRISPRessoPooled
$ podman run --it --rm --entrypoint /usr/local/bin/CRISPRessoPooled   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CRISPRessoPooled   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CRISPRessoPooledWGSCompare

```bash
$ singularity exec <container> /usr/local/bin/CRISPRessoPooledWGSCompare
$ podman run --it --rm --entrypoint /usr/local/bin/CRISPRessoPooledWGSCompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CRISPRessoPooledWGSCompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CRISPRessoWGS

```bash
$ singularity exec <container> /usr/local/bin/CRISPRessoWGS
$ podman run --it --rm --entrypoint /usr/local/bin/CRISPRessoWGS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CRISPRessoWGS   -v ${PWD} -w ${PWD} <container> -c " $@"
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