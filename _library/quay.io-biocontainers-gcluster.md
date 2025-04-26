---
layout: container
name:  "quay.io/biocontainers/gcluster"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gcluster/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gcluster/container.yaml"
updated_at: "2025-04-26 03:42:08.652721"
latest: "2.06--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/gcluster"
aliases:
 - "Gcluster.pl"
 - "interested_gene_generation.pl"
 - "test.pl"
 - "clm"
 - "clmformat"
 - "clxdo"
 - "mcl"
 - "mclblastline"
 - "mclcm"
 - "mclpipeline"
 - "mcx"
 - "mcxarray"
 - "mcxassemble"
versions:
 - "2.0.5--hdfd78af_1"
 - "2.06--hdfd78af_0"
 - "2.06--hdfd78af_2"
 - "2.0.7--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for gcluster"
config: {"url": "https://biocontainers.pro/tools/gcluster", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gcluster", "latest": {"2.06--hdfd78af_2": "sha256:f32e05b46ce8312c6325f7bf8a4667ea4463b5fa9fb9fea583dc43b21b2bd589"}, "tags": {"2.0.5--hdfd78af_1": "sha256:7388de9566bf822b6e59b40e9a9e14022985004d165a1f6f265048a049102bd4", "2.06--hdfd78af_0": "sha256:897ce3aa26db9f138dc7915b625ccce8107f8f340bbd4b7365fcd9828d9ef3f9", "2.06--hdfd78af_2": "sha256:f32e05b46ce8312c6325f7bf8a4667ea4463b5fa9fb9fea583dc43b21b2bd589", "2.0.7--hdfd78af_0": "sha256:9fba6d689fd41594b9eca37822622872565888c74c793e6835f2d25fecdca70a"}, "docker": "quay.io/biocontainers/gcluster", "aliases": {"Gcluster.pl": "/usr/local/bin/Gcluster.pl", "interested_gene_generation.pl": "/usr/local/bin/interested_gene_generation.pl", "test.pl": "/usr/local/bin/test.pl", "clm": "/usr/local/bin/clm", "clmformat": "/usr/local/bin/clmformat", "clxdo": "/usr/local/bin/clxdo", "mcl": "/usr/local/bin/mcl", "mclblastline": "/usr/local/bin/mclblastline", "mclcm": "/usr/local/bin/mclcm", "mclpipeline": "/usr/local/bin/mclpipeline", "mcx": "/usr/local/bin/mcx", "mcxarray": "/usr/local/bin/mcxarray", "mcxassemble": "/usr/local/bin/mcxassemble"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gcluster.
shpc-registry automated BioContainers addition for gcluster
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gcluster
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gcluster:2.06--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gcluster/2.06--hdfd78af_2
$ module help quay.io/biocontainers/gcluster/2.06--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gcluster-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gcluster-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gcluster-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gcluster-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gcluster-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gcluster-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Gcluster.pl

```bash
$ singularity exec <container> /usr/local/bin/Gcluster.pl
$ podman run --it --rm --entrypoint /usr/local/bin/Gcluster.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Gcluster.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interested_gene_generation.pl

```bash
$ singularity exec <container> /usr/local/bin/interested_gene_generation.pl
$ podman run --it --rm --entrypoint /usr/local/bin/interested_gene_generation.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interested_gene_generation.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test.pl

```bash
$ singularity exec <container> /usr/local/bin/test.pl
$ podman run --it --rm --entrypoint /usr/local/bin/test.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clm

```bash
$ singularity exec <container> /usr/local/bin/clm
$ podman run --it --rm --entrypoint /usr/local/bin/clm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clmformat

```bash
$ singularity exec <container> /usr/local/bin/clmformat
$ podman run --it --rm --entrypoint /usr/local/bin/clmformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clmformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clxdo

```bash
$ singularity exec <container> /usr/local/bin/clxdo
$ podman run --it --rm --entrypoint /usr/local/bin/clxdo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clxdo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcl

```bash
$ singularity exec <container> /usr/local/bin/mcl
$ podman run --it --rm --entrypoint /usr/local/bin/mcl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclblastline

```bash
$ singularity exec <container> /usr/local/bin/mclblastline
$ podman run --it --rm --entrypoint /usr/local/bin/mclblastline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclblastline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclcm

```bash
$ singularity exec <container> /usr/local/bin/mclcm
$ podman run --it --rm --entrypoint /usr/local/bin/mclcm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclcm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclpipeline

```bash
$ singularity exec <container> /usr/local/bin/mclpipeline
$ podman run --it --rm --entrypoint /usr/local/bin/mclpipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclpipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcx

```bash
$ singularity exec <container> /usr/local/bin/mcx
$ podman run --it --rm --entrypoint /usr/local/bin/mcx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxarray

```bash
$ singularity exec <container> /usr/local/bin/mcxarray
$ podman run --it --rm --entrypoint /usr/local/bin/mcxarray   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxarray   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxassemble

```bash
$ singularity exec <container> /usr/local/bin/mcxassemble
$ podman run --it --rm --entrypoint /usr/local/bin/mcxassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
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