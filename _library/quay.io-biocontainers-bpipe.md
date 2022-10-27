---
layout: container
name:  "quay.io/biocontainers/bpipe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bpipe/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bpipe/container.yaml"
updated_at: "2022-10-27 00:31:23.320162"
latest: "0.9.9.9--0"
container_url: "https://biocontainers.pro/tools/bpipe"
aliases:
 - "bg-bpipe"
 - "bpipe"
 - "bpipe-pbspro.sh"
 - "bpipe-slurm.sh"
 - "bpipe-torque.sh"
 - "bpipe-utils.sh"
 - "groovy_script"
versions:
 - "0.9.9.9--0"
description: "shpc-registry automated BioContainers addition for bpipe"
config: {"url": "https://biocontainers.pro/tools/bpipe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bpipe", "latest": {"0.9.9.9--0": "sha256:0fb865041714af50badf982cfd7f27e90404d095cf5aeafe6f1c269745a4680e"}, "tags": {"0.9.9.9--0": "sha256:0fb865041714af50badf982cfd7f27e90404d095cf5aeafe6f1c269745a4680e"}, "docker": "quay.io/biocontainers/bpipe", "aliases": {"bg-bpipe": "/usr/local/bin/bg-bpipe", "bpipe": "/usr/local/bin/bpipe", "bpipe-pbspro.sh": "/usr/local/bin/bpipe-pbspro.sh", "bpipe-slurm.sh": "/usr/local/bin/bpipe-slurm.sh", "bpipe-torque.sh": "/usr/local/bin/bpipe-torque.sh", "bpipe-utils.sh": "/usr/local/bin/bpipe-utils.sh", "groovy_script": "/usr/local/bin/groovy_script"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bpipe.
shpc-registry automated BioContainers addition for bpipe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bpipe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bpipe:0.9.9.9--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bpipe/0.9.9.9--0
$ module help quay.io/biocontainers/bpipe/0.9.9.9--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bpipe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bpipe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bpipe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bpipe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bpipe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bpipe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bg-bpipe

```bash
$ singularity exec <container> /usr/local/bin/bg-bpipe
$ podman run --it --rm --entrypoint /usr/local/bin/bg-bpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bg-bpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpipe

```bash
$ singularity exec <container> /usr/local/bin/bpipe
$ podman run --it --rm --entrypoint /usr/local/bin/bpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpipe-pbspro.sh

```bash
$ singularity exec <container> /usr/local/bin/bpipe-pbspro.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bpipe-pbspro.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpipe-pbspro.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpipe-slurm.sh

```bash
$ singularity exec <container> /usr/local/bin/bpipe-slurm.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bpipe-slurm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpipe-slurm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpipe-torque.sh

```bash
$ singularity exec <container> /usr/local/bin/bpipe-torque.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bpipe-torque.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpipe-torque.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpipe-utils.sh

```bash
$ singularity exec <container> /usr/local/bin/bpipe-utils.sh
$ podman run --it --rm --entrypoint /usr/local/bin/bpipe-utils.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpipe-utils.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### groovy_script

```bash
$ singularity exec <container> /usr/local/bin/groovy_script
$ podman run --it --rm --entrypoint /usr/local/bin/groovy_script   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/groovy_script   -v ${PWD} -w ${PWD} <container> -c " $@"
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