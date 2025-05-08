---
layout: container
name:  "quay.io/biocontainers/vsearch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vsearch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vsearch/container.yaml"
updated_at: "2025-05-08 03:58:02.651052"
latest: "2.30.0--hd6d6fdc_0"
container_url: "https://biocontainers.pro/tools/vsearch"
aliases:
 - "vsearch"
versions:
 - "2.9.1--h96824bc_0"
 - "2.21.1--hf1761c0_1"
 - "2.20.1--h95f258a_0"
 - "2.19.0--h95f258a_0"
 - "2.18.0--h95f258a_0"
 - "2.17.1--h95f258a_0"
 - "2.27.0--h6a68c12_1"
 - "2.26.1--h6a68c12_0"
 - "2.25.0--h6a68c12_0"
 - "2.24.0--h6a68c12_0"
 - "2.23.0--h6a68c12_0"
 - "2.28.1--h6a68c12_0"
 - "2.27.1--h6a68c12_0"
 - "2.28.1--h6a68c12_1"
 - "2.29.0--h6a68c12_0"
 - "2.29.1--h6a68c12_0"
 - "2.29.2--hd6d6fdc_0"
 - "2.29.3--hd6d6fdc_0"
 - "2.30.0--hd6d6fdc_0"
 - "2.29.4--hd6d6fdc_0"
description: "shpc-registry automated BioContainers addition for vsearch"
config: {"url": "https://biocontainers.pro/tools/vsearch", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vsearch", "latest": {"2.30.0--hd6d6fdc_0": "sha256:0e57b8ef3e4e7947ebdd6b1dd88a3696ce883ec664cae0cd29606e661f6ad1fb"}, "tags": {"2.9.1--h96824bc_0": "sha256:3d96497fa5360f15f24079ec865dddb4ec7d50d4e7eed5ef17aba4758e4434e5", "2.21.1--hf1761c0_1": "sha256:9263eefb7cae8774850c82c958c2afa0b55f5d8e57ddeb5142b72ecfef3870a5", "2.20.1--h95f258a_0": "sha256:bbdff0cf8ef6349001c1dec752906b49681ee56b84bf3e50bd5c858fab206a18", "2.19.0--h95f258a_0": "sha256:cc0e7d61953a4f56e7b0e0f3600664d66dfb75976b5bc145059b906579351c34", "2.18.0--h95f258a_0": "sha256:8df52d62144e949a96d66dc18e1c91f3a8670513b67be5aab417662b7ad61d8e", "2.17.1--h95f258a_0": "sha256:f3a9df446c426f2d5417273d0d6b35a7e40ec814d8f771f5536b83adb53c2847", "2.27.0--h6a68c12_1": "sha256:52c23e6e9aa74f7a996011b20bb23a5d1bd3a54884161dc00efe4466695f725b", "2.26.1--h6a68c12_0": "sha256:38ab0f9bbf0300cc63e218cc08e6f9a2321ee9f8bc661b5e5d95e510457dfa16", "2.25.0--h6a68c12_0": "sha256:55aa4a4720c2ec7e7828d75647a9ccb11f29afbd4929749eac4e6ecae5de408e", "2.24.0--h6a68c12_0": "sha256:65af905a3a4da237d639b557efe3c107d1b34774db00edb9bac1559840d0f42e", "2.23.0--h6a68c12_0": "sha256:5df56a26fa9b79ce3dea0d607a1442b9a102a85cf23e25b0c6f1257153656120", "2.28.1--h6a68c12_0": "sha256:e040e8f05ae1b0ec64c421f2ed464e18230c9ffdc1b99d65557f425b2b36c8f4", "2.27.1--h6a68c12_0": "sha256:6f98cbfca59b1eba2bfe2444723173d6fb5832c6e558ce5d2a3e312da6cc8669", "2.28.1--h6a68c12_1": "sha256:215cda8c7c268ec0b2d86b642a6e1ffb0feefddcfd1cb43dd2bc6fecb215f526", "2.29.0--h6a68c12_0": "sha256:f37b597237dce64acb8da1dcd2c3fb8eac3d369092b1f8923af5a643ea13da4b", "2.29.1--h6a68c12_0": "sha256:bdd02e8c157650b1fbc6a2670b933af0c675cb35504948bc1abf384d1d6c8077", "2.29.2--hd6d6fdc_0": "sha256:bd72013f1a0600af1de85f059a8d1cc46f143eee505c32bacc616b81f643b7b0", "2.29.3--hd6d6fdc_0": "sha256:c4dbbab2a62803b3983556750314f1aad1e396c6c213d98bebb1a0bce59948eb", "2.30.0--hd6d6fdc_0": "sha256:0e57b8ef3e4e7947ebdd6b1dd88a3696ce883ec664cae0cd29606e661f6ad1fb", "2.29.4--hd6d6fdc_0": "sha256:00e3b0b26a12f43c11100a7c7e7aa42f74c869f1277df5c2e4c4b939aefcd8e0"}, "docker": "quay.io/biocontainers/vsearch", "aliases": {"vsearch": "/usr/local/bin/vsearch"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vsearch.
shpc-registry automated BioContainers addition for vsearch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vsearch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vsearch:2.30.0--hd6d6fdc_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vsearch/2.30.0--hd6d6fdc_0
$ module help quay.io/biocontainers/vsearch/2.30.0--hd6d6fdc_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vsearch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vsearch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vsearch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vsearch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vsearch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vsearch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vsearch

```bash
$ singularity exec <container> /usr/local/bin/vsearch
$ podman run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
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