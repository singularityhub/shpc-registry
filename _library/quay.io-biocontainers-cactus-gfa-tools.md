---
layout: container
name:  "quay.io/biocontainers/cactus-gfa-tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cactus-gfa-tools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cactus-gfa-tools/container.yaml"
updated_at: "2025-11-17 03:42:50.265234"
latest: "0.1--h9948957_0"
container_url: "https://biocontainers.pro/tools/cactus-gfa-tools"
aliases:
 - "faprefix.sh"
 - "gaf2paf"
 - "gaf2unstable"
 - "gaffilter"
 - "mzgaf2paf"
 - "paf2lastz"
 - "paf2stable"
 - "pafcoverage"
 - "pafmask"
 - "rgfa-split"
 - "rgfa2paf"
versions:
 - "0.1--h9948957_0"
description: "singularity registry hpc automated addition for cactus-gfa-tools"
config: {"url": "https://biocontainers.pro/tools/cactus-gfa-tools", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for cactus-gfa-tools", "latest": {"0.1--h9948957_0": "sha256:6fafebd3c38f4a45ea0f8427f9056fa9ce1a6e9bc96969cf76628381ba0dd0e9"}, "tags": {"0.1--h9948957_0": "sha256:6fafebd3c38f4a45ea0f8427f9056fa9ce1a6e9bc96969cf76628381ba0dd0e9"}, "docker": "quay.io/biocontainers/cactus-gfa-tools", "aliases": {"faprefix.sh": "/usr/local/bin/faprefix.sh", "gaf2paf": "/usr/local/bin/gaf2paf", "gaf2unstable": "/usr/local/bin/gaf2unstable", "gaffilter": "/usr/local/bin/gaffilter", "mzgaf2paf": "/usr/local/bin/mzgaf2paf", "paf2lastz": "/usr/local/bin/paf2lastz", "paf2stable": "/usr/local/bin/paf2stable", "pafcoverage": "/usr/local/bin/pafcoverage", "pafmask": "/usr/local/bin/pafmask", "rgfa-split": "/usr/local/bin/rgfa-split", "rgfa2paf": "/usr/local/bin/rgfa2paf"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cactus-gfa-tools.
singularity registry hpc automated addition for cactus-gfa-tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cactus-gfa-tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cactus-gfa-tools:0.1--h9948957_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cactus-gfa-tools/0.1--h9948957_0
$ module help quay.io/biocontainers/cactus-gfa-tools/0.1--h9948957_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cactus-gfa-tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cactus-gfa-tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cactus-gfa-tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cactus-gfa-tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cactus-gfa-tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cactus-gfa-tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### faprefix.sh

```bash
$ singularity exec <container> /usr/local/bin/faprefix.sh
$ podman run --it --rm --entrypoint /usr/local/bin/faprefix.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faprefix.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gaf2paf

```bash
$ singularity exec <container> /usr/local/bin/gaf2paf
$ podman run --it --rm --entrypoint /usr/local/bin/gaf2paf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gaf2paf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gaf2unstable

```bash
$ singularity exec <container> /usr/local/bin/gaf2unstable
$ podman run --it --rm --entrypoint /usr/local/bin/gaf2unstable   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gaf2unstable   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gaffilter

```bash
$ singularity exec <container> /usr/local/bin/gaffilter
$ podman run --it --rm --entrypoint /usr/local/bin/gaffilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gaffilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mzgaf2paf

```bash
$ singularity exec <container> /usr/local/bin/mzgaf2paf
$ podman run --it --rm --entrypoint /usr/local/bin/mzgaf2paf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mzgaf2paf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paf2lastz

```bash
$ singularity exec <container> /usr/local/bin/paf2lastz
$ podman run --it --rm --entrypoint /usr/local/bin/paf2lastz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paf2lastz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paf2stable

```bash
$ singularity exec <container> /usr/local/bin/paf2stable
$ podman run --it --rm --entrypoint /usr/local/bin/paf2stable   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paf2stable   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pafcoverage

```bash
$ singularity exec <container> /usr/local/bin/pafcoverage
$ podman run --it --rm --entrypoint /usr/local/bin/pafcoverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pafcoverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pafmask

```bash
$ singularity exec <container> /usr/local/bin/pafmask
$ podman run --it --rm --entrypoint /usr/local/bin/pafmask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pafmask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rgfa-split

```bash
$ singularity exec <container> /usr/local/bin/rgfa-split
$ podman run --it --rm --entrypoint /usr/local/bin/rgfa-split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rgfa-split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rgfa2paf

```bash
$ singularity exec <container> /usr/local/bin/rgfa2paf
$ podman run --it --rm --entrypoint /usr/local/bin/rgfa2paf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rgfa2paf   -v ${PWD} -w ${PWD} <container> -c " $@"
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