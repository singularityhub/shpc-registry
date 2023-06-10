---
layout: container
name:  "quay.io/biocontainers/mmseqs2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mmseqs2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mmseqs2/container.yaml"
updated_at: "2023-06-10 02:58:11.363778"
latest: "14.7e284--pl5321h6a68c12_2"
container_url: "https://biocontainers.pro/tools/mmseqs2"
aliases:
 - "gawk-5.0.0"
 - "mmseqs"
 - "awk"
 - "gawk"
versions:
 - "9.d36de--h76f5088_0"
 - "14.7e284--pl5321hf1761c0_0"
 - "13.45111--pl5321hf1761c0_2"
 - "12.113e3--h2d02072_2"
 - "11.e1a1c--h2d02072_0"
 - "10.6d92c--h2d02072_0"
 - "14.7e284--pl5321h6a68c12_2"
description: "shpc-registry automated BioContainers addition for mmseqs2"
config: {"url": "https://biocontainers.pro/tools/mmseqs2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mmseqs2", "latest": {"14.7e284--pl5321h6a68c12_2": "sha256:39fdd64b142a968dadfc9235fa43ea42fed83a88c50236c5b2103048b18dd19d"}, "tags": {"9.d36de--h76f5088_0": "sha256:be4e2ed37332d1f7ed7290cedd7b90d6ef1dd01bdb5d3fa5a88d6078fb312f9b", "14.7e284--pl5321hf1761c0_0": "sha256:113d8ea13a66348f7be35045b0a94633a9fe0e2325116c08b8f441888ccc2320", "13.45111--pl5321hf1761c0_2": "sha256:72c1e3c7d017f5ce6131ee254f507d4d08c9836d10a5d91f0946696bdfa00fe3", "12.113e3--h2d02072_2": "sha256:b83cad00191547e71d736313a10003a8dcea362e8e019bada34bb12b93b82c26", "11.e1a1c--h2d02072_0": "sha256:822a6538814a5f2e19aeea8279e2bb0ad97fe0f2bf704a4761bf1ee96549122b", "10.6d92c--h2d02072_0": "sha256:d6ff6adc468dacaba19a7090bc95a9b1e5316f04811a1f2f7863c35da6cece9f", "14.7e284--pl5321h6a68c12_2": "sha256:39fdd64b142a968dadfc9235fa43ea42fed83a88c50236c5b2103048b18dd19d"}, "docker": "quay.io/biocontainers/mmseqs2", "aliases": {"gawk-5.0.0": "/usr/local/bin/gawk-5.0.0", "mmseqs": "/usr/local/bin/mmseqs", "awk": "/usr/local/bin/awk", "gawk": "/usr/local/bin/gawk"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mmseqs2.
shpc-registry automated BioContainers addition for mmseqs2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mmseqs2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mmseqs2:14.7e284--pl5321h6a68c12_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mmseqs2/14.7e284--pl5321h6a68c12_2
$ module help quay.io/biocontainers/mmseqs2/14.7e284--pl5321h6a68c12_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mmseqs2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mmseqs2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mmseqs2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mmseqs2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mmseqs2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mmseqs2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gawk-5.0.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.0.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.0.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.0.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mmseqs

```bash
$ singularity exec <container> /usr/local/bin/mmseqs
$ podman run --it --rm --entrypoint /usr/local/bin/mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
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