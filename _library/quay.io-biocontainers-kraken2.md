---
layout: container
name:  "quay.io/biocontainers/kraken2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kraken2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kraken2/container.yaml"
updated_at: "2026-01-13 03:57:37.289085"
latest: "2.17.1--pl5321h077b44d_0"
container_url: "https://biocontainers.pro/tools/kraken2"
aliases:
 - "kraken2"
 - "kraken2-build"
 - "kraken2-inspect"
 - "rsync-ssl"
 - "rsync"
 - "xxh128sum"
 - "xxh32sum"
 - "xxh64sum"
 - "xxhsum"
 - "tar"
 - "edirect.py"
 - "filter-columns"
 - "fuse-segments"
versions:
 - "2.1.2--pl5321h9f5acd7_2"
 - "2.1.2--pl5321h9f5acd7_3"
 - "2.1.2--pl5321h4ac6f70_4"
 - "2.1.3--pl5321hdcf5f25_0"
 - "2.1.3--pl5321hdcf5f25_1"
 - "2.1.3--pl5321hdcf5f25_2"
 - "2.1.3--pl5321hdcf5f25_3"
 - "2.1.3--pl5321h077b44d_4"
 - "2.14--pl5321h077b44d_0"
 - "2.1.5--pl5321h077b44d_0"
 - "2.1.6--pl5321h077b44d_0"
 - "2.17.1--pl5321h077b44d_0"
description: "shpc-registry automated BioContainers addition for kraken2"
config: {"url": "https://biocontainers.pro/tools/kraken2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kraken2", "latest": {"2.17.1--pl5321h077b44d_0": "sha256:c5eb4764f23e9db975cbc3e545d330e1fe468307f5e59a99c0ce8f4c1f6f09e2"}, "tags": {"2.1.2--pl5321h9f5acd7_2": "sha256:2208f6895251786e2a673789a3242d62873ac9e10d0edb40213e97ef7c92e980", "2.1.2--pl5321h9f5acd7_3": "sha256:7906d6b83f3f267e1bf2757d4c645182aa8268835ff161e247549d8e052b7688", "2.1.2--pl5321h4ac6f70_4": "sha256:fb9e117364facd81410de17959d94443be7eddca6e1706751a77110cef8e99ac", "2.1.3--pl5321hdcf5f25_0": "sha256:c1a6841172e73fd7c8e323471b7f10eb53d980ba0f01f487bc50bf984add8cb3", "2.1.3--pl5321hdcf5f25_1": "sha256:9b5374e9f97cce833534d09d2e29080061a50669b27ea304ce2dab2be9c59485", "2.1.3--pl5321hdcf5f25_2": "sha256:ede4b82d04f8c928613610df5dc6ee14c415d98ba233a9afc84cc3979e2295ae", "2.1.3--pl5321hdcf5f25_3": "sha256:9ea12c3f39c41ff7631f02e18ac5b492ae38bfe3d47cbcd05e874f48ec37c56b", "2.1.3--pl5321h077b44d_4": "sha256:a57825271a3306c9d35bee7ab6b497032fe34c37919165c0c235b5080ac5b3da", "2.14--pl5321h077b44d_0": "sha256:bb8bc0cf086413faf02715d060457f6078ff271f6d18d54b2734d740ac27e2d6", "2.1.5--pl5321h077b44d_0": "sha256:3fc4bff398ade0eba6674cc60d1de4879a26ec0e8f0ef0c27dc8decbed167db4", "2.1.6--pl5321h077b44d_0": "sha256:e34b3c44d75897c6ef640fbccbc49427a1ad60ec0e51388c255055c8f0ad1c66", "2.17.1--pl5321h077b44d_0": "sha256:c5eb4764f23e9db975cbc3e545d330e1fe468307f5e59a99c0ce8f4c1f6f09e2"}, "docker": "quay.io/biocontainers/kraken2", "aliases": {"kraken2": "/usr/local/bin/kraken2", "kraken2-build": "/usr/local/bin/kraken2-build", "kraken2-inspect": "/usr/local/bin/kraken2-inspect", "rsync-ssl": "/usr/local/bin/rsync-ssl", "rsync": "/usr/local/bin/rsync", "xxh128sum": "/usr/local/bin/xxh128sum", "xxh32sum": "/usr/local/bin/xxh32sum", "xxh64sum": "/usr/local/bin/xxh64sum", "xxhsum": "/usr/local/bin/xxhsum", "tar": "/usr/local/bin/tar", "edirect.py": "/usr/local/bin/edirect.py", "filter-columns": "/usr/local/bin/filter-columns", "fuse-segments": "/usr/local/bin/fuse-segments"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kraken2.
shpc-registry automated BioContainers addition for kraken2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kraken2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kraken2:2.17.1--pl5321h077b44d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kraken2/2.17.1--pl5321h077b44d_0
$ module help quay.io/biocontainers/kraken2/2.17.1--pl5321h077b44d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kraken2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kraken2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kraken2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kraken2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kraken2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kraken2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kraken2

```bash
$ singularity exec <container> /usr/local/bin/kraken2
$ podman run --it --rm --entrypoint /usr/local/bin/kraken2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken2-build

```bash
$ singularity exec <container> /usr/local/bin/kraken2-build
$ podman run --it --rm --entrypoint /usr/local/bin/kraken2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kraken2-inspect

```bash
$ singularity exec <container> /usr/local/bin/kraken2-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/kraken2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kraken2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsync-ssl

```bash
$ singularity exec <container> /usr/local/bin/rsync-ssl
$ podman run --it --rm --entrypoint /usr/local/bin/rsync-ssl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsync-ssl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsync

```bash
$ singularity exec <container> /usr/local/bin/rsync
$ podman run --it --rm --entrypoint /usr/local/bin/rsync   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsync   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxh128sum

```bash
$ singularity exec <container> /usr/local/bin/xxh128sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh128sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh128sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxh32sum

```bash
$ singularity exec <container> /usr/local/bin/xxh32sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh32sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh32sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxh64sum

```bash
$ singularity exec <container> /usr/local/bin/xxh64sum
$ podman run --it --rm --entrypoint /usr/local/bin/xxh64sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxh64sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xxhsum

```bash
$ singularity exec <container> /usr/local/bin/xxhsum
$ podman run --it --rm --entrypoint /usr/local/bin/xxhsum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xxhsum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tar

```bash
$ singularity exec <container> /usr/local/bin/tar
$ podman run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edirect.py

```bash
$ singularity exec <container> /usr/local/bin/edirect.py
$ podman run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-columns

```bash
$ singularity exec <container> /usr/local/bin/filter-columns
$ podman run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fuse-segments

```bash
$ singularity exec <container> /usr/local/bin/fuse-segments
$ podman run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
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