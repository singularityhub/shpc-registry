---
layout: container
name:  "quay.io/biocontainers/abismal"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/abismal/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/abismal/container.yaml"
updated_at: "2025-02-16 03:28:13.236716"
latest: "3.2.4--h077b44d_1"
container_url: "https://biocontainers.pro/tools/abismal"
aliases:
 - "abismal"
 - "abismalidx"
 - "simreads"
versions:
 - "3.1.1--hd03093a_0"
 - "3.1.1--hd03093a_1"
 - "3.1.1--hdcf5f25_2"
 - "3.2.0--h84372a0_0"
 - "3.2.2--h4ac6f70_0"
 - "3.2.3--hdcf5f25_0"
 - "3.2.4--hdcf5f25_0"
 - "3.2.4--h077b44d_1"
description: "shpc-registry automated BioContainers addition for abismal"
config: {"url": "https://biocontainers.pro/tools/abismal", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for abismal", "latest": {"3.2.4--h077b44d_1": "sha256:adace4bfb9e8ef0eec6c052e14cb5f23237e6bc121252bdc0e20740ee536583b"}, "tags": {"3.1.1--hd03093a_0": "sha256:ba2852ae4d7adc88ca99f8d25ab7df9a74bf397138867dfd88ecd6130ab5998d", "3.1.1--hd03093a_1": "sha256:787094fb7bee8f4f5ce8965231db57cfb680a47953d2eb9d9d9df594534f8c4c", "3.1.1--hdcf5f25_2": "sha256:97a6c8f0d592af3fc210b272ade3aa3f3502eff656a8acc5c077e8c513dbbfdf", "3.2.0--h84372a0_0": "sha256:a5df40f609b2b436aa3fd43d1e8c190724305afca18e2fd675e7643c54fdf7d1", "3.2.2--h4ac6f70_0": "sha256:d4b723e00324c8551c6ac7278246b26d4f76ab4de27eb488fbe14f71b59b85bf", "3.2.3--hdcf5f25_0": "sha256:7bb8487e6f449234e9a845f86f03acc63dddfd9a8a8c51ce5fdfb9c456647e23", "3.2.4--hdcf5f25_0": "sha256:b022187f37d8dec1cf75949376f3a48963a81795215a9154b1c9afd7a2f3cce4", "3.2.4--h077b44d_1": "sha256:adace4bfb9e8ef0eec6c052e14cb5f23237e6bc121252bdc0e20740ee536583b"}, "docker": "quay.io/biocontainers/abismal", "aliases": {"abismal": "/usr/local/bin/abismal", "abismalidx": "/usr/local/bin/abismalidx", "simreads": "/usr/local/bin/simreads"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/abismal.
shpc-registry automated BioContainers addition for abismal
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/abismal
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/abismal:3.2.4--h077b44d_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/abismal/3.2.4--h077b44d_1
$ module help quay.io/biocontainers/abismal/3.2.4--h077b44d_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### abismal-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### abismal-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### abismal-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### abismal-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### abismal-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### abismal-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### abismal

```bash
$ singularity exec <container> /usr/local/bin/abismal
$ podman run --it --rm --entrypoint /usr/local/bin/abismal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abismal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abismalidx

```bash
$ singularity exec <container> /usr/local/bin/abismalidx
$ podman run --it --rm --entrypoint /usr/local/bin/abismalidx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abismalidx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simreads

```bash
$ singularity exec <container> /usr/local/bin/simreads
$ podman run --it --rm --entrypoint /usr/local/bin/simreads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simreads   -v ${PWD} -w ${PWD} <container> -c " $@"
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