---
layout: container
name:  "quay.io/biocontainers/rosella"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rosella/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rosella/container.yaml"
updated_at: "2025-01-17 02:54:32.557485"
latest: "0.5.5--h8e1a5b0_0"
container_url: "https://biocontainers.pro/tools/rosella"
aliases:
 - "remove_minimap2_duplicated_headers"
 - "rosella"
 - "starcode"
 - "parsort"
 - "env_parallel"
 - "env_parallel.ash"
 - "env_parallel.bash"
 - "env_parallel.csh"
 - "env_parallel.dash"
 - "env_parallel.fish"
 - "env_parallel.ksh"
 - "env_parallel.mksh"
 - "env_parallel.pdksh"
versions:
 - "0.4.2--h6f8cb4c_1"
 - "0.4.2--h8e1a5b0_2"
 - "0.5.1--h8e1a5b0_0"
 - "0.5.2--h8e1a5b0_0"
 - "0.5.3--h8e1a5b0_0"
 - "0.5.4--h8e1a5b0_0"
 - "0.5.5--h8e1a5b0_0"
description: "shpc-registry automated BioContainers addition for rosella"
config: {"url": "https://biocontainers.pro/tools/rosella", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rosella", "latest": {"0.5.5--h8e1a5b0_0": "sha256:29a921ccd59de40caa6809508545bab8c0acac8befb86bafc8c9f34277e5a3c3"}, "tags": {"0.4.2--h6f8cb4c_1": "sha256:fcb2fcaae42cdc1e56176dde8ee177f3ba4f0b9fe220f6e5e7ee3aacc374c6a2", "0.4.2--h8e1a5b0_2": "sha256:3a4d0c0189f5cc296dde835d24491f901cbef447cafff4102fed896e77838268", "0.5.1--h8e1a5b0_0": "sha256:3e3815389e45839026de67cc4c2f34e1006be044d67a8da1a3cf172ec25c39e8", "0.5.2--h8e1a5b0_0": "sha256:909fe34694197733e957c6184813a0641a037e9dcdbe321bfded34fd377bf2b7", "0.5.3--h8e1a5b0_0": "sha256:4f5a544b278d0ef41289c81f7d50e74c21107cf0fa0aedbd9945db8397a00cec", "0.5.4--h8e1a5b0_0": "sha256:6018222cbfab3c5b64ff9594c9b29e810fd22e7e2fbb6aa6f7e3a4012f0d6ca2", "0.5.5--h8e1a5b0_0": "sha256:29a921ccd59de40caa6809508545bab8c0acac8befb86bafc8c9f34277e5a3c3"}, "docker": "quay.io/biocontainers/rosella", "aliases": {"remove_minimap2_duplicated_headers": "/usr/local/bin/remove_minimap2_duplicated_headers", "rosella": "/usr/local/bin/rosella", "starcode": "/usr/local/bin/starcode", "parsort": "/usr/local/bin/parsort", "env_parallel": "/usr/local/bin/env_parallel", "env_parallel.ash": "/usr/local/bin/env_parallel.ash", "env_parallel.bash": "/usr/local/bin/env_parallel.bash", "env_parallel.csh": "/usr/local/bin/env_parallel.csh", "env_parallel.dash": "/usr/local/bin/env_parallel.dash", "env_parallel.fish": "/usr/local/bin/env_parallel.fish", "env_parallel.ksh": "/usr/local/bin/env_parallel.ksh", "env_parallel.mksh": "/usr/local/bin/env_parallel.mksh", "env_parallel.pdksh": "/usr/local/bin/env_parallel.pdksh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rosella.
shpc-registry automated BioContainers addition for rosella
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rosella
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rosella:0.5.5--h8e1a5b0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rosella/0.5.5--h8e1a5b0_0
$ module help quay.io/biocontainers/rosella/0.5.5--h8e1a5b0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rosella-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rosella-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rosella-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rosella-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rosella-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rosella-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### remove_minimap2_duplicated_headers

```bash
$ singularity exec <container> /usr/local/bin/remove_minimap2_duplicated_headers
$ podman run --it --rm --entrypoint /usr/local/bin/remove_minimap2_duplicated_headers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove_minimap2_duplicated_headers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rosella

```bash
$ singularity exec <container> /usr/local/bin/rosella
$ podman run --it --rm --entrypoint /usr/local/bin/rosella   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rosella   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### starcode

```bash
$ singularity exec <container> /usr/local/bin/starcode
$ podman run --it --rm --entrypoint /usr/local/bin/starcode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/starcode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parsort

```bash
$ singularity exec <container> /usr/local/bin/parsort
$ podman run --it --rm --entrypoint /usr/local/bin/parsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel

```bash
$ singularity exec <container> /usr/local/bin/env_parallel
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.ash

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.ash
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.ash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.ash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.bash

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.bash
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.csh

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.csh
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.dash

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.dash
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.dash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.dash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.fish

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.fish
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.fish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.fish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.ksh

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.ksh
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.ksh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.ksh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.mksh

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.mksh
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.mksh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.mksh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### env_parallel.pdksh

```bash
$ singularity exec <container> /usr/local/bin/env_parallel.pdksh
$ podman run --it --rm --entrypoint /usr/local/bin/env_parallel.pdksh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/env_parallel.pdksh   -v ${PWD} -w ${PWD} <container> -c " $@"
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