---
layout: container
name:  "quay.io/biocontainers/dnmtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dnmtools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dnmtools/container.yaml"
updated_at: "2024-11-05 02:55:06.483184"
latest: "1.4.3--h4dfc31f_0"
container_url: "https://biocontainers.pro/tools/dnmtools"
aliases:
 - "dnmtools"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.2.1--h9f5acd7_0"
 - "1.2.1--h4ac6f70_1"
 - "1.3.0--hbb19d65_1"
 - "1.4.2--h0432e7c_0"
 - "1.4.3--h4dfc31f_0"
description: "singularity registry hpc automated addition for dnmtools"
config: {"url": "https://biocontainers.pro/tools/dnmtools", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for dnmtools", "latest": {"1.4.3--h4dfc31f_0": "sha256:08b15c5a64e989c486504d9f0c887d20d115686ab947244ef954f98626b1d3ab"}, "tags": {"1.2.1--h9f5acd7_0": "sha256:ef65bb16ddfdb036345e434c31fea50167717a170b91a73220ce48edab3cc499", "1.2.1--h4ac6f70_1": "sha256:331fce1505d9d0c4717926a2dd9bc526ef9a9a2446c07606570358adf40a8a79", "1.3.0--hbb19d65_1": "sha256:c139fc37e15d4aa10673a9595a5e6a2d38ec771162ed968c6e113aebf59f5cfa", "1.4.2--h0432e7c_0": "sha256:a7e05346c7a6c343c0dc96aaf502fe456a5db2bc97a2f8b17cd8f07817a03dd3", "1.4.3--h4dfc31f_0": "sha256:08b15c5a64e989c486504d9f0c887d20d115686ab947244ef954f98626b1d3ab"}, "docker": "quay.io/biocontainers/dnmtools", "aliases": {"dnmtools": "/usr/local/bin/dnmtools", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dnmtools.
singularity registry hpc automated addition for dnmtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dnmtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dnmtools:1.4.3--h4dfc31f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dnmtools/1.4.3--h4dfc31f_0
$ module help quay.io/biocontainers/dnmtools/1.4.3--h4dfc31f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dnmtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dnmtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dnmtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dnmtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dnmtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dnmtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dnmtools

```bash
$ singularity exec <container> /usr/local/bin/dnmtools
$ podman run --it --rm --entrypoint /usr/local/bin/dnmtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnmtools   -v ${PWD} -w ${PWD} <container> -c " $@"
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