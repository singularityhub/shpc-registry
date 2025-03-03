---
layout: container
name:  "quay.io/biocontainers/kpop"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kpop/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kpop/container.yaml"
updated_at: "2025-03-03 03:01:28.860123"
latest: "1.1.1--h9ee0642_1"
container_url: "https://biocontainers.pro/tools/kpop"
aliases:
 - "KPopCount"
 - "KPopCountDB"
 - "KPopTwist"
 - "KPopTwistDB"
 - "KPopTwist_"
 - "pcre2posix_test"
 - "hb-info"
 - "tjbench"
versions:
 - "1.1.1--h9ee0642_0"
 - "1.1.1--h9ee0642_1"
description: "singularity registry hpc automated addition for kpop"
config: {"url": "https://biocontainers.pro/tools/kpop", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for kpop", "latest": {"1.1.1--h9ee0642_1": "sha256:f9fd6a1ab3bccf0afd23995c0f4b5e9adacca6ad6da1b7a5dab86cd4b051a545"}, "tags": {"1.1.1--h9ee0642_0": "sha256:a8c5c0ed1011707c57f38fc55556a96234d94315cf3f2e590944f1c08aeda0cc", "1.1.1--h9ee0642_1": "sha256:f9fd6a1ab3bccf0afd23995c0f4b5e9adacca6ad6da1b7a5dab86cd4b051a545"}, "docker": "quay.io/biocontainers/kpop", "aliases": {"KPopCount": "/usr/local/bin/KPopCount", "KPopCountDB": "/usr/local/bin/KPopCountDB", "KPopTwist": "/usr/local/bin/KPopTwist", "KPopTwistDB": "/usr/local/bin/KPopTwistDB", "KPopTwist_": "/usr/local/bin/KPopTwist_", "pcre2posix_test": "/usr/local/bin/pcre2posix_test", "hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kpop.
singularity registry hpc automated addition for kpop
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kpop
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kpop:1.1.1--h9ee0642_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kpop/1.1.1--h9ee0642_1
$ module help quay.io/biocontainers/kpop/1.1.1--h9ee0642_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kpop-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kpop-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kpop-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kpop-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kpop-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kpop-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### KPopCount

```bash
$ singularity exec <container> /usr/local/bin/KPopCount
$ podman run --it --rm --entrypoint /usr/local/bin/KPopCount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/KPopCount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### KPopCountDB

```bash
$ singularity exec <container> /usr/local/bin/KPopCountDB
$ podman run --it --rm --entrypoint /usr/local/bin/KPopCountDB   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/KPopCountDB   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### KPopTwist

```bash
$ singularity exec <container> /usr/local/bin/KPopTwist
$ podman run --it --rm --entrypoint /usr/local/bin/KPopTwist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/KPopTwist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### KPopTwistDB

```bash
$ singularity exec <container> /usr/local/bin/KPopTwistDB
$ podman run --it --rm --entrypoint /usr/local/bin/KPopTwistDB   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/KPopTwistDB   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### KPopTwist_

```bash
$ singularity exec <container> /usr/local/bin/KPopTwist_
$ podman run --it --rm --entrypoint /usr/local/bin/KPopTwist_   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/KPopTwist_   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pcre2posix_test

```bash
$ singularity exec <container> /usr/local/bin/pcre2posix_test
$ podman run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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