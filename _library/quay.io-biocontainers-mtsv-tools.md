---
layout: container
name:  "quay.io/biocontainers/mtsv-tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mtsv-tools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mtsv-tools/container.yaml"
updated_at: "2023-12-24 02:44:26.038608"
latest: "2.0.2--h031d066_3"
container_url: "https://biocontainers.pro/tools/mtsv-tools"
aliases:
 - "mtsv-binner"
 - "mtsv-build"
 - "mtsv-chunk"
 - "mtsv-collapse"
 - "mtsv-collapse-old"
 - "mtsv-readprep"
versions:
 - "2.0.2--hec16e2b_1"
 - "2.0.2--hec16e2b_2"
 - "2.0.2--h031d066_3"
description: "shpc-registry automated BioContainers addition for mtsv-tools"
config: {"url": "https://biocontainers.pro/tools/mtsv-tools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mtsv-tools", "latest": {"2.0.2--h031d066_3": "sha256:19221fdc1edae2978949f1009230e409e9bd130bc887a214f9e9075e39cce615"}, "tags": {"2.0.2--hec16e2b_1": "sha256:c4fddadca62e7ffc6ad73b116202f73bd612fac8a7a83e8908213ba32ada2e13", "2.0.2--hec16e2b_2": "sha256:adb213e6d582d830927ddac6d202d2a079d095ebc90d2a296e9ab8c151c57b4a", "2.0.2--h031d066_3": "sha256:19221fdc1edae2978949f1009230e409e9bd130bc887a214f9e9075e39cce615"}, "docker": "quay.io/biocontainers/mtsv-tools", "aliases": {"mtsv-binner": "/usr/local/bin/mtsv-binner", "mtsv-build": "/usr/local/bin/mtsv-build", "mtsv-chunk": "/usr/local/bin/mtsv-chunk", "mtsv-collapse": "/usr/local/bin/mtsv-collapse", "mtsv-collapse-old": "/usr/local/bin/mtsv-collapse-old", "mtsv-readprep": "/usr/local/bin/mtsv-readprep"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mtsv-tools.
shpc-registry automated BioContainers addition for mtsv-tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mtsv-tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mtsv-tools:2.0.2--h031d066_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mtsv-tools/2.0.2--h031d066_3
$ module help quay.io/biocontainers/mtsv-tools/2.0.2--h031d066_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mtsv-tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mtsv-tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mtsv-tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mtsv-tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mtsv-tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mtsv-tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mtsv-binner

```bash
$ singularity exec <container> /usr/local/bin/mtsv-binner
$ podman run --it --rm --entrypoint /usr/local/bin/mtsv-binner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mtsv-binner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mtsv-build

```bash
$ singularity exec <container> /usr/local/bin/mtsv-build
$ podman run --it --rm --entrypoint /usr/local/bin/mtsv-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mtsv-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mtsv-chunk

```bash
$ singularity exec <container> /usr/local/bin/mtsv-chunk
$ podman run --it --rm --entrypoint /usr/local/bin/mtsv-chunk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mtsv-chunk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mtsv-collapse

```bash
$ singularity exec <container> /usr/local/bin/mtsv-collapse
$ podman run --it --rm --entrypoint /usr/local/bin/mtsv-collapse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mtsv-collapse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mtsv-collapse-old

```bash
$ singularity exec <container> /usr/local/bin/mtsv-collapse-old
$ podman run --it --rm --entrypoint /usr/local/bin/mtsv-collapse-old   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mtsv-collapse-old   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mtsv-readprep

```bash
$ singularity exec <container> /usr/local/bin/mtsv-readprep
$ podman run --it --rm --entrypoint /usr/local/bin/mtsv-readprep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mtsv-readprep   -v ${PWD} -w ${PWD} <container> -c " $@"
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