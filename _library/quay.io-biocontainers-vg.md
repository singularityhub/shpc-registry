---
layout: container
name:  "quay.io/biocontainers/vg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vg/container.yaml"
updated_at: "2023-12-19 02:46:17.259987"
latest: "1.53.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/vg"
aliases:
 - "vg"
versions:
 - "1.43.0--h9ee0642_0"
 - "1.44.0--h9ee0642_0"
 - "1.45.0--h9ee0642_0"
 - "1.46.0--h9ee0642_0"
 - "1.47.0--h9ee0642_0"
 - "1.48.0--h9ee0642_0"
 - "1.49.0--h9ee0642_0"
 - "1.50.1--h9ee0642_0"
 - "1.51.0--h9ee0642_0"
 - "1.52.0--h9ee0642_0"
 - "1.53.0--h9ee0642_0"
description: "shpc-registry automated BioContainers addition for vg"
config: {"url": "https://biocontainers.pro/tools/vg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vg", "latest": {"1.53.0--h9ee0642_0": "sha256:11f680378fc69c2a80fec9229cffe5c62a96455b45271d1e7b37bbc51d26cd2d"}, "tags": {"1.43.0--h9ee0642_0": "sha256:767ff7be84ce574899ca0ce2fd8a7305835dba741aeb9bd45974b56c7095b8f2", "1.44.0--h9ee0642_0": "sha256:3a91a6f0e09b3e4a555fccd56e35fa6ff941050b2530b328ac38c70a7d1a1679", "1.45.0--h9ee0642_0": "sha256:753390f9fc26ce541bb3e6949beeeecaae0e4290121229cbd5315f08692df8a8", "1.46.0--h9ee0642_0": "sha256:5eddfb5b0db1828e4ab9eebba3b8f5305867f16d582c971d6da638d1b172699b", "1.47.0--h9ee0642_0": "sha256:d4d51e56250b777c6a2248b658ef285cd685febf80e069b85b1c628b182e0c35", "1.48.0--h9ee0642_0": "sha256:0220f8f2ad88f9aaf2f97ef4b9d1b37de55fe280e3998e15a769ee587d6625ba", "1.49.0--h9ee0642_0": "sha256:86dcd55ecee78836356ca1d7096b27c8821e9d502a80228c50e2c930f6fe120e", "1.50.1--h9ee0642_0": "sha256:c3b63f3f7a526f703576afeffd3a061011446fa15a73689e09baa0b418723910", "1.51.0--h9ee0642_0": "sha256:9ecd42707d3637ab213e9467e39e446b10234607953e6e581c8eb5865245dd96", "1.52.0--h9ee0642_0": "sha256:fd605c71e6fa2718f14e3dcddd597a8dd4b34616f99cb8ebac5c24aa34bbafdd", "1.53.0--h9ee0642_0": "sha256:11f680378fc69c2a80fec9229cffe5c62a96455b45271d1e7b37bbc51d26cd2d"}, "docker": "quay.io/biocontainers/vg", "aliases": {"vg": "/usr/local/bin/vg"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vg.
shpc-registry automated BioContainers addition for vg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vg:1.53.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vg/1.53.0--h9ee0642_0
$ module help quay.io/biocontainers/vg/1.53.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vg

```bash
$ singularity exec <container> /usr/local/bin/vg
$ podman run --it --rm --entrypoint /usr/local/bin/vg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vg   -v ${PWD} -w ${PWD} <container> -c " $@"
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