---
layout: container
name:  "quay.io/biocontainers/mirfix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mirfix/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mirfix/container.yaml"
updated_at: "2022-10-27 00:33:45.621034"
latest: "2.1.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/mirfix"
aliases:
 - "MIRfix.py"
 - "dialign2-2"
 - "runMIRfix.sh"
 - "testMIRfix.sh"
versions:
 - "2.1.0--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for mirfix"
config: {"url": "https://biocontainers.pro/tools/mirfix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mirfix", "latest": {"2.1.0--hdfd78af_0": "sha256:ddc45e81f31a1fcd852867932873d38608da93672640adf9df3bca43f4233f55"}, "tags": {"2.1.0--hdfd78af_0": "sha256:ddc45e81f31a1fcd852867932873d38608da93672640adf9df3bca43f4233f55"}, "docker": "quay.io/biocontainers/mirfix", "aliases": {"MIRfix.py": "/usr/local/bin/MIRfix.py", "dialign2-2": "/usr/local/bin/dialign2-2", "runMIRfix.sh": "/usr/local/bin/runMIRfix.sh", "testMIRfix.sh": "/usr/local/bin/testMIRfix.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mirfix.
shpc-registry automated BioContainers addition for mirfix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mirfix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mirfix:2.1.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mirfix/2.1.0--hdfd78af_0
$ module help quay.io/biocontainers/mirfix/2.1.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mirfix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mirfix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mirfix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mirfix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mirfix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mirfix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MIRfix.py

```bash
$ singularity exec <container> /usr/local/bin/MIRfix.py
$ podman run --it --rm --entrypoint /usr/local/bin/MIRfix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MIRfix.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dialign2-2

```bash
$ singularity exec <container> /usr/local/bin/dialign2-2
$ podman run --it --rm --entrypoint /usr/local/bin/dialign2-2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dialign2-2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runMIRfix.sh

```bash
$ singularity exec <container> /usr/local/bin/runMIRfix.sh
$ podman run --it --rm --entrypoint /usr/local/bin/runMIRfix.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runMIRfix.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### testMIRfix.sh

```bash
$ singularity exec <container> /usr/local/bin/testMIRfix.sh
$ podman run --it --rm --entrypoint /usr/local/bin/testMIRfix.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testMIRfix.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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