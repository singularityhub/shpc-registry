---
layout: container
name:  "quay.io/biocontainers/lumpy-sv-minimal"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lumpy-sv-minimal/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lumpy-sv-minimal/container.yaml"
updated_at: "2024-08-03 03:16:18.482803"
latest: "0.3.1--h43eeafb_4"
container_url: "https://biocontainers.pro/tools/lumpy-sv-minimal"
aliases:
 - "lumpy"
 - "lumpy_filter"
 - "lumpyexpress"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.3.1--h5ef6573_0"
 - "0.3.1--hea94271_1"
 - "0.3.1--hff880f7_2"
 - "0.3.1--h6ab5fc9_3"
 - "0.3.1--h43eeafb_4"
description: "shpc-registry automated BioContainers addition for lumpy-sv-minimal"
config: {"url": "https://biocontainers.pro/tools/lumpy-sv-minimal", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lumpy-sv-minimal", "latest": {"0.3.1--h43eeafb_4": "sha256:e29240b3eb48e87ebf442c4b8c515e0f5064f9cc64296b12a58cd6d1db1b65bd"}, "tags": {"0.3.1--h5ef6573_0": "sha256:11e86639741d51440c28b755ec3c03b390ea552a4ea590104bc1c695dd60a698", "0.3.1--hea94271_1": "sha256:229b022eae4cb6ffab7ec8cd271f5da2a4795fa42576f8f3f80d446cc8c20e7c", "0.3.1--hff880f7_2": "sha256:b15758b173fc3458e7641986d9a40733c66a5bba3636fe725acc6c0482d2c301", "0.3.1--h6ab5fc9_3": "sha256:bf30e1865cb9f65726de604f88b2669e8caa369d252dbbd00d62bbe385281667", "0.3.1--h43eeafb_4": "sha256:e29240b3eb48e87ebf442c4b8c515e0f5064f9cc64296b12a58cd6d1db1b65bd"}, "docker": "quay.io/biocontainers/lumpy-sv-minimal", "aliases": {"lumpy": "/usr/local/bin/lumpy", "lumpy_filter": "/usr/local/bin/lumpy_filter", "lumpyexpress": "/usr/local/bin/lumpyexpress", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lumpy-sv-minimal.
shpc-registry automated BioContainers addition for lumpy-sv-minimal
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lumpy-sv-minimal
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lumpy-sv-minimal:0.3.1--h43eeafb_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lumpy-sv-minimal/0.3.1--h43eeafb_4
$ module help quay.io/biocontainers/lumpy-sv-minimal/0.3.1--h43eeafb_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lumpy-sv-minimal-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lumpy-sv-minimal-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lumpy-sv-minimal-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lumpy-sv-minimal-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lumpy-sv-minimal-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lumpy-sv-minimal-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lumpy

```bash
$ singularity exec <container> /usr/local/bin/lumpy
$ podman run --it --rm --entrypoint /usr/local/bin/lumpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lumpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lumpy_filter

```bash
$ singularity exec <container> /usr/local/bin/lumpy_filter
$ podman run --it --rm --entrypoint /usr/local/bin/lumpy_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lumpy_filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lumpyexpress

```bash
$ singularity exec <container> /usr/local/bin/lumpyexpress
$ podman run --it --rm --entrypoint /usr/local/bin/lumpyexpress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lumpyexpress   -v ${PWD} -w ${PWD} <container> -c " $@"
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