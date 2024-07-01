---
layout: container
name:  "quay.io/biocontainers/auspice"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/auspice/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/auspice/container.yaml"
updated_at: "2024-07-01 03:42:04.102174"
latest: "2.52.0--hdbdd923_0"
container_url: "https://biocontainers.pro/tools/auspice"
aliases:
 - "auspice"
 - "corepack"
 - "node"
 - "npm"
 - "npx"
versions:
 - "2.39.0--h87f3376_1"
 - "2.40.0--h87f3376_0"
 - "2.40.1--h87f3376_0"
 - "2.42.0--h87f3376_0"
 - "2.43.0--h87f3376_0"
 - "2.45.1--h87f3376_0"
 - "2.44.0--h87f3376_0"
 - "2.46.0--h87f3376_0"
 - "2.45.1--hdbdd923_2"
 - "2.46.0--hdbdd923_2"
 - "2.48.0--hdbdd923_0"
 - "2.47.0--hdbdd923_0"
 - "2.49.0--hdbdd923_0"
 - "2.50.0--hdbdd923_0"
 - "2.52.0--hdbdd923_0"
description: "shpc-registry automated BioContainers addition for auspice"
config: {"url": "https://biocontainers.pro/tools/auspice", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for auspice", "latest": {"2.52.0--hdbdd923_0": "sha256:69bfb7b8cabbb4ec3e5afd3ea76855399f078ddcbf784de3ebb2e849f0a1abe1"}, "tags": {"2.39.0--h87f3376_1": "sha256:1cd30df83fb16d5115e85ffced86830112b53cb2ccee821647cea6235800f268", "2.40.0--h87f3376_0": "sha256:0c9ca157de340a1d48f111c37287b37b9ea7aafe12b8801308c7c115a0464cc6", "2.40.1--h87f3376_0": "sha256:2c3797464f1bb1e4b3990345769fc46c16db288ec533cd1c7add9743d4f8cb45", "2.42.0--h87f3376_0": "sha256:7242eb667dcae730d89aa33280463f9d708b4ddedba83a1018c8ccee5c9f729d", "2.43.0--h87f3376_0": "sha256:88bdc1596254654f81170713be157a66e6e816111629000b1c7b3a116019b7d4", "2.45.1--h87f3376_0": "sha256:ace5097e9312ca9fb979dad7f247149ddaabf73c4a90568916499349af0ae583", "2.44.0--h87f3376_0": "sha256:76ed82d6b6b05a9aed3ab442d0a00048a8d4bc0e460a6c42f6e372e2dcbc625a", "2.46.0--h87f3376_0": "sha256:1be70841edf734b22e73e847e0907edd7d5b29282e03fe667c5ca7da1a419a74", "2.45.1--hdbdd923_2": "sha256:9a15daa1cf5e9f418cb5e117e3e618bc48235b629a2786d1e17a48dad02a92bd", "2.46.0--hdbdd923_2": "sha256:b90a730f596193d7e175025b86120525f895bba33b8b2e4f34f7a6010af1dcac", "2.48.0--hdbdd923_0": "sha256:76ec09b845e669b6e9af2e790f643addf66617f45879d57c856a1cdaf438b245", "2.47.0--hdbdd923_0": "sha256:97d18fdf5445f7cef37d126fab96584b780a1cc56099dc042d15807b1a8c305c", "2.49.0--hdbdd923_0": "sha256:4af2c57e012691311f71fee1802ebb25d52a541f845fd36108ee907ef77a939c", "2.50.0--hdbdd923_0": "sha256:831690ac8cfad93b24e2f18bac86d548b9a306ebe071be9f0eefd43681c60d9c", "2.52.0--hdbdd923_0": "sha256:69bfb7b8cabbb4ec3e5afd3ea76855399f078ddcbf784de3ebb2e849f0a1abe1"}, "docker": "quay.io/biocontainers/auspice", "aliases": {"auspice": "/usr/local/bin/auspice", "corepack": "/usr/local/bin/corepack", "node": "/usr/local/bin/node", "npm": "/usr/local/bin/npm", "npx": "/usr/local/bin/npx"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/auspice.
shpc-registry automated BioContainers addition for auspice
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/auspice
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/auspice:2.52.0--hdbdd923_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/auspice/2.52.0--hdbdd923_0
$ module help quay.io/biocontainers/auspice/2.52.0--hdbdd923_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### auspice-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### auspice-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### auspice-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### auspice-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### auspice-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### auspice-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### auspice

```bash
$ singularity exec <container> /usr/local/bin/auspice
$ podman run --it --rm --entrypoint /usr/local/bin/auspice   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/auspice   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### corepack

```bash
$ singularity exec <container> /usr/local/bin/corepack
$ podman run --it --rm --entrypoint /usr/local/bin/corepack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/corepack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### node

```bash
$ singularity exec <container> /usr/local/bin/node
$ podman run --it --rm --entrypoint /usr/local/bin/node   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/node   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### npm

```bash
$ singularity exec <container> /usr/local/bin/npm
$ podman run --it --rm --entrypoint /usr/local/bin/npm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/npm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### npx

```bash
$ singularity exec <container> /usr/local/bin/npx
$ podman run --it --rm --entrypoint /usr/local/bin/npx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/npx   -v ${PWD} -w ${PWD} <container> -c " $@"
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