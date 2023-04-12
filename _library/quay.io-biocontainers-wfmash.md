---
layout: container
name:  "quay.io/biocontainers/wfmash"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/wfmash/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/wfmash/container.yaml"
updated_at: "2023-04-12 02:59:20.188847"
latest: "0.10.2--h71f629c_1"
container_url: "https://biocontainers.pro/tools/wfmash"
aliases:
 - "wfmash"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.9.1--hfdddef0_3"
 - "0.10.0--hfdddef0_0"
 - "0.10.0--hfdddef0_2"
 - "0.10.1--hfdddef0_0"
 - "0.10.2--hfdddef0_0"
 - "0.10.2--h71f629c_1"
description: "shpc-registry automated BioContainers addition for wfmash"
config: {"url": "https://biocontainers.pro/tools/wfmash", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for wfmash", "latest": {"0.10.2--h71f629c_1": "sha256:7c9bd0a8cbf23716bae907cbb134197712915dc32c6e95cf5284dbace87faf80"}, "tags": {"0.9.1--hfdddef0_3": "sha256:a4d74aac03fac24d65c01df40db6018830824f22ed0e1a3645f6ddcbb0186fbc", "0.10.0--hfdddef0_0": "sha256:835276ccd4754e135c64c509f909077fd9d29dc32e9e0d04566b23587abee4c2", "0.10.0--hfdddef0_2": "sha256:c1ba386d30c832d896605d3903975a986993d7d3d8e121e2d5257e7cc3b35054", "0.10.1--hfdddef0_0": "sha256:14e8ad45827a0cff4f7cfdf259d8cf94551d30ce834b2c55a918d0acebca2baf", "0.10.2--hfdddef0_0": "sha256:6a45ccf742075051599b8d15ad26e10b054504ab3cc70559d8d9a01d623be415", "0.10.2--h71f629c_1": "sha256:7c9bd0a8cbf23716bae907cbb134197712915dc32c6e95cf5284dbace87faf80"}, "docker": "quay.io/biocontainers/wfmash", "aliases": {"wfmash": "/usr/local/bin/wfmash", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/wfmash.
shpc-registry automated BioContainers addition for wfmash
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/wfmash
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/wfmash:0.10.2--h71f629c_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/wfmash/0.10.2--h71f629c_1
$ module help quay.io/biocontainers/wfmash/0.10.2--h71f629c_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### wfmash-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### wfmash-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### wfmash-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### wfmash-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### wfmash-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### wfmash-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wfmash

```bash
$ singularity exec <container> /usr/local/bin/wfmash
$ podman run --it --rm --entrypoint /usr/local/bin/wfmash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wfmash   -v ${PWD} -w ${PWD} <container> -c " $@"
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