---
layout: container
name:  "quay.io/biocontainers/genome_updater"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genome_updater/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genome_updater/container.yaml"
updated_at: "2025-01-23 03:02:35.642415"
latest: "0.6.4--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/genome_updater"
aliases:
 - "genome_updater.sh"
 - "bc"
 - "dc"
 - "tar"
 - "gawk-5.1.0"
 - "basenc"
 - "b2sum"
 - "awk"
 - "base32"
 - "base64"
 - "basename"
versions:
 - "0.5.1--hdfd78af_0"
 - "0.5.2--hdfd78af_0"
 - "0.6.0--hdfd78af_0"
 - "0.6.2--hdfd78af_0"
 - "0.6.3--hdfd78af_0"
 - "0.6.3--hdfd78af_1"
 - "0.6.4--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for genome_updater"
config: {"url": "https://biocontainers.pro/tools/genome_updater", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genome_updater", "latest": {"0.6.4--hdfd78af_0": "sha256:a2d4becbfb8157866adae9d21a3bd84ab448136e833b4d37bf3b4137a5bde7f7"}, "tags": {"0.5.1--hdfd78af_0": "sha256:05e4f37e192c064941ca4ae049044b580906a209d5ce45a12bf26727c55e9a1a", "0.5.2--hdfd78af_0": "sha256:6b4e411389cd39be54436b51f6e4aa1892cdf154830097be8ee367024c9afb22", "0.6.0--hdfd78af_0": "sha256:9fe91437aa8f4d51593c8fbbb4daf9b8a99586748492de3261d30fe2bb63812a", "0.6.2--hdfd78af_0": "sha256:fb25281bef18c89c90db922b7d7a9fabd727a82c2d6f4f5512db831010566553", "0.6.3--hdfd78af_0": "sha256:558e76752cf1a9f10dd2cd3284c09cd228c5ea61bb69c9ab88e92ae62273969b", "0.6.3--hdfd78af_1": "sha256:6cc36e48226df3d923a57b262ee023bcce7603e86f435d233caaaeb8d5eeeb1c", "0.6.4--hdfd78af_0": "sha256:a2d4becbfb8157866adae9d21a3bd84ab448136e833b4d37bf3b4137a5bde7f7"}, "docker": "quay.io/biocontainers/genome_updater", "aliases": {"genome_updater.sh": "/usr/local/bin/genome_updater.sh", "bc": "/usr/local/bin/bc", "dc": "/usr/local/bin/dc", "tar": "/usr/local/bin/tar", "gawk-5.1.0": "/usr/local/bin/gawk-5.1.0", "basenc": "/usr/local/bin/basenc", "b2sum": "/usr/local/bin/b2sum", "awk": "/usr/local/bin/awk", "base32": "/usr/local/bin/base32", "base64": "/usr/local/bin/base64", "basename": "/usr/local/bin/basename"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genome_updater.
shpc-registry automated BioContainers addition for genome_updater
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genome_updater
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genome_updater:0.6.4--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genome_updater/0.6.4--hdfd78af_0
$ module help quay.io/biocontainers/genome_updater/0.6.4--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genome_updater-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genome_updater-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genome_updater-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genome_updater-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genome_updater-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genome_updater-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### genome_updater.sh

```bash
$ singularity exec <container> /usr/local/bin/genome_updater.sh
$ podman run --it --rm --entrypoint /usr/local/bin/genome_updater.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genome_updater.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bc

```bash
$ singularity exec <container> /usr/local/bin/bc
$ podman run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dc

```bash
$ singularity exec <container> /usr/local/bin/dc
$ podman run --it --rm --entrypoint /usr/local/bin/dc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tar

```bash
$ singularity exec <container> /usr/local/bin/tar
$ podman run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.1.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basenc

```bash
$ singularity exec <container> /usr/local/bin/basenc
$ podman run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### b2sum

```bash
$ singularity exec <container> /usr/local/bin/b2sum
$ podman run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### awk

```bash
$ singularity exec <container> /usr/local/bin/awk
$ podman run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### base32

```bash
$ singularity exec <container> /usr/local/bin/base32
$ podman run --it --rm --entrypoint /usr/local/bin/base32   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/base32   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### base64

```bash
$ singularity exec <container> /usr/local/bin/base64
$ podman run --it --rm --entrypoint /usr/local/bin/base64   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/base64   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basename

```bash
$ singularity exec <container> /usr/local/bin/basename
$ podman run --it --rm --entrypoint /usr/local/bin/basename   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basename   -v ${PWD} -w ${PWD} <container> -c " $@"
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