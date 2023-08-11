---
layout: container
name:  "quay.io/biocontainers/fraggenescan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fraggenescan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fraggenescan/container.yaml"
updated_at: "2023-08-11 02:31:01.688313"
latest: "1.31--h031d066_6"
container_url: "https://biocontainers.pro/tools/fraggenescan"
aliases:
 - "FragGeneScan"
 - "run_FragGeneScan.pl"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.31--hec16e2b_4"
 - "1.31--h031d066_6"
description: "shpc-registry automated BioContainers addition for fraggenescan"
config: {"url": "https://biocontainers.pro/tools/fraggenescan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fraggenescan", "latest": {"1.31--h031d066_6": "sha256:3f526607afa5c14ac82543d109ebf9e411fb2e7f742b874de3bb789911965abb"}, "tags": {"1.31--hec16e2b_4": "sha256:aa423a24228d6ea9b6916e4e48aa9d2c000c8786ddcbd9de3194474c5b4ce00b", "1.31--h031d066_6": "sha256:3f526607afa5c14ac82543d109ebf9e411fb2e7f742b874de3bb789911965abb"}, "docker": "quay.io/biocontainers/fraggenescan", "aliases": {"FragGeneScan": "/usr/local/bin/FragGeneScan", "run_FragGeneScan.pl": "/usr/local/bin/run_FragGeneScan.pl", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fraggenescan.
shpc-registry automated BioContainers addition for fraggenescan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fraggenescan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fraggenescan:1.31--h031d066_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fraggenescan/1.31--h031d066_6
$ module help quay.io/biocontainers/fraggenescan/1.31--h031d066_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fraggenescan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fraggenescan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fraggenescan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fraggenescan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fraggenescan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fraggenescan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### FragGeneScan

```bash
$ singularity exec <container> /usr/local/bin/FragGeneScan
$ podman run --it --rm --entrypoint /usr/local/bin/FragGeneScan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FragGeneScan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_FragGeneScan.pl

```bash
$ singularity exec <container> /usr/local/bin/run_FragGeneScan.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run_FragGeneScan.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_FragGeneScan.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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