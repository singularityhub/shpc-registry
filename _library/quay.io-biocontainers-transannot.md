---
layout: container
name:  "quay.io/biocontainers/transannot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/transannot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/transannot/container.yaml"
updated_at: "2025-01-31 02:51:07.516155"
latest: "3.70b2a60--pl5321h6a68c12_1"
container_url: "https://biocontainers.pro/tools/transannot"
aliases:
 - "transannot"
 - "aria2c"
 - "gawk-5.1.0"
 - "awk"
 - "gawk"
 - "idn2"
 - "wget"
versions:
 - "1.fa9ebab--pl5321h6a68c12_0"
 - "3.70b2a60--pl5321h6a68c12_1"
 - "3.7f1c8e1--pl5321h6a68c12_0"
 - "3.0.0--h6a68c12_0"
 - "3.0.0--hd6d6fdc_1"
description: "singularity registry hpc automated addition for transannot"
config: {"url": "https://biocontainers.pro/tools/transannot", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for transannot", "latest": {"3.70b2a60--pl5321h6a68c12_1": "sha256:28418c3d7716512fd79b9b1555584466268545b1e90eb7d765a3755598543110"}, "tags": {"1.fa9ebab--pl5321h6a68c12_0": "sha256:4e32c47c5372096271de24bf9e49904dd63b7ca3adaeaaa908ed72f3f1e78b51", "3.70b2a60--pl5321h6a68c12_1": "sha256:28418c3d7716512fd79b9b1555584466268545b1e90eb7d765a3755598543110", "3.7f1c8e1--pl5321h6a68c12_0": "sha256:0178bd67085296f626062265842df772e2c66df4b727010df7730fa439c72308", "3.0.0--h6a68c12_0": "sha256:701f2d0e401170d7849cd9586da030d53eaf69abdc1614b7f3c34d1da2beda7f", "3.0.0--hd6d6fdc_1": "sha256:9948594b353ede293c849ccb59ef6cb80be98dba51ebbebdb2814b540dc42032"}, "docker": "quay.io/biocontainers/transannot", "aliases": {"transannot": "/usr/local/bin/transannot", "aria2c": "/usr/local/bin/aria2c", "gawk-5.1.0": "/usr/local/bin/gawk-5.1.0", "awk": "/usr/local/bin/awk", "gawk": "/usr/local/bin/gawk", "idn2": "/usr/local/bin/idn2", "wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/transannot.
singularity registry hpc automated addition for transannot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/transannot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/transannot:3.70b2a60--pl5321h6a68c12_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/transannot/3.70b2a60--pl5321h6a68c12_1
$ module help quay.io/biocontainers/transannot/3.70b2a60--pl5321h6a68c12_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### transannot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### transannot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### transannot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### transannot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### transannot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### transannot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### transannot

```bash
$ singularity exec <container> /usr/local/bin/transannot
$ podman run --it --rm --entrypoint /usr/local/bin/transannot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transannot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aria2c

```bash
$ singularity exec <container> /usr/local/bin/aria2c
$ podman run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.1.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### awk

```bash
$ singularity exec <container> /usr/local/bin/awk
$ podman run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk

```bash
$ singularity exec <container> /usr/local/bin/gawk
$ podman run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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