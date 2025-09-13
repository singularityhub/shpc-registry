---
layout: container
name:  "quay.io/biocontainers/biscuit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biscuit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biscuit/container.yaml"
updated_at: "2025-09-13 02:52:30.203559"
latest: "1.7.0.20250512--hc4b60c0_0"
container_url: "https://biocontainers.pro/tools/biscuit"
aliases:
 - "QC.sh"
 - "biscuit"
 - "build_biscuit_QC_assets.pl"
 - "build_biscuit_QC_assets.pl.bak"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.1.0.20220707--he272189_1"
 - "1.2.0.20230130--he272189_0"
 - "1.2.0.20230130--h0be9327_2"
 - "1.2.1.20230601--h0be9327_2"
 - "1.3.0.20231027--h0be9327_0"
 - "1.4.0.20240108--h0be9327_0"
 - "1.5.0.20240506--h0be9327_0"
 - "1.6.0.20241216--h0886490_0"
 - "1.6.0.20241216--h0886490_1"
 - "1.6.1.20250415--h0886490_0"
 - "1.7.0.20250512--hc4b60c0_0"
description: "shpc-registry automated BioContainers addition for biscuit"
config: {"url": "https://biocontainers.pro/tools/biscuit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biscuit", "latest": {"1.7.0.20250512--hc4b60c0_0": "sha256:6051ea5105f3cb5fc0031306a64db25f2dcd266cab9dd33d63dae3f5ffe36286"}, "tags": {"1.1.0.20220707--he272189_1": "sha256:ca540d2b392d0e2ea6525b0b4e88e99eed713deff2bd6cec942e01b14333e270", "1.2.0.20230130--he272189_0": "sha256:9a6f6516d9e3d1c9a2d849cdfaa622ccc7124852e3351ad09cf8f33bb4c39cd9", "1.2.0.20230130--h0be9327_2": "sha256:3964101e1a5ca1fd50de20843a5e2dfeb012740b09881e5667ce89854ffff054", "1.2.1.20230601--h0be9327_2": "sha256:9b64ff83dec11fbebac4b2f0569519726515f38f1816768e0a329eaa6313c32d", "1.3.0.20231027--h0be9327_0": "sha256:12a82775c4dc35e5e1b0d7dfdc91b9450bf116e40bc3314ee834498481c4cb96", "1.4.0.20240108--h0be9327_0": "sha256:f3706dad7a813f1916cc1ab02fb4ac99d22399be5a5e1b74f983692a5f297f29", "1.5.0.20240506--h0be9327_0": "sha256:5a400f2d5f1dc8a7e1553eff4461125e1c5b050e01ec305fba61c26310490cfe", "1.6.0.20241216--h0886490_0": "sha256:9d47018abfa1308ffd2de83ebdc055baf284bb9b94fbf9eb48baf23576e2bb14", "1.6.0.20241216--h0886490_1": "sha256:01e406e77781f26e7b0896e4f802f41c86556c49903b54f3d9638d82f56a7044", "1.6.1.20250415--h0886490_0": "sha256:9393d7cc263d4749f5297858fd092f66b70c9f4b350909c0627f4dda731b696f", "1.7.0.20250512--hc4b60c0_0": "sha256:6051ea5105f3cb5fc0031306a64db25f2dcd266cab9dd33d63dae3f5ffe36286"}, "docker": "quay.io/biocontainers/biscuit", "aliases": {"QC.sh": "/usr/local/bin/QC.sh", "biscuit": "/usr/local/bin/biscuit", "build_biscuit_QC_assets.pl": "/usr/local/bin/build_biscuit_QC_assets.pl", "build_biscuit_QC_assets.pl.bak": "/usr/local/bin/build_biscuit_QC_assets.pl.bak", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biscuit.
shpc-registry automated BioContainers addition for biscuit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biscuit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biscuit:1.7.0.20250512--hc4b60c0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biscuit/1.7.0.20250512--hc4b60c0_0
$ module help quay.io/biocontainers/biscuit/1.7.0.20250512--hc4b60c0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biscuit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biscuit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biscuit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biscuit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biscuit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biscuit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### QC.sh

```bash
$ singularity exec <container> /usr/local/bin/QC.sh
$ podman run --it --rm --entrypoint /usr/local/bin/QC.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/QC.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### biscuit

```bash
$ singularity exec <container> /usr/local/bin/biscuit
$ podman run --it --rm --entrypoint /usr/local/bin/biscuit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biscuit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_biscuit_QC_assets.pl

```bash
$ singularity exec <container> /usr/local/bin/build_biscuit_QC_assets.pl
$ podman run --it --rm --entrypoint /usr/local/bin/build_biscuit_QC_assets.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_biscuit_QC_assets.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### build_biscuit_QC_assets.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/build_biscuit_QC_assets.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/build_biscuit_QC_assets.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_biscuit_QC_assets.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
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