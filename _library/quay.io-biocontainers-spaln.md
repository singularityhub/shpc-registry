---
layout: container
name:  "quay.io/biocontainers/spaln"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/spaln/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/spaln/container.yaml"
updated_at: "2025-08-10 04:18:12.850583"
latest: "3.0.7--pl5321h077b44d_0"
container_url: "https://biocontainers.pro/tools/spaln"
aliases:
 - "catchr.pl"
 - "makblk.pl"
 - "makdbs"
 - "makeidx.pl"
 - "makmdm"
 - "sortgrcd"
 - "spaln"
 - "spspaln.pl"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "2.4.9--pl5321hd03093a_0"
 - "2.4.13--pl5321h9f5acd7_0"
 - "2.4.13--pl5321h9f5acd7_1"
 - "2.4.13--pl5321h4ac6f70_2"
 - "3.0.1--pl5321h4ac6f70_0"
 - "3.0.4--pl5321hdcf5f25_0"
 - "3.0.6--pl5321hdcf5f25_0"
 - "3.0.6b--pl5321hdcf5f25_0"
 - "3.0.6b--pl5321h077b44d_1"
 - "3.0.7--pl5321h077b44d_0"
description: "shpc-registry automated BioContainers addition for spaln"
config: {"url": "https://biocontainers.pro/tools/spaln", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for spaln", "latest": {"3.0.7--pl5321h077b44d_0": "sha256:e1c03c8eab2debb63713db52f068923de5d2ecf9ee7a7cb4efda17a48667248a"}, "tags": {"2.4.9--pl5321hd03093a_0": "sha256:34800f4b833dbeaefb8795acfcc53083680e2bb1baa5ea01b680d52764dec858", "2.4.13--pl5321h9f5acd7_0": "sha256:56acb30ea1b953c21a8e8e76d7ba6118bbcf9860f2dcd3e4a4fda66b75400927", "2.4.13--pl5321h9f5acd7_1": "sha256:2ace59f46140dd2ab4d8abba3fb31b2c0fa227e01b7c53e95f0c5ce396effb73", "2.4.13--pl5321h4ac6f70_2": "sha256:a70af0d5daf8c0e9d13d8d7bd6f8f5230ecbd8c7d016c0d7e636047c4e710fcf", "3.0.1--pl5321h4ac6f70_0": "sha256:eac11f9a86d2e0fcaa25191122498b2d7538810b0a38e2146ae52bad4ba18d64", "3.0.4--pl5321hdcf5f25_0": "sha256:862f09e437de86f2cc937fc3f8846e98d4e1c3ac612728ee3325657542391c5b", "3.0.6--pl5321hdcf5f25_0": "sha256:957dbb276068579a8aee4fe9d339c0d48166a60ce74bfeb8c04231903bd5d4a3", "3.0.6b--pl5321hdcf5f25_0": "sha256:369473900c9e9ecd0942792b114b598ba778d9302da83193fa95b6f27cd1b130", "3.0.6b--pl5321h077b44d_1": "sha256:918b99867b16845930c5c4171b7088412b9a94c3d2383dc9627493bf261400ac", "3.0.7--pl5321h077b44d_0": "sha256:e1c03c8eab2debb63713db52f068923de5d2ecf9ee7a7cb4efda17a48667248a"}, "docker": "quay.io/biocontainers/spaln", "aliases": {"catchr.pl": "/usr/local/bin/catchr.pl", "makblk.pl": "/usr/local/bin/makblk.pl", "makdbs": "/usr/local/bin/makdbs", "makeidx.pl": "/usr/local/bin/makeidx.pl", "makmdm": "/usr/local/bin/makmdm", "sortgrcd": "/usr/local/bin/sortgrcd", "spaln": "/usr/local/bin/spaln", "spspaln.pl": "/usr/local/bin/spspaln.pl", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/spaln.
shpc-registry automated BioContainers addition for spaln
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/spaln
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/spaln:3.0.7--pl5321h077b44d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/spaln/3.0.7--pl5321h077b44d_0
$ module help quay.io/biocontainers/spaln/3.0.7--pl5321h077b44d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spaln-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spaln-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spaln-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spaln-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spaln-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spaln-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### catchr.pl

```bash
$ singularity exec <container> /usr/local/bin/catchr.pl
$ podman run --it --rm --entrypoint /usr/local/bin/catchr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/catchr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makblk.pl

```bash
$ singularity exec <container> /usr/local/bin/makblk.pl
$ podman run --it --rm --entrypoint /usr/local/bin/makblk.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makblk.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makdbs

```bash
$ singularity exec <container> /usr/local/bin/makdbs
$ podman run --it --rm --entrypoint /usr/local/bin/makdbs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makdbs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeidx.pl

```bash
$ singularity exec <container> /usr/local/bin/makeidx.pl
$ podman run --it --rm --entrypoint /usr/local/bin/makeidx.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeidx.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makmdm

```bash
$ singularity exec <container> /usr/local/bin/makmdm
$ podman run --it --rm --entrypoint /usr/local/bin/makmdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makmdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sortgrcd

```bash
$ singularity exec <container> /usr/local/bin/sortgrcd
$ podman run --it --rm --entrypoint /usr/local/bin/sortgrcd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sortgrcd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spaln

```bash
$ singularity exec <container> /usr/local/bin/spaln
$ podman run --it --rm --entrypoint /usr/local/bin/spaln   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spaln   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spspaln.pl

```bash
$ singularity exec <container> /usr/local/bin/spspaln.pl
$ podman run --it --rm --entrypoint /usr/local/bin/spspaln.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spspaln.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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