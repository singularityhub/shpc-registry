---
layout: container
name:  "quay.io/biocontainers/wgdi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/wgdi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/wgdi/container.yaml"
updated_at: "2025-08-25 03:24:44.502433"
latest: "0.74--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/wgdi"
aliases:
 - "divvier"
 - "iqtree2"
 - "pal2nal.pl"
 - "wgdi"
 - "readal"
 - "statal"
 - "trimal"
 - "iqtree"
 - "FastTreeMP"
 - "muscle"
 - "FastTree"
 - "fasttree"
 - "baseml"
 - "basemlg"
versions:
 - "0.6.1--pyhdfd78af_0"
 - "0.6.2--pyhdfd78af_0"
 - "0.6.3--pyhdfd78af_0"
 - "0.6.4--pyhdfd78af_0"
 - "0.6.5--pyhdfd78af_0"
 - "0.72--pyhdfd78af_0"
 - "0.71--pyhdfd78af_0"
 - "0.7--pyhdfd78af_1"
 - "0.74--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for wgdi"
config: {"url": "https://biocontainers.pro/tools/wgdi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for wgdi", "latest": {"0.74--pyhdfd78af_0": "sha256:39559e4d5992bafe1f0e700b7d9505b01ac620bc28095335a680b6eb8653fd38"}, "tags": {"0.6.1--pyhdfd78af_0": "sha256:323c2e9fed19e2b6fd9665b68495a900e8606906ddf412e13dd415196d8c0abf", "0.6.2--pyhdfd78af_0": "sha256:250504ee7e5846d3ae2065002cd372f0b59b531142a83d7c5730574466805c77", "0.6.3--pyhdfd78af_0": "sha256:eaa1a7be35d4c2aa306c9fc48daf798aab7c20bf8df9a6aec3d33353fc7c1abe", "0.6.4--pyhdfd78af_0": "sha256:798431848dd975f1a6e8ac80911729b06dd54d41a887d0d27e3654d217376b84", "0.6.5--pyhdfd78af_0": "sha256:66c016c9a432849cda3ec17e3d07be338c1d17c0249b5ce2cfdb1ba37d300083", "0.72--pyhdfd78af_0": "sha256:a6e06c9176cd4c3538269e3b86a74d22c95435ede781bb918a6e62bdefd0b3b7", "0.71--pyhdfd78af_0": "sha256:e9aa6b58bbb29d99918bb80fbce4a4374c8fb1991a8544964f9ed18431f1dad7", "0.7--pyhdfd78af_1": "sha256:ed202ce70542b9174abf839a7bf74fd87b6d950d71443a4d925063df946ffd0a", "0.74--pyhdfd78af_0": "sha256:39559e4d5992bafe1f0e700b7d9505b01ac620bc28095335a680b6eb8653fd38"}, "docker": "quay.io/biocontainers/wgdi", "aliases": {"divvier": "/usr/local/bin/divvier", "iqtree2": "/usr/local/bin/iqtree2", "pal2nal.pl": "/usr/local/bin/pal2nal.pl", "wgdi": "/usr/local/bin/wgdi", "readal": "/usr/local/bin/readal", "statal": "/usr/local/bin/statal", "trimal": "/usr/local/bin/trimal", "iqtree": "/usr/local/bin/iqtree", "FastTreeMP": "/usr/local/bin/FastTreeMP", "muscle": "/usr/local/bin/muscle", "FastTree": "/usr/local/bin/FastTree", "fasttree": "/usr/local/bin/fasttree", "baseml": "/usr/local/bin/baseml", "basemlg": "/usr/local/bin/basemlg"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/wgdi.
shpc-registry automated BioContainers addition for wgdi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/wgdi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/wgdi:0.74--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/wgdi/0.74--pyhdfd78af_0
$ module help quay.io/biocontainers/wgdi/0.74--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### wgdi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### wgdi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### wgdi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### wgdi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### wgdi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### wgdi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### divvier

```bash
$ singularity exec <container> /usr/local/bin/divvier
$ podman run --it --rm --entrypoint /usr/local/bin/divvier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/divvier   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iqtree2

```bash
$ singularity exec <container> /usr/local/bin/iqtree2
$ podman run --it --rm --entrypoint /usr/local/bin/iqtree2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iqtree2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pal2nal.pl

```bash
$ singularity exec <container> /usr/local/bin/pal2nal.pl
$ podman run --it --rm --entrypoint /usr/local/bin/pal2nal.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pal2nal.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wgdi

```bash
$ singularity exec <container> /usr/local/bin/wgdi
$ podman run --it --rm --entrypoint /usr/local/bin/wgdi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wgdi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readal

```bash
$ singularity exec <container> /usr/local/bin/readal
$ podman run --it --rm --entrypoint /usr/local/bin/readal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### statal

```bash
$ singularity exec <container> /usr/local/bin/statal
$ podman run --it --rm --entrypoint /usr/local/bin/statal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/statal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trimal

```bash
$ singularity exec <container> /usr/local/bin/trimal
$ podman run --it --rm --entrypoint /usr/local/bin/trimal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iqtree

```bash
$ singularity exec <container> /usr/local/bin/iqtree
$ podman run --it --rm --entrypoint /usr/local/bin/iqtree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iqtree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTreeMP

```bash
$ singularity exec <container> /usr/local/bin/FastTreeMP
$ podman run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTreeMP   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### muscle

```bash
$ singularity exec <container> /usr/local/bin/muscle
$ podman run --it --rm --entrypoint /usr/local/bin/muscle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/muscle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FastTree

```bash
$ singularity exec <container> /usr/local/bin/FastTree
$ podman run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastTree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasttree

```bash
$ singularity exec <container> /usr/local/bin/fasttree
$ podman run --it --rm --entrypoint /usr/local/bin/fasttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasttree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### baseml

```bash
$ singularity exec <container> /usr/local/bin/baseml
$ podman run --it --rm --entrypoint /usr/local/bin/baseml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/baseml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basemlg

```bash
$ singularity exec <container> /usr/local/bin/basemlg
$ podman run --it --rm --entrypoint /usr/local/bin/basemlg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basemlg   -v ${PWD} -w ${PWD} <container> -c " $@"
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