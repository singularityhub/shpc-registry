---
layout: container
name:  "quay.io/biocontainers/bioconductor-bnbc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bnbc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bnbc/container.yaml"
updated_at: "2023-07-25 03:30:33.770051"
latest: "1.20.0--r42hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-bnbc"
aliases:
 - "mpichversion"
 - "mpivars"
 - "parkill"
 - "hydra_nameserver"
 - "hydra_persist"
 - "hydra_pmi_proxy"
 - "mpiexec.hydra"
 - "mpifort"
 - "mpic++"
 - "mpicc"
versions:
 - "1.8.0--r36he1b5a44_0"
 - "1.16.0--r41hc247a5b_2"
 - "1.14.0--r41h399db7b_0"
 - "1.12.0--r40h399db7b_1"
 - "1.10.0--r40h5f743cb_0"
 - "1.20.0--r42hc247a5b_0"
 - "1.20.0--r42hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-bnbc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bnbc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bnbc", "latest": {"1.20.0--r42hf17093f_1": "sha256:95147d3a6c281c1ef15eaa46974793b3f9aae5db6157f5f6cf1979196d789b23"}, "tags": {"1.8.0--r36he1b5a44_0": "sha256:114a99caacce74252d1bbe103d2b0123058af05be6d58b7c03bb3d4992eafe7f", "1.16.0--r41hc247a5b_2": "sha256:f3c38e13c960ec0205f755b36cf2818f1b2027b4e6f1c0681082f9a627106052", "1.14.0--r41h399db7b_0": "sha256:5e6dbc7d9a895e847d2352d35c42a64ecd3b0f1654f2e7970b307dba6794324f", "1.12.0--r40h399db7b_1": "sha256:71e534da1ded5c5ab7f930ff921f25e627ed0002ac432f398bdc66255e3d3ce4", "1.10.0--r40h5f743cb_0": "sha256:8a3be8da821051f97627c0cad0af4bfc6957ecf2c5e2f4545390a0d0e9c15dff", "1.20.0--r42hc247a5b_0": "sha256:ef950e1598a42aff2f954dc3851887faff02c57ed175a11ff652dc2be461fc32", "1.20.0--r42hf17093f_1": "sha256:95147d3a6c281c1ef15eaa46974793b3f9aae5db6157f5f6cf1979196d789b23"}, "docker": "quay.io/biocontainers/bioconductor-bnbc", "aliases": {"mpichversion": "/usr/local/bin/mpichversion", "mpivars": "/usr/local/bin/mpivars", "parkill": "/usr/local/bin/parkill", "hydra_nameserver": "/usr/local/bin/hydra_nameserver", "hydra_persist": "/usr/local/bin/hydra_persist", "hydra_pmi_proxy": "/usr/local/bin/hydra_pmi_proxy", "mpiexec.hydra": "/usr/local/bin/mpiexec.hydra", "mpifort": "/usr/local/bin/mpifort", "mpic++": "/usr/local/bin/mpic++", "mpicc": "/usr/local/bin/mpicc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bnbc.
shpc-registry automated BioContainers addition for bioconductor-bnbc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bnbc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bnbc:1.20.0--r42hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bnbc/1.20.0--r42hf17093f_1
$ module help quay.io/biocontainers/bioconductor-bnbc/1.20.0--r42hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bnbc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bnbc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bnbc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bnbc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bnbc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bnbc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mpichversion

```bash
$ singularity exec <container> /usr/local/bin/mpichversion
$ podman run --it --rm --entrypoint /usr/local/bin/mpichversion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpichversion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpivars

```bash
$ singularity exec <container> /usr/local/bin/mpivars
$ podman run --it --rm --entrypoint /usr/local/bin/mpivars   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpivars   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parkill

```bash
$ singularity exec <container> /usr/local/bin/parkill
$ podman run --it --rm --entrypoint /usr/local/bin/parkill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parkill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hydra_nameserver

```bash
$ singularity exec <container> /usr/local/bin/hydra_nameserver
$ podman run --it --rm --entrypoint /usr/local/bin/hydra_nameserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hydra_nameserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hydra_persist

```bash
$ singularity exec <container> /usr/local/bin/hydra_persist
$ podman run --it --rm --entrypoint /usr/local/bin/hydra_persist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hydra_persist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hydra_pmi_proxy

```bash
$ singularity exec <container> /usr/local/bin/hydra_pmi_proxy
$ podman run --it --rm --entrypoint /usr/local/bin/hydra_pmi_proxy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hydra_pmi_proxy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpiexec.hydra

```bash
$ singularity exec <container> /usr/local/bin/mpiexec.hydra
$ podman run --it --rm --entrypoint /usr/local/bin/mpiexec.hydra   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpiexec.hydra   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpifort

```bash
$ singularity exec <container> /usr/local/bin/mpifort
$ podman run --it --rm --entrypoint /usr/local/bin/mpifort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpifort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpic++

```bash
$ singularity exec <container> /usr/local/bin/mpic++
$ podman run --it --rm --entrypoint /usr/local/bin/mpic++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpic++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpicc

```bash
$ singularity exec <container> /usr/local/bin/mpicc
$ podman run --it --rm --entrypoint /usr/local/bin/mpicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpicc   -v ${PWD} -w ${PWD} <container> -c " $@"
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