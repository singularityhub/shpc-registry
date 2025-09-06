---
layout: container
name:  "quay.io/biocontainers/mosdepth"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mosdepth/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mosdepth/container.yaml"
updated_at: "2025-09-06 03:40:47.757903"
latest: "0.3.11--h0ec343a_1"
container_url: "https://biocontainers.pro/tools/mosdepth"
aliases:
 - "mosdepth"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.3.3--h37c5b7d_2"
 - "0.3.3--hd299d5a_3"
 - "0.3.4--hd299d5a_0"
 - "0.3.5--hd299d5a_0"
 - "0.3.6--hd299d5a_0"
 - "0.3.7--hd299d5a_0"
 - "0.3.8--hd299d5a_0"
 - "0.3.10--hd299d5a_0"
 - "0.3.10--h4e814b3_1"
 - "0.3.11--h0ec343a_1"
description: "shpc-registry automated BioContainers addition for mosdepth"
config: {"url": "https://biocontainers.pro/tools/mosdepth", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mosdepth", "latest": {"0.3.11--h0ec343a_1": "sha256:3e49d0f00c85930ff894a648147a82910df38d281bf81faf4f0ca07a72e60e6b"}, "tags": {"0.3.3--h37c5b7d_2": "sha256:d550465fce1cbfbe9cfe0facd4aa910b455f9ba93f4f4d701a08a7096e8f7d6e", "0.3.3--hd299d5a_3": "sha256:ef76d433d242983979b72ff2ee03624be59330ea8a5bd7c70004953d265fcced", "0.3.4--hd299d5a_0": "sha256:472e9be8cb302027b0f498bebb8e629cfe36035670ebe1c669dc7fa98f97fc3e", "0.3.5--hd299d5a_0": "sha256:3a6d1f534b7d2cf7032fafc6cb84b992e016be84718e9f69157234ec3dfb10bb", "0.3.6--hd299d5a_0": "sha256:f2cbf66ac630cf14ae562294cc629a6885078c9271d713cb391de33e83238b64", "0.3.7--hd299d5a_0": "sha256:941c21a80e5214d4371343f35ef7287c3313e18987cbb8eb56c665fdd5bcea9e", "0.3.8--hd299d5a_0": "sha256:2decf63be02007796b4d1ab8389e99564a8c2eebeb5bad6983bdb1d7a99a657f", "0.3.10--hd299d5a_0": "sha256:d008e9dcea6d78a2176e0b7eb97e324271f795a041327104624db9deb3fe1e9a", "0.3.10--h4e814b3_1": "sha256:94b54a6a5610da01030307377ae75963820f661df8c251668c4156b0fdd0b76c", "0.3.11--h0ec343a_1": "sha256:3e49d0f00c85930ff894a648147a82910df38d281bf81faf4f0ca07a72e60e6b"}, "docker": "quay.io/biocontainers/mosdepth", "aliases": {"mosdepth": "/usr/local/bin/mosdepth", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mosdepth.
shpc-registry automated BioContainers addition for mosdepth
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mosdepth
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mosdepth:0.3.11--h0ec343a_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mosdepth/0.3.11--h0ec343a_1
$ module help quay.io/biocontainers/mosdepth/0.3.11--h0ec343a_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mosdepth-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mosdepth-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mosdepth-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mosdepth-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mosdepth-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mosdepth-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mosdepth

```bash
$ singularity exec <container> /usr/local/bin/mosdepth
$ podman run --it --rm --entrypoint /usr/local/bin/mosdepth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mosdepth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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