---
layout: container
name:  "quay.io/biocontainers/bioconductor-adsplit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-adsplit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-adsplit/container.yaml"
updated_at: "2025-05-22 03:35:54.558029"
latest: "1.76.0--r44he5774e6_1"
container_url: "https://biocontainers.pro/tools/bioconductor-adsplit"

versions:
 - "1.64.0--r41hc247a5b_2"
 - "1.68.0--r42hc247a5b_0"
 - "1.68.0--r42hf17093f_1"
 - "1.70.0--r43hf17093f_0"
 - "1.72.0--r43hf17093f_0"
 - "1.76.0--r44he5774e6_0"
 - "1.76.0--r44he5774e6_1"
description: "shpc-registry automated BioContainers addition for bioconductor-adsplit"
config: {"url": "https://biocontainers.pro/tools/bioconductor-adsplit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-adsplit", "latest": {"1.76.0--r44he5774e6_1": "sha256:a1463d90d079fe1ae5ab52fb9d1ab3a6fb938d4386bdead0fde50a49e0144daa"}, "tags": {"1.64.0--r41hc247a5b_2": "sha256:e4dd6d27681cf17eb292caf820f636bede369e7cc1b126224a8f78fa6e90b3d9", "1.68.0--r42hc247a5b_0": "sha256:4e83cc2418d6d49510a3c71ca93739f9df1d4f7c5386b0c98ffa3d70697772a9", "1.68.0--r42hf17093f_1": "sha256:c243793b44c563ffa810c87c421cc36a2b420a3f8313703ef02391a8a747b30d", "1.70.0--r43hf17093f_0": "sha256:fee112aebc0c0d3cbe0f844ef4269750e328051e56d35fdb196e758096235772", "1.72.0--r43hf17093f_0": "sha256:ee1f5a67b88043f663d2cbd824fdc2ce65eaf9ca71dc6f6e7db1b43ac482491b", "1.76.0--r44he5774e6_0": "sha256:dff132ee11f555bc7f36194b2d518d61bc609ee2dd7fab6cfd423e9d969a9c44", "1.76.0--r44he5774e6_1": "sha256:a1463d90d079fe1ae5ab52fb9d1ab3a6fb938d4386bdead0fde50a49e0144daa"}, "docker": "quay.io/biocontainers/bioconductor-adsplit"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-adsplit.
shpc-registry automated BioContainers addition for bioconductor-adsplit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-adsplit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-adsplit:1.76.0--r44he5774e6_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-adsplit/1.76.0--r44he5774e6_1
$ module help quay.io/biocontainers/bioconductor-adsplit/1.76.0--r44he5774e6_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-adsplit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-adsplit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-adsplit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-adsplit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-adsplit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-adsplit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-adsplit

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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